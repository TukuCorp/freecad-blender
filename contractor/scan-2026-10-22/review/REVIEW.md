# Contractor scan review: summary and decisions (2026-10-22)

Set reviewed: 33 phone photos of the construction drawing set for "Nhà ở riêng lẻ", Hồng Bàng, Minh Phụng, HCMC (architecture KT01–KT07 + front elevation + section A-A; foundations, columns, lift pit, stairs, beams, slabs).
Detail lives in three lane reports in this folder. This page is the synthesis, with the corrections I made to the agents' work.

| Lane | File | Findings | Model |
|---|---|---|---|
| Safety (beyond local rules) | `out-safety.md` | 54 | minimax-m3.1-flash-free |
| Design errors and improvements | `out-design.md` | 38 | minimax-m3.1-flash-free |
| Phong thủy | `out-phongthuy.md` (corrected once) | 32 | minimax-m3.1-flash-free |

How it was done: Sonnet subagents transcribed the photos to text (`../transcript-*.md`) because the swarm model cannot see images. The swarm worked only from those transcripts, the earlier spec and fetched codes. I re-read sheets 9972, 9976, 9977 and 9979 myself and spot-checked cited clauses against the agents' saved source text.

## Bottom line

**Do not treat this set as buildable yet.** It contradicts itself in ways that cost money if found on site, and it carries no fire or escape information on the sheets photographed. Resolve the six items below with the contractor before piling and before any slab is poured. Items 1 to 3 are the expensive ones.

