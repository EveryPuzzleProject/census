"""Print the OCR text around a word on loc.gov newspaper pages, and save the page's image links.
Usage: loc_page_text.py <word regex> <out dir> <resource url> [<resource url> ...]"""
import json
import os
import re
import sys
import time
import urllib.request

pat, outdir, urls = sys.argv[1], sys.argv[2], sys.argv[3:]
os.makedirs(outdir, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (research script)"}


def get(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            print("  retry", attempt, e, file=sys.stderr)
            time.sleep(20 * (attempt + 1))
    return None


for u in urls:
    base = u.split("&q=")[0]
    raw = get(base + "&fo=json")
    time.sleep(6)
    if raw is None:
        print("==", u, "\n  could not fetch")
        continue
    try:
        d = json.loads(raw)
    except ValueError:
        print("==", u, "\n  not JSON (blocked?)")
        continue
    ft = (d.get("resource") or {}).get("fulltext_file") or ""
    imgs = [p.get("url") for p in (d.get("page") or []) if isinstance(p, dict) and "iiif" in str(p.get("url"))]
    key = re.sub(r"[^0-9a-z]+", "_", base.split("/resource/")[1].lower()).strip("_")
    json.dump({"url": base, "fulltext": ft, "images": imgs}, open(os.path.join(outdir, key + ".json"), "w"))
    print("==", base)
    if not ft:
        print("  no text link")
        continue
    t = get(ft)
    time.sleep(6)
    if t is None:
        print("  text not fetched")
        continue
    t = t.decode("utf-8", "replace")
    try:
        j = json.loads(t)
        t = " ".join(str(v.get("full_text") if isinstance(v, dict) else v) for v in j.values())
    except ValueError:
        pass
    t = re.sub(r"\s+", " ", t).encode("ascii", "replace").decode()
    open(os.path.join(outdir, key + ".txt"), "w").write(t)
    hits = list(re.finditer(pat, t, re.I))
    print("  text chars:", len(t), "hits:", len(hits))
    last = -10**9
    for m in hits:
        if m.start() - last < 500:
            continue
        last = m.start()
        print("  ...", t[max(0, m.start() - 350):m.end() + 500], "...")
