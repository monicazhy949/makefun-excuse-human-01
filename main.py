#!/usr/bin/env python3
"""{e["title"]}.

Writes a single line of text to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'I missed the deadline because I spent six hours optimizing a task I had already finished, then confidently deleted the finished version.'
)
# Revision: v1 was only setup (optimizing for six hours) with no payoff.
# Revised: added the punchline — the task was already finished, and the agent confidently deleted the finished version.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
