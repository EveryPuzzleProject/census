# Newspaper Navigator as a crossword finder

Checked 2026-11-19. In short: a Library of Congress dataset made to find photographs and
maps in old newspapers also found thousands of crosswords, filed as maps. It names the page
of each one in the Library's free scans, so those puzzles can be harvested without a
subscription database. It finds nothing before 1924, and it misses a lot.

## What it is

[Newspaper Navigator](https://github.com/LibraryOfCongress/newspaper-navigator) (Benjamin
Lee and the Library of Congress, 2020) ran a picture detector over 16.37 million pages of
Chronicling America, the Library's free newspaper scans, as they stood in March 2020. It
drew a box around every photograph, illustration, map, comic, cartoon, headline and
advertisement, and kept the Library's machine-read text inside each box. Lee's own account
of the dataset notes that crossword grids were often labelled "map"
("Compounded Mediation", *Digital Humanities Quarterly* 15.4, 2021).

The Library retired the dataset's website in April 2025. A public-domain copy is on Hugging
Face as [`biglam/newspaper-navigator`](https://huggingface.co/datasets/biglam/newspaper-navigator);
its `maps` part has the 200,188 boxes the detector was at least 90% sure were maps (197,247
after removing duplicate scans), dated 1850 to 1950.

## What was done

- **Text test.** A box counts as a crossword if its text has "horizontal" and "vertical",
  or "cross-word" in any spelling. 5,213 boxes pass; 5,186 are dated 1924-02-24 or later.
- **Checked by eye.** Of 11 passing boxes from 1924–26 looked at, all 11 were crosswords.
  Of 24 that did not pass, 2 were crosswords, so the test undercounts. The 27 passing boxes
  dated before 1924 are war maps and sewing patterns.
- **1913–1923.** The 4,311 boxes of those years with the most small numbers in their text
  were fetched as thumbnails and put through a grid finder; 345 passed, and none is a
  crossword (stock charts, ship-position maps, township and oil-lease maps, schedules). The
  one puzzle is a letter grid, the Omaha Daily Bee's "Shakespeare Tercentenary Prize Puzzle"
  of 1916-04-09. About 36,000 less likely boxes were not fetched.
- **The denominator.** The project's page manifests list every page processed, so for any
  paper we know which issues the detector saw: 2,235,650 issues in all, and 462,720 issues of
  869 papers for 1913–1923.

## What it found

34 papers, 1924 to 1950. Dates are those with at least one box passing the text test.

| Paper | Place | Dates found | First | Last | Entry |
|---|---|---|---|---|---|
| Evening Star | Washington, D.C. | 3,347 | 1924-02-24 | 1950-12-31 | [entry](publications/evening-star-washington.md) |
| Bismarck Tribune | Bismarck, N.D. | 477 | 1924-11-11 | 1937-11-11 | [entry](publications/bismarck-tribune.md) |
| Indianapolis Times | Indianapolis, Ind. | 459 | 1924-10-14 | 1935-12-24 | [entry](publications/indianapolis-times.md) |
| New Britain Herald | New Britain, Conn. | 240 | 1924-10-16 | 1930-11-13 | [entry](publications/new-britain-herald.md) |
| Times-News | Hendersonville, N.C. | 117 | 1933-01-03 | 1938-12-31 | [entry](publications/hendersonville-times-news.md) |
| Wilmington Morning Star | Wilmington, N.C. | 102 | 1940-01-21 | 1947-03-08 | [entry](publications/wilmington-morning-star.md) |
| Coconino Sun | Flagstaff, Ariz. | 50 | 1924-12-19 | 1926-04-30 | [entry](publications/coconino-sun.md) |
| Midland Journal | Rising Sun, Md. | 49 | 1924-12-05 | 1934-04-27 | [entry](publications/midland-journal.md) |
| Mountain Home Republican | Mountain Home, Idaho | 26 | 1924-12-26 | 1925-10-30 | |
| Daily Independent | Elizabeth City, N.C. | 23 | 1936-09-11 | 1937-08-04 | |
| Butler County Press | Hamilton, Ohio | 21 | 1925-01-09 | 1925-08-14 | |
| Redwood Gazette | Redwood Falls, Minn. | 21 | 1925-01-28 | 1925-07-08 | |
| Winslow Mail | Winslow, Ariz. | 20 | 1925-03-06 | 1925-07-10 | |
| Kevin Review | Kevin, Mont. | 19 | 1924-12-25 | 1925-12-10 | |
| Henderson Daily Dispatch | Henderson, N.C. | 17 | 1940-01-09 | 1946-03-27 | |
| Detroit Tribune | Detroit, Mich. | 14 | 1937-12-04 | 1938-08-06 | |
| Bozeman Courier | Bozeman, Mont. | 13 | 1925-01-07 | 1926-01-08 | |
| Richmond Planet | Richmond, Va. | 13 | 1924-11-01 | 1925-08-01 | |
| The Independent | Elizabeth City, N.C. | 12 | 1924-12-19 | 1925-05-15 | |
| Wolf Point Herald | Wolf Point, Mont. | 11 | 1925-02-05 | 1925-04-30 | |
| Coolidge Examiner | Coolidge, Ariz. | 10 | 1933-07-28 | 1934-01-12 | |
| Arizona Sun | Phoenix, Ariz. | 8 | 1950-04-21 | 1950-11-23 | |
| Saturday Press | Minneapolis, Minn. | 6 | 1927-09-24 | 1934-08-18 | |
| Carolina Watchman | Salisbury, N.C. | 5 | 1936-11-06 | 1937-01-22 | |
| Marion Progress | Marion, N.C. | 5 | 1933-06-01 | 1933-07-06 | |
| Eureka Mirror | Eureka, Mont. | 3 | 1933-07-27 | 1934-01-18 | |
| Key West Citizen | Key West, Fla. | 3 | 1933-01-20 | 1933-10-02 | |
| Idaho County Free Press | Grangeville, Idaho | 3 | 1924-12-11 | 1924-12-25 | |
| Watauga Democrat | Boone, N.C. | 3 | 1925-01-22 | 1925-02-19 | |
| Apache Sentinel | Fort Huachuca, Ariz. | 2 | 1944-01-21 | 1945-04-20 | |
| Filer Record | Filer, Idaho | 1 | 1924-12-19 | 1924-12-19 | |
| Nogales International | Nogales, Ariz. | 1 | 1942-12-11 | 1942-12-11 | |
| Las Vegas Age | Las Vegas, Nev. | 1 | 1925-02-28 | 1925-02-28 | |
| Connecticut Chronicle | Hartford, Conn. | 1 | 1948-06-05 | 1948-06-05 | |

The eight with an entry were looked at (the Midland Journal only as text). The other 26 are
leads: the text test passed, nobody has looked at the page. Many are small weeklies of
1924–25, the kind the Western Newspaper Union supplied (see
[research-notes-weekly-syndication.md](research-notes-weekly-syndication.md)); the Coconino
Sun's puzzles carry that credit.

## How much it misses

For the Evening Star, a known 1924 run and a 1935 sample give two measures:

- Of 41 Sunday puzzle pages from 1924 saved by hand, the text test finds 18 (44%); another
  11 dates have a number-heavy box that was not checked.
- In 1935 it finds a puzzle on 23% of weekday issues. Of 30 weekdays picked at random from
  the rest, 26 have the puzzle on one of three pages checked. So nearly every miss that
  year is the dataset's.

By year, the share of the Star's weekday issues with a find runs from 86% (1925) down to 22%
(1936) and back to 89% (1938). So a paper's absence from the table, or a gap in its dates,
says little. What the dataset is good for is naming papers and periods to look at; a paper's
real run then has to be found on its pages, which the manifests list issue by issue.

It only covers what was in Chronicling America in March 2020: 4.4 million pages from the
1910s, 1.55 million from the 1920s, about 360,000 from each of the 1930s and 1940s.

## Not done

- The other parts of the dataset (illustrations, comics, cartoons), where more crosswords
  may be filed.
- Boxes the detector was less than 90% sure of, which the Hugging Face copy leaves out.
- The 26 leads in the table.
- Matching puzzles between papers to name the syndicates. Three or more papers ran the
  same themed, picture-in-the-grid puzzle in the 1930s with no credit line on the crops seen.
