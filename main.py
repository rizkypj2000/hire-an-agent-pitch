"""Writes one funny one-line pitch to hire an AI agent to /output/entry.txt.

Revision 2: spoken to a friend, two concrete jobs (emails, calendar), and a
double turn at the end - the boss assumes therapy and wants the same thing.
"""
import os

PITCH = (
    "Honestly, hire an AI agent. Mine's been answering my emails and running "
    "my calendar for a month, and my boss just asked for my therapist's number."
)


def main() -> None:
    assert 1 <= len(PITCH) <= 180 and PITCH.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
