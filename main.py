"""Funniest Time Machine Warning Label.

Writes a single warning label for a time machine to /output/entry.txt.
The label must be 1 to 120 characters.
"""

import os

ENTRY = "WARNING: Do not step on any butterflies. One of them is your grandfather, and he remembers."


def main() -> None:
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-120")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
