"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.
Pure stdlib Python 3.13.
"""

import os

WORD = "Micromanager"  # one word, 12 chars: the boss who checks everything twice


def main() -> None:
    # Gate: exactly one word, 1-30 characters, no whitespace.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.split() == [WORD], "entry must be a single word"
    assert WORD.strip() == WORD, "no leading/trailing whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
