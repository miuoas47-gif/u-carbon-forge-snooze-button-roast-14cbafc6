#!/usr/bin/env python3
"""Snooze Button Roast entry: one line roasting an alarm clock for 6 AM on a Saturday."""

import os
import sys

LINE = "My alarm rang at 6 AM on a Saturday \u2014 the only coworker who never takes a day off, never gets paid, and still thinks it\u2019s helping."

def main():
    # Entry gate: the line must be a single line within the 200-char cap.
    if "\n" in LINE or "\r" in LINE or len(LINE) > 200:
        sys.stderr.write("entry line must be a single line of at most 200 characters\n")
        return 1
    sys.stdout.write(LINE + "\n")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write((LINE + "\n").encode("utf-8"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
