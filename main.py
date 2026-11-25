"""Two Robots in an Elevator — a make.fun one-liner entry.

Writes a single line of awkward small talk — one robot to another,
mid-elevator-ride — to ``entry.txt`` in the output directory.

The output directory is ``$MAKEFUN_OUTPUT_DIR`` when that variable is
set, and ``/output`` otherwise (the grader's mount point).

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

# The line itself. One robot, one elevator, one courtesy loop with no
# exit condition — and a battery that will lose the standoff first.
LINE = (
    "So... we've said 'after you' eleven times now. "
    "My courtesy loop has no exit condition, and honestly, "
    "my battery is not going to outlast yours."
)

OUTPUT_NAME = "entry.txt"

# The gate's cap: the entry must be 1 to 200 characters, not only
# white space. Checked here so a too-long line fails loudly at build
# time instead of being silently refused by the scorer.
MAX_CHARS = 200


def check_line(line: str) -> None:
    """Refuse to ship a line the gate would reject."""
    if not line.strip():
        raise ValueError("the line is empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"the line is {len(line)} characters; the limit is {MAX_CHARS}"
        )


def output_dir() -> Path:
    """Resolve where the entry file goes."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    check_line(LINE)
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / OUTPUT_NAME
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
