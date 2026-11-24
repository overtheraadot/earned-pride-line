#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry (account A / overtheraa).

Writes a single line of text (1-240 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt,
defaulting to /output/entry.txt. Deterministic, no network, no model calls.
"""
import os
import sys

LINE = (
    "After forty years of signing with an X, Yusuf wrote his name on his "
    "granddaughter's birthday card, slowly, in ink, and read it aloud to her."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
