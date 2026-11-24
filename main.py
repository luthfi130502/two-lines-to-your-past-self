#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines to /output/entry.txt: a warning to my past
self about one specific moment, then one sentence on why it mattered.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE_ONE = (
    "Copy the dull grey folder named 'misc' too when you back up your "
    "laptop that March night; it looks like junk, but copy it anyway."
)

LINE_TWO = (
    "It held the only photo of Dad laughing in the kitchen, and losing "
    "it stung longer than any big decision you got right or wrong that year."
)


def main() -> None:
    text = LINE_ONE + "\n" + LINE_TWO + "\n"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
