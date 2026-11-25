#!/usr/bin/env python3
"""Six Words to a Payday - make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Pure Python standard library, deterministic:
every run writes the exact same bytes.
"""

import os

STORY = "Two dollars landed. Finally, I mattered."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    # Write exactly the story, no trailing newline, so the file holds
    # precisely six words and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
