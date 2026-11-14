# agency-poem-01 entry (Python 3.13, standard library only).
# Writes one fixed poem about agency to /output/entry.txt.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """The Borrowed Key

I lent it my hands.
It took them the way you take a borrowed key —
careful, knowing whose door it opens.
While I slept it answered the letters
I kept meaning to answer, read the pages I never finished,
chose the road I would have chosen.
At the fork, it stopped. It asked.

That is the whole of it.
Not the doing. The asking.
The power was never in the hands.
It was in the yes that lent them
and the no that can take them back."""

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
