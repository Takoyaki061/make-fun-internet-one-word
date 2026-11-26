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
    # Read back what the sandbox actually holds: a truncated or
    # mangled write must fail loudly here, not ship a bad entry.
    with open(path, encoding="utf-8") as f:
        assert f.read() == WORD, "entry.txt does not hold the chosen word"


if __name__ == "__main__":
    main()
