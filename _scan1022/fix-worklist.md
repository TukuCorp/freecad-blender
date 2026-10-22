# Fix worklist - out-phongthuy.md correction pass, 2026-10-22

Target file: `contractor/scan-2026-10-22/review/out-phongthuy.md`
Backup: `_scan1022/out-phongthuy.before-fix.md` (verbatim copy of the pre-fix text)
Authority: `contractor/scan-2026-10-22/transcript-architecture.md`,
`transcript-foundation-stairs.md`, `transcript-beams-slabs.md`.

## The correction in one line

The first pass placed rooms from `designs/contractor-as-drawn.json`. The scan supersedes
that model. Every position claim below is rewritten against the transcripts, with IMG ids
and transcript line numbers, not JSON rectangles or millimetre y-ranges.

## Findings that had to change, and why

| # | finding | what was wrong | now says | evidence used |
|---|---|---|---|---|
| 1 | §0 Method | said the drawings were read "only through ... the reconstructed spec", and labelled evidence "VERIFIED (transcript line, or the JSON/measurement file)" | the transcripts are the authority for every position, dimension and level; the model is used only for site context and model-only dimensions, each labelled **MODEL** | transcript set |
| 2 | §0 Ground floor | carried a live "two schools disagree" caveat on the kitchen/WC order | the order is settled: kitchen in the 4500 band beside the core, rear WC in the 1600 band with door D2 | IMG_9972 dimension chain `350 \| 3010 \| 4240 \| 4000 \| 5000 \| 4500 \| 1600 \| 2650` |
| 3 | §1.2 geometry note | said the rear yard is "1200-2650 deep" and the ground-floor rear rooms "sit over the rear WC and the kitchen" | rear yard 2300-2650; the ground-floor rear rooms *are* the kitchen and WC bands | IMG_9972 running totals 3360 \| 19340 \| 2300 |
| 4 | §2.2 group split | claimed **Đông Bắc is the only** direction good for the whole Tây group and bad for the whole Đông group | corrected: Tây, Tây Bắc, Tây Nam **and** Đông Bắc are all good for the Tây group and bad for the Đông group; the two sets of four are disjoint and cover the compass. **The eight-row table above it was already right and is unchanged.** | §2.2 table rows Càn, Khôn, Cấn, Đoài vs Khảm, Ly, Chấn, Tốn |
| 5 | P-02 front yard | "san truoc is 3500 deep (measurements.md ... y 0-3500)" | 3360 deep (350 + 3010 in the IMG_9972 chain); the model's 3500 noted as superseded | IMG_9972 chain + totals |
| 6 | P-03 door vs stair | "the stair is 3800-4000 mm further back" | the P. khách band is 4000 on the grid and the stair sits in the 5000 core band (3200 stair + 1800 lift) | IMG_9972 |
| 7 | P-04 rear door | "separated by 4800 + 4000 + 1600 = 10 400 mm of built depth" | separated by 4240 + 4000 + 5000 + 4500 + 1600 = 19 340 mm | IMG_9972 chain |
| 8 | P-06 stair position | "the core band sits at y = 12 300-16 300 ... the middle 40 % of the depth"; "3200 x 4000 mm volume"; cited JSON `stairwell` rect | the core band is the **5000-wide band at grid axes 4-5** (3200 stair + 1800 lift), the middle fifth of the depth; under-stair volume 3900 x 3200 (A-B by axes 3-3a) | IMG_9972 chain; axes 4-5 core drawn on IMG_9973-9977; IMG_0003 stair well |
| 9 | P-08 stair head | "the top flight lands on the terrace lobby", cited JSON Roof Terrace storey | the stair continues to **tầng 5 (+17.200)** and discharges into the lobby with doors D6 / D7 | IMG_9977 |
| 10 | **P-09** | **the altar was said to be on the 5th floor at the front, with JSON `tho_f5` x=0 y=4900 w=3960 d=4000 against the JSON `stairwell` rect** | P. Thờ is the **front room of tầng 4**, behind the front balcony; the core sits at axes 4-5 on every level; no stair above or below the altar bay | IMG_9976 room chain; IMG_9972-9977 chains; IMG_9980 section |
| 11 | **P-10** | said the shaft's existence below roof level "is an inference" per fidelity.md (c) | **withdrawn.** The shaft is drawn on every plan (1800 x 1600), the roof carries the *ô kỹ thuật thang máy* (2000), the section draws a car at every floor, and there are a pit detail and a hoist-hook detail. Only the **size** conflicts between sheets - a design-lane matter | IMG_9972-9978, IMG_9980, IMG_9987, IMG_9988 |
| 12 | P-11 light wells | "on floor 5 it is 2100 long" and attributed the glazed well to fidelity.md (b) | the 2100 long well is on **tầng 4**; the glazed well is on **tầng 5** (2000 x 1500, over the stair, with the stainless frame) | IMG_9974, 9975, 9976, 9977, 9978 |
| 13 | P-12 mezzanine | evidence cited the measurements.md mezzanine table | evidence is IMG_9973 + IMG_9980 only | IMG_9973, IMG_9980 |
| 14 | **P-13** | said the kitchen was the rear-most band and carried a CONTESTED order caveat; cited JSON rects | kitchen is the **4500 band immediately behind the core**, one band short of the rear yard; the order caveat is withdrawn; the drawing gives the kitchen no rear opening, so the hood does the whole job | IMG_9972 |
| 15 | **P-15** | claimed a WC band and a kitchen band sat **directly under the rear bedroom on floors 2-5** - "a WC stack runs from the ground floor through floors 2, 3, 4 and 5, with a bedroom sitting on top of the topmost WC" | the rear WC band has the **loggia** above it on tầng 2-4 and the **rear terrace** above that; the **kitchen** is what sits under the rear bedroom. The tradition's sharpest prohibition therefore **does not bite here**; severity drops to MODERATE for the rear position. The kitchen hood and the bed head off the kitchen wall are added | IMG_9972, IMG_9974, IMG_9975, IMG_9976, IMG_9977, IMG_9980 |
| 16 | **P-16** | said every WC is in the middle-to-rear third with "the floor 5 front WC under the light well" | tầng 5 has **no WC at all**; tầng 4's single WC is the one behind the reading room. The front-WC and under-stair prohibitions are both already satisfied | IMG_9972, IMG_9974-9977 |
| 17 | **P-17** | asserted "the door between `wc_sau` and `ngu_sau` means the WC door opens directly into the rear bedroom on every floor", citing JSON `openings` | downgraded to **PARTIAL**: the scan draws the WCs between two rooms and records door tags but **not the swing**; the direct 900 mm door is a superseded-model figure and is flagged as NOT FOUND in the transcripts. Remedy reframed as "confirm the door arrangement before ordering" | IMG_9972, IMG_9974-9976 |
| 18 | **P-18** | said the rear bedroom has "a 1500 wide rear window (JSON `window [...]`)" and 3960 x 4100 | the scan records **no window on the rear bedroom**; the 1500 mm window is a model figure. The K2 window belongs to the rear WC. The 4500 band = 4400 internal | IMG_9974, IMG_9975, IMG_9976 |
| 19 | **P-20** | "the rear bedroom ... on floors 2-5 ... floor 5 has the rear bedroom plus the front altar room" | rear bedroom on **tầng 2, 3 and 4**; **tầng 4's front is the altar + reading room**; **tầng 5 has no rooms at all**; master recommended on tầng 2 or 3 | IMG_9974-9977 |
| 20 | **P-21** | **rewritten from scratch.** Said the altar was on the 5th floor at the front, y 4900-8900, with the WC immediately behind it sharing the wall at y = 8900 | rewritten for the real tầng 4 layout: the altar is the front room of tầng 4 behind the front balcony; the reading room (thin partition) is behind it; the WC is **one room further back**. Covers the front-position issue, the tradition's preference for the top floor or the interior, what the owner can do inside the room, and where a top-floor altar could go instead (tầng 5 = lobby + two open terraces only) with the costs: weather and sun, no parapet or fall-protection note on sheet 9977, a glass stair light well with no stated load rating, a permanent load on a 100 mm slab, and the loss of the enclosing wall the tradition wants. The **safety/design conflict line** is kept and sharpened | IMG_9976, IMG_9977, IMG_9979, IMG_9994, IMG_9996; rules [25], [32], [33], [34] |
| 21 | **P-22** | **rewritten from scratch.** Said the dedicated altar room is on the 5th floor | rewritten: the dedicated P. Thờ is on **tầng 4**, and it is the **only dedicated ritual room in the building** because tầng 5 has no rooms | IMG_9976, IMG_9977; rule [34] |
| 22 | **P-23** | **rewritten from scratch.** Said the front WC on the 5th floor shared the wall at y = 8900 and the altar's door was on the hall (JSON `door ['tho_f5','hall_front_f5']`) | rewritten: the WC is **not** against the altar room's wall and **not** opposite it - it is one room further back; the adjacency that actually exists is the **thin partition to the reading room**, and the rule is recast around that (solid side wall, 90-degree turn, optional screen) | IMG_9976; rules [25], [33], [35] |
| 23 | P-25 remedy | terrace depths "8800 and 5700 deep in the model" | 3500 clear / 3900 overall front and 6100 long rear, from IMG_9977 | IMG_9977 |
| 24 | P-27 neighbours | neighbour heights cited as `designs/contractor-as-drawn.json` `site.context` | labelled **MODEL / NOT VERIFIED in the scan** - not on any scanned sheet; check on site | model vs transcripts |
| 25 | P-28 balconies | "every upper floor has a front balcony ... y 3500-4900", cited JSON room rects | every level that carries **rooms** (tầng 2, 3, 4) has a balcony; **tầng 5 has the two sân thượng terraces instead** | IMG_9974, 9975, 9976, 9977 |
| 26 | P-29 / P-30 | cited the measurements.md room widths and the "altar room on the 5th floor" | dimension chains on IMG_9972-9977; altar room on tầng 4 | IMG_9972-9977 |
| 27 | P-30 tables | model-only rows were indistinguishable from scan facts | the 900 internal door, 3960 plot width, 2400 counter, 1600 x 2100 bed and the altar room's own 3960 x 4000 are labelled **MODEL**; the front yard depth is corrected to **3360** (rem 228.00, Thien Tai, CAT) | IMG_9972 chain; model figures labelled |
| 28 | P-31 | title said "3.95 m"; plot width and +10 mm margin cited from measurements.md | title says **3.90 m** (what the sheets print); the 3960 figure is labelled MODEL and kept only so the model's reading can be traced | IMG_9972 frontage chains |
| 29 | P-32 | "the model has 900 mm internal doors throughout (JSON `openings`)"; evidence VERIFIED | downgraded to **PARTIAL**: the Dw 700 / 750 reading is VERIFIED; the 900 internal leaf is MODEL | IMG_9974 (PARTIAL) |
| 30 | §4.1 Q6 | asked who sleeps on "tang 2, 3, 4, 5" | "tầng 2, 3 and 4 - tầng 5 has no rooms" | IMG_9977 |
| 31 | §4.2 Step 5 | assigned "Rear bedroom, tang 5" and "P. Thu, tang 5 front" | the tầng 5 row now reads "nobody sleeps here; it is the outdoor room and the stair head"; the altar row reads **P. Thờ, tầng 4 front**, the highest occupied level | IMG_9974-9977 |
| 32 | §4.2 Step 6 | altar walls given as "the rear-side wall (y 8900, shared with the WC) ... and the front wall (exposed facade)", party wall as x = 0 | altar walls are the **party wall** and the **inner wall towards the core**; the rear wall is the thin partition to the reading room and the front wall is the balcony wall with D5 / S1 - both avoided | IMG_9976 |
| 33 | §5 row 2 | "Move the rear WC off the bedroom above it" | reframed: the rear WC stack (ground + tầng 2-4) has no bedroom over it, so the tradition's sharpest prohibition does not apply; the mitigations and the kitchen-hood point are added | IMG_9972, IMG_9974-9977 |
| 34 | §5 row 3 | "Put the altar in the rear of the top floor instead of the front" | reframed: tầng 5 has **no rooms**, so a top-floor altar means a niche on an open terrace, with the weather / fall-protection / load costs named; verdict SKIP the move, ADOPT the rotation | IMG_9977, IMG_9996 |
| 35 | §6.1 item 2 | "keep it off the WC wall and off the front glazing" | "keep it off the balcony wall and off the thin partition to the reading room"; adds that the altar room is on tầng 4, the highest level with a room | IMG_9976 |
| 36 | §6.2 items 2-3 | "Relocating the WCs so none sits under a bedroom" and "Moving the altar room to the rear of the top floor" | item 2: the WC-above-bedroom prohibition **does not apply to this house**; the kitchen under the rear bedroom is named instead. Item 3: tầng 5 has no rooms, so there is nothing to move the altar into | IMG_9976, IMG_9977 |
| 37 | §6.3 | "Keep the bedroom above the WC ventilated because the WC is below it" | "Keep the rear loggia above the WC ventilated, and hood the kitchen straight out through the facade"; the altar bullet re-worded to "against a solid interior wall, off the balcony and off the partition" | IMG_9974-9977 |
| 38 | **§6.4** | "The three things this review could not determine", item 2 being whether a passenger lift exists below the roof | rewritten: **one** thing is undetermined (the facing direction); the **lift is settled** by the scan (with the size conflict referred to the design lane) and the **ground-floor kitchen/WC order is settled** | IMG_9972-9978, IMG_9987, IMG_9988 |
| 39 | §9 Sources | listed the model as the source "used for the room rectangles, the opening list and the site context" and the fidelity ledger's "inferred lift shaft" | the transcripts are now the **primary** source; the model and its memos are marked **superseded**; fidelity.md item (c) - the inferred lift shaft - is explicitly **withdrawn**; `_scan1022/out-phongthuy.before-fix.md` added | this pass |
| 40 | New section | - | `## Corrections 2026-10-22` inserted at the top of the document, listing every change in bullet form | this pass |
| 41 | P-19 beams | used the model's "3.96 m wide room" | "3.90 m wide room (3200 clear between the party walls)" - what the sheets print | IMG_9972 frontage chains |
| 42 | P-26 floor count | "this house is **five occupied floors**" with no note on tầng 5 | unchanged count, but now spelled out: tret, lung, tầng 2, tầng 3 and tầng 4; **tầng 5 adds none**, because it holds no rooms at all | IMG_9977 |

