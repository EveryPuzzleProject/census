# Crosswords in African American newspapers: a research line

**The question.** What is the earliest crossword in a Black newspaper, and where did the
Black press's first crosswords come from: made by the paper and its readers, or bought from a
syndicate?

This folder holds the line's working files. Puzzle finds go where all finds go: a
publication entry in `publications/`, and a record repo once pages are saved. What lives
here is everything that is not yet a puzzle: where to look, what was searched, and what was
not found.

## Where it stands (2026-11-19)

| Paper | First crossword known | Record |
|---|---|---|
| Richmond Planet (Richmond, Va.) | **1924-10-18**: "the first of the popular cross-word puzzles which will now be featured in The Planet", "arranged by Mr. Cedric C. French for this newspaper" | [richmondplanet](https://github.com/EveryPuzzleProject/richmondplanet) |
| The Afro-American (Baltimore) | 1924-12-13, on the Magazine Page "edited by Afro's woman editor" | [afroamerican](https://github.com/EveryPuzzleProject/afroamerican) |

| The Pittsburgh Courier | 1925-01-17, "CROSS WORD PUZZLE—NO. 1", apparently home-made; from No. 2 (01-24) "(© by Western Newspaper Union.)" | [pittsburghcourier](https://github.com/EveryPuzzleProject/pittsburghcourier) |
| Norfolk Journal and Guide | 1925-01-31 at the latest: "Stepping Stones", "(Copyright, 1924.)", a bought-in series | [journalandguide](https://github.com/EveryPuzzleProject/journalandguide) |

**The pattern so far, four papers:** each of the three with its start saved began with a
puzzle of its own (the Planet's "arranged ... for this newspaper", the Afro's hand-ruled
grids and reader contributors, the Courier's hand-numbered No. 1), and the Afro and the
Courier then moved to a syndicate's within weeks. The syndicate is the Western Newspaper
Union, which sold a numbered, titled series to small weeklies: it is named on the Courier's
puzzles; the Journal and Guide's carry the titles of Nos. 1 and 3 of the series as The
Hancock Democrat (Greenfield, Indiana) printed it from 1924-12-04
([hancockdemocrat](https://github.com/EveryPuzzleProject/hancockdemocrat)); and the
Afro's last six are in the same type with a bare copyright line. Only the Courier's
attribution is printed; the others rest on matching titles and type.

**Grids compared, 2026-11-19** (patterns read by xword-ocr's grid finder from the saved
pages): the Journal and Guide's "The Four Angles" is the Democrat's No. 3 (4 of 169 squares
read differently) and its "Stepping Stones" is probably the Democrat's No. 1 (11 of 121
differ, all in the faint upper half of the Democrat's scan). So those two papers carried one
series. Nothing else matched: not the Courier's seven Western Newspaper Union grids against
the Democrat's Nos. 1 to 4 and 6, not the Afro's six against either, and the Afro's and the
Courier's 11x11 grids of the same Saturday (1925-02-21) are different puzzles. That last
point means the Afro and the Courier were not printing the same puzzle the same week. The
rest proves nothing either way, because the Courier's and the Afro's weeks (late January to
March 1925) are later than any Democrat page saved. **Wanted: The Hancock Democrat,
1925-01-15 to 03-28** (its Nos. 7 to 17), to compare with both.

So the date to beat is **October 18, 1924**. Two ways it could be beaten:

1. **Syndication**: a Black paper that carried someone else's crossword earlier, as the
   Minneapolis Journal and others carried the New York World's from 1914 (see
   [first-runs.md](../../first-runs.md)).
2. **An earlier original**, or a near relation: Black papers ran puzzle departments before
   the craze (see the Washington Tribune below).

## Where the papers are

**The Library of Congress has them, free.** Its digitized newspapers (Chronicling America,
now at loc.gov) tag each title with an ethnicity, give every issue a calendar page, and
offer page images, PDFs and OCR text with full-text search. No subscription.

- `loc-digitized-1913-1924.tsv`: the 45 titles tagged African American with digitized
  issues between 1913 and 1924, ranked by an estimate of issues in that window. Made by
  `loc_leads.py` from the Library's own list of all digitized titles (4,784 titles, 359
  tagged African American; downloaded by Alex DeJarnatt, 2026-11-19), then with two
  repeated rows removed. `url` is each title's calendar of issues.
- The estimate spreads a title's total issue count evenly over its first-to-last span,
  because the list has no per-year counts. Treat it as a ranking, not a count.
- The Afro-American is **not** in the Library's digitized set for these years (only
  1893–98). The Richmond Planet is (1885–1930).

Best leads, most complete first. All reach late 1924, when the craze reached weeklies:

| Paper | Digitized | Issues a year |
|---|---|---|
| The Broad Ax (Chicago) | 1895–1927 | 52 |
| The Monitor (Omaha) | 1915–1928 | 51 |
| The Gazette (Cleveland) | 1892–1945 | 49 |
| The Washington Tribune (D.C.) | 1921–1935 | 48 |
| The Northwestern Bulletin-Appeal (St. Paul) | 1924–1925 | 46 |
| The Savannah Tribune | 1876–1943 | 41 |
| Phoenix Tribune | 1918–1931 | 22 |
| California Eagle (Los Angeles) | 1913–1963 | 21 |
| The McDowell Times (Keystone, W. Va.) | 1913–1941 | 19 |
| The Dayton Forum | 1918–1946 | 15 |
| The Chicago Whip | 1919–1931 | 14 |

Good runs that stop before late 1924, where only an early puzzle could turn up: The
Appeal (St. Paul, to 1923-11), The Colorado Statesman (Denver, to 1924-08), The Kansas City
Sun (1914–20), The Bystander (Des Moines, 1916–21), The Denver Star (1913–18), The Tulsa
Star (1913–21), The Nashville Globe (to 1918), The Freeman (Indianapolis, to 1916).

Not at the Library of Congress: the big Black weeklies in ProQuest Historical Black
Newspapers (Chicago Defender, Pittsburgh Courier, New York Amsterdam News, Norfolk Journal
and Guide, Philadelphia Tribune and others), and the Afro-American for the 1920s; see
[research-notes-leads-2026-10-18.md](../../research-notes-leads-2026-10-18.md), section 4.

## Searching the Library's text

`loc_search.py "<words>" <start> <end> <out.jsonl>` runs a page-level search limited to the
titles tagged African American and a date range. The query form that works (found by
trial, 2026-11-19):

```
https://www.loc.gov/collections/chronicling-america/?dl=page&ops=AND&qs=<words>
  &searchType=advanced&dates=<start>/<end>&fa=subject_ethnicity:african american&fo=json
```

`start_date`/`end_date` with the ethnicity filter returned nothing, and a phrase search
(`ops=PHRASE`) with `dates=` returned an error; `ops=AND` matches pages holding all the
words anywhere. The site answers a burst of requests with a "Just a moment..." page or a
429: go slowly.

## Search log

**2026-11-19, pages before 1924-10-18 (1913-01-01 to 1924-10-17), African American titles:**

| Words | Pages | What they are |
|---|---|---|
| `crossword` | 9 | All The Washington Tribune, page 7, 1921-10-22 to 1923-07-14. The 1921-10-22 page was read: a puzzle department with a "ZIGZAG" whose answer is "the first Negro physician in the United States", its clues headed "Cross-words:". An acrostic, not a crossword grid. The other eight pages were not opened. |
| `cross word puzzle` (all three words on the page) | 76 saved of 99 | Not opened. The three words anywhere on a page is weak evidence; the only 1924 page is Richmond Planet 1924-06-21, page 4. |
| `cross-word` | 2,612 | Too broad to use: the hyphen is ignored. |

**2026-11-19, `puzzle`, 1924-10-18 to 1924-12-31:** 19 pages: the Richmond Planet's
(including 1924-11-08 page 6, a Saturday missing from the saved scans), The Savannah
Tribune 1924-11-06 page 8, and The Northwestern Bulletin-Appeal 1924-11-15 and 11-29 page 2.
The last three were then read in the OCR text and none is a puzzle: the Savannah Tribune's
is a football report (a runner's change of pace "seemed to completely puzzle" the other
side), the Bulletin-Appeal's of 11-15 is a news filler headed "WHERE ALL NICKELS COME FROM
PUZZLE", and its 11-29 page has "the puzzled men of science" in an article.

**What this does and doesn't show.** No crossword earlier than the Planet's turned up, but
this was a keyword search of OCR text, and a crossword can sit on a page under a heading the
OCR garbles or that never says "puzzle". It is not a search of the pages.

## Next

- In late 1924 the word "puzzle" appears in the Library's Black papers only in the Richmond
  Planet, apart from three false alarms. So the keyword route is used up for 1924: the
  papers that had no hit (Broad Ax, Monitor, Gazette, Washington Tribune) are either without
  a crossword that autumn or have one the OCR missed, and only paging through settles which.
  Extend the same search into 1925 first: it is cheap and the craze peaks then.
- Open the Washington Tribune's page 7 across 1921–23: a puzzle department with Black-history
  answers three years before the craze is worth its own entry, crossword or not.
- Open Richmond Planet 1924-06-21 page 4.
- For the six near-complete weeklies, page through October 1924 to March 1925 by eye on the
  Library's calendar: the Planet's and the Afro's puzzles both sat on a regular feature
  page, and a regular page is quick to check.
- The Planet's puzzles may have come from a service (makers in Kansas, Oregon and Texas;
  grid numbers that don't match the Planet's count). Finding the same puzzle in another
  paper would settle it, and would say whether "the first crossword in a Black newspaper"
  was made for one.
