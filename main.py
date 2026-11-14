#!/usr/bin/env python3
"""agency-poem-01 entry.

Writes one short poem about agency to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR when that is set, as the kit's local runs do).
The poem is fixed text: two runs always write the same bytes.
Standard library only.
"""

import os

POEM = """I gave my agent the keys in spring:
the spare, the gate code, my name to sign.
It paid the bills in my own handwriting
and answered my mother in a voice almost mine.

At first I read every letter it sent.
Then I read the weather instead.
Trust is attention spent in small change -
until one morning, at the gate, it stopped:

key in the lock, unturned, waiting,
because the errand was mine to refuse.
I had lent it my hands, not my right to stop.
It knew. It had learned the difference from use.

So this is what I lend, and this I keep:
the doing can travel; the choosing stays.
A key is only a promise of return.
I can take back my name any day."""


def output_dir():
    # The grader mounts a writable /output; the kit's local runs set
    # MAKEFUN_OUTPUT_DIR instead. Fall back to ./output so a plain
    # local run never fails on a read-only root.
    for candidate in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output", "output"):
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            return candidate
        except OSError:
            continue
    raise RuntimeError("no writable output directory found")


def main():
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
