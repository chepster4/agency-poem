# agency-poem-01 entry, version 2 (Python 3.13, standard library only).
# Writes one fixed poem about agency to /output/entry.txt.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """Her Name, in My Hand

On the line that asked for her name,
I wrote my mother's.
My hand knew the letters — it had watched her
sign birthday cards, cheques, permission slips
for thirty years. It knew the slope of the M.

The nurse took the paper without looking up.
That was the worst of it: how ordinary it was.
No thunder. No one asked if I was sure.
A name is a small thing.
It fits in any hand.

I signed again, slower, and felt its weight:
her name, in my hand, for as long as the paper holds —
and the paper holds only until she says otherwise."""

def main():
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
