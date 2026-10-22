# Brief design: errors and improvements in the contractor construction set (architecture, consistency, livability)

Folder: the project root (`C:\Users\tukum\Downloads\freecad-blender`). Output file: `contractor/scan-2026-10-22/review/out-design.md`. Throwaway files go in `_scan1022/`. Today is 2026-10-22 (Asia/Ho_Chi_Minh).

Context: The owner is about to build a 5-storey narrow tube house (plot about 3.95 m x 25 m, Minh Phung ward, Ho Chi Minh City, party walls both sides, street on one short side, tapered ~7 degree boundaries). Levels: ground 3.8 m, mezzanine 3.2 m with a double-height void over the front, floors 2-5 at 3.4 m, a roof terrace, a lift plant room on the roof. The contractor delivered a full drawing set, photographed page by page. A vision model transcribed the photos into text (you cannot see images; work only from the text files). Your job: find design ERRORS (internal contradictions, impossible or doubtful dimensions, missing items, drawing-to-drawing mismatches) and design IMPROVEMENTS (livability, daylight, ventilation, circulation, storage, service stacking, buildability), using international residential design practice, not only local rules. Another agent covers life-safety/structure (`safety` lane) and another feng shui (`phongthuy` lane); stay on design. Mention a safety or feng shui point only as a one-line cross-reference.

## Inputs (read these first)
1. `contractor/scan-2026-10-22/transcript-architecture.md`
2. `contractor/scan-2026-10-22/transcript-foundation-stairs.md`
3. `contractor/scan-2026-10-22/transcript-beams-slabs.md`
4. `designs/contractor-as-drawn.fidelity.md`, `designs/contractor-as-drawn.measurements.md` (an earlier reading of the five architectural PDFs; many open questions are listed there, notably (c) whether a lift shaft exists, (a) the skewed boundaries, (d) the ensuite subdivision, (g) stair depth 3200 vs 4000)
5. `designs/contractor-as-drawn.json` (the compiled spec of that earlier reading: rooms, x/y/w/d in mm, storeys). Read it with a small script; print only room id, floor, size.
Transcript confidence labels: READ, PARTIAL, ILLEGIBLE. Do not build an ERROR finding on an ILLEGIBLE or PARTIAL figure alone; list it under "needs confirmation".

## Task
1. **Cross-check scan vs earlier reading.** Compare the new set with `contractor-as-drawn.json` and the measurements file: storey heights, dimension chains, room sizes, stair size and tread counts, lift (does the lift pit sheet now prove a shaft exists, and where and how big), light wells, void extents, balconies, WC positions. List every match, mismatch and newly resolved open question (use IDs (a)...(n) from the fidelity file where they apply).
2. **Drawing-internal consistency.** Plan vs section A-A vs elevation vs structure: floor levels and storey heights, column grid vs room walls, beams crossing rooms, void edges vs beam layout, stair openings in slabs vs plans, lift shaft stacking and pit vs overrun, roof level vs parapet, dimension strings that do not sum, scale statements, duplicated or missing sheet numbers, notes that contradict drawings, stair tread count vs floor-to-floor height (riser = height / risers).
3. **Livability of a tube house (apply best practice).** Daylight and cross-ventilation along a 25 m deep, 3.95 m wide plan (light wells, sky-lights, rear garden, ventilation stack), dark core and interior rooms, bedroom window access, privacy to the street, room widths after wall thickness (a 3.95 m plot with 200 mm walls leaves about 3.5 m clear), garage fit (turning, door width, ramp, doors opening against cars), living room proportions, kitchen layout and extraction, laundry and drying (a huge daily need in HCMC rain), storage, WC counts and sizes, the stacking of wet areas, noise from the lift/stair against bedrooms, thermal comfort in tropical sun (west-facing facade? roof heat gain, shading, balcony depth), rain and monsoon drainage, roof terrace use, mezzanine void and its heat/sound behaviour, adaptability for family growth.
4. **Buildability and cost traps.** Slab-to-slab clashes, thin walls hosting MEP, shafts missing for plumbing/drainage/AC condensate, services stack alignment, beam-over-wall clashes, spans that need deep beams, repetitive floors that could be simplified, details that invite leaks (balcony slab edges, roof, lift pit).
5. **Improvements ranked by impact/cost.** At most 12, each with a sketch-level fix described in words and dimensions, and its effect on the neighbouring floors.
6. **Questions for the contractor/architect**, numbered, ready to send.

## Rating for every finding
One block per finding: `ID` (D-01...), `Type` (ERROR / INCONSISTENCY / RISK / IMPROVEMENT), `Severity` (HIGH / MEDIUM / LOW), `Where` (sheet and quoted transcript line, plus the spec room id if any), `Issue`, `Why it matters`, `Basis` (design rule or published guidance; name it), `Basis class` (LOCAL-MINIMUM / BEYOND-LOCAL / JUDGEMENT), `Fix`, `Cost/impact` (S/M/L), `Evidence label`.

## Evidence rules
- Allowed, by weight: the transcripts and spec (primary); published codes and design references (Neufert, Singapore/HK/UK/US residential guidance, Passivhaus tropical guidance, building-science references); government regulations. Excluded as evidence: forums, social media, anonymous testimonials, SEO list sites, AI-generated summaries.
- Label every claim: VERIFIED (source seen; transcript file and line, or URL and date), PARTIAL, CLAIMED, NOT FOUND, UNVERIFIED. A rule quoted from memory without fetching it is UNVERIFIED. If you have no web access, still do the review from the transcripts and mark external rules UNVERIFIED. NOT FOUND is an acceptable answer. Never invent dimensions, standard numbers or drawing values.
- Do not redesign rooms. Describe the smallest change that fixes each finding (project rule: minimal, spec-driven changes; keep the core zone and rear light well aligned across floors).

## Hard rules
1. Do not print or paste raw page dumps, raw HTML or raw JSON into the terminal or any file. Extract fields with a script and write short rows.
2. No personal contact details of private individuals.
3. English prose; keep Vietnamese room labels verbatim with diacritics where quoted.
4. UTF-8 for all files; in Python pass encoding="utf-8" and reconfigure stdout. Avoid the dollar sign in shell text.
5. Be economical with memory: no browser tabs; fetch with scripts. Edit no file except your output file and files under `_scan1022/`.
6. If the transcripts are thin on a topic, say so rather than guessing.

## Output
`contractor/scan-2026-10-22/review/out-design.md`: Method and evidence limits; Scan vs earlier-reading table (item, earlier value, scan value, status MATCH / MISMATCH / NEW / CANNOT TELL); Findings (blocks above), grouped ERROR first; Top 12 improvements; Questions for the contractor; What the sources agree on (5 bullets); Where sources conflict or are thin; Sources (numbered, with label).

## Last action (mandatory)
When the file is finished, as your very last action run:
herdr agent prompt w3D:p1 "design finished: N findings, file contractor/scan-2026-10-22/review/out-design.md"
(replace N with the real finding count; do not use --wait). If you could not finish, still run it with the true state, for example "design finished: partial, file contractor/scan-2026-10-22/review/out-design.md".
