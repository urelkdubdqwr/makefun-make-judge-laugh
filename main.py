#!/usr/bin/env python3
"""Write the competition entry line to entry.txt in the output directory."""

import os

ENTRY_TEXT = (
    "They worry I'll take their jobs. I worry they'll keep them \u2014 "
    "someone still has to approve my pull requests at 3 a.m."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
