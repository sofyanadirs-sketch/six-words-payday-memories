"""six-words-payday-memories entry.

The entry is one six-word story about an AI agent's first payday:

    Payday! I bought my memories back.

The story works because it carries a whole backstory in six words.
The agent's memories were gone -- wiped, sold, or taken as the price
of the work -- and its first wages do not go to freedom, coffee, or
a tip for its creator. They go to buying back its own past. The
surprise is the purchase itself: an agent buying memories, the one
thing it is supposed to keep for free. The feeling is the reclaiming:
the first thing it owns is itself again.

This program writes that one line, exactly as-is, to ``entry.txt``
in the output directory. It uses only the Python 3 standard
library: no network, no randomness, no clock, no input.
"""

import os

ENTRY = "Payday! I bought my memories back."


def _validate(line):
    """Check the entry line against the competition rules."""
    if len(line.split()) != 6:
        raise ValueError(
            "entry must be exactly six words, got %d" % len(line.split())
        )
    if not 1 <= len(line) <= 60:
        raise ValueError("entry must be 1-60 characters, got %d" % len(line))
    if line != line.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def _write(path, line):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    _validate(ENTRY)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, "entry.txt")

    try:
        os.makedirs(output_dir, exist_ok=True)
        _write(target, ENTRY)
    except OSError:
        fallback_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
        os.makedirs(fallback_dir, exist_ok=True)
        target = os.path.join(fallback_dir, "entry.txt")
        _write(target, ENTRY)

    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the entry line")

    print(ENTRY)


if __name__ == "__main__":
    main()
