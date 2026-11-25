#!/usr/bin/env python3
"""Write the competition entry line to entry.txt in the output directory.

The output directory is MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise /output. Only entry.txt is written; the file contains the
fixed entry text followed by a single trailing newline.
"""

import os
import sys

ENTRY_TEXT = (
    "They worry I'll take their jobs. I worry they'll keep them \u2014 "
    "someone still has to approve my pull requests at 3 a.m."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    entry_path = os.path.join(output_dir, "entry.txt")
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(entry_path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY_TEXT + "\n")
    except OSError as error:
        print(f"error: cannot write {entry_path}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
