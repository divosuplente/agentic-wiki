#!/usr/bin/env python3
"""Wiki TUI Launcher."""

import argparse
import importlib.util
import os
import subprocess
import sys
import time
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def _has_module(name: str) -> bool:
    """Return True if *name* can be imported."""
    try:
        return importlib.util.find_spec(name) is not None
    except (ModuleNotFoundError, ValueError, ImportError):
        return False


def _check_markdown() -> None:
    """Exit with instructions if the ``markdown`` package is missing."""
    if _has_module("markdown"):
        return
    print("=" * 60)
    print("Dependency missing: 'markdown'")
    print("=" * 60)
    print("The wiki apps require the 'markdown' package.")
    print("Install it with:")
    print("  pip install markdown")
    print("or:")
    print("  pip install -r requirements.txt")
    sys.exit(1)


def _detect_features() -> dict[str, bool]:
    """Return a map of optional features and whether they are available."""
    return {
        "textual": _has_module("textual"),
    }


def _show_logo() -> None:
    """Print a framed ASCII art logo for Chapter DevEx Wiki."""
    print()
    print("########################################################")
    print("#                                                      #")
    print("#  ####   #    #   ####   #####   ######  ######  ##### #")
    print("# #    #  #    #  #    #  #    #    ##    #       #    ##")
    print("# #       #    #  #    #  #    #    ##    #       #    ##")
    print("# #       ######  ######  #####     ##    #####   ##### #")
    print("# #       #    #  #    #  #         ##    #       #   # #")
    print("# #    #  #    #  #    #  #         ##    #       #    ##")
    print("#  ####   #    #  #    #  #         ##    ######  #     #")
    print("#                                                      #")
    print("#         #####   ######  #    #  ######  #    #       #")
    print("#         #    #  #       #    #  #        #  #        #")
    print("#         #    #  #       #    #  #         ##         #")
    print("#         #    #  #####   #    #  #####     ##         #")
    print("#         #    #  #        #  #   #         ##         #")
    print("#         #    #  #        #  #   #        #  #        #")
    print("#         #####   ######    ##    ######  #    #       #")
    print("#                                                      #")
    print("#            #    #  ######  #    #  ######            #")
    print("#            #    #    ##    #   #     ##              #")
    print("#            # ## #    ##    #  #      ##              #")
    print("#            ######    ##    ####      ##              #")
    print("#            ######    ##    #  #      ##              #")
    print("#            # ## #    ##    #   #     ##              #")
    print("#            #    #  ######  #    #  ######            #")
    print("#                                                      #")
    print("########################################################")
    print()


def _show_spinner(duration: float = 1.5) -> None:
    """Display a rotating terminal spinner for *duration* seconds, then erase it."""
    chars = "|/-\\"
    end = time.time() + duration
    idx = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {chars[idx % len(chars)]}  Preparing knowledge base...")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()


def _launch(script: str) -> None:
    """Run *script* in the same directory using the current interpreter."""
    target = SCRIPT_DIR / script
    if not target.exists():
        print(f"Error: {script} not found in {SCRIPT_DIR}")
        sys.exit(1)
    _show_logo()
    _show_spinner()
    subprocess.run([sys.executable, str(target)], cwd=SCRIPT_DIR)


def main() -> None:
    """Parse arguments, check dependencies, then launch the TUI."""
    parser = argparse.ArgumentParser(description="Launcher for the wiki TUI.")
    parser.add_argument(
        "--auto",
        choices=["tui"],
        help="Launch the TUI directly (default behavior).",
    )
    args = parser.parse_args()

    os.chdir(SCRIPT_DIR)
    _check_markdown()
    features = _detect_features()

    if not features["textual"]:
        print("Error: The 'textual' package is required for the TUI.")
        print("Install it with:")
        print("  pip install textual")
        sys.exit(1)

    _launch("wiki_tui.py")


if __name__ == "__main__":
    main()
