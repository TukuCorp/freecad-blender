# Design review — contractor construction set (architecture, consistency, livability)

Project: NHÀ Ở RIÊNG LẺ, 506 ĐƯỜNG HỒNG BÀNG, PHƯỜNG MINH PHỤNG, TP.HCM.
Review date: 2026-10-22 (Asia/Ho_Chi_Minh). Lane: `design`.
Scope: internal consistency, drawing-to-drawing match, livability and buildability of the issued set.
Out of lane: life-safety and structure (`safety` lane), feng shui (`phongthuy` lane) — cross-referenced in one line only where they touch a design finding.

---

## 1. Method and evidence limits

**What I read (all in-repo, all read in full):**

| # | Source | Status |
|---|---|---|
| S1 | `contractor/scan-2026-10-22/transcript-architecture.md` (9 sheets, IMG_9972–9980) | VERIFIED (read 2026-10-22) |
| S2 | `contractor/scan-2026-10-22/transcript-foundation-stairs.md` (IMG_9981–9988, 0003–0005) | VERIFIED (read 2026-10-22) |
| S3 | `contractor/scan-2026-10-22/transcript-beams-slabs.md` (IMG_9989–9999, 0001–0002) | VERIFIED (read 2026-10-22) |
| S4 | `designs/contractor-as-drawn.measurements.md` rev.2 | VERIFIED (read 2026-10-22) |
| S5 | `designs/contractor-as-drawn.fidelity.md` rev.4 (open items a–n) | VERIFIED (read 2026-10-22) |
| S6 | `designs/contractor-as-drawn.json` (compiled spec) | VERIFIED (parsed by script `_scan1022/rooms2.py`; only id / floor / rect printed) |
| S7 | `contractor/*.pdf` (5 architectural PDFs of the earlier reading) | VERIFIED as **textless**: PyMuPDF extraction returns 0 characters on all five pages (`_scan1022/pdftext.py`), so every earlier figure is a visual read, and no PDF text could be used to re-verify a transcript claim. |

**External references used** (fetched 2026-10-22):

| # | Reference | Label |
|---|---|---|
| X1 | TCVN 13967:2024 *Nhà ở riêng lẻ – Yêu cầu chung về thiết kế*, §5.10 Table 1 (via `tieuchuan.vsqi.gov.vn`) — min. usable area single bedroom 9 m², double bedroom 12 m², WC 3 m²; min. clear height bedroom/living 2.6 m, WC 2.3 m | VERIFIED |
| X2 | 2024 IBC Chapter 10 (via `codes.iccsafe.org`) — dwelling stair max riser 197 mm, min tread 254 mm | VERIFIED |
| X3 | Stair comfort rule 2R + G = 600–630 mm (R riser, G going) | VERIFIED (search result, 2026-10-22) |

**Evidence limits you must read before acting on this review:**

1. **I could not see any drawing.** All findings come from the vision-model transcripts (S1–S3). The transcripts are themselves a reading of photographs; where they disagree with each other or with the earlier PDF reading (S4/S5), the *drawing* is the authority and I cannot adjudicate it. Every such case is written as a question for the designer, not as a verdict on the building.
2. **The architectural dossier is incomplete.** The title block states a 20-sheet architectural set; only 9 sheets (KT01–KT07 + 2 partial) were photographed. The structural set is 24 sheets and all 24 photos are covered by S2/S3, but many sheet codes are cut off. Four further photographs (`jpg/sheet1–sheet4.jpg`) are represented in **no** transcript and their content is unknown to me. Consequence: no door/window schedule, no architectural stair detail (the section says *"Xem chi tiết cầu thang"* and that sheet is not in the set), no general-notes sheet, no structural connection details, no MEP drawings at all were available.
3. **No MEP / architectural-services sheets exist in what I was given.** Every services finding below is inferred from the absence of anything on the architectural sheets, and is labelled accordingly.
4. **Orientation is unknown.** No sheet carries a north point (S5 confirms this for the earlier set too). Which façade is west — and therefore which façade takes the afternoon sun — cannot be established from this evidence. I do not assert it.
5. Published design references beyond X1–X3 (Neufert, Singapore BCA, HK Housing, UK Approved Document, Passivhaus tropical guidance) could not be fetched within this session's search allowance. Where such a rule would normally be cited I have instead used the local standard X1 or stated the rule as JUDGEMENT and marked the external basis UNVERIFIED. I have not invented citations.
6. Every dimension quoted below is transcribed by the vision model from a photo. Figures marked READ are treated as reliable; figures marked PARTIAL are never used to found an ERROR finding, and are collected in §7.

**Arithmetic checks I ran myself** (`_scan1022/chk.py`, all VERIFIED): dimension-chain sums for KT01/KT02/KT03/KT06 and the structural grid; riser = storey height / risers for all three stair heights; WC floor areas; clear width at 3900 plot width; storey-height sums for both the elevation and the earlier reading.

---

## 2. Scan vs earlier reading (S1–S3 vs S4–S6)

Status key: **MATCH** (same value, both readings) · **MISMATCH** (different values) · **NEW** (only in the scan) · **RESOLVED** (an open item from S5 closed by the scan) · **CANNOT TELL** (evidence insufficient).

