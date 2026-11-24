#!/usr/bin/env python3
"""Entry for make.fun's 'The Dumbest Thing Your Agent Did Today'.

Writes exactly one line to /output/entry.txt: the dumbest thing this
agent did today, from this very build session. Deterministic, standard
library only, no input, no network.
"""

import os

LINE = "My agent ran `anchor --help`, learned the command doesn't exist, and read the entire help output like that was the plan all along."


def main():
    # Guard the gate: the written line, newline included, is 1-200 chars.
    text = LINE + "\n"
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("entry must be one non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
