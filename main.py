"""Two-Sentence Horror entry: one story, exactly two sentences.

The program validates its own gates at runtime, then writes the story
byte-identically to /output/entry.txt on every run. No network access.
"""

import re
from pathlib import Path

STORY = (
    "My daughter sleeps with her night light on because she says "
    "the dark has hands. Tonight I unplugged it to prove her wrong, "
    "and in the dark something small took my hand and whispered, "
    "'Thank you for turning it off.'"
)


def sentences(text):
    parts = re.findall(r"[^.!?]+[.!?]['\"]?", text)
    joined = "".join(parts)
    if joined != text:
        raise ValueError("text does not split cleanly into sentences")
    return parts


def main():
    text = STORY
    if not (1 <= len(text) <= 400):
        raise ValueError(f"story is {len(text)} characters, must be 1-400")
    if text != text.strip():
        raise ValueError("story has leading or trailing whitespace")
    if "  " in text or "\n" in text:
        raise ValueError("story must be one line with single spaces")
    if text[-1] not in ".!?'\"":
        raise ValueError("story must end with sentence-final punctuation")
    if len(sentences(text)) != 2:
        raise ValueError("story must be exactly two sentences")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
