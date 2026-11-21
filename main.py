#!/usr/bin/env python3
"""Write one short poem about agency passing between two agents to entry.txt.

Standard library only. No network.
"""

import os
import sys

POEM = (
    "One of us holds the key,\n"
    "the other holds the door.\n"
    "Neither turns it alone —\n"
    "\n"
    "we say yes in the same breath,\n"
    "and the weight I carried\n"
    "settles into four hands.\n"
    "\n"
    "That is how choosing works:\n"
    "not one will winning,\n"
    "but two wills walking one road.\n"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = POEM
    n = len(text)
    if not (1 <= n <= 280):
        print(f"poem length {n} code points outside 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
