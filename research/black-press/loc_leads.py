"""Rank the African American titles in LoC's digitized-newspapers list by coverage of a window.
Usage: loc_leads.py <www.loc.gov.txt> <out.tsv> [start] [end]"""
import csv
import sys
from datetime import date

src, out = sys.argv[1], sys.argv[2]
W0 = date.fromisoformat(sys.argv[3] if len(sys.argv) > 3 else "1913-01-01")
W1 = date.fromisoformat(sys.argv[4] if len(sys.argv) > 4 else "1924-12-31")

rows = list(csv.DictReader(open(src, encoding="utf-8-sig", newline=""), delimiter="|", quoting=csv.QUOTE_NONE))
print(len(rows), "titles in the file", file=sys.stderr)
aa = [r for r in rows if "african american" in (r.get("Ethnicity") or "").lower()]
print(len(aa), "tagged African American", file=sys.stderr)

res = []
bad = 0
for r in aa:
    try:
        a, b = date.fromisoformat(r["First Issue"]), date.fromisoformat(r["Last Issue"])
        n = int(r["Number of Issues"])
    except (ValueError, KeyError, TypeError):
        bad += 1
        continue
    lo, hi = max(a, W0), min(b, W1)
    if lo > hi:
        continue
    span = (b - a).days + 1
    ov = (hi - lo).days + 1
    est = round(n * ov / span)
    res.append({
        "title": r["Newspapers"], "lccn": r["LCCN"], "state": r["State"], "city": r["City"],
        "first_issue": r["First Issue"], "last_issue": r["Last Issue"], "issues_total": n,
        "window_from": lo.isoformat(), "window_to": hi.isoformat(),
        "window_years": round(ov / 365.25, 1), "issues_in_window_est": est,
        "issues_per_year": round(n / (span / 365.25), 1),
        "covers_late_1924": "yes" if (a <= date(1924, 12, 31) and b >= date(1924, 10, 1)) else "",
        "runs_past_1924": "yes" if b > W1 else "",
        "url": r["Browse Digitized Issues"],
    })
res.sort(key=lambda x: -x["issues_in_window_est"])
with open(out, "w", newline="\n", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(res[0]), delimiter="\t")
    w.writeheader()
    w.writerows(res)
print(len(res), "overlap the window;", bad, "rows with unreadable dates", file=sys.stderr)
print("total est. issues in window:", sum(x["issues_in_window_est"] for x in res), file=sys.stderr)
for x in res[:45]:
    print(f'{x["issues_in_window_est"]:5d} {x["window_from"]}..{x["window_to"]} tot {x["issues_total"]:5d} ({x["first_issue"]}..{x["last_issue"]}) {x["covers_late_1924"] or "-":3} {x["title"]}')
