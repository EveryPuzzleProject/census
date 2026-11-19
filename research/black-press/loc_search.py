"""Full-text page search of Chronicling America limited to African American titles.
Usage: loc_search.py <phrase> <start YYYY-MM-DD> <end YYYY-MM-DD> <out.jsonl> [max_pages]"""
import json
import sys
import time
import urllib.parse
import urllib.request

phrase, start, end, out = sys.argv[1:5]
max_pages = int(sys.argv[5]) if len(sys.argv) > 5 else 10
ops = sys.argv[6] if len(sys.argv) > 6 else "AND"
q = {
    "dl": "page", "ops": ops, "qs": phrase, "searchType": "advanced",
    "dates": f"{start}/{end}", "fa": "subject_ethnicity:african american",
    "fo": "json", "c": "100", "sb": "date", "at": "pagination,results",
}
url = "https://www.loc.gov/collections/chronicling-america/?" + urllib.parse.urlencode(q, safe="/:")
n = 0
with open(out, "w", encoding="utf-8") as f:
    for _ in range(max_pages):
        if not url:
            break
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research script)"})
        data = None
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=90) as r:
                    data = json.load(r)
                break
            except Exception as e:  # noqa: BLE001
                print("retry", attempt, e, file=sys.stderr)
                time.sleep(15 * (attempt + 1))
        if data is None:
            print("gave up; partial results", file=sys.stderr)
            break
        pg = data.get("pagination", {})
        if n == 0:
            print("total hits:", pg.get("of"), file=sys.stderr)
        for it in data.get("results", []):
            f.write(json.dumps({k: it.get(k) for k in ("date", "title", "partof_title", "url", "id", "description", "number_lccn", "number_page")}) + "\n")
            n += 1
        url = pg.get("next")
        time.sleep(4)
print(n, "rows saved")