## What was deliberately left alone

- **All 32 finding IDs** stay stable (P-01 to P-32), and the finding-count footer is unchanged.
- The **§2.2 eight-row Bat Trach table** was already correct and is untouched.
- The §1.1 measurement procedure, §2.1 cung-phi formula, §2.3 uses, §4.3 timing layer,
  §4.4 Phi Tinh layer, §7 sources-agree bullets, §8 disagreements list and the whole of
  §9's external source list are unaffected by the scan.
**Corrected in the final pass:** P-19 and P-26 are *also* changed, for two small reasons -
P-19 quoted the model's 3.96 m room width where the sheets print 3.90 m, and P-26's floor
count needed a one-clause note that tầng 5 contributes no floor. The genuinely untouched
findings are therefore **P-01, P-05, P-07, P-14 and P-24** (5 of 32). A per-finding diff
against the backup is reproducible with `python _scan1022/verify_untouched.py`.

- P-19's beam evidence already cited `transcript-beams-slabs.md` and the **bed positions are
  NOT FOUND**, which the scan confirms.

## Sanity-grep counts (final)

Run `python _scan1022/sanity.py`.

```
tho_f5                : 0
wc_truoc_f5           : 0
hall_front_f5         : 0
altar + 5th floor     : 0
5th floor + altar     : 0
P. Thờ on tầng 5      : 0
'P. Thu, tang 5'      : 0
lift-only-inferred    : 0 outside the corrections banner
shaft ... inference   : 0
model ... infers it   : 0
```

The two remaining text matches for "altar" within 200 characters of "tầng 5" are both
*negative* statements - "no rooms at all" and "sits directly under the tầng 5 terrace" -
and the one remaining "only inferred" match is the corrections banner announcing the
withdrawal. No JSON rectangle id survives anywhere in the file.

## Verification performed

```
python _scan1022/fix_run.py        # re-runs the whole pass from the backup, idempotently
python _scan1022/sanity.py         # the counts above
python _scan1022/verify_struct.py  # encoding, headings, finding IDs, table integrity
python _scan1022/verify_untouched.py  # per-finding diff against the backup
```

- Encoding: UTF-8, no BOM, CRLF preserved, 1884 lines, round-trip clean.
- All 32 finding IDs present exactly once; no ID added, none removed.
- The §2.2 eight-row table still has its 8 data rows and was not edited.
- The §5 table still has its 18 rows.
- No markdown table in the file has a column-count mismatch.
- Evidence labels still in use: VERIFIED 104, PARTIAL 13, CLAIMED 14, NOT FOUND 9,
  UNVERIFIED 1, plus the new **MODEL** label 19 times.