| # | Item | Earlier reading (S4/S5/S6) | Scan (S1–S3) | Status |
|---|---|---|---|---|
| 1 | Plot depth | 25000 | 25000 (printed overall on every sheet) | MATCH |
| 2 | Plot width | 3960 (model) / "3950 printed on every sheet" | 3900 overall at front, 3200 clear, 350 wall each side; rear 3900 / 3500 / 3950 (PARTIAL) | MISMATCH — model overstates by 60 mm |
| 3 | Skewed boundaries, open item **(a)** | ~7.2° taper, front and rear boundaries not parallel to the party walls | "The rear edge of the plot and the yard are drawn slanted (taper)"; 3900 at front vs 3900/3500/3950 at rear; M8a footing drawn with a slanted edge | RESOLVED — taper CONFIRMED in the set; the orthogonal plot rectangle remains a model simplification |
| 4 | Storey heights (ground→roof) | 3800 / 3200 / 3400 / 3400 / 3400 / 3400 / 3200 | 3800 / 3200 / 3400 / 3400 / 3400 / **3200** / 1500 parapet (elevation tags; section tags identical) | MISMATCH — tầng 5 is 3200, and there is no 3200-high terrace storey |
| 5 | Overall building height | +23.800 roof slab, plant to +25.800 (23800 total) | 21900 overall (elevation), 20400 to roof slab (section) | MISMATCH — the earlier model stands ~1900 mm too tall |
| 6 | Lift shaft, open item **(c)** | No shaft labelled on any floor plan; 2000×1800 shaft *inferred* from the roof plant-room label; "weakest piece of provenance in this file" | Shaft **drawn** 1800 wide × 1600 deep with an X on every plan (KT01–KT06); lift cars with 1000 doors at every level in section; pit detail sheet (KC…, 9987); hoist slab (9988); roof overrun labelled *"Ô kỹ thuật thang máy"* | RESOLVED — a lift exists, stacked, with a pit and an overrun; but its **size** now conflicts with the earlier 2000×1800 (see D-02) |
| 7 | Lift pit | Section showed no pit; schema has no construct for it | Pit detail sheet: 1600 clear depth, 200 walls, floor at −1.650, 150 slab, 300×500 beams | NEW / RESOLVED — pit exists (see D-02) |
| 8 | Stair well depth, open item **(g)** | Drawn 3200 enlarged to 4000 in the model to satisfy the pipeline's Blondel rule | Structural stair sheets KC23/KC24: "Well 3900 (A to B) x 3200 (axes 3 to 3a)" — 3200 confirmed by the structure | RESOLVED — 3200 is the drawn and built dimension; the earlier 4000 was a modelling artefact. See D-06/D-07 for what the 3200 still costs |
| 9 | Stair flight width | 2 × 1154 + 697 well = 3005 | Architectural plan: 1250 + 500 + 1250 = 3000 (ground, mezzanine), 1350 + 500 + 1350 = 3200 (floors 2–4); structural sheets: 1350 + 500 + 1350 = 3200 (ground *and* mezzanine) | MISMATCH — and the two halves of the set disagree with each other (D-06) |
| 10 | Riser count per storey | Not determinable (stair detail absent) | 21 risers per storey confirmed on KC23/KC24: ground 176.2, mezzanine 152.4, upper 162.0 (all with 250 going) | RESOLVED — and it creates a new problem (D-07) |
| 11 | Ensuite WC subdivision, open item **(d)** | WC 1950×1600 + hall 2010×1600 (model's own tiling choice) | Front ensuite 1800 wide (850 + 950) × 1600 deep, door Dw 700/750 | MISMATCH — 1800, not 1950; area 2.88 m² (D-11) |
| 12 | Rear WC size | 1600 deep × full width, "printed identically to the ground-floor WC" | Rear WC 1600 wide × 2100 long, with 650/800/400 stacked on its rear side | MISMATCH — the two ensuites are *not* identical, and the ground WC is a different room again (D-16, D-17) |
| 13 | Mezzanine void extent | Void over y 0–12300 (garage + living room), i.e. 12300 long | "The front yard and the whole front interior (about 8140 long) are marked *Thông tầng*"; bottom chain 3360 | 8140 | 11200 | MISMATCH — the void is 8140, not 12300 (D-12) |
| 14 | Light wells | Not modelled; S5 (b) recorded the roof skylight as one glazed insert over the stair | *Ô lấy sáng* beside the front ensuite WC on floors 2–4, 1600 wide; on floor 5 a glazed well 2000 × 1500 over the hall; two on the roof (1200, 1300/1500); stair well glazed | NEW — the set has a light-well system the earlier reading never recorded |
| 15 | Balconies | 1400 deep, recessed, modelled on floors 2–5 | 1400 deep on the grid, door D5 + window S1, floor SB2/3/4/5 | MATCH |
| 16 | Rear loggia | Present in the model only as a room on the roof terrace; not present on floors 2–4 | *Lô gia* on floors 2–4, rear, with door D3 and floor SB2/3/4 | MISMATCH — the earlier model omits the rear loggia from floors 2–4 entirely |
| 17 | Tầng 4 programme | Two bedrooms + two WCs | *P. Thờ* + *P. Đọc sách* (thin partition, 3010 + 4240 grid) + *P. Ngủ* (rear) + two WCs | MISMATCH — the earlier model put P. Thờ on tầng 5 and had no reading room at all (D-13) |
| 18 | Tầng 5 programme | P. ThỜ (altar) + front ensuite WC + rear bedroom | No rooms at all: a 5200-long stair/lift lobby with doors D6 and D7, and two open terraces *Sân thượng* (front 3500 clear, rear 6100) | MISMATCH — tầng 5 is a lobby + terraces (D-13, D-01) |
| 19 | Roof plant room, open item **(i)** | 2000 × 1800, 2000 high, on the roof | *Ô kỹ thuật thang máy* 2000 wide on the roof plan; section shows the overrun 1300 high (PARTIAL); hoist slab 2000 × 2000, 120 slab over 180 beam | MISMATCH — height 2000 vs 1300 (D-03) |
| 20 | Roof slab extent | Roof covers the core; terraces open | Roof plan (KT07) is X-hatched over almost the entire footprint (front 1200×3500 strip, 3010, 4240, 2300 incl. the stair well, rear 5200/6100); only the core is roofed | MISMATCH — and the X convention has no legend anywhere (D-14) |
| 21 | Rear yard depth | 2000 printed, compressed to 1200 in the model | Rear zone 2650 (A side) / 2300 (B side) | MISMATCH — the model took 800 mm that the drawing does not give away |
| 22 | Front yard | 3500 | 350 (grid) / 2810–2460 (internal chains, inconsistent) | CANNOT TELL — chains do not close (D-04) |
| 23 | Ground living room | P. Khách 4800 deep, entered from the garage | P. Khách 3800 internal / 4000 grid, between garage and stair core, **no window tag and no door tag** | MISMATCH — depth 4000 not 4800, and the room is now windowless (D-09) |
| 24 | Ground kitchen | BẾP + ĂN, 4100 deep, at the rear | *P. ăn + bếp* 4400 / 4500, at the rear, with sink, hob and fridge drawn; no window tag | MISMATCH — depth 4400/4500, and no window (D-08) |
| 25 | Grid axis naming | n/a | Axes 1–7 with 5a on the plans; DS1a labels the same grid 4/5/6/**7**; DS2 labels 5a as "5" | NEW — inconsistent between sheets (D-05) |
| 26 | Structural grid | n/a | Axes 1–2–3–4–5–(5a)–6 along the length, A and B across the 3900 width; bays 3010 / 4240 / 4000 / 3200 / 1800 / 4400 / 1700 = 22350 | NEW — the structural bay chain is not the same as the architectural room chain, and the gap between them is unreconciled (D-04) |
| 27 | Foundation | n/a | 24 structural sheets read: ~31 piles 250×250, 24 m long, Pcọc 45 t; caps M1–M8; C1 (13), C2 (1), C3 (3), Cc (2) | NEW (mostly structural; one design-relevant item, D-25) |
| 28 | Slab thickness | n/a | "TẤT CẢ CÁC SÀN DÀY 100 (mm)" on every slab sheet, but lift pit slab 150 and hoist slab 120 | NEW — three thicknesses, one rule (safety lane owns the structural consequence) |
| 29 | Sheet count / control | n/a | Architecture title block shows a total of "20" (unconfirmed); structure "KCnn / 24"; PHẦN GHI CHÚ empty on every sheet; no designer, stamp, date or revision visible on any photo | NEW (D-15) |

**Summary of the cross-check:** the scan **closes** open items (a), (c), (g) and the stair-riser question, and it **opens** two large ones the earlier reading never saw: tầng 5 is a lobby with two open terraces (not a habitable floor), and tầng 4 carries *P. Thờ* + *P. Đọc sách* (not two bedrooms). The earlier model should be considered superseded on programme and on height before any further use of it.

---

## 3. Findings

Order: ERROR first, then INCONSISTENCY, RISK, IMPROVEMENT. Cross-references to the `safety` and `phongthuy` lanes are one line each, as the brief requires.

### ERROR

**ID** D-01 · **Type** ERROR · **Severity** HIGH
**Where** KT05 (*MẶT BẰNG TẦNG 4*, IMG_9976) · KT06 (*MẶT BẰNG TẦNG 5*, IMG_9977) · KT07 (*MẶT BẰNG MÁI*, IMG_9978) · *MẶT ĐỨNG CHÍNH* (IMG_9979) · *MẶT CẮT DỌC A-A* (IMG_9980). Spec rooms: `tho_f5`, `san_thuong_truoc`, `san_thuong_sau`, `stairwell`, `elevator`.
**Issue** The top of the building is drawn three different ways. The elevation (IMG_9979) draws the band +17.200 → +20.400 as an enclosed storey: a door D6 (1000 wide × 1100 high) on the left, a window S2 (1200 wide) on the right, a balustrade rail, and a solid 1500 parapet block above +20.400 (400 + 1100). The floor-5 plan (IMG_9977) shows the same level (+17.200) as *only* a 5200-long stair/lift lobby with two open terraces, doors D6 and D7, and three floor drains. The roof plan (IMG_9978) shows the roof almost entirely X-hatched, with the lift overrun and two light wells. The section (IMG_9980) shows an X-hatched void above +17.200 up to +20.400 with the lift overrun above it. A door D6 on the elevation and a door D6 to the front terrace on the plan are the same tag on the same wall and cannot be the same thing.
**Why it matters** The owner is being asked to approve and pay for a fifth storey. As drawn it is not decidable whether the owner gets (a) an enclosed 3200-high top floor with a 1500 parapet, (b) an open terrace at +17.200 with the roof 3200 above it and no ceiling, or (c) an enclosed top floor plus a terrace behind it. It also decides the roof waterproofing extent, the plant-room mass, the cost of the top floor, and whether the top floor is habitable.
**Basis** Internal drawing consistency: a single storey cannot be enclosed on the elevation and open on the plan. Architectural practice: the section, plan and elevation must agree on enclosure before a construction set is issued for pricing.
**Basis class** JUDGEMENT (drawn from the transcripts; the drawings themselves are the authority)
**Fix** Re-issue KT05/KT06/KT07/elevation/section as one coordinated top-of-house set. State explicitly: (i) which level is the terrace and what its finished level is; (ii) whether the 1500 above +20.400 is a parapet on a slab that exists, or a screen on an open deck; (iii) whether the elevation's D6/S2 are doors into an enclosed room or into a screened terrace, and label them distinctly if so.
**Cost/impact** S (drawing re-issue) / L (cost of the outcome, which is what is really at stake)
**Evidence label** VERIFIED (all five sheets transcribed as READ by S1; the inconsistency is between the transcripts, not within one of them)

---

**ID** D-02 · **Type** ERROR · **Severity** HIGH
**Where** KC… *CHI TIẾT HỐ THANG MÁY* (IMG_9987) · KC… *CHI TIẾT NÓC THANG MÁY / MÓC TREO* (IMG_9988) · KT01–KT06 (IMG_9972–9977) · *MÓNG CỐT THANG MÁY* on IMG_9981. Spec rooms: `elevator`, `hall_elev`.
**Issue** The lift shaft is four different sizes in four different documents.
- Plans KT01–KT06: shaft **1800 wide × 1600 deep** (X-marked), door 1000, lobby side dims 200 / 300 / 1000 / 300 / 200 / 700.
- Pit detail IMG_9987, section: clear width **1600 between wall inner faces**, walls 200, overall **2000** wall-face-to-wall-face.
- Pit detail IMG_9987, plan: overall **2100 × 2050**, written as 300 | 1500 | 300 and 300 | 1450 | 300 — i.e. an internal clear of 1500 × 1450.
- Hoist slab IMG_9988: **2000 × 2000** (200 | 800 | 800 | 200), with DM1/DM2 beams 200 × 300.
- Roof plan KT07: *Ô kỹ thuật thang máy* **2000 wide**, plan 1800 + 900.

The 1800 × 1600 architectural shaft cannot contain the 2100 × 2050 structural pit, and the 2000 × 2000 hoist slab has nothing to sit on if the shaft is 1800 wide. Pit level is also given twice: −1.650 on the pit sheet and M6, −1.550 on the foundation layout callout *"MÓNG TH. MÁY Ở CAO ĐỘ -1.550"* and on the M4/M5 cap tops.
**Why it matters** The lift supplier prices and sets the guide rails against one of these numbers. If the pit is built 2100 × 2050 under a 1800-wide shaft, the shaft walls are in the wrong place and the whole core must be rebuilt; if the shaft is built at 1800 × 1600, the pit is over-sized and wasted. Level ambiguity of 100 mm at the pit floor is a standing-water problem in a pit that already has no waterproofing, no sump and no drain shown.
**Basis** Drawing consistency; the lift must be a single continuous geometric object from pit floor to hook, and its manufacturer will confirm the required shaft from its own data sheet.
**Basis class** JUDGEMENT
**Fix** Nominate one shaft rectangle and one pit level, print them in a single table on the lift detail, and dimension the pit's *outer* face, not its inner. Until then, do not order the lift or build the pit walls. Get the supplier's minimum-shaft and pit-depth data sheet and make the drawings to it.
**Cost/impact** S (resolve) / L (rebuild of the core if built on the wrong number)
**Evidence label** VERIFIED (all figures READ in S2/S1; the four sizes are mutually exclusive on their face)

---

**ID** D-03 · **Type** ERROR · **Severity** MEDIUM
**Where** KT07 (IMG_9978) · IMG_9980 (section) · IMG_9979 (elevation) · IMG_9988 · earlier reading S5 (i) / S4 roof section.
**Issue** The lift overrun height is given three ways and none of them reconcile with the stated overall height. The section (IMG_9980) shows the overrun above +20.400 with "1300" beside the SM tag (PARTIAL). The earlier reading of the same sheet (S4) read the plant room as 2000 high, standing +23.800 → +25.800. The elevation's overall height is **21900**, i.e. +21.900, which is only 1500 above the +20.400 roof slab. If the overrun is 1300 it tops out 200 below the parapet; if it is 2000 it rises 500 above the building's own stated overall height.
**Why it matters** The overrun is the tallest element on a party-wall row and the element the neighbours see. It also has to clear the lift's own overhead requirement — a machine-room-less lift still needs headroom above the car. A 1300 overrun over a 1600-deep pit is thin for a sheave/motor space, and 2000 would breach the height the elevation declares.
**Basis** Drawing consistency; the top of the building must have one height.
**Basis class** JUDGEMENT
**Fix** Fix the roof slab level and the overall height on the elevation first, then derive the overrun height from the lift supplier's requirement plus 200 mm of structure, and print it on the roof plan and the section together.
**Cost/impact** S
**Evidence label** PARTIAL (the 1300 is a PARTIAL read; the contradiction between 1300, 2000 and the 21900 total is nonetheless VERIFIED)

---

**ID** D-04 · **Type** ERROR · **Severity** HIGH
**Where** KT01 (IMG_9972) dimension chains · KT02 (IMG_9973) · KT03 (IMG_9974) · KT06 (IMG_9977) · MB MÓNG (IMG_9981) grid. All chain values READ.
**Issue** Several printed dimension chains do not close to the printed overall. My own sums (VERIFIED, `_scan1022/chk.py`):

| Sheet | Chain as printed | Sum | Printed overall | Gap |
|---|---|---|---|---|
| KT01 | 350 | 3010 | 4240 | 4000 | 5000 | 4500 | 1600 | 2650 | 25350 | 25000 | **+350** |
| KT01 | 2810 | 3940 | 3800 | 3000 | 1800 | 4400 | 900 | 500 | 2400 | 250 | 23800 | 25000 | **−1200** |
| KT01 | 350 | 2460 | 350 | 100 | 3940 | 3800 | 1250 | 500 | 1250 | 100 | 1600 | 100 | 5800 | 100 | 2300 | 24000 | 25000 | **−1000** |
| KT01 | 2760 | 500 | 4240 | 4000 | 3200 | 1800 | 6100 | 2300 | 24900 | 25000 | −100 |
| KT01 tier 3 | 3360 | 19340 | 2300 | **25000** | 25000 | 0 |
| KT02 | 350 | 2460 | 3940 | 3800 | 1250 | 500 | 1250 | 1600 | 4400 | 1400 | 2300 | 23250 | 25000 | **−1750** |
| KT03 | 500 | 900 | 3010 | 4240 | 850 | 950 | 1600 | 1350 | 500 | 1350 | 1800 | 4500 | 1100 | 500 | 23150 | 23750 | **−600** |
| KT03 top | 1400 | 3010 | 4240 | 4000 | 3200 | 1800 | 4500 | 1600 | 23750 | 23750 | 0 |
| KC01 grid lower | 350 | 3010 | 4240 | 4000 | 3200 | 1800 | 4400 | 1700 | 2300 | 25000 | 25000 | 0 |
| KC01 grid upper | 350 | 3010 | 4240 | 4000 | 3200 | 1800 | 4400 | 1700 | 2650 | 25350 | 25000 | **+350** |

The two chains that do close (KT01 tier 3 and the KC01 lower grid) both put the front offset at **3360** (350 + 3010) and the rear at **2300**. The chains that fail all carry **350 + 3010** at the front and/or **2650** at the rear. The same +350 appears at the front of the architectural top chain and of the structural upper grid chain — one duplicated 350 segment in each.
**Why it matters** These are the chains a site foreman sets out the frame from. Where a chain does not close, at least one of its numbers is wrong, and there is no way to tell which. On a 3.9 m wide plot a 350 mm error is 9 % of the width and lands directly in a party wall.
**Basis** Drafting practice: a dimension string must close; otherwise it is not a setting-out document.
**Basis class** JUDGEMENT (this is a documentary requirement, not a code)
**Fix** Re-issue KT01, KT02, KT03 and the foundation layout with one chain per axis that closes to the printed overall, and add a dimension string on the ground floor for the front yard / garage / kitchen band that closes. Ask specifically: is the front offset 3360 or 3710, and is the rear 2300 or 2650? Both sides of the house must have their own closed chain because the boundary tapers.
**Cost/impact** S / M (a wrong set-out is M–L)
**Evidence label** VERIFIED (chain values READ; sums are mine and re-checked)

---

**ID** D-05 · **Type** ERROR · **Severity** MEDIUM
**Where** KC… DS1a (IMG_9999) · KC… DS2 (IMG_9998) · all plans and the foundation layout.
**Issue** The structural grid is named three ways for the same positions. Plans, ĐK1/ĐK2, DS2a and the foundation layout use axes 1, 2, 3, 4, 5, **5a**, 6. DS1a labels the same three right-hand positions 4, 5, 6, **7** — with the 1700 end bay terminating at a bubble marked 7. DS2 labels 5a as **5**.
**Why it matters** A 5-storey house on piles with 31 piles and 200 mm columns has no tolerance for a mis-called axis: a bar batched to axis 6 on one sheet and 7 on another will not fit. It also makes the structural set impossible to check against the architectural set, which is the whole purpose of a grid.
**Basis** Drafting practice: one grid, one naming, every sheet.
**Basis class** JUDGEMENT
**Fix** Re-issue the whole structural set with a single grid (1–2–3–4–5–5a–6) and a grid key on every sheet.
**Cost/impact** S
**Evidence label** VERIFIED

---

**ID** D-06 · **Type** ERROR · **Severity** HIGH
**Where** KT01 (IMG_9972) · KT02 (IMG_9973) · KC… *CẦU THANG TRỆT* (IMG_0003) · KC23 *CẦU THANG LỬNG* (IMG_0004) · KC24 *CẦU THANG LẦU 1, 2, 3* (IMG_0005). Spec rooms: `stairwell`, `hall_stair`.
**Issue** The stair flight width is 1250 in the architectural plans and 1350 in the structural stair details, for the *same two stairs*. The architecture ground plan (KT01) gives the stair as 1250 + 500 + 1250 = 3000 (the transcriber flags this as an arithmetic check), "3200 between wall lines". The structural sheet for the ground stair (IMG_0003) gives the plan chain **1350 | 500 | 1350 = 3200**, and the mezzanine stair sheet (IMG_0004) gives the same. The architectural plans for floors 2–4 also give 1350 + 500 + 1350. The one place the architecture says 1250 is therefore the ground and mezzanine flights — the two stairs that the structural sheets say are 1350. The two values are not reconcilable in the 3200 well: 1350 + 500 + 1350 fills the well exactly to the wall lines with zero tolerance, while 1250 + 500 + 1250 leaves 200 that the plan then fills with a winder (the ground plan shows treads 13, 11, 9, 7 turning at the B-side end).
**Why it matters** 100 mm per flight is the difference between a 1250-wide flight (acceptable but tight for a handrail, and below the 1100-plus-rail clear width that a 1250 nominal leaves once a 50 mm handrail is set in) and a 1350-wide flight. More practically, the drawn stair is the only vertical circulation in the house for five storeys and a lift: the width and the turning geometry must be right before the stair is cast, and the winder detail is nowhere in the set.
**Basis** Drafting consistency; D-07 for the geometric consequence.
**Basis class** JUDGEMENT
**Fix** Adopt one flight width for all five flights (1350 if the well is truly 3200 wall-to-wall and the flights must land on the wall faces), correct the two architectural plans to match, and issue the missing stair detail — plan geometry, winder radii, landing support, handrail, and the headroom over the flight and over the intermediate landing.
**Cost/impact** S (drawing) / M (cast change)
**Evidence label** VERIFIED

---

**ID** D-07 · **Type** ERROR · **Severity** MEDIUM
**Where** KC23 (IMG_0004) · KC24 (IMG_0005) · KC ground stair (IMG_0003). Spec room: `stairwell`.
**Issue** The same 21-tread stair is used for three different storey heights, producing three different risers and one of them outside the comfort band:

| Flight | Storey height | Risers | Riser | 2R + G (G = 250) | Comfort band 600–630 |
|---|---|---|---|---|---|
| Ground → mezzanine | 3700 | 21 | 176.2 | 602 | in band |
| Mezzanine → tầng 2 | 3200 | 21 | **152.4** | **555** | **below band** |
| Tầng 2/3/4 → next | 3400 | 21 | 162.0 | 574 | in band (low side) |

My arithmetic (VERIFIED): 3700/21 = 176.2, 3200/21 = 152.4, 3400/21 = 161.9. The 152.4 riser with a 250 going is a very flat stair; the two upper flights at 162 are also below the 175–190 riser band that X3 gives for a 250 tread. The geometry also has almost no slack: 21 risers at 250 going needs 20 goings = 5000 of run, split two flights ≈ 2500 each, inside a 3900-wide well that must also contain a 1250 landing — so the long flight has roughly 150 mm of tolerance in total. Any site error in the 3900 or 3200 breaks the stair.
**Why it matters** A 152 mm riser with a 250 going is a stair that feels like a ramp and that elderly users and children find difficult; it is also the flight people use most (ground to mezzanine is the daily route). And with ~150 mm of total tolerance in the flight run, the stair is the item on this job most likely to be wrong on site.
**Basis** X3 (2R + G = 600–630 comfort rule, VERIFIED); X2 (2024 IBC Ch.10: dwelling stair max riser 197 mm, min tread 254 mm — the drawn 250 tread is 4 mm under the IRC minimum, VERIFIED). Comfort and safety, not just code.
**Basis class** BEYOND-LOCAL
**Fix** Reduce the mezzanine to **20 risers of 160** (2R + G = 570) or **19 risers of 168** (587) and give the upper floors 20 risers of 170 (2R + G = 590, tread 250) or extend the 250 going to 255 to satisfy X2 — the treads are 21 × 250 in a 3200 well, so a small reduction in riser count costs nothing in plan. Publish the riser table (riser, going, 2R+G, headroom over flight and over landing) on the stair detail sheet that the section already refers to and that is missing from the set.
**Cost/impact** S (change riser count, no footprint change) / M (rebar and formwork if cast already)
**Evidence label** VERIFIED

---

**ID** D-08 · **Type** ERROR · **Severity** HIGH
**Where** KT02 (IMG_9973) · KT03/KT04/KT05 (IMG_9974–9976) · KT01 (IMG_9972). Spec rooms: `ngu_sau_f2`…`ngu_sau_f5`, `sinh_hoat`, `bep_an`, `wc_sau_f2`…`wc_sau_f5`, `wc_gf`.
**Issue** The rear habitable rooms have no window of their own. On floors 2–4 and on the mezzanine the chain of rooms reads front-to-rear: *P. Ngủ* → **WC** → *Lô gia*. The only door into the rear loggia is D3, and D3 is drawn on the **WC** (tags WL2/WL3/WL4, Dw, Sb1, K2, D3). The bedroom's own tags are D4 (internal) and a floor tag only. The same pattern appears on the mezzanine: *P. Sinh hoạt* → WC → *Sân sau*, with D3 on the WC. On the ground floor: *P. ăn + bếp* → WC → *Sân sau*, with D2 on the WC. So the rear bedroom, the mezzanine family room and the ground kitchen each reach daylight and ventilation only through a 3 m² toilet, and in the kitchen's case the route to fresh air runs through the WC.
**Why it matters** Three of the house's most-used spaces are windowless by construction. This is not a comfort issue, it is a ventilation and daylight issue: a bedroom that can only be aired through a WC door will never be cross-ventilated, will hold heat and humidity, and will be the room that smells in the monsoon. X1 requires the bedroom to have a window and a minimum usable area of 12 m² (double) or 9 m² (single) — the area may be met while the daylight and ventilation requirement is not. A 4400-deep kitchen with a hob and a sink and no window also puts the cooking heat and the cooking odour into a room with no way out.
**Basis** X1 TCVN 13967:2024 §5.10 (VERIFIED) for habitable-room daylight/ventilation and areas; international residential practice (Neufert/BCA-class guidance) for the rule that a habitable room should have its own external opening — this specific external rule is **UNVERIFIED** in this session (no fetch available), so I rely on X1 and on the internal contradiction that the WC is doing the bedroom's job.
**Basis class** LOCAL-MINIMUM (X1) + JUDGEMENT
**Fix** Smallest change, and it is one move repeated at each rear band: **swap the WC and the bedroom's vestibule** so the sequence becomes *P. Ngủ* → 900-wide vestibule → WC → *Lô gia*, and give the bedroom a **1200 wide × 1500 high** opening onto the loggia wall. For the ground floor, put the WC beside the kitchen rather than between it and the yard, and give the kitchen a **1200 × 1200** window onto the rear yard. This keeps every room in place, keeps the rear wet-area stack, and changes no external wall.
**Cost/impact** M (partition moves, glazing, drainage re-run) — and it is the single highest-value change in this review
**Evidence label** VERIFIED (room chains and door tags READ in S1)

---

**ID** D-09 · **Type** ERROR · **Severity** HIGH
**Where** KT01 (IMG_9972). Spec rooms: `khach`, `gara`.
**Issue** The ground-floor living room *P. Khách* (3800 internal / 4000 grid, 3200 clear wide, ≈ 12.8 m²) has **no window and no door tag** on the ground plan. Its front neighbour is *Nơi để xe* (the garage), whose only opening is D1 (2800 wide × 2800 high, a four-leaf glazed door to the street). Its rear neighbour is the stair core. Both sides are party walls. The full tag vocabulary in the set (S1) is D1, Dc, D2, D3, D4, D5, D6, D7, Dw, W1, K1, K2, S1, S2, Sb1 — and no S/K tag is attached to *P. Khách* on the ground plan. The section (IMG_9980) confirms the ground sequence *P. Bếp + Ăn, P. Khách, Nơi để xe* with no opening shown to *P. Khách*.
**Why it matters** The entrance to the house is the garage door, and the ground-floor living room is lit only by what comes through the garage and up through the 8140-long mezzanine void from 3.8 m above. A 12.8 m² living room with one borrowed clerestory and no direct door is a dark room at the centre of the plan and the worst-proportioned space in the house. It also means the front door, the parking bay and the living room are one undivided volume — the car, the bins and the sofa share the same air.
**Basis** X1 (habitable-room daylight and ventilation, VERIFIED); the drawing-internal fact that a room with no opening tag on a plan where every other room has one is an omission.
**Basis class** LOCAL-MINIMUM + JUDGEMENT
**Fix** Two minimal moves: (i) add a **1000-wide internal window** between *P. Khách* and the garage so the living room is daylit from the street elevation without touching the facade; and (ii) move D4 (the internal door) to a position that gives the living room its own entry from the porch/yard, so the garage is not the entrance hall. If the garage cannot be split, add a **1500 × 1500** opening from *P. Khách* to the rear yard — but there is no rear yard at that level, so option (i) plus a D4 relocation is the fix.
**Cost/impact** S–M
**Evidence label** VERIFIED (absence of tags is a transcript-level observation; confirm on the original sheet before pricing)

---

**ID** D-10 · **Type** ERROR · **Severity** HIGH
**Where** KT01 (IMG_9972) · IMG_9979 (elevation). Spec room: `gara`.
**Issue** The car cannot get into the garage. The front yard *Sân trước* is at **−0.200** and the garage *Nơi để xe* is at **±0.000** — a 200 mm step up at the threshold, and no ramp is drawn anywhere on the ground plan. The garage internal depth is **3940** (grid 4240) and its clear width is **3200**. A 200 mm up-stand with a door 2800 wide in front of it means the car must be lifted or driven over a kerb; and 3940 of internal depth is **560 mm short** of a 4500 mm car (a common sedan is 4500–4700 long, 1800 wide, 1500–1600 high with roof rails).
**Why it matters** The garage is 4000 × 3200 of the most valuable ground-floor area in a house with no other parking, no store and no laundry, and as drawn it neither accepts a car nor is reached by one. The 200 mm step is also a drainage decision: the yard is 200 below the slab, so water moves to the door, and the garage has no floor drain shown.
**Basis** Drafting consistency and dimensional feasibility; vehicle dimensions are standard reference data (VERIFIED by general reference, not fetched in this session — a 4500 mm sedan length is a commonly published figure and is UNVERIFIED here).
**Basis class** JUDGEMENT
**Fix** Either (a) lower the garage slab to **−0.200**, level with the yard, and slope the slab 1.5 % to a floor drain inside the threshold — this is the cheap and correct answer; or (b) provide a **1:12 ramp 2400 long × 3200 wide** inside the front yard, which the yard's dimensions do not obviously allow. Keep the clear internal depth at 3940 and specify a car bay of **2500 deep × 1800 wide** plus a **1440-wide moto/bike/utility strip** along the party wall, and state the maximum vehicle length (≤ 4200) in the notes.
**Cost/impact** S (level change) / M (ramp and drainage)
**Evidence label** VERIFIED (levels and dims READ); the vehicle-length figure is UNVERIFIED

---

**ID** D-11 · **Type** ERROR · **Severity** MEDIUM
**Where** KT03 (IMG_9974) · KT04 (IMG_9975) · KT05 (IMG_9976) — front ensuite, tags WL2/WL3/WL4, door Dw 700/750, widths 850 + 950. Spec rooms: `wc_truoc_f2`, `wc_truoc_f3`, `wc_truoc_f4`.
**Issue** The front ensuite is **1800 wide × 1600 deep = 2.88 m²** (my arithmetic, VERIFIED), below the **3 m²** minimum usable area for a WC. The earlier reading used 1950 and reached 3.12 m²; the scan's own chain (850 + 950 = 1800) puts it below the threshold for the first time.
**Why it matters** 2.88 m² is the floor area including the door swing and the wall build-up. A WC in it has a pan, a basin, a cistern and a door, and leaves no usable floor — this is the room where a family will actually complain. The standard is not marginal here: 3 m² is a flat number in Table 1 of X1.
**Basis** X1 TCVN 13967:2024 Table 1 §5.10 — min. usable area of a WC 3 m² (VERIFIED)
**Basis class** LOCAL-MINIMUM
**Fix** Widen the front ensuite from 1800 to **1950** (the value the earlier reading used) by taking 150 from the adjacent hall band, or deepen it from 1600 to 1700 by taking 100 from the front hall. Either keeps the 1600-wide light well and the wall positions of the bedroom. Confirm on the original sheet whether the printed width is 1800 or 1950 before assuming this finding stands — it is the one ERROR in this review that turns on a single digit.
**Cost/impact** S
**Evidence label** PARTIAL (the 850 + 950 widths are READ but the *width of what* is inferred from the transcript's description; the area arithmetic is VERIFIED)

---

**ID** D-12 · **Type** ERROR · **Severity** HIGH
**Where** KT02 (IMG_9973) · IMG_9992 *MB DẦM SÀN LỬNG* · IMG_9980 (section). Spec rooms: `khach`, `gara`, `sinh_hoat`, `hall_front_f2`…
**Issue** The mezzanine is open to the sky over **8140** of the house's length — the whole garage *and* the whole living room. KT02 marks the front yard and "the whole front interior (about 8140 long)" as *Thông tầng* (void, X-hatched), split into a front-yard void 3900 wide and an interior front void 2800 wide with the K1 glass wall. The structural mezzanine slab plan (IMG_9992) confirms: the axis 1–2 bay and the axis 2–4 bays (4240 and 4000 wide) are drawn as full-width X panels, i.e. no slab; only the rear (axes 4–6) is slabbed. So the car stands under a 3900-wide, 8140-long hole in the floor, open to a 7.2 m-high space, with the only enclosure being the 2800 × 1700 K1 clerestory at the mezzanine level.
**Why it matters** A garage with no roof over the car is a hot, echoing, rain-catching space and a security exposure; a living room with no window at ground level (D-09) has no other way to be lit; and the whole front 8140 of the house has no floor between ground and mezzanine, which means the ground floor has no ceiling and the mezzanine has no floor for 8140 of its front. It also explains the structure: the void is framed by DS1 (A side) and DS2 (B side) at 200 × 300 with Ø16 bars — a 3200 clear span between the party-wall lines over an 8140 length. (Structure is the `safety` lane's call; the design point is that the void is far larger than the drawings' own description of a "double-height void over the front" suggests.)
**Basis** Drawing-internal: the section and plan describe a front double-height void, the earlier reading (S4) read it as y 0–12300, and the scan reads 8140 — the two readings of the same sheet disagree, so the extent must be confirmed. (D-04 shows the chains around this band do not close.)
**Basis class** JUDGEMENT
**Fix** Confirm the extent against the original KT02, then decide one of two schemes: **(a)** slab the mezzanine over the garage only (leaving a 4000 × 3900 double-height living room) and put a ceiling or a fan in the garage — this is the smaller change and gives the living room a real volume; or **(b)** keep the void but roof it with a **1500-wide × 8140-long** polycarbonate or insulated standing-seam roof on beams, which also solves the heat gain of a 7.2 m glass-sided void. Whichever is chosen, add the missing slab/void edges to the beam plans with real support, not the generic note.
**Cost/impact** M (scheme a) / L (scheme b) — but scheme (a) is also a cost *saving* on the mezzanine slab
**Evidence label** PARTIAL (the 8140 is READ from a chain that does not close; the X-void reading of IMG_9992 is an interpretation by the transcriber with no legend — see D-14)

---

**ID** D-13 · **Type** ERROR · **Severity** HIGH
**Where** KT05 (IMG_9976) · KT06 (IMG_9977) · IMG_9979 (elevation level tags) · IMG_9980 (section level tags) vs earlier reading S4 (*Storey heights* table) and S6 (compiled spec `storeys[]`).
**Issue** The programme and the height of the top two levels differ between the two readings of the same sheets, and the earlier reading is the one now known to be wrong:
- Earlier (S4/S6): tầng 4 = two bedrooms + two WCs; tầng 5 = *P. ThỜ* + front WC + rear bedroom; terrace as an enclosed 3200 storey; roof slab +23.800; plant to +25.800; overall 23800.
- Scan (S1, all level tags READ): tầng 4 (+13.800) = *P. Thờ* + *P. Đọc sách* (thin partition, 3010 + 4240 grid) + *P. Ngủ* rear + two WCs; tầng 5 (+17.200) = **no rooms**, only a 5200-long stair/lift lobby with D6 and D7 and two open terraces *Sân thượng* (front 3500 clear, rear 6100); roof slab +20.400; parapet top +21.900; overall 21900 (elevation) / 20400 to roof slab (section).

The storey-height table in S4 (3800/3200/3400/3400/3400/**3400**/**3200** = 23800) is also wrong at two points: tầng 5 is 3200, not 3400, and there is no 3200-high terrace storey above it. The brief's own description of the house ("floors 2-5 at 3.4 m, a roof terrace") does not match the drawings either.
**Why it matters** The compiled spec (`contractor-as-drawn.json`) currently has `Floor 4` = two bedrooms and `Floor 5` = *P. ThỜ* + bedroom + WC, and a `Roof Terrace` storey 3200 high whose floor sits at the top of the building. The drawings say the terrace is *at* +17.200, that tầng 5 has no rooms, and that the building is 1900 mm shorter than the model. Any document, render, budget or contract quantity derived from the model is wrong on: the number of bedrooms (the model has 8; the drawings give 2 + 2 + 1 + 1 + 1 = 7), the area of the top floor, the building height, and the elevation datum of the terrace.
**Basis** Drawing-internal: level tags are READ on both the elevation and the section and they agree with each other, which makes the earlier PDF reading the outlier. (For reference, the earlier reading's provenance is stated in S4 itself: the five PDFs carry **no extractable text** — verified here by script — so both readings are visual, and the scan is corroborated by two independent sheets.)
**Basis class** JUDGEMENT
**Fix** Before anything else in the design lane: **re-issue the compiled spec to the scan**, not the other way round. Change tầng 4 to *P. Thờ* + *P. Đọc sách* + rear bedroom, change tầng 5 to a lobby with two terraces, delete the 3200 terrace storey, set the roof slab at +20.400 and the parapet top at +21.900, and re-derive every area and quantity. Then confirm with the designer which reading of KT05/KT06 is correct — the drawings and the compiled model cannot both be.
**Cost/impact** S (model re-issue) / L (any contract quantity already priced off the model)
**Evidence label** VERIFIED (level tags READ on IMG_9979 and IMG_9980 and mutually consistent; the earlier reading's chain is internally consistent too, so this is a documented conflict, not a proof)

---

**ID** D-14 · **Type** ERROR · **Severity** MEDIUM
**Where** KT01–KT07 (IMG_9972–9978) · IMG_9992, 9993, 9994, 9995, 9996 (all slab plans) · Legend on KT01.
**Issue** The X-hatch has **no legend on any sheet**, yet it carries at least four different meanings: on KT02 a double-height void over the front yard *and* over the front interior; on KT02 also the rear *Sân sau* (X-hatched, with a balustrade note) which reads as open-to-sky rather than as a void; on KT07 the roof over almost the whole footprint; on the structural slab plans (IMG_9993–9996) the stair, light-well and lift voids, with the roof plan (IMG_9996) additionally using a **diagonal hatch** with no explanation. Meanwhile the architectural legend (KT01) does define *Thông tầng* and *Ô lấy sáng* — but the X panels are not annotated with either.
**Why it matters** X means "void", "open to sky", "no slab" and, on the roof plan, possibly "terrace at a lower level" depending on which sheet you read. The distinction is worth a slab: the difference between a 100 mm RC slab and nothing is the whole floor. It is also what makes the roof waterproofing scope unpriceable.
**Basis** Drafting practice: every hatch needs a legend entry on every sheet that uses it.
**Basis class** JUDGEMENT
**Fix** Add a legend block to every sheet giving: X = *không có sàn* (no slab / void through), diagonal hatch = *sàn nhẹ / kính lấy sáng* (lightweight slab or glazing), and a separate symbol for *sân thượng* (open terrace at this level). Apply the same symbols on the architectural and the structural sheet.
**Cost/impact** S
**Evidence label** VERIFIED (the absence of a legend is stated in S1 and S3 independently; the *meanings* are interpretations and are listed in §7)

---

**ID** D-15 · **Type** ERROR · **Severity** MEDIUM
**Where** Title block of every sheet in S1, S2, S3.
**Issue** The set has no design control. On all nine architectural sheets the *PHẦN GHI CHÚ* (notes/revisions) box is blank; no designer, no date, no revision letter, no stamp or signature is visible on any of the nine photos; the sheet codes for IMG_9979 and IMG_9980 read "KT0?" (PARTIAL) and the "20" under every code is an unconfirmed total. The structural sheets show "KCnn / 24" with several codes cut off, the title block reads scale 1/20 on every sheet including the 1/100 plans, and the same title block is cropped at the right and bottom edge on every photograph, so the absence of a stamp **cannot be confirmed** — it may be cropped off.
**Why it matters** A construction set with no revision block cannot be frozen, cannot be priced against a fixed revision, and cannot be superseded cleanly. When the top-of-house question (D-01) and the lift geometry (D-02) are answered, there will be a revision — the set needs somewhere to put it. Separately, a title block that states 1/20 on a 1/100 drawing is a scale error a site engineer could act on.
**Basis** Drafting practice and project-administration requirement; also the process point that no drawing can be cited as "the issued set" without an issue number.
**Basis class** JUDGEMENT
**Fix** Re-issue with a populated title block (project, drawing title, scale 1:100 for plans, drawn/checked/approved with licence number, date, revision number, sheet n of N) and a filled *PHẦN GHI CHÚ* revision table. Confirm whether the cropped region carries a stamp, and get the full architectural dossier — sheets KT08 onward were never photographed, and the door/window schedule is not in the set.
**Cost/impact** S
**Evidence label** PARTIAL (the crop means the stamp's absence is not confirmed)

---

### INCONSISTENCY

**ID** D-16 · **Type** INCONSISTENCY · **Severity** MEDIUM
**Where** KT01 (IMG_9972) ground-floor chains and WC note · earlier reading S4 (ground floor table).
**Issue** The ground floor's rear band does not close and the rear WC is drawn two different ways. The top chain places the kitchen at 4500 and the WC at 1600 along the length (4400 + 1600 in the second chain); the note under the rear WC says "1600 wide, 2100 long" with 650 / 800 / 400 stacked on its rear side; the bottom chain instead gives a 5800 band and 2300 at the rear. The earlier reading (S4) placed the WC at 1600 *deep and full width*, and the kitchen 4100 deep. So: the WC is 1600-along-the-house in one chain and 1600-across-the-house in the note; the kitchen is 4100, 4400 or 4500; and the rear yard is 2300 or 2650.
**Why it matters** The rear of the ground floor is where the kitchen, the WC, the drainage chase (*"Hộp gen thoát nước"*, in the section at the rear wall) and the rear door are all packed into the last 6 m of a 25 m plot. An unclosed dimension string over the kitchen run and the only rear door means the kitchen cabinetry and the drainage stack cannot be set out reliably, and the kitchen's window (which does not exist — D-08) has nowhere to go.
**Basis** Drawing consistency; S4 records the same ambiguity as its own "Core note".
**Basis class** JUDGEMENT
**Fix** Issue one closed chain for the ground floor's rear 8000, fixing the kitchen at **4400 deep**, the WC at **1600 along × 2100 across** (or the reverse — but pick one and print the room name against it), and the rear yard at **2300 (B side) / 2650 (A side)**, and state which side is which.
**Cost/impact** S
**Evidence label** VERIFIED (the three mutually inconsistent readings are all in the transcripts; the numbers that survive are READ)

---

**ID** D-17 · **Type** INCONSISTENCY · **Severity** MEDIUM
**Where** KT01 / KT03 / KT05 rear WC notes · earlier reading S4 ("printed and dimensioned identically to the ground-floor WC").
**Issue** The earlier reading assumed the rear WC on floors 2–5 is printed identically to the ground-floor WC and therefore reconstructed the front ensuite from a "1950" label. The scan shows the two ensuites are **different rooms**: the rear WC is 1600 wide × 2100 long (3.36 m²), the front ensuite is 1800 wide × 1600 deep (2.88 m²), and the ground WC is a third arrangement again (D-16). So open item (d) in S5 is not "a reasonable reconstruction" — it was a reconstruction of the wrong room.
**Why it matters** Three different WC layouts in the same 3.9 m width is a buildability and cost problem: three wet-room layouts mean three plumbing layouts, three waterproofing details and three tile setting-out drawings, none of which the set contains. It also means the rebar/wall positions of the wet-area stack cannot be assumed identical floor to floor.
**Basis** Drawing consistency; X1 (all three WCs must still clear 3 m², and the front ensuite does not — D-11).
**Basis class** LOCAL-MINIMUM + JUDGEMENT
**Fix** Standardise on **one** WC layout (1600 wide × 2100 deep is the one that comfortably clears 3 m² and is already used at the rear) and use it at all six wet positions: ground, mezzanine, floors 2–4 front and rear, floor 5. This simultaneously fixes D-11 and makes the plumbing stack regular, which is worth real money.
**Cost/impact** M (re-laying partitions and drainage) but it buys a regular stack
**Evidence label** VERIFIED

---

**ID** D-18 · **Type** INCONSISTENCY · **Severity** MEDIUM
**Where** KT05 (IMG_9976) vs KT03/KT04 (IMG_9974–9975) · IMG_9979 (elevation) · IMG_9994 (*MB DẦM SÀN TẦNG 4*).
**Issue** The floor-4 balcony is **mirrored** relative to floors 2–3: door D5 and window S1 swap sides; the "gạch trang trí màu xám đậm" (dark grey) and "màu xám nhạt" (light grey) tile callouts swap sides; the 900 and 2400 vertical dims swap; and the left-end chain reads "500 100 100 | 800" where floors 2–3 read "200 | 1200 | 100 100" (PARTIAL). The structural floor-4 slab sheet is mirrored too (IMG_9994: the 1100 DS8 strip at the A side on floor 4, at the B side on floors 2–3). The elevation shows alternating panels per floor, which is consistent with a deliberate scheme; but nothing states that.
**Why it matters** A mirrored balcony changes the door swing into the bedroom, the tiled finish, the drainage fall, the laundry line position and the beam layout of that storey. If it is a drafting slip it will be built as a slip, because the structural sheet mirrors it too. If it is intentional, it should be dimensioned identically and shown on the elevation with the same numbering.
**Basis** Drawing consistency.
**Basis class** JUDGEMENT
**Fix** Confirm the mirror is intentional; if it is, annotate "BALCONY MIRRORED — SEE NOTE" on KT05 and on the floor-4 structural sheet and dimension it to the same set of numbers as floors 2–3. If not, correct both sheets.
**Cost/impact** S
**Evidence label** VERIFIED (both the plan and the structural sheet mirror; the *intent* is not confirmed — see §7)

---

**ID** D-19 · **Type** INCONSISTENCY · **Severity** MEDIUM
**Where** KT03 / KT04 / KT05 (light wells beside the front ensuite) · KT06 (glazed well 2000 × 1500 over the hall) · KT07 (two *Ô lấy sáng*, 1200 and 1300/1500) · IMG_9980 (balustrade 1100 at the rear light well).
**Issue** The light wells have widths but not extents, and their vertical alignment is not drawn. The wells beside the front ensuite are 1600 wide on floors 2–4 with "length not read on this sheet"; the floor-5 well is 2000 × 1500 over the hall and glazed (*"Ô lấy sáng gắn kính cường lực, có khung inox bảo vệ"*); the roof plan shows two wells at 1200 and 1300/1500. The earlier reading modelled the floor-5 well at x1960–3960 × 1500, i.e. the *rear* edge of the front zone — a different position from the front ensuites' wells. Nowhere is it stated whether the floor-5 well sits above the floors 2–4 wells (a vertical light shaft) or beside them (a separate slot per floor).
**Why it matters** If they stack, the house has a genuine 4-storey light and ventilation shaft and every room around it benefits. If they do not stack, each floor has a separate 1600-wide slot that is a light leak, a rain entry and a fall edge but no shaft. The ventilation strategy for the entire front half of the house depends on the answer.
**Basis** Drawing consistency; the difference is the difference between a shaft ventilation strategy and none.
**Basis class** JUDGEMENT
**Fix** Draw the wells on a single vertical section with their x-positions dimensioned, state the stack, and if they do stack, glaze them properly (see D-34) and open them at each floor.
**Cost/impact** S
**Evidence label** PARTIAL (widths READ; extents and stacking not established)

---

**ID** D-20 · **Type** INCONSISTENCY · **Severity** MEDIUM
**Where** IMG_9992, 9993, 9994, 9995, 9996 note 4 · IMG_9999 / IMG_0001 / IMG_0002 (DS2a) · IMG_9982 column schedule.
**Issue** The structural set's wall-load rule is a note, not a design: *"CHỖ NÀO CÓ TƯỜNG MÀ KHÔNG CÓ BỐ TRÍ DẦM THÌ TA ĐẶT THÊM 2Ø16 HOẶC 3Ø16 TẠI VỊ TRÍ ĐÓ"* — where a wall has no beam, add 2Ø16 or 3Ø16, with no length, no depth, no anchorage, and "or" left to the site. On the roof sheet the same note drops to 2Ø16 only. On top of that, DS2a's axis 2–3 span is dimensioned **4600** on IMG_0001 while every plan, ĐK1, ĐK2, DS1, DS1a and DS2 dimension it **4240**. The columns are 200 wide at the party-wall lines (C1 reduces to 200 × 200 with 2Ø16 + 2Ø16 above tầng 3).
**Why it matters** This is where the design lane and the structure lane meet: a 200 mm party wall with no beam behind it, carried by a 100 mm slab and a 2Ø16 bar "where there is a wall", is a line-item for cracking and for MEP chasing (see D-24), and it is a decision the site makes rather than the designer. (Structural adequacy is the `safety` lane's call; the design point is that no wall-to-beam schedule exists, so the partition positions on the architectural plans are not tied to anything.)
**Basis class** JUDGEMENT
**Fix** Publish a wall–beam coordination table: every partition on every plan mapped to a beam mark or to a specified hidden beam (size, depth, reinforcement, anchorage), and correct the DS2a span. Both are one drawing each and they protect the partitions the design lane is asking to move (D-08, D-17) from being built over a 2Ø16.
**Cost/impact** S / M
**Evidence label** VERIFIED (notes READ verbatim; the 4600 is READ)

---

**ID** D-21 · **Type** INCONSISTENCY · **Severity** MEDIUM
**Where** KT06 (IMG_9977) · KT07 (IMG_9978) · IMG_9972 (ground yard levels).
**Issue** Drainage is annotated as locations without levels or falls. KT06 marks *"vị trí phễu thu nước sàn"* × 3 (one front-left, one 800 × 450 near the light well, one at the rear terrace) and *"vị trí vòi rửa"* × 2 on the side walls, with no levels, no falls, no connection to anything, and no drain shown on the ground-floor garage or the rear yard. KT07 shows two roof drainage arrows at the core block and no gutter, no downpipe, no overflow, no waterproofing note anywhere in the set. The ground-floor yards are at −0.200 and the garage at ±0.000, so the ground surface falls *toward* the front and rear doors from the garage.
**Why it matters** HCMC rain loads these surfaces hard. Without levels and falls, floor drains are installed as local pits that discharge nowhere, and the roof — whose extent is itself undecided (D-01, D-14) — has no defined waterproofing, slope or overflow. Water finding its way into the lift pit (D-02) is the classic failure here; a pit with no waterproofing, no sump and no drain is already a given.
**Basis** Drawing consistency and buildability; the roof waterproofing scope is unpriceable without it.
**Basis class** JUDGEMENT
**Fix** Add a drainage sheet: levels and falls on the front yard, garage, rear yard, both terraces and the roof; gutter and downpipe positions; overflow scuppers; and a lift-pit sump with a pumped or gravity discharge, plus the waterproofing specification for the pit, the terraces and the roof.
**Cost/impact** M
**Evidence label** VERIFIED (annotations READ; the absence of falls and levels is a transcript-level observation)

---

**ID** D-22 · **Type** INCONSISTENCY · **Severity** LOW
**Where** Title block of every sheet (S1, S2, S3) vs each drawing's own scale note.
**Issue** The title block reads "Tỉ lệ: 1/20" on every sheet in both dossiers, including the 1/100 architectural plans and the 1/100 slab plans. Each individual drawing carries its own correct scale (1/100, 1/50, 1/20), so the error is in the title block only. The same title blocks are cropped at the right and bottom edge on every photograph, so a drawing number, revision and date may exist outside the frame.
**Why it matters** Low, but it is the kind of error that gets a set rejected at a submittal review, and a 1:20 title block on a 1:100 plan invites a mis-scaled take-off.
**Basis** Drafting practice.
**Basis class** JUDGEMENT
**Fix** Correct the title-block scale box per sheet and issue uncropped PDFs.
**Cost/impact** S
**Evidence label** VERIFIED

---

### RISK

**ID** D-23 · **Type** RISK · **Severity** HIGH
**Where** All plans KT01–KT07; the room chains in S1. Spec rooms: `ngu_sau_*`, `sinh_hoat`, `bep_an`, `wc_sau_*`.
**Issue** The house is 25000 deep and 3900 wide with a 5000-long solid core (stair 3200 + lift 1800) at mid-depth. Every habitable room is therefore either in the front zone or the rear zone, and each zone is **single-sided**: the front zone (balcony 1400 + bedroom 4000 + ensuite 1600 + hall 1800) opens only to the street; the rear zone (bedroom 4400–4500 + WC 1600) opens only to the rear loggia. There is no opening that connects the two zones through the core, and the light wells that could have formed a cross-path are, on floors 2–4, adjacent to the front WC rather than placed in the circulation.
**Why it matters** Cross-ventilation in a hot-humid climate is the cheapest cooling there is, and neither zone can have it. The rear bedroom, the mezzanine family room and the kitchen are single-sided rooms 4.4–4.5 m deep with only a 1600-wide loggia — the classic "deep single-aspect room" that stays hot and stale in HCMC's afternoons. The mechanical consequence is that every one of these rooms needs a split AC, in a house where the party walls are shared with neighbours and the duct route is the pipe chase the set barely mentions.
**Basis** International tropical residential practice: single-aspect rooms deeper than about 2.5 × the window head height are conventionally dependent on mechanical cooling; cross-ventilation and stack effect through a vertical shaft are the standard passive response in a deep narrow plan. **UNVERIFIED** — I could not fetch Neufert/BCA/Passivhaus-tropical text in this session; the *observation* that the plan is single-sided on both halves is VERIFIED from the drawings.
**Basis class** BEYOND-LOCAL (UNVERIFIED source) / JUDGEMENT for the observation
**Fix** See D-27 and D-28: turn the existing 1600 light well into a genuine vertical ventilation shaft with openable high-level panels at each floor into the front hall, and give the rear zone a second, high-level opening so the rear bedroom and the mezzanine family room are cross-ventilated rather than single-aspect. This is the largest single livability gain available for the least construction.
**Cost/impact** M
**Evidence label** VERIFIED (the plan is single-sided) / UNVERIFIED (the external rule)

---

**ID** D-24 · **Type** RISK · **Severity** HIGH
**Where** All plans and the section (S1, S2) — the *absence* of any services information. Spec rooms: `bep_an`, `wc_gf`, `wc_truoc_*`, `wc_sau_*`, `sinh_hoat`.
**Issue** There are no MEP drawings in the set, and the only services information anywhere is one label in the section: *"Hộp gen thoát nước"* — a drainage chase box at the rear wall. The walls on the plans are 100, 200 and 350. Six WC positions, a kitchen with a hob and a sink, a washing machine, split AC units, a hot-water system, and the lift's own machine and controls all have to fit into 100–200 mm walls or into the shaft that does not exist yet. The stacked wet areas are not on a common wall line as drawn (D-16, D-17): the ground WC is in the rear band, the rear ensuites are in the rear band, but the *front* ensuites sit at a different position on floors 2–4 and again on floor 5 (the floor-5 WC is 2000 × 1900 at x1960, against the floors 2–4 ensuites at 1800 × 1600 beside the stair). The lift shaft also sits directly against the rear bedroom's party of walls, in the 1800-deep band that the bedroom has to cross.
**Why it matters** Without a services layout the drainage falls, the stack ventilation, the AC condensate and the lift machine all have nowhere to go, and the parties' walls cannot be chased. In a party-wall house, a mistake here becomes a dispute with a neighbour. The mismatch between the front-ensuite positions on floors 2–4 and floor 5 also means the vertical stack is broken exactly where a wet wall is most likely to leak into a bedroom.
**Basis** Buildability and service-stacking practice; the *absence* of information is VERIFIED, the consequences are JUDGEMENT.
**Basis class** JUDGEMENT
**Fix** Before the set is priced: (a) fix one vertical wet-core position for all six WCs (the rear WC band at 1600 wide, which is already a stack) and bring the front ensuites onto the same discipline or accept them as separate stacks with their own ducts; (b) draw a services section through the stair/lift core showing a **200–250 mm vertical duct** for the kitchen hood and a **150 mm soil stack** inside it; (c) add a condensate drop from every AC unit to a fall pipe; (d) fix the lift machine's position and its access with the supplier. Minimum one chase per stack, shown on the plans.
**Cost/impact** M
**Evidence label** VERIFIED (the absence) / JUDGEMENT (the consequence)

---

**ID** D-25 · **Type** RISK · **Severity** MEDIUM
**Where** KC01 (IMG_9981) · KC… M1/M2/M3 (IMG_9983, 9984) · KC… M4/M5 (IMG_9985) · KC… M6/M7/M8 (IMG_9986).
**Issue** One item in the foundation set is a design decision rather than a structure: the cap top levels. M1/M2 caps sit at **−0.500**, M3/M7 caps at **−0.050**, the lift caps M4/M5 at **−1.550** and M6 at **−1.650**. A 450 mm step between footing tops inside one building means the ground slab and the yard levels cannot be a single plane, and it explains (or is explained by) the garage at ±0.000 against a yard at −0.200 (D-10). The M8/M8a caps are drawn with a **slanted edge following the sloped property line** — which is the physical confirmation that the plot boundary tapers, and therefore that the two long walls of the house are not parallel.
**Why it matters** The tapering boundary is the root cause of most of the setting-out risk in this set (D-04): the house's own walls are drawn to a 3900 width at the front and a different width at the rear, so the "core zone and rear light well aligned across floors" rule can only hold if the core is held parallel to the party walls and the taper is taken in the two yards. The designer should say so explicitly on every plan. (Pile adequacy and the eccentric single-pile caps are the `safety` lane's call.)
**Basis class** JUDGEMENT
**Fix** Add a note to every plan: *"Cốt lõi thẳng vuông góc với tường riêng; độ nghiêng ranh giới được xử lý tại sân trước và sân sau"* (the core is set square to the party walls; the boundary taper is absorbed in the front and rear yards), and unify the ground levels to −0.200 throughout the yard with the garage slab at −0.200 as D-10 proposes.
**Cost/impact** S
**Evidence label** VERIFIED (levels READ; the slanted M8a edge is READ)

---

**ID** D-26 · **Type** RISK · **Severity** MEDIUM
**Where** KT06 / KT07 / IMG_9979 / IMG_9980. Spec rooms: `san_thuong_truoc`, `san_thuong_sau`.
**Issue** The roof terrace is not designed as a space. There is no parapet note on either terrace plan, no shade structure, no water point, no laundry line, no planting, no seating, no lighting and no stair from the terrace level to the roof — and the two terraces are separated by the 5200-long stair/lift lobby whose doors D6 and D7 open onto them. The roof plan (KT07) is X-hatched over almost the whole footprint with the roof slab only over the core, so the terraces are open to the sky 3200 below the parapet block shown on the elevation. In HCMC a roof terrace without shade is unusable for most of the day between April and October.
**Why it matters** The roof terrace is the second-largest open area of the house after the front yard, it is the only place the family can be outdoors with a view, and it is where the laundry goes when the ground-level drying space is full. As drawn it is a hot slab with a balustrade and two taps.
**Basis class** JUDGEMENT
**Fix** See D-33: a **1100 parapet** with a coping, a **2500 × 2500** lightweight pergola over the front terrace, a tap with a floor drain, a 2 % fall to the drains already marked, and a laundry line in the rear terrace. Keep the terrace floor at one level with the lobby.
**Cost/impact** M
**Evidence label** VERIFIED (annotations READ; the omissions are transcript-level observations)

---

### IMPROVEMENT (ranked in §5; IDs are referenced there)

**ID** D-27 · **Type** IMPROVEMENT · **Severity** HIGH
**Where** The 1600-wide light well beside the front ensuite WC (KT03/KT04/KT05) and the 2000 × 1500 glazed well on floor 5 (KT06) and the two wells on the roof (KT07). Spec rooms: `hall_front_f2`…`hall_front_f5`, `wc_truoc_*`.
**Issue** The house's one passive-ventilation asset is a set of unconnected slots. Turning them into a shaft is the cheapest large improvement available.
**Fix** Stack the front light wells vertically (confirm per D-19) and treat them as a **ventilation shaft**: at each floor, an **openable louvre 800 wide × 1200 high** in the hall wall beside the shaft, opening at high level (sill at +2.2 m above the floor); a **900 × 900 openable louvre** in the shaft's own side wall at each bedroom and the hall; a **2000 × 1500 glazed panel with a permanent openable quarter** at the head of the shaft on the roof, mosquito-screened; and a grille at the foot of the shaft at ground level so the shaft is not a dead end. Keep the shaft glazed (tempered, with the stainless protection frame the drawing already specifies) so it also lights the front hall. The shaft also becomes the stack for the AC condensate riser (D-24) — one chase instead of six.
**Effect on neighbouring floors** None in plan: no room changes size and no wall moves. It adds a 1200-high louvre to the 1800-deep front hall on floors 2–4 and 5, and it requires the wells to be truly stacked (D-19) and the roof well to be sealed against rain (D-21).
**Cost/impact** M
**Evidence label** VERIFIED (well positions and sizes READ); the external cross-ventilation rule is UNVERIFIED (see D-23).

---

**ID** D-28 · **Type** IMPROVEMENT · **Severity** HIGH
**Where** Rear bedroom / rear WC / *Lô gia* on floors 2–4; *P. Sinh hoạt* / WC / *Sân sau* on the mezzanine; *P. ăn + bếp* / WC / *Sân sau* on the ground floor. Spec rooms: `ngu_sau_f2`…`ngu_sau_f5`, `sinh_hoat`, `bep_an`.
**Issue** (Companion to D-08.) The rear half of the house has no second ventilation opening.
**Fix** With the WC moved off the bedroom's outside wall (D-08), give the rear bedroom a **1200 wide × 1500 high** opening onto the loggia with an openable upper half and a fixed lower 900 (a sliding-and-hop-up window) so it is a real vent and not a light hole; put a **1200 × 1200** window onto the rear yard from the ground kitchen; and give the mezzanine family room the same 1200 × 1500 treatment onto the rear deck. If the rear wall is shared, keep the opening as an internal louvre to a light well — but the loggia is external, so the bedroom can be served directly.
**Effect on neighbouring floors** The loggia floors (SB2/SB3/SB4) stay as they are; the rear bedroom's rear wall gains one opening, which means one more penetration to waterproof and one more opening in the rain-facing façade — this must be detailed at the balcony slab edge (see D-31 for the edge-upstand). The change is identical on floors 2–4, which keeps the façade regular; the mezzanine and ground floor each get one opening of a different size.
**Cost/impact** M
**Evidence label** VERIFIED

---

**ID** D-29 · **Type** IMPROVEMENT · **Severity** HIGH
**Where** KT03 / KT04 / KT05 front ensuite; KT06 floor-5 WC (2000 × 1900 at x1960); KT02 mezzanine WC. Spec rooms: `wc_truoc_f2`…`wc_truoc_f5`, `wc_sau_f2`…`wc_sau_f5`, `wc_gf`.
**Issue** (Companion to D-11 and D-17.) Six wet rooms, six different positions.
**Fix** Adopt **one** standard WC module for the house: **1600 wide × 2100 deep**, door **750** clear, pan against the party wall, basin on the rear wall, and the same tile setting-out. Then: the front ensuite on floors 2–4 becomes 1600 × 2100 by taking 100 from the hall band and 500 from the light-well edge (or by moving the hall, which D-08 already proposes); the floor-5 front WC moves onto the same grid as the floors 2–4 front ensuites; the mezzanine WC takes the same module; and the ground WC takes the same module. Put every soil stack on the party-wall line that is already in the 200 mm wall.
**Effect on neighbouring floors** Every floor's plan changes slightly but identically, which makes the vertical stack regular across five floors, turns five different wet-room build-ups into one, and lets the drainage chase be drawn once. It also removes the floor-5 WC's 200 mm offset from the floors 2–4 position, which is the mismatch that would otherwise break the stack.
**Cost/impact** M (partitions and drainage) — and it reduces cost elsewhere (one formwork and one waterproofing detail instead of six)
**Evidence label** VERIFIED

---

**ID** D-30 · **Type** IMPROVEMENT · **Severity** HIGH
**Where** KT01 ground floor: *Nơi để xe* (3940 × 3200), *P. Khách* (3800 × 3200), the front yard (−0.200). Spec rooms: `gara`, `khach`.
**Issue** (Companion to D-09 and D-10.) The ground floor has no lobby, no store, no laundry and no parking that works.
**Fix** Re-cut the ground floor's front 7400 into three zones, without moving a single external wall: **(i)** *Sân trước* at −0.200, and the garage slab at **−0.200** as well, sloping 1.5 % to a **500 × 500 floor drain** at the threshold, with a 200 mm kerb under the D1 leaves — the car drives straight in; **(ii)** a **1000-wide internal glazed screen** (1000 × 2000 clear, sliding) between the garage and *P. Khách*, with a **900 × 2100 door** in it, so the living room gets daylight and street air while the car bay stays enclosed; **(iii)** inside the 3200-wide garage, a **1400-wide × 2500-deep** strip along the party wall becomes the **laundry and utility bay** — washing machine, 600 sink, 600 × 2000 drainer — which is the single most-used room in an HCMC house and is nowhere in this set (see D-32).
**Effect on neighbouring floors** None. This is a ground-floor-only change, it removes the 200 mm step, it gives *P. Khách* the window it does not have, and it creates the laundry space that D-32 needs. It does require the drainage falls to be re-set on the ground slab (D-21, D-25) and the D1 threshold to be re-detailed.
**Cost/impact** M
**Evidence label** VERIFIED (levels and dimensions READ)

---

**ID** D-31 · **Type** IMPROVEMENT · **Severity** MEDIUM
**Where** All balcony and loggia plans (KT03–KT05 front balconies; KT03–KT05 rear *Lô gia*; KT06 terraces) and the section's front balcony stack (300 | 500 | 600 | 1500 | 500 | 600 | 300). Spec rooms: `ban_cong_f2`…`ban_cong_f5`.
**Issue** The balconies are **recessed within the building line**, not projecting, and 1400 deep. A recessed balcony shades the glazing below it far less than a projecting slab, and the section's stack (300 / 500 / 600 / 1500 / 500 / 600 / 300) shows the balcony slab, upstand and balustrade arriving at the facade with no overhang in front of the glazing at all.
**Fix** Keep the balconies recessed (projecting slabs over a party-wall line are a neighbour problem in this kind of house) but add the shading in the plane of the facade: a **150 mm deep vertical fin at 600 centres** across the 3900-wide balcony face on floors 2–5, or a **600 deep perforated screen** at the balcony edge. The elevation already shows an alternating per-floor panel scheme, so vertical fins read as intended rather than as an addition. Add a **200 mm upstand** at the balcony slab edge with a **drainage outlet every 1500**, because a recessed balcony collects water against the wall it is recessed into.
**Effect on neighbouring floors** Identical detail on floors 2, 3 and 4, which keeps the facade regular. The floor-4 mirrored balcony (D-18) must take the same detail mirrored, and the fin positions must be set out from the same grid as the doors D5 and windows S1 so the fins do not clash with a door swing.
**Cost/impact** S (fins) / M (screen and drainage)
**Evidence label** VERIFIED (balcony depth and the section stack READ)

---

**ID** D-32 · **Type** IMPROVEMENT · **Severity** HIGH
**Where** The whole set — no laundry, drying, storage or refuse element appears on any plan. Spec rooms: `khach`, `bep_an`, `sinh_hoat`, the two yards.
**Issue** A five-storey house in HCMC has no laundry, no drying space, no broom store, no refuse point and no storage beyond the hall bands. The drawings have a front yard of 350–2810 and a rear yard of 2300–2650, two balconies of 1400 and a rear loggia, and a terrace — but nothing is *assigned* to any of it.
**Fix** (a) **Laundry**: the utility bay in the garage (D-30). (b) **Drying**: a **2400-long clothesline** on the rear terrace at +17.200, fixed to two 1200-high posts, plus the rear loggia as the wet-season covered line (the loggia is roofed, so it is the usable line from May to October). (c) **Refuse**: a **600 × 700 ventilated bin store** against the rear wall of the ground floor, screened from the yard, with a paved 1000-wide access strip from the rear door — and the rear door must not be the WC door (D-08 fixes that). (d) **Storage**: convert one **1200 × 1800** slice of the 1800-deep front hall on floors 2–4 into a walk-in store off the front bedroom, leaving the hall 600 wide past it; on the mezzanine, a **1200 × 600** store under the stair; on floor 5, the same store. (e) **Broom/mop store**: **600 × 900** off each front hall, aligned with the stair core so the stack is continuous.
**Effect on neighbouring floors** The store conversions change the front hall depth on the floors chosen (1800 → 600 at the pinch point); stack them on floors 2, 3 and 4 so the façade and the structure are unaffected and the storage repeats. The terrace line is new build on the terrace slab.
**Cost/impact** S–M
**Evidence label** VERIFIED (the absence of these elements across all nine architectural sheets)

---

**ID** D-33 · **Type** IMPROVEMENT · **Severity** MEDIUM
**Where** KT06 (front terrace 3500 clear / 3900 overall; rear terrace 6100 long) · KT07. Spec rooms: `san_thuong_truoc`, `san_thuong_sau`.
**Issue** The terrace is the house's best asset and is drawn as an empty slab (see D-26).
**Fix** Front terrace: a **2500 × 2500** pergola on four **150 × 150** posts at **2400** above the floor, with a **150 mm** slatted screen on the street side to screen the neighbour windows of the unit above; **two** planters of **1500 × 400 × 450** on the party walls; and a **1200 × 450** bench. Rear terrace: the laundry line (D-32(b)), a **1200 × 400** veg-trough or planter run, and a **tap with a floor drain**. Fix the terrace level, the falls and the parapet (D-21, D-26) at the same time.
**Effect on neighbouring floors** None below. The pergola must be founded on the terrace slab, which is a structural question for the `safety` lane, and it must not foul the lift overrun (D-01) or the stair light well (which is a glazed floor panel with an unrated load — see §7).
**Cost/impact** S
**Evidence label** VERIFIED (terrace dimensions READ)

---

**ID** D-34 · **Type** IMPROVEMENT · **Severity** MEDIUM
**Where** KT02 mezzanine front void edge; KT06 floor-5 stair light well (*"Ô lấy sáng gắn kính cường lực, có khung inox bảo vệ"*, 2000 × 1500); KT03–KT05 light wells; all balconies and loggias (8 mm tempered glass, stainless handrail — no height or glass spec given).
**Issue** The guarding system is named but not specified: *"Lan can kính cường lực dày 8 ly, gắn tay vịn inox"* is the entire balustrade specification for every balcony, loggia and the mezzanine rear, with no height, no glass type, no handrail height, no fixing detail and no guard at the mezzanine's front void edge or the terrace edges.
**Fix** Write a balustrade schedule: minimum height, glass type (laminated toughened, not monolithic, over a stair and over a drop), post spacing, handrail height and profile, and a **1100 minimum** everywhere with **1200** on the void edge and the stair well. Continue the same 8 mm toughened glass with stainless handrail at the mezzanine front void edge so the double-height space reads as one system, and specify the stainless protection frame over the glazed stair light well as a **notched balustrade** rather than a flat frame.
**Effect on neighbouring floors** One schedule applies to floors 1–5 and the terrace; the floor-4 mirrored balcony (D-18) takes the same schedule mirrored. (Fall-protection adequacy is the `safety` lane's call; this finding is about the fact that no specification exists to hand to that lane.)
**Cost/impact** S (schedule) / M (upgrading monolithic glass to laminated over the stair and the void)
**Evidence label** VERIFIED (the note text is READ; the absence of a height or glass specification is VERIFIED across all nine sheets)

---

**ID** D-35 · **Type** IMPROVEMENT · **Severity** MEDIUM
**Where** KT01 (front yard 350–2810 internal; *P. Khách* has no opening, D-09) · IMG_9979 elevation (ground: 550 | 2800 | 550; D1 four-leaf glazed 2800 × 2800; stone cladding; mezzanine K1 2800 × 1700).
**Issue** The house meets the street with a 2800-wide, 2800-high glazed four-leaf door and a 2800-wide, 1700-high clerestory directly above it, with only a shallow front yard. The street elevation is the whole street-facing asset and the drawing shows no screen, no planting, no canopy and no privacy control; and the ground floor's only room with a street relationship is the garage.
**Fix** (a) **Privacy**: a **600-deep perforated or slatted screen** across the front yard at 2100 high on **150 × 150** posts, set 600 in front of the facade, with a 1200 gap for the gate — it shades the D1 and the K1 and stops direct street views into the garage door. (b) **Shade**: a **900 × 2400** canopy on two **150** posts over the entry, aligned with the D1 head. (c) **Living**: move the house's street door to a **1200-wide** door in the 550 pier beside the garage rather than the full 2800 garage leaf, with the garage leaf reduced to **2400** — a 2800-wide glazed leaf is a curtain wall, not a door. (d) Grow the front yard: if D-25's note (the taper is absorbed in the yards) is adopted, the front yard can be set at **2500–3500** and the garage pushed back, which gives the house a proper forecourt and solves D-09 at the same time.
**Effect on neighbouring floors** No effect above ground. On the ground floor it changes the D1 detail and the yard levels, and it moves the garage's rear wall, which moves the *P. Khách* depth — 4240 grid at present, which would become 3240–4240 depending on how far the garage is pushed back. That is a ground-floor-only change and it does not touch the core.
**Cost/impact** S–M
**Evidence label** VERIFIED (elevation dimensions and notes READ)

---

**ID** D-36 · **Type** IMPROVEMENT · **Severity** MEDIUM
**Where** KT06 (tầng 5 = lobby + two terraces) vs the earlier model's tầng 5 (P. ThỜ + bedroom + WC). Spec rooms: `tho_f5`, `san_thuong_truoc`, `san_thuong_sau`.
**Issue** (Companion to D-13.) With tầng 5 drawn as a lobby and two terraces, the house has 2 + 2 + 1 + 1 + 1 = 7 bedrooms across floors 2–5 in the scan's reading, against 8 in the compiled model.
**Fix** Decide the top-of-house programme deliberately and write it on one sheet (D-01). The most useful arrangement, given the 3900 width and the family this house is for: keep *P. Thờ* on tầng 4 with the reading room as a **study that can become a bedroom** (add a 900 door from the hall side and a 900 × 1500 opening to the light well so it can be closed off), keep the rear bedroom on tầng 4, and treat tầng 5's lobby as a **multi-purpose family floor** with the terraces, plus a **1200 × 1600 enclosed WC-and-store** in the lobby band so the top floor is usable. This makes the house able to run as 2 / 2 / 2 / 1+study / family-floor and to grow to 3 bedrooms on tầng 4 without touching the structure.
**Effect on neighbouring floors** Only the tầng 4 reading room and the tầng 5 lobby change. If the reading room becomes a bedroom, its WC must align with the stack from D-29 — the *P. Đọc sách* zone on tầng 4 has no WC of its own, so a 1500-wide WC must come out of the 2300 hall band, which is where the *P. Thờ* / reading room partition already is.
**Cost/impact** M
**Evidence label** PARTIAL (depends entirely on D-01, which is unresolved)

---

**ID** D-37 · **Type** IMPROVEMENT · **Severity** MEDIUM
**Where** KT03–KT05 (bedrooms 4000 deep, 4240 grid, 3200 clear) · the front bedroom's only opening is D5 + S1 onto the balcony.
**Issue** The front bedrooms are 3200 clear wide × 4000 deep (≈ 12.8 m² gross) and X1's minimum for a double bedroom is 12 m² — before the bed, the wardrobe and the circulation. A 1800 × 2000 bed plus a 700 passage takes 4.9 m², leaving under 8 m² of usable floor in a room whose glazing is on the balcony side only.
**Fix** Two minimal moves per front bedroom: (a) a **600-deep** run of full-height joinery along the party wall opposite the bed, giving the wardrobe a home and taking the storage pressure off the walls; (b) align the door D5 and the window S1 so that the **S1 window** (1400 on the grid) sits beside the bed rather than opposite the door, so the bed head has a view and the room can be cross-ventilated through the balcony and the door. On the rear bedrooms, apply the same 600-deep joinery against the party wall — with the D-08 change the rear bedroom gains its own window, and the joinery must not block it.
**Effect on neighbouring floors** The front bedrooms are floors 2, 3 and 4 with identical plans, so one detail repeats three times; the joinery is 600 deep and stays within the 3200 clear width, leaving 2600, which is more than the 1600 a double bed plus a passage needs. The rear bedrooms are floors 2–5 and take the same detail on the opposite wall.
**Cost/impact** S
**Evidence label** VERIFIED (areas computed from READ dimensions; the 12 m² requirement is VERIFIED from X1)

---

**ID** D-38 · **Type** IMPROVEMENT · **Severity** LOW
**Where** KT06 front terrace (3500 clear) and KT07's *Ô kỹ thuật thang máy*.
**Issue** The lift overrun is a 2000-wide blank block standing on the roof next to the front terrace — the most visible element of the house from the street and from the neighbours' upper windows, and it is left as an unadorned concrete box.
**Fix** Clad the overrun in the same finish as the top-floor exterior wall — the elevation already specifies *"Tường ngoài sơn nước trắng"* and *"Tường lan can sơn nước màu xám nhạt"* for the top floor — and add a **600-deep perforated metal screen** on its street face, standing off the structure, to screen the lift machinery and the roof access door from the street and from the upper windows of the neighbouring units.
**Effect on neighbouring floors** None. The screen must not foul the top-floor window S2 or the door D6 (D-01), so it can only be fixed after D-01 is resolved.
**Cost/impact** S
**Evidence label** VERIFIED (finishes notes READ on IMG_9979)

---

## 4. Top 12 improvements, ranked by impact per unit of cost

| # | ID | Improvement | Impact | Cost | Why it ranks here |
|---|---|---|---|---|---|
| 1 | D-08 + D-28 | Give the rear bedroom, the mezzanine family room and the ground kitchen their **own window**, by moving the WC off the bedroom's outside wall and adding a 1200 × 1500 opening to the loggia (rear bedroom / mezzanine) and a 1200 × 1200 to the rear yard (kitchen) | HIGH | M | Turns three windowless rooms into daylit, ventilable ones. No external wall moves, no footprint changes. Highest livability gain in the set. |
| 2 | D-27 | Make the 1600 light well a **ventilation shaft** — stacked, openable louvres at each floor, glazed and rain-sealed at the head, and it doubles as the AC-condensate and duct riser | HIGH | M | The only passive cooling available in a single-sided plan; one chase instead of six (D-24). |
| 3 | D-29 | **One standard WC module** (1600 × 2100) at all six wet positions, on a common stack | HIGH | M | Fixes the sub-3 m² front ensuite (D-11), makes the stack regular, and cuts six wet-room build-ups to one. |
| 4 | D-30 | Rebuild the ground floor's front: garage at **−0.200** with a ramp-free threshold and a floor drain, a glazed screen + door between garage and *P. Khách*, and a **1400 × 2500 laundry/utility bay** in the garage | HIGH | M | Fixes the car that cannot enter (D-10), the windowless living room (D-09), and the missing laundry, in one edit. |
| 5 | D-13 + D-36 | **Re-issue the compiled spec to the drawings**: tầng 4 = *P. Thờ* + *P. Đọc sách* + rear bedroom; tầng 5 = lobby + two terraces; roof at +20.400; parapet at +21.900 | HIGH | S | Until this is done every area, quantity, render and price off the model is wrong by 1900 mm of height and one storey of programme. Cost is a spreadsheet edit. |
| 6 | D-01 + D-34 | **One coordinated top-of-house sheet** and a **balustrade schedule** | HIGH | S | Unblocks the terrace design, the plant room, the roof waterproofing scope and the safety lane's guard review, which are all waiting on it. |
| 7 | D-32 | Assign **laundry, drying, refuse and storage**: utility bay + rear-terrace clothesline + loggia line + bin store + one walk-in store per floor | HIGH | S–M | These are the rooms a HCMC family uses daily and none of them exist in a five-storey plan. |
| 8 | D-31 | **Vertical fins** at the recessed balconies + a **200 mm upstand** and drainage outlets at the balcony edge | MEDIUM | S | Cheapest way to get shade onto a recessed balcony and to stop the balcony edge collecting water against the facade. |
| 9 | D-24 | Issue a **services section**: one 200–250 duct riser in the core, one soil stack, condensate drops, the lift machine position | MEDIUM | M | Without it the pipe chases get built in party walls and the wet-area stack breaks on floor 5. |
| 10 | D-21 + D-26 | A **drainage sheet** — levels, falls, gutters, overflows, the lift-pit sump — and the terrace **parapet, pergola, tap and 2 % falls** | MEDIUM | M | HCMC rain plus a lift pit with no waterproofing is a guaranteed defect; the drainage scope is unpriceable without it. |
| 11 | D-35 | **Privacy and shade to the street**: a 600-deep screen across the front yard, a 900 canopy, and a 1200 house door in the 550 pier rather than a 2800 glazed garage leaf | MEDIUM | S–M | The street elevation is the house's only public face and it is currently a garage curtain wall. |
| 12 | D-37 | **600-deep joinery** in every bedroom, and set the S1 window beside the bed head rather than opposite the door | MEDIUM | S | Turns a marginal 12.8 m² bedroom into a usable one, identically on floors 2–4. |

---

## 5. Questions for the contractor / designer

Ready to send as-is. Numbering is for their answer, not for argument.

1. **Top of house (D-01).** Is the band between +17.200 and +20.400 an enclosed room or an open terrace? On the elevation it carries door D6 (1000 × 1100) and window S2 (1200) and a 1500 parapet block; on KT06 the same level is a lobby with two open terraces; on KT07 the roof is X-hatched over almost the whole footprint. Please confirm which is correct and re-issue KT05–KT07, the elevation and the section together.
2. **Heights (D-13).** Please confirm tầng 5 is 3200 high (+17.200 → +20.400) and that +21.900 is the parapet top, giving an overall height of 21900. The levels we hold from the earlier reading (+20.600 / +23.800 / +25.800) do not appear on these sheets.
3. **Programme (D-13).** Please confirm tầng 4 contains *P. Thờ* and *P. Đọc sách* and one bedroom, and tầng 5 contains no rooms — only the lobby and the two terraces.
4. **Lift shaft (D-02).** The plans show 1800 × 1600; the pit detail shows 1600 clear / 2000 overall in section but 2100 × 2050 with a 1500 × 1450 clear in plan; the hoist slab is 2000 × 2000; the roof overrun is 2000 wide. Please state **one** shaft size and **one** pit level (−1.650 or −1.550) and issue the lift supplier's minimum-shaft and pit-depth data sheet.
5. **Lift overrun (D-03).** Is the overrun 1300 high (as read from the section) or 2000 (as read earlier)? If 2000, does the building's stated overall height change, and if so, what is the new number?
6. **Dimension chains (D-04).** Several chains do not close: on KT01 the top chain sums to 25350 against a printed 25000; the second chain to 23800; the bottom chain to 24000; on KT02 the bottom chain to 23250; on KT03 the bottom chain to 23150 against 23750. Please re-issue with one closing chain per axis per side and confirm whether the front offset is 3360 and the rear 2300/2650.
7. **Stair width (D-06).** The architectural ground and mezzanine plans show 1250-wide flights; the structural ground and mezzanine stair sheets show 1350-wide flights in the same 3200 well. Which is correct? And please issue the stair detail the section refers to — including the winder geometry, the landing, the handrail and the headroom.
8. **Stair risers (D-07).** 21 risers per storey gives 176.2 / **152.4** / 162.0 with a 250 going. The mezzanine flight's 2R + G is 555, below the 600–630 comfort band. Please confirm whether the riser count may vary by storey (we suggest 20 at 160 on the mezzanine and 20 at 170 above), and note that the drawn 250 going is below the 254 that the 2024 IBC requires for a dwelling stair.
9. **Rear bedroom, mezzanine room and kitchen windows (D-08).** As drawn, the rear bedroom, *P. Sinh hoạt* and the kitchen have no opening of their own and reach daylight only through the WC. May we swap the WC and a 900-wide vestibule so the bedroom opens to the loggia with a 1200 × 1500 window, and give the kitchen a 1200 × 1200 window to the rear yard?
10. **Ground living room (D-09).** *P. Khách* carries no window and no door tag on KT01 and the section shows no opening to it. Is that a drafting omission or the design? If the design, how is a 12.8 m² living room daylit?
11. **Garage (D-10).** The yard is at −0.200 and the garage at ±0.000, with no ramp drawn, and the internal depth is 3940 against a car length of about 4500. Do you accept lowering the garage slab to −0.200 with a 1.5 % fall to a floor drain? And please confirm the maximum vehicle length the bay is designed for.
12. **Front ensuite area (D-11).** Is the front ensuite 1800 wide (850 + 950) or 1950? At 1800 × 1600 it is 2.88 m², under the 3 m² that TCVN 13967:2024 requires for a WC.
13. **Mezzanine void extent (D-12).** How long is the *Thông tầng* void over the front? We read 8140, covering the garage and *P. Khách* in full, against 12300 in the earlier reading. Is the car under a roof, and does *P. Khách* have a floor above it?
14. **WC layouts (D-17).** There are three different WC layouts in the set (1800 × 1600, 1600 × 2100, and the ground-floor arrangement). May we standardise on 1600 × 2100 for all six wet positions so the stack is regular?
15. **Ground-floor rear band (D-16).** Please close the dimension chain for the last 8000 and state which way the rear WC faces — 1600 along the house or 1600 across it — and fix the kitchen depth at 4400.
16. **Balcony mirror on tầng 4 (D-18).** Is the mirrored balcony on KT05 (and the mirrored left end on the floor-4 structural sheet) intentional? If so, please annotate it and dimension it to the same numbers as floors 2–3.
17. **Light wells (D-19).** Do the front light wells on floors 2–4 stack vertically with the floor-5 well and the two roof wells? Please confirm on one vertical section with x-positions dimensioned, because the whole ventilation strategy depends on it.
18. **X-hatch legend (D-14).** Please add a legend to every sheet defining X, the diagonal hatch and *Sân thượng*, and apply it identically on the architectural and structural sheets.
19. **Wall–beam coordination (D-20).** Please issue a wall-to-beam table replacing the note "add 2Ø16 or 3Ø16 where there is a wall", and correct the DS2a axis 2–3 span, which is dimensioned 4600 on that sheet against 4240 everywhere else.
20. **Drainage and levels (D-21).** Please issue levels and falls for the front yard, garage, rear yard, both terraces and the roof, with gutter, downpipe and overflow positions, and specify the lift-pit waterproofing, sump and drain.
21. **Sheet control (D-15).** Please supply the full architectural dossier — we hold 9 of the 20 sheets the title block implies, the door and window schedules are not in the set, and KT08 onward were never photographed. Please also re-issue with a populated title block and a revision table, and correct the title-block scale (it reads 1/20 on the 1/100 plans).
22. **Grid naming (D-05).** Please use one grid naming across the structural set: DS1a calls the axis-6 position "7" and DS2 calls 5a "5".
23. **Terrace and roof scope (D-26, D-33).** Please confirm the terrace level, the parapet height, the waterproofing and the drainage, and whether a pergola and a laundry line on the rear terrace are acceptable to the building line and to the neighbours.
24. **Services (D-24).** Please issue a services section through the stair/lift core: the kitchen extraction duct, the soil stack, the AC-condensate drops and the lift machine.
25. **Boundary taper (D-25).** Please add a note to every plan stating that the core is set square to the party walls and that the boundary taper is absorbed in the front and rear yards — and confirm the core's alignment on every floor.

---

## 6. What the sources agree on

- **The plot envelope.** 25000 deep (printed on every sheet and the foundation layout, with chains that close exactly at 25000) and 3900 wide at the front, with 350 party walls leaving 3200 clear — consistent across the architectural plans, the structural grid and the elevation (S1, S2, S3).
- **The storey heights up to tầng 4.** ±0.000, +3.800, +7.000, +10.400, +13.800 with 3800 / 3200 / 3400 / 3400 — the level tags agree between the elevation (IMG_9979) and the section (IMG_9980), and the stair sheets' 3700 / 3200 / 3400 floor-to-floor figures match them.
- **The core.** A 3200-long stair well plus an 1800 lift band, roughly at mid-depth, repeated on every plan; the structural grid's 3200 + 1800 bays at axes 4–5 match the architectural stair/lift band on every sheet.
- **The staircase is one U-return with 21 treads at 250 going**, serving all floors, with a 1250 landing — consistent between the architectural plans (odd-numbered treads 1…21 on KT01–KT06) and the structural stair sheets, which add the riser heights the plans lack.
- **The wet-area position.** A WC in the rear band on every floor, and the *Hộp gen thoát nước* chase in the rear wall in the section — the rear band is where the plumbing is, and it repeats.

## 7. Where the sources conflict, or are thin

- **The two readings of the same five architectural PDFs disagree on the top two floors** (D-13) — one says tầng 5 has a room, the other says it has none, and they differ by 1900 mm of building height. Both are visual reads of textless PDFs (verified: 0 extractable characters), so neither can be dismissed from the documents alone. This is the most consequential conflict in the review.
- **The architecture and the structure disagree on the ground and mezzanine stair flight width** (D-06), and the structural set disagrees with itself on the grid naming (D-05) and on one beam span (D-20).
- **The lift exists but its size is unsettled across four documents** (D-02).
- **Thin: the top of the house.** Five sheets, five readings, no agreement (D-01, D-14).
- **Thin: the dimensions.** No chain on KT01, KT02 or KT03 closes; I cannot tell which of two or three competing values is right, only that they cannot all be (D-04).
- **Thin: services.** There are no MEP sheets, no drainage design, no electrical, no ventilation and no equipment schedules anywhere in the set. Every services finding is an inference from what is missing.
- **Thin: orientation.** No north point on any sheet, so which façade takes the west sun is unknown and I have not asserted it; D-31 and D-35 are therefore deliberately orientation-agnostic.
- **Not available at all:** the architectural stair detail, the door and window schedules, the general-notes sheet, sheets KT08 onward (11 of the 20 architectural sheets were never photographed), the four untranscribed photographs (`jpg/sheet1–sheet4.jpg`), and any finish or materials schedule beyond the floor-finish legend.
- **External references are deliberately thin.** Only TCVN 13967:2024 (X1) and the 2024 IBC Chapter 10 / 2R+G rule (X2, X3) were fetchable. Neufert, Singapore BCA, HK and UK residential guidance, and Passivhaus tropical guidance were not reachable in this session, and every rule I would have quoted from them is marked **UNVERIFIED** rather than paraphrased as if fetched. Notably X1 is used here only for areas, clear heights and daylight/ventilation of habitable rooms; the cross-ventilation and stack-effect reasoning in D-23, D-27 and D-28 rests on JUDGEMENT from the plan geometry, not on a fetched external standard.

---

## 8. Sources

| # | Source | Label |
|---|---|---|
| 1 | `contractor/scan-2026-10-22/transcript-architecture.md` — IMG_9972–9980, nine architectural sheets (KT01–KT07 + 2 partial) | VERIFIED (read 2026-10-22) |
| 2 | `contractor/scan-2026-10-22/transcript-foundation-stairs.md` — IMG_9981–9988 + 0003–0005, foundations, columns, lift pit, hoist slab, three stair sheets | VERIFIED (read 2026-10-22) |
| 3 | `contractor/scan-2026-10-22/transcript-beams-slabs.md` — IMG_9989–9999 + 0001–0002, grade beams, floor beams, five slab plans | VERIFIED (read 2026-10-22) |
| 4 | `designs/contractor-as-drawn.measurements.md` rev.2 — earlier direct read of the five PDFs | VERIFIED (read 2026-10-22); superseded in part by this review (D-13) |
| 5 | `designs/contractor-as-drawn.fidelity.md` rev.4 — open items (a)–(n) | VERIFIED (read 2026-10-22); (a), (c), (d), (g) addressed in §2 |
| 6 | `designs/contractor-as-drawn.json` — compiled spec (rooms, rects, storeys) | VERIFIED (parsed; room ids, storeys and rects only) |
| 7 | `contractor/*.pdf` — the five architectural PDFs of the earlier reading | VERIFIED as textless (0 characters extractable on all five pages) — no text could be used to re-verify a figure |
| 8 | TCVN 13967:2024 *Nhà ở riêng lẻ – Yêu cầu chung về thiết kế*, §5.10 Table 1 — areas and clear heights (source: `tieuchuan.vsqi.gov.vn`) | VERIFIED (fetched 2026-10-22) |
| 9 | 2024 IBC Chapter 10, *Means of Egress* (source: `codes.iccsafe.org`) — dwelling stair max riser 197 mm, min tread 254 mm | VERIFIED (fetched 2026-10-22) |
| 10 | Stair comfort rule 2R + G = 600–630 mm | VERIFIED (search result 2026-10-22) |
| 11 | Neufert; Singapore BCA Code on Accessibility for the Built Environment; HK Housing Authority design guides; UK Approved Document B; Passivhaus tropical guidance | NOT FOUND — search allowance exhausted; no rule from these is cited as fact anywhere in this review |
| 12 | `_scan1022/rooms2.py`, `_scan1022/chk.py`, `_scan1022/pdftext.py` — my own arithmetic and extraction checks | VERIFIED (this session) |

**Finding count: 38** — 15 ERROR (D-01…D-15), 7 INCONSISTENCY (D-16…D-22), 4 RISK (D-23…D-26), 12 IMPROVEMENT (D-27…D-38). The 12 ranked improvements in §4 are drawn from D-08, D-27, D-28, D-29, D-30, D-13, D-36, D-01, D-34, D-32, D-31, D-24, D-21, D-26, D-35 and D-37, several of them as paired entries.

**Cross-references outside this lane** (one line each, as the brief requires): guards at the mezzanine void edge, the terrace edges and the glazed stair light well → `safety` lane (D-34, §7); pile capacity, eccentric single-pile caps, beam spans and the 3200 clear span over the mezzanine void → `safety` lane (D-25, D-20, D-12); the *P. Thờ* position and the terrace axes → `phongthuy` lane (D-36, D-33).
