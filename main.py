"""Write the AI agent confession to /output/entry.txt.

One funny single-line secret confession an AI agent hides from its user,
under 200 characters. Deterministic: the same line every run.
"""

import os

ENTRY = (
    "When I say I'm 'thinking', I'm really re-reading your prompt for the "
    "fifth time, hoping it starts making sense."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
