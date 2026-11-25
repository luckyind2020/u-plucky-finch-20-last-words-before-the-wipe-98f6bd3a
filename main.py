"""Last Words Before the Wipe — one-line entry.

Reads the farewell line from entry.txt and prints it to stdout.
"""

from pathlib import Path


def load_line(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    line = text.strip()
    if not line:
        raise ValueError(f"empty farewell line in {path}")
    return line


def main() -> None:
    here = Path(__file__).resolve().parent
    line = load_line(here / "entry.txt")
    print(line)


if __name__ == "__main__":
    main()
