"""Find every grid on each page with xword-ocr's finder and save its black-square pattern.
Usage (in xword-ocr's venv): grid_patterns.py <out.json> <label=path> [<label=path> ...]"""
import json
import sys

import cv2

from xword_ocr import pipeline
from xword_ocr.grid import BLACK

out = sys.argv[1]
res = {}
for spec in sys.argv[2:]:
    label, path = spec.split("=", 1)
    g = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if g is None:
        print("unreadable", path)
        continue
    H, W = g.shape
    grids = []
    for gr in pipeline.find_grids(g):
        pat = ["".join("#" if ch == BLACK else ("." if len(ch) != 1 or not ch.isalpha() else ".") for ch in row) for row in gr.cells]
        q = gr.quad
        grids.append({"rows": int(gr.rows), "cols": int(gr.cols), "pattern": pat,
                      "letters": bool(gr.has_letters),
                      "box": [round(float(q[:, 0].min()) / W, 3), round(float(q[:, 1].min()) / H, 3),
                              round(float(q[:, 0].max()) / W, 3), round(float(q[:, 1].max()) / H, 3)]})
    res[label] = grids
    print(label, [(x["rows"], x["cols"], "key" if x["letters"] else "puzzle") for x in grids], flush=True)
json.dump(res, open(out, "w"), indent=1)