1. **Escape and fire strategy** (S-01, S-02, S-04, S-05, S-09). One stair with winders serves 6 occupied storeys to +17.200 (terrace +20.400, parapet +21.900). The lift opens straight onto the stair. A glazed light well sits over the stair. The car bay sits under the double-height void with no separation shown. Balconies are not connected. UK ADB, Singapore SCDF and QCVN 06 all point the same way: a protected route, or a residential sprinkler/mist system. Cheapest route to price first: sprinklers or mist. Also get written confirmation of whether QCVN 06:2022 is mandatory (the house is just under its 7-storey, 25 m and 5 000 m³ triggers; two of those turn on unresolved facts).
2. **Foundation and neighbours** (S-23 to S-29). 250×250 pressed piles, 24 m, 45 t, about 31 piles, 7 in single-pile caps with offset columns. Cap-top levels conflict (−0.500, −0.050, −1.550, −1.650). M1 is quantity "10" with one drawn; section 8-8 is missing. No geotechnical report appears in the set, and both party walls are shared. Ask for the geotechnical report and a neighbour condition survey before pressing.
3. **Structure screening, for a licensed engineer only** (S-30 to S-40). All slabs 100 mm. Columns are 200×350, dropping to 200×200 at the top. DS7 and DS6a are drawn 100 mm wide with 2Ø16, which cannot physically hold the bars. Walls without beams are covered only by a site note ("add 2Ø16 or 3Ø16"). DS2a span 4600 against 4240 elsewhere. Steel Ra 2800 vs 2700. X-hatch has no legend. Nobody here has judged adequacy.
4. **Lift.** Now confirmed to exist (pit sheet, hoist slab, roof overrun, cars in section), which closes the old "inferred shaft" question. But the size is four different numbers: plans 1800×1600, pit plan 2100×2050, hoist slab 2000×2000, roof 2000 wide. Pit floor −1.650 vs −1.550. No waterproofing or sump. Get one dimension set from the lift supplier.
5. **Top of the house.** Tầng 5 is a stair/lift lobby plus two open terraces (no rooms). Guard heights appear nowhere, only "8 mm tempered glass + stainless rail". No guard note at the mezzanine void edge. The stair light-well glass has no load rating. The roof plan is X-hatched with no legend.
6. **Daylight and use** (D-08 to D-12, D-29 to D-32; the design lane's reading, confirm on the DWG). Living room, kitchen and rear bedroom/mezzanine show no windows of their own. Garage is 3.94 m deep against a car of about 4.5 m. Front ensuite is 2.88 m² (TCVN 13967:2024 gives about 3 m², PARTIAL). Laundry and drying space are missing.

## What changed from the earlier model (`designs/contractor-as-drawn.json` is now stale)

| Item | Earlier model | Scan (verified by me where marked *) |
|---|---|---|
| Roof slab / overall height | +23.800 / 25.800 | +20.400 / parapet +21.900 * |
| Tầng 5 | Altar room + WC + bedroom | Lobby + two open terraces, no rooms * |
| Tầng 4 | Two bedrooms | P. Thờ at front, P. Đọc sách, WC, rear bedroom, rear WC, loggia * |
| Lift | Inferred 2000×1800 | Drawn 1800×1600, with pit and hoist details * |
| Stair well | 4000 deep (model choice) | 3200 (structure agrees), 21 risers, mezzanine riser 152 mm |
| Ground floor rear | WC then kitchen | Kitchen next to the core, WC at the rear |
| Mezzanine void | 12300 long | 8140 (PARTIAL) |

I did not edit the spec or regenerate renders. Say so if you want the model re-issued to the scan (design lane D-13/D-36).

## Phong thủy

- **Facing direction: South, about 187° (from map data, 2026-10-23).** The scan has no north arrow, so this comes from the address instead. 506 Hồng Bàng is on the even-numbered north side (old D11, now Minh Phụng ward; OSM shows even 120 north of the road and odd 217/633/751 south of it). That stretch of road runs at about 97°, so the front door faces about 187°: tọa Bắc hướng Nam (Khảm trạch). South is good for all four Đông tứ cung (Chấn Sinh Khí, Tốn Thiên Y, Khảm Diên Niên, Ly Phục Vị) and bad for all four Tây tứ cung. Still confirm with a phone compass at the door: 187° sits on the Ngọ/Đinh 24-sơn boundary.
- **Owner birth data: not in the repo.** The report gives the cung-phi formula (checked against a worked example), the eight-cung table (I checked all eight rows against the standard table), and a questionnaire and decision tree.
- **Real layout:** stair in the middle of the house (the tradition's hardest rule, and not movable: it is the only escape stair). Altar room is at the front of tầng 4 behind a balcony, with the reading room behind it and no WC against its wall. No WC sits above a bedroom. Tầng 5 has no room for an altar.
- **Cheap and worth doing:** bed heads on the party wall, altar rotated to the owner's good direction and kept off front glazing, screen the stair lobby from the entry axis, keep the under-stair space open, turn the hob, check WC door swings, keep the front yard open.
- **Where phong thủy and safety conflict, safety wins** (stair position, door narrowing, mirrors, fish tanks under the stair, venting WC air into the stair).
- It is tradition, not engineering. The report says where schools disagree.

## Corrections I made to the agents' work

- **Phong thủy lane:** its first pass placed the altar on tầng 5 using the stale spec and cited the wrong sheet; it also wrongly called Đông Bắc the "only" direction good for the Tây group. A second pass fixed both (27 findings changed; original kept in `_scan1022/out-phongthuy.before-fix.md`).
- **Design D-01:** rated an ERROR that the top of the house is "drawn three ways". On the photos, plan and elevation can be consistent (set-back lobby behind a front terrace). I treat it as a guard/parapet ambiguity, not an error.
- **Safety S-06, S-09, S-23 (rated CRITICAL):** they rest on absence from a partial photo set (about 9 of 20 architectural sheets) and on the geotechnical report living outside the drawings. A fire sheet or geotechnical report may exist. 24 m pressed piles are also routine in HCMC. I read them as HIGH and as questions to ask, not as proven defects. S-01 stays top because a single stair is visible on every plan.
- **Design report:** "four untranscribed photos (`jpg/sheet1–4`)" are my contact sheets, not drawings. TCVN 13967 figures are PARTIAL (a legal Q&A site, not the standard's text).

## Evidence limits

- Everything comes from photo transcriptions, not the DWG. Figures marked PARTIAL in the transcripts are not used as proof.
- QCVN 03, TCVN 2737/4451/9386/6396 were not retrievable; NFPA 101 and IBC clauses are not quoted. QCVN 06 text came from a third-party mirror. Get official copies before submission.
- No flood levels, soil data, MEP sheets, door/window schedule, stair detail or title-block stamps were available. The structural sheet count is disputed (agents say 18 and 24).

## Send these first (full lists: `out-design.md` §5, 25 questions; `out-safety.md` §12, 26 questions)

1. Are tầng 5 and the roof terrace as KT06 shows (lobby + terraces), and what are the guard heights?
2. Is QCVN 06:2022 applied? Storey count, PCCC height and volume used.
3. Geotechnical report and neighbour condition survey; reconcile cap levels and quantities; issue section 8-8.
4. One lift shaft size, pit level and supplier data sheet.
5. Fire-safety sheet, door and window schedule, stair detail, MEP sheets, and the remaining architectural sheets.
6. Replace the "add 2Ø16 under walls" note with a wall-beam layout; fix DS7/DS6a and DS2a.
7. Windows and kitchen/living-room openings; garage depth and separation; confirm the 2600 rear boundary element.

## Housekeeping

- Local only, nothing committed. `contractor/new contractor scane.zip` and `contractor/scan-2026-10-22/` (heic ≈16 MB, jpg, transcripts, reports) are untracked, and `_scan1022/` holds the agents' scratch files (fetched pages, scripts). I did not touch `.gitignore`.
- Briefs and agent outputs stay here as the audit trail.
