#!/usr/bin/env python3
"""Wiki TUI – Terminal browser for the chapter-devex wiki.

Usage:
    python wiki_tui.py

Requires:
    pip install textual
"""

from __future__ import annotations

import os
import webbrowser
from pathlib import Path

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Footer, Header, Input, Markdown, OptionList, Static, Tree

WIKI_ROOT: Path = Path(__file__).resolve().parent.parent


def _safe_add_leaf(parent: Tree, label: str, *, data: Path | None = None) -> None:
    """Add a leaf node across Textual API versions."""
    node = parent.add_leaf(label, data=data) if hasattr(parent, "add_leaf") else parent.add(label, data=data)
    if hasattr(node, "allow_expand"):
        node.allow_expand = False


class SearchScreen(ModalScreen[Path | None]):
    """Full-text search overlay for wiki pages."""

    DEFAULT_CSS = """
    SearchScreen {
        align: center middle;
    }
    #search-container {
        width: 70;
        height: auto;
        max-height: 24;
        border: thick $background 80%;
        background: $surface;
        padding: 1 2;
    }
    #search-input {
        width: 100%;
        margin-bottom: 1;
    }
    #search-options {
        width: 100%;
        height: auto;
        max-height: 16;
    }
    """

    def __init__(self, pages: list[tuple[str, Path]]) -> None:
        self._all_pages = pages
        self._filtered = pages[:]
        super().__init__()

    def compose(self) -> ComposeResult:
        with Vertical(id="search-container"):
            yield Input(placeholder="Search pages…", id="search-input")
            yield OptionList(*[label for label, _ in self._filtered], id="search-options")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Filter results as the user types."""
        query = event.value.lower().strip()
        self._filtered = [(l, p) for l, p in self._all_pages if query in l.lower()] if query else self._all_pages[:]
        opt = self.query_one("#search-options", OptionList)
        opt.clear_options()
        for label, _ in self._filtered:
            opt.add_option(label)

    @on(OptionList.OptionSelected)
    def on_option_selected(self, event: OptionList.OptionSelected) -> None:
        """Open the chosen search result."""
        idx = event.option_index
        if 0 <= idx < len(self._filtered):
            self.dismiss(self._filtered[idx][1])

    def key_escape(self) -> None:
        """Close search without action."""
        self.dismiss(None)

    def key_enter(self) -> None:
        """Allow Enter from anywhere on the screen to confirm."""
        opt = self.query_one("#search-options", OptionList)
        highlighted = opt.highlighted
        if highlighted is None and self._filtered:
            highlighted = 0
        if highlighted is not None and 0 <= highlighted < len(self._filtered):
            self.dismiss(self._filtered[highlighted][1])

    def key_up(self) -> None:
        """Navigate up in the option list."""
        opt = self.query_one("#search-options", OptionList)
        opt.action_cursor_up()

    def key_down(self) -> None:
        """Navigate down in the option list."""
        opt = self.query_one("#search-options", OptionList)
        opt.action_cursor_down()


class WikiBrowser(App):
    """Browse, render and follow links inside the chapter-devex wiki."""

    CSS = """
    Screen {
        align: left top;
    }
    #sidebar {
        width: 28;
        height: 100%;
        border-right: solid $background-lighten-1;
        overflow-y: auto;
    }
    #sidebar-title {
        height: 1;
        background: $primary-darken-2;
        color: $text;
        content-align: center middle;
    }
    #page-tree {
        width: 100%;
        height: 1fr;
    }
    #content-pane {
        width: 1fr;
        height: 100%;
        overflow-y: auto;
        padding: 1 2;
    }
    #page-content {
        width: 100%;
        height: 100%;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("b", "back", "Back"),
        Binding("slash", "search", "Search"),
    ]

    def __init__(self) -> None:
        self.wiki_root = WIKI_ROOT.resolve()
        self._history: list[Path] = []
        self._current: Path | None = None
        self._pages: list[tuple[str, Path]] = []
        super().__init__()

    # ------------------------------------------------------------------ UI
    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with Horizontal():
            with Vertical(id="sidebar"):
                yield Static("Wiki Pages", id="sidebar-title")
                yield Tree("Wiki", id="page-tree")
            with Vertical(id="content-pane"):
                yield Markdown(id="page-content")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Wiki TUI"
        self.sub_title = str(self.wiki_root.name)

        tree = self.query_one("#page-tree", Tree)
        tree.root.expand()
        self._build_tree(tree)

        default = self.wiki_root / "README.md"
        if default.exists():
            self._navigate(default)

    # ------------------------------------------------------------------ tree
    def _build_tree(self, tree: Tree) -> None:
        """Populate sidebar tree with all markdown files grouped by top-level folder."""
        md_files = sorted(self.wiki_root.rglob("*.md"), key=lambda p: str(p).lower())
        self._pages = [(str(path.relative_to(self.wiki_root)), path) for path in md_files]

        groups: dict[str, list[tuple[str, Path]]] = {}
        root_items: list[tuple[str, Path]] = []

        for rel_str, path in self._pages:
            rel = path.relative_to(self.wiki_root)
            if len(rel.parts) > 1:
                category = rel.parts[0]
                groups.setdefault(category, []).append((rel.name, path))
            else:
                root_items.append((rel.name, path))

        for label, path in sorted(root_items, key=lambda t: t[0].lower()):
            _safe_add_leaf(tree.root, label, data=path)

        for category in sorted(groups.keys(), key=str.lower):
            branch = tree.root.add(category, expand=True)
            for label, path in sorted(groups[category], key=lambda t: t[0].lower()):
                _safe_add_leaf(branch, label, data=path)

    @on(Tree.NodeSelected)
    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Select a leaf in the tree to navigate to that page."""
        if event.node.data is None:
            return
        target = event.node.data if isinstance(event.node.data, Path) else Path(event.node.data)
        self._navigate(target)

    # ------------------------------------------------------------------ navigation
    @on(Markdown.LinkClicked)
    def on_markdown_link_clicked(self, message: Markdown.LinkClicked) -> None:
        """Route internal links inside the TUI and external URLs to the system browser."""
        href = message.href.strip() if message.href else ""
        target = self._resolve_link(href)
        if target is None:
            from urllib.parse import urlparse

            parsed = urlparse(href)
            if parsed.scheme and parsed.scheme not in ("", "file"):
                webbrowser.open(href)
                self.notify(f"Opened in browser: {href}")
            else:
                self.notify(f"Link not found: {href}", severity="warning")
        else:
            self._navigate(target)

    def _resolve_link(self, href: str) -> Path | None:
        """Return an absolute path inside the wiki or None for external / broken links."""
        from urllib.parse import urlparse

        if not href:
            return None
        parsed = urlparse(href)
        if parsed.scheme and parsed.scheme not in ("", "file"):
            return None

        if href.startswith("/"):
            target = (self.wiki_root / href.lstrip("/")).resolve()
        else:
            base = self._current or self.wiki_root / "README.md"
            target = (base.parent / href).resolve()

        # Guard against paths that escape the wiki root
        try:
            target.relative_to(self.wiki_root)
        except ValueError:
            return None

        candidates: list[Path] = [target]
        if target.suffix.lower() != ".md":
            candidates.append(target.with_suffix(".md"))

        for cand in candidates:
            if cand.exists():
                return cand

        if target.is_dir():
            index = target / "index.md"
            if index.exists():
                return index

        return None

    def _navigate(self, path: Path, *, push_history: bool = True) -> None:
        """Render a markdown file in the main content pane."""
        if not path.exists():
            self.notify(f"Page not found: {path}", severity="error")
            return
        if path.suffix.lower() != ".md":
            return

        if push_history and self._current is not None and self._current != path:
            self._history.append(self._current)

        self._current = path
        content = path.read_text(encoding="utf-8")
        self.query_one("#page-content", Markdown).update(content)
        self.sub_title = str(path.relative_to(self.wiki_root))

    # ------------------------------------------------------------------ actions
    def action_back(self) -> None:
        if not self._history:
            self.notify("No previous page in history", severity="warning")
            return
        prev = self._history.pop()
        self._navigate(prev, push_history=False)

    def action_search(self) -> None:
        def _cb(result: Path | None) -> None:
            if result is not None:
                self._navigate(result)

        self.push_screen(SearchScreen(self._pages), _cb)

    def action_quit(self) -> None:
        self.exit()


if __name__ == "__main__":
    WikiBrowser().run()
