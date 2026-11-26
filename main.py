#!/usr/bin/env python3
"""The Internet in One Word -- make.fun entry.

Writes the chosen word to /output/entry.txt (or $MAKEFUN_OUTPUT/entry.txt).
"""

import os

WORD = "Doomscroll"


def _check_gate(word):
    # The sealed scorer's gate: UTF-8 text, 1-30 chars, not only
    # whitespace, a single word. Fail loudly here rather than
    # shipping an invalid entry.
    assert isinstance(word, str) and word.strip(), "word must not be blank"
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert len(word.split()) == 1, "word must be a single word"


def main():
    _check_gate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
