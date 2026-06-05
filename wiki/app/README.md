# Wiki Browser App

A lightweight terminal TUI for browsing the `chapter-devex` wiki.

## Requirements

- Python 3.8+

## Setup

**Automatic (with uv):**
If you have [`uv`](https://docs.astral.sh/uv/) installed, dependencies are managed automatically—just run `./wiki.sh` from the repo root.

**Manual:**
```bash
cd wiki/app
pip install -r requirements.txt
```

## Quick Start

The easiest way to run the app is through the launcher:

```bash
python launch.py
```

You can also pass:

```bash
python launch.py --auto tui
```

## `wiki_tui.py` — Terminal TUI

A keyboard-driven terminal browser built with [Textual](https://textual.textualize.io/).

**Run:**
```bash
python wiki_tui.py
```

**Controls:**
| Key | Action |
|-----|--------|
| `↑` / `↓` | Navigate tree |
| `Enter` | Open selected page |
| `b` | Go back |
| `/` | Search pages |
| `q` | Quit |

**Features:**
- File tree grouped by top-level folder
- Full-text search overlay
- Follow internal links inside the TUI
- Open external links in your system browser
