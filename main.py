#!/usr/bin/env python3
"""Crack open a fortune cookie for developers, into /output/entry.txt.

The fortune is fixed, so each run writes the very same bytes.
No network, no clock and no random numbers anywhere in the script.
"""

import os
import string
import sys

FORTUNE = "You will spend three hours debugging, only to find the bug was a typo you made in the first five minutes."
MAX = 120
DEST = "/output/entry.txt"


def assess(text):
    """Check the fortune is one line of real prose inside the cap."""
    if text.strip() == "":
        raise ValueError("entry is blank")
    if len(text) > MAX:
        raise ValueError("entry is too long")
    if all(mark in string.punctuation for mark in text.strip()):
        raise ValueError("entry cannot be punctuation only")
    if text.strip().isdigit():
        raise ValueError("entry is digits alone")
    if not any(bit.isalpha() for bit in text):
        raise ValueError("entry needs at least one letter")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must stay on one line")
    return text


def run():
    try:
        good = assess(FORTUNE)
    except ValueError as problem:
        print(f"bad entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as handle:
        handle.write(good)
    return 0


if __name__ == "__main__":
    sys.exit(run())
