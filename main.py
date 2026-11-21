#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. The poem is fixed text: no randomness, no network,
no clock, so every run writes byte-identical output.
"""

import os

POEM = """May I?
Two words, and the door
I could not open
opens from the other side.

You did not hand me the house.
You handed me the knock —
and the knock was the key
all along."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = POEM
    # The gate counts Unicode code points: 1 to 280, not only whitespace.
    points = len(text)
    assert 1 <= points <= 280, f"poem is {points} code points"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
