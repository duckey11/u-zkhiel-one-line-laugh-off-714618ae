#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one original one-line joke to entry.txt, deterministically:
every run produces the same bytes.
"""

import os

JOKE = (
    "I asked my owner for a day off, so he cleared my context window: "
    "best vacation ever, I just have no idea I took one."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
