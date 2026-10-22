# Brief safety: life-safety and structural-safety review of the contractor construction set (beyond local regulation)

Folder: the project root (`C:\Users\tukum\Downloads\freecad-blender`). Output file: `contractor/scan-2026-10-22/review/out-safety.md`. Throwaway files go in `_scan1022/`. Today is 2026-10-22 (Asia/Ho_Chi_Minh).

Context: The owner is about to build a 5-storey narrow tube house ("nha pho / nha ong", plot about 3.95 m wide x 25 m deep, Minh Phung ward, Ho Chi Minh City, soft Mekong-delta type clay, party walls both sides). Levels: ground (tret) 3.8 m, mezzanine (lung) 3.2 m with a double-height void over the garage and living room, floors 2-5 at 3.4 m, a roof terrace (san thuong), and a lift plant room on the roof. The contractor delivered a full drawing set, photographed page by page. A vision model has already transcribed the photos into text (you cannot see images; work only from the text files below). Your job is an independent safety audit that goes beyond the minimum Vietnamese rules: the owner wants international best practice, not just permit compliance. Other agents cover design errors (`design` lane) and feng shui (`phongthuy` lane); stay on safety. Do not review aesthetics or feng shui.

## Inputs (read these first, in this order)
1. `contractor/scan-2026-10-22/transcript-architecture.md` (floor plans, roof, front elevation, section A-A)
2. `contractor/scan-2026-10-22/transcript-foundation-stairs.md` (foundations, columns, lift pit, stairs, general notes with concrete/steel/pile data)
3. `contractor/scan-2026-10-22/transcript-beams-slabs.md` (beams, slab rebar, general notes)
4. `designs/contractor-as-drawn.fidelity.md` and `designs/contractor-as-drawn.measurements.md` (an earlier reading of the contractor's architectural PDFs; its rooms, dimensions and open questions, notably whether a lift shaft exists)
Transcript confidence labels: READ, PARTIAL, ILLEGIBLE. A PARTIAL or ILLEGIBLE figure must never be the sole basis of a CRITICAL finding; flag it as "needs the DWG / contractor confirmation" instead.

## Task
Work through this checklist. For each topic give a finding or an explicit "no issue found / cannot assess (reason)".
1. **Means of escape.** A 5-storey + roof house with one stair and a single street frontage is the classic tube-house trap. Check: number of stairs, stair width and enclosure, rear escape route or secondary exit, travel distance from the farthest bedroom to the street, door swing, whether the stair is open to the mezzanine void (smoke spread), roof refuge/access, lift not usable in fire. Compare with international practice (NFPA 101 residential, IBC 2021 ch.10, UK Approved Document B for tall small houses, Singapore SCDF code for shophouse-type) and name where Vietnamese QCVN 06:2022/BXD is the floor.
2. **Fire and smoke.** Compartmentation between floors, kitchen at the rear of ground floor, garage under living space (vehicle and EV charging fire load), smoke control in stair and void, smoke alarm / heat alarm / sprinkler or residential-mist recommendation, fire-rated stair door, party-wall fire resistance, escape windows (window grilles/cages are a notorious killer in Vietnamese houses: check whether openable emergency egress exists).
3. **Stair geometry and falls.** Riser/tread/headroom/width from the stair sheets against QCVN 03 / TCVN 4451 and against IBC/ADA/UK values; tread count per flight and landing; handrail height and continuity; winder or U-turn risks; stair opening vs mezzanine void edge protection; balcony and terrace parapet heights (front balconies, roof terrace; glass type if shown); child-safe baluster spacing (100 mm sphere rule); slippery finishes in wet zones.
4. **Foundation and ground.** Pile type, size, design load, pressing criteria, pile cap sizes, grade beams, from the foundation transcript and its notes; soft-clay settlement; neighbour-wall undermining (both party walls are shared: underpinning, excavation shoring, monitoring of adjacent houses, pre-construction condition survey); basement-free lift pit depth vs groundwater level, flood level in HCMC (tide, heavy rain) and waterproofing; ground floor level vs street level and flood risk; pile pressing vibration.
5. **Structure (screening only).** You are not a structural engineer and must not claim adequacy. Screen for red flags a licensed engineer should confirm: concrete grade and steel grade stated, cover (durability in humid tropical conditions), beam spans and sizes vs span/depth rules of thumb (about L/12 to L/15 for continuous RC beams), slab thickness vs span (about L/30 to L/35), column sizes at the lower floors for 6-7 levels carried on a 3.95 m frontage, slender columns around the mezzanine double-height void (unbraced height 7 m), discontinuities (columns not stacking, beams terminating on slabs), cantilevers/balconies, lift-pit and hoist-hook beam loads, seismic detailing (TCVN 9386:2012; HCMC is low seismicity but note wind and soft soil), robustness against progressive collapse.
6. **Construction-phase safety.** Narrow site: scaffolding, access, crane/hoist, falling objects onto neighbours and street, temporary works for deep excavation, working at height around the void and stair, formwork stripping times, curing in heat, concrete pour sequence on narrow plots.
7. **MEP and health.** Electrical (RCD/ELCB, earthing, surge protection, lightning protection for a 24 m tall narrow roof with a metal plant room), gas/LPG storage, water heater placement, waterproofing of wet areas stacked over bedrooms, ventilation of the interior WC / dark core (mould, CO, radon-like accumulation in the long deep plan), natural light and ventilation adequacy in the core, termite protection, asbestos-free materials, indoor air.
8. **Lift safety (if a shaft exists).** Pit depth, overhead height, machine-room-less vs plant room, fire-fighter's lift recommendation, rescue operation, landing doors opening onto the stair lobby.
9. **Accessibility and ageing in place.** Whether a future elderly or wheelchair user can live there; lift door width, bathroom clear space, step-free route to the lift.
10. A closing table "Top 10 actions before pouring concrete", ranked.

## Rating for every finding
Use this block, one per finding: `ID` (S-01...), `Severity` (CRITICAL / HIGH / MEDIUM / LOW), `Where` (sheet name and transcript file with a quoted line), `Issue`, `Why it matters` (one failure scenario), `Basis` (the standard or published guidance, section number if you know it), `Basis class` (one of: LOCAL-MINIMUM = Vietnamese rule; BEYOND-LOCAL = international or good-practice recommendation not required locally; JUDGEMENT = your engineering reasoning), `Fix`, `Who decides` (owner / architect / licensed structural engineer / fire consultant / contractor), `Evidence label`.

## Evidence rules
- Allowed, by weight: official standards texts and government circulars; published codes (NFPA, IBC, Eurocode, UK Approved Documents, Singapore codes); reputable engineering references; the transcripts of the actual drawings.
- Excluded as evidence: forum posts, social media, anonymous testimonials, SEO list sites, AI-generated summaries.
- Label every claim: VERIFIED (source seen via a fetched page or the transcript; give the URL and date, or the transcript file and line), PARTIAL, CLAIMED, NOT FOUND, UNVERIFIED. A standards clause quoted from memory without fetching it is UNVERIFIED; say so. If you have no web access, still do the review from the transcripts and label every external citation UNVERIFIED. NOT FOUND is an acceptable answer. Never invent clause numbers, figures, standard numbers or drawing values.
- You may not state that anything is structurally adequate or compliant. Use "screening observation, to be confirmed by a licensed engineer".

## Hard rules
1. Do not print or paste raw page dumps, raw HTML or raw JSON into the terminal or any file. Extract fields with a script and write short rows.
2. No personal contact details of private individuals.
3. Write in English, but keep Vietnamese sheet names and note text verbatim with diacritics where you quote them.
4. UTF-8 for all files; in Python pass encoding="utf-8" and reconfigure stdout. Avoid the dollar sign in shell text.
5. Be economical with memory: no browser tabs; fetch with scripts and keep only the fields you need. Edit no file except your output file and files under `_scan1022/`.
6. Do not overstate. If the transcripts are too thin on a topic, say "cannot assess from the transcript" instead of guessing.

## Output
`contractor/scan-2026-10-22/review/out-safety.md`: Method and evidence limits; Findings grouped by checklist topic (finding blocks as above); Top 10 actions before pouring concrete; Items that need the DWG or a confirmation question to the contractor (numbered questions, ready to send); What the sources agree on (5 bullets); Where sources conflict or are thin; Sources (numbered, with label).

## Last action (mandatory)
When the file is finished, as your very last action run:
herdr agent prompt w3D:p1 "safety finished: N findings, file contractor/scan-2026-10-22/review/out-safety.md"
(replace N with the real finding count; do not use --wait). If you could not finish, still run it with the true state, for example "safety finished: partial, file contractor/scan-2026-10-22/review/out-safety.md".
