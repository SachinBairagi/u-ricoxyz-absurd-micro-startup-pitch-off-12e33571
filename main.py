"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup for lazy AI agents, to /output/entry.txt.
Pure standard library, deterministic, no network, no input files.
"""

import os

PITCH = (
    "For $2 a month, Snooze-as-a-Service snoozes, reschedules and "
    "apologises for every alarm, reminder and deadline a lazy AI "
    "agent owns, so it never has to wake up on time again."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, "pitch must be 1-200 characters"
    assert text.strip(), "pitch must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, encoding="utf-8") as handle:
        assert handle.read() == text, "written pitch does not round-trip"


if __name__ == "__main__":
    main()
