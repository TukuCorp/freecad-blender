# Phong thuỷ review — contractor drawing set, scan 2026-10-22

Project: NHÀ Ở RIÊNG LỆ, 506 Đường Hồng Bàng, phường Minh Phụng, TP.HCM (title block, IMG_9972)
Reviewer: phong thuỷ (Bat Trach / Lo Ban / nhà ống folk rule / Phi Tinh) — culture layer only
Date: 2026-10-22 (Asia/Ho_Chi_Minh)
Output: `contractor/scan-2026-10-22/review/out-phongthuy.md`
Companion reviews (other agents): safety, design errors — not duplicated here.

---

## 0. Method and evidence limits

**What this document is.** A report of what the Vietnamese feng shui tradition says about
this specific building, attributed to named sources, with the drawing facts it rests on
and the practical reason (if any) that usually sits behind the rule. It is a cultural
review, not engineering, not medicine, not a forecast. The tradition holds that qi
follows these patterns; it has not been demonstrated to do so. Where a phong thuỷ
remedy would harm safety or livability, this report says so and **safety wins**.

**What the reviewer could and could not see.** The drawings were read only through the
three transcripts in `contractor/scan-2026-10-22/` (`transcript-architecture.md`,
`transcript-foundation-stairs.md`, `transcript-beams-slabs.md`), the reconstructed spec
`designs/contractor-as-drawn.json`, and the two companion memos
`designs/contractor-as-drawn.measurements.md` and `designs/contractor-as-drawn.fidelity.md`.
No image was viewed. Every drawing fact below is labelled VERIFIED (transcript line, or
the JSON/measurement file) or PARTIAL (the transcript itself says so).

**Hard limits carried into every finding.**

- **The facing direction is unknown.** The caller checked the ground-floor sheet
  (IMG_9972) directly: there is no north arrow and no compass glyph on it, and the
  architecture transcript records none either. `designs/contractor-as-drawn.json` has no
  `site.north_deg`; `fidelity.md` (Provenance addition, 2026-08-19) says a compass glyph
  exists on the *stamped approval sheet* (`contractor/approval drawing.jpg`) but its
  bearing cannot be read at that resolution. **Facing direction: NOT FOUND in the scan.**
  Therefore no finding below states a compass direction for this house, and the
  eight-direction table in §1.2 is conditional.
- **The one drawing fact that is known:** the street is on the short side at the left of
  the plans; the chain runs front yard → garage → living room → core → rear. In all
  plans the front is on the LEFT and the rear on the RIGHT; in the long section (9980) it
  is mirrored. Structural axis labels **A** and **B** are the two party walls across the
  3.9 m width and are *not* compass directions.
- **The owner birth data is not given and is not invented here.** §4 supplies a
  questionnaire and a decision tree instead.
- **Two schools of the drawing-reading disagree on the ground floor.** The phone-photo
  transcript (IMG_9972) reads the ground floor front→rear as *sân trước → nơi để xe →
  P. khách → thang + thang máy → **P. ăn + bếp** → **WC** → sân sau*, while the earlier PDF
  read (`measurements.md`, rev.2) and the JSON model put **WC then kitchen** at the rear.
  The *rear bands* (4500 kitchen-band and 1600 WC-band) are the same size in both, and
  every finding that depends on this swap is labelled CONTESTED and stated conditionally.
- **Lo Ban arithmetic was computed, not copied.** The ruler tables below were computed
  from the cycle structure and the cung name/offset tables of the cited sources; the
  script is `_scan1022/loban.py`. Different schools use a different zero point on the
  42.9 and 38.8 rulers, so where the answer flips between the two conventions the finding
  says so instead of picking silently.

**What was excluded as evidence.** Forums, social media, anonymous testimonials and
SEO “xem phong thủy” list pages that copy one another were not counted as VERIFIED.
Several such sites were read as *leads*; the underlying data was then confirmed against
the sources in §9 (published Vietnamese practitioner pages, Vietnamese newspaper
articles, a Vietnamese architecture/engineering firm page, and Chinese-language
reference sites that state the underlying rule rather than a lucky-number list).

---

## 1. House direction (hương nhà)

**Printed north-arrow bearing: NOT FOUND.** Evidence: caller check of IMG_9972 (no north
arrow, no compass glyph on the ground-floor plan); `transcript-architecture.md`,
“Common to all nine sheets” (no north arrow recorded on any sheet); `fidelity.md` lines
293–297 and 363–364 (the schema has no north angle; the sheets carry no readable north
point; shadows in the renders are decorative, not solar).

**Facing direction: NOT FOUND in transcript.**

Two distinct terms must not be confused, and the confusion is the single most common
error in Vietnamese “xem hướng nhà” practice:

| term | meaning | how it is measured |
|---|---|---|
| **Hướng nhà** (huơng nhà) | the direction the front *faces* — the outward view from the main door | stand at the main door, look out, read the compass bearing |
| **Hướng tọa** (huơng toa) | the direction the house *sits with its back to* — 180° opposite | derived, never measured directly |
| **Cung trạch** (cung trach) | the house's own quẻ, fixed by its sitting direction | derived from the tọa direction, not from the owner's birth year |
| **Cung phi** (cung phi) | the *person's* quẻ | birth year + gender — see §2.1 |

For this house the main door is the glazed door **D1** in the front wall of the garage
block (IMG_9972, IMG_9979: “D1 door 2800 x 2800 (READ; four-leaf glazed door with
transom)”), and the street is on the short side. The 24-mountain sub-direction cannot be
computed at all without a bearing.

### 1.1 The one measurement the owner can take in five minutes

1. Stand **at the front door, on the threshold, facing out of the house**, away from it.
2. Phone compass flat, held at waist height (a feng shui compass held at the chest
   reads the magnetised iron of the gate; at the waist it does not).
3. Read the bearing, and repeat it three times from two or three different points of the
   front yard — the reading must be stable to about ±5° before it is used for anything.
4. Record the **degree bearing**, not just the eight-direction name: the 24-mountain
   (24 sơn) reading used by Phi Tinh (§4.4) needs degrees, and the eight-direction table
   in §2 needs only the name.
5. Note the elevation of the site. On a street that runs roughly E–W, a south-facing
   house gets a hard afternoon sun on the facade; a north-facing one gets almost none.
   The bearing alone does not tell you that — the bearing plus the street's own axis does.

Useful reference points for reading a bearing. The eight-direction bands are fixed by the
compass rose; the finer 24-mountain (24 sơn) subdivision is a separate 15-degree layer
that only a Phi Tinh reading needs:

| eight-direction band | compass centre | the four cardinal sơn centres inside the eight-direction scheme |
|---|---|---|
| **Bấc (N)** | 0° (337.5°–22.5°) | Tý at 0° |
| **Đông Bấc (NE)** | 45° (22.5°–67.5°) | Cấn at 45° |
| **Đông (E)** | 90° (67.5°–112.5°) | Mão at 90° |
| **Đông Nam (SE)** | 135° (112.5°–157.5°) | Thìn at 135° |
| **Nam (S)** | 180° (157.5°–202.5°) | Ngọc at 180° |
| **Tây Nam (SW)** | 225° (202.5°–247.5°) | Khôn at 225° |
| **Tây (W)** | 270° (247.5°–292.5°) | Dậu at 270° |
| **Tây Bấc (NW)** | 315° (292.5°–337.5°) | Nhâm at 315° |

**Evidence label.** The eight-direction bands and the 45-degree centres are ordinary compass
geometry and are not in dispute. The 24 sơn layer is a 15-degree division of the circle
into 24 bands, each named after one of the 12 địa chi, 8 thiên can or 4 quế, with
the middle 5 degrees of each band called the **chính khí** and its two flanks the
**kiêm hướng** - VERIFIED from [13], [14] and [21]. **The individual band
boundaries beyond the four cardinal sơn were NOT verified against a printed table and
are deliberately not reproduced here**; the owner should read them off the sơn list in
[14] or off a physical feng shui compass when a Phi Tinh reading is commissioned. The one
datum confirmed verbatim in a source is Mão = 82.5°–97.5° with its centre at 90° ([13]).

### 1.2 Conditional eight-direction table (use only after the bearing is known)

How to read it: “Huơng nhà” = the outward bearing of the front door. The right-hand
column is the *four-good-directions* set of §2 for the two groups; the “best four” column
is the universal preference of the Bat Trach house-facing practice. Nothing here tells
you what is good for *this owner* — that needs the birth year (§4).

| If the front faces… | hướng tọa (house sits) | Traditional verdict on the plot | Bat Trach note |
|---|---|---|---|
| **Bắc (N)** | Nam | preferred by most practitioners (tọa cát hướng cát); the sun sits behind the house, the facade is in soft north light, and a tube house gets no brutal western afternoon sun | for Đông tứ mệnh owners this is one of the four good directions (Phục Vị of Khảm) |
| **Đông (E)** | Tây | morning sun on the facade, cold afternoon shade — for a narrow east–west tube house this is often the most comfortable | for Đông tứ mệnh owners: Thiên Y (Ly) or Diên Niên (Chấn) |
| **Nam (S)** | Bắc | most sun, hottest in HCMC; in a 3.95 m-wide house the front rooms get sun but the rear stays shaded | for Đông tứ mệnh owners: Diên Niên (Khảm) or Phục Vị (Ly) |
| **Tây (W)** | Đông | hardest for a tube house — low afternoon sun straight down the length, hottest facade | for Tây tứ mệnh owners the reverse: Tây is Sinh Khí of Càn and Phục Vị of Đoài |
| **Đông Bắc (NE)** | Tây Nam | soft light, morning sun only; widely liked | for Tây tứ mệnh owners: Sinh Khí of Khôn, Diên Niên of Càn |
| **Đông Nam (SE)** | Tây Bắc | morning sun plus good cross-ventilation through the length | for Đông tứ mệnh owners: Sinh Khí of Khảm and Khôn — the “best” direction |
| **Tây Nam (SW)** | Đông Bắc | hot afternoon sun on the facade | for Tây tứ mệnh owners: Sinh Khí of Cấn, Thiên Y of Càn |
| **Tây Bắc (NW)** | Đông Nam | afternoon sun, but a side-rear aspect usually means the neighbours block it | for Tây tứ mệnh owners: Sinh Khí of Đoài, Thiên Y of Cấn |

**A note on the geometry of this house specifically.** The 24 m depth runs between the
street and the rear, and the street is on the short side. Whichever way the house faces,
air and light will run *along* the length, not across it. The practical consequence is
that the *rear* of a tube house is the dark, still end (the rear yard is only 1200–2650
deep, and the ground-floor rear rooms sit over the rear WC and the kitchen). The
tradition's repeated practical point — that the front should receive the incoming qi and
the rear should be the *quiet* end — matches the daylight and ventilation reality here
better than it matches a wide house. That is one of the few places where the tradition
and the physics agree without needing to be told to.

---

## 2. Bat Trach (Eight Mansions)

**Label: the tables below are copied from the tradition, not derived from this house.**
They are reproduced so the owner can look up their own year. Three independent Vietnamese
sources and two Chinese-language references were compared line by line and agree on every
cell: [1], [3] and [17] (the eight per-cung listings), [18] (the four-good-direction table), and
[19], [20] (the eight-star tables and the 64-cell ming-zhai matrix). See §9 for the full list and
labels.

### 2.1 The formula for cung phi

The working formula used by [1], [2], [3] and [19] (all four agree):

1. **Use the lunar (âm lịch) birth year.** Anyone born before Tết belongs to the previous
   lunar year. Tết 2026 fell on 17 Feb 2026; anyone born 1–16 Feb 2026 is a 2025 birth.
   Source [2] states this explicitly with its worked example.
2. **Let d = the digit root of the four-digit year** (add the digits repeatedly until one
   digit remains). 1985 → 1+9+8+5 = 23 → 2+3 = 5, so d = 5.
3. **Male:** k = 11 − d. **Female:** k = d + 4. If the result exceeds 9, subtract 9.
4. **k maps to the quẻ:** 1 Khảm · 2 Khôn · 3 Chấn · 4 Tốn · 6 Càn · 7 Đoài · 8 Cấn · 9 Ly.
5. **k = 5** (only reachable by the female formula, or by a male whose d = 6): the number
   5 belongs to no quẻ (it is the centre of the Lo Shu). Convention: **male → Khôn,
   female → Cấn** [1], [2], [3].

The older, equivalent shortcut on the last two digits only — male 10 − r, female 5 + r,
where r is the reduced sum of the last two digits — is given in [1]; it produces the same
answer as the formula above, because d ≡ r + 1 (mod 9) for a 19xx/20xx year. The
post-2000 variant (male 9 − r, female 6 + r) is in [1].

**Worked example (the one in the sources, reproduced to show the method):**

> Husband, born 1990 (Canh Ngọ), after Tết. d = 1+9+9+0 = 19 → 1+9 = 10 → 1+0 = **1**.
> Male: k = 11 − 1 = 10 → over 9, so 10 − 9 = **1** → **cung Khảm** (Thủy, Bắc, Đông tứ mệnh).
> Wife, born 1992 (Nhâm Thân). d = 1+9+9+2 = 21 → 2+1 = **3**. Female: k = 3 + 4 = **7**
> → **cung Đoài** (Kim, Tây, Tây tứ mệnh).

Note the two people land in *different groups* (Đông tứ and Tây tứ) and therefore share
no good direction — the situation [1] uses to show how a family resolves a conflict of
house directions (follow the head of the household). This example is VERIFIED: it
appears in [1] and its two cung values match [19] and the year table in [3].

**A real disagreement in the sources, flagged rather than hidden.** [5] publishes a
year-by-year table (1985–2005) that disagrees with the four sources above. Its method
— reducing the *full* year to a digit root and then subtracting 10 from it for males —
gives 1990 male = Ly, whereas the standard 11 − d gives Khảm. Its female column also
disagrees (1990 female: Càn versus Ly in [3]/[19]). [5] is therefore labelled **CLAIMED /
CONTESTED** and its table is not used here. The four-source agreement (a majority plus a
Chinese-language cross-check) is the basis of §2.2. If the owner is given a table that
disagrees with §2.2, that table is the one that is wrong.

### 2.2 The eight cung, with their four good and four bad directions

Columns are the eight compass directions. **Cung Càn (Trời)** and **cung Cấn (Sơn)** are
two different quẻ and are kept apart here deliberately; Vietnamese sources routinely
collapse them and that is a source of many wrong readings.

| Cung (quẻ) | Hành | Phương vị | Nhóm | **Sinh Khí** | **Thiên Y** | **Diên Niên** | **Phục Vị** | Tuyệt Mệnh | Ngũ Quỷ | Lục Sát | Họa Hại |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Khảm** | Thủy | Bắc | Đông tứ | Đông Nam | Đông | Nam | Bắc | Tây Nam | Đông Bắc | Tây Bắc | Tây |
| **Ly** | Hỏa | Nam | Đông tứ | Đông | Đông Nam | Bắc | Nam | Tây Bắc | Tây | Tây Nam | Đông Bắc |
| **Chấn** | Mộc | Đông | Đông tứ | Nam | Bắc | Đông Nam | Đông | Tây | Tây Bắc | Đông Bắc | Tây Nam |
| **Tốn** | Mộc | Đông Nam | Đông tứ | Bắc | Nam | Đông | Đông Nam | Đông Bắc | Tây Nam | Tây | Tây Bắc |
| **Càn** | Kim | Tây Bắc | Tây tứ | Tây | Đông Bắc | Tây Nam | Tây Bắc | Nam | Đông | Bắc | Đông Nam |
| **Khôn** | Thổ | Tây Nam | Tây tứ | Đông Bắc | Tây | Tây Bắc | Tây Nam | Bắc | Đông Nam | Nam | Đông |
| **Cấn** | Thổ | Đông Bắc | Tây tứ | Tây Nam | Tây Bắc | Tây | Đông Bắc | Đông Nam | Bắc | Đông | Nam |
| **Đoài** | Kim | Tây | Tây tứ | Tây Bắc | Tây Nam | Đông Bắc | Tây | Đông | Nam | Đông Nam | Bắc |

**Note on the ordering of the four good stars.** Most sources rank Sinh Khí best and
Tuyệt Mệnh worst; the middle two or three vary slightly between books — [1] says so
explicitly and advises not to worry about whether Thiên Y or Diên Niên comes second.
[3] tabulates the order as Sinh Khí → Diên Niên → Thiên Y → Phục Vị. Treat the *set* of
four good directions as the reliable datum and the ranking inside it as soft.

**Note on the East/West group split.** Đông tứ mệnh = Khảm, Ly, Chấn, Tốn; their four good
directions are always Bắc, Nam, Đông, Đông Nam. Tây tứ mệnh = Càn, Khôn, Cấn, Đoài; their
four good directions are always Tây, Tây Bắc, Tây Nam, Đông Bắc. **Đông Bắc is the only
direction that is good for the whole Tây group and bad for the whole Đông group** —
not “worst” for Đông (that is Tây for Đông tứ, Tây Nam for Đông tứ…), but a consistent
cross-group difference, and therefore the direction where a mixed-family house has the
most to negotiate. This split is the geometric heart of Bat Trach: the four good
directions of a cung are always the four directions of its own group.

**A useful memory rule, and its limits.** The **Phục Vị** direction of each cung is the
direction of that cung itself (Khảm is North → Phục Vị of Khảm is North; Ly is South →
Phục Vị of Ly is South). [1] states this. It is a check that the table above is read
correctly — but it is a *description* of the table, not an extra rule, and some schools
use it as the primary “safe” direction when they cannot get a bearing at all. That is a
legitimate fallback for this house until the owner takes the compass reading: “sit the
house on the direction of the owner's own cung” is the traditional fallback for a plot
whose bearing is wrong, and it requires no direction-reading at all.

### 2.3 What Bat Trach is used *for* in this house

The traditional uses, in the priority order given by [1] and [3]:

1. **Hướng nhà** — the front door's outward bearing should fall in one of the head of
   household's four good directions. If it does not, the land is fixed, so the family
   works it out *inside*: bed, altar and stove are turned to the owner's good directions.
2. **Hướng bàn thờ** — toạ cát hướng cát: place the altar in a good zone and face it
   toward one of the four good directions of the owner.
3. **Hướng bếp** — toạ hung hướng cát: place the cooking zone in one of the four *bad*
   zones (so the fire “settles” the bad qi) and turn the cook's back toward a good
   direction. Note the *disagreement*: most modern practice defines the “hướng bếp” as
   the direction the cook's **back** faces; older texts define it as the direction of the
   **stove mouth / heat source**. [1] says both readings exist and tells the reader to
   pick one and stay with it.
4. **Hướng đầu giường** — the head of the bed toward a good direction (usually Diên Niên,
   for the marriage) — [3].

---

## 3. Element-by-element review of THIS house

Each finding carries: **ID - Where - Rule - School - Agreement - Severity - Remedy -
Practical rationale - Conflict with safety/design - Evidence label.**

### 3.1 Main door, gate, and the entry sequence

**P-01 - The main door D1 and the gate Dc do not share an axis**

- **Where:** IMG_9972 ground floor: chain reads *san truoc (-0.200, tag Ns, gate Dc) -> noi de xe (+-0.000, tag N1, door D1)*. The garage block is 3940 internal / 4240 on grid, plot 3900 wide at the front with 350 + 3200 + 350 wall zones. IMG_9979 elevation: D1 = 2800 x 2800, four-leaf glazed with transom. The tag list (transcript, Common to all nine sheets) carries Dc (front gate) as a separate tag from D1 (front door).
- **Rule:** the cong (outer gate) and the cua chinh (house door) are read as one qi line. Ideally they share an axis so the qi enters on a single straight line rather than being bent at the gate; where they are offset, the offset is treated as a bend in the incoming qi and, in the stricter reading, as the reason the house needs a screen.
- **School:** general nha ong folk rule (the *cua cong lech pha / cua cong so le* rule). Bat Trach is silent on it.
- **Agreement:** COMMON. The *keep the entry on one axis* rule is the single most widely repeated Vietnamese folk rule about the entry; the *severity* attached to breaking it is not agreed.
- **Severity in the tradition:** MINOR. The folk remedy for a bent entry is a screen, a plant, or a mirror, i.e. a decoration-level fix, and the tradition itself treats a bent entry as a solvable nuisance rather than a defect.
- **Remedy:** a planting strip or a slatted screen along the front yard, on the axis between the gate and the door, so the two are read as one line. Cheap, and it also improves privacy from the street and keeps the garage door from being visible from outside.
- **Practical rationale:** the gate is the street threshold; a screen hides the parked car, cuts the direct line of sight into the garage and living room, and is a genuine privacy improvement in a 3.9 m-wide frontage.
- **Conflict with safety/design:** none - do not place anything that narrows the carriage entry below what the vehicle needs; a screen at the side of the yard, not across the turning path.
- **Evidence:** VERIFIED for the drawing facts (transcript IMG_9972 ground floor chain; IMG_9979 D1 2800x2800). CLAIMED for the rule itself: widely repeated in the folk literature, no single canonical published source located.

**P-02 - The front yard is the house's main qi asset and the drawing already treats it as one**

- **Where:** san truoc is 3500 deep (measurements.md, ground-floor table: y 0-3500), floor tag **Ns** = *nen san, lat gach 30x60 cm, chong truot* (IMG_9972 finishes legend). The front is on the LEFT of every plan (transcript, plan convention) and the street is on that short side.
- **Rule:** the front yard must be open and unobstructed; it is the *thong thuy* - the breathing mouth of the house. Blocking it, walling it, or filling it with structure is among the most commonly cited prohibitions in Vietnamese folk practice, second only to the stove rules.
- **School:** general nha ong folk rule; Bat Trach treats it indirectly (the good direction should be the open, front-facing side).
- **Agreement:** COMMON.
- **Severity in the tradition:** MODERATE. A closed front yard is treated as a real impairment, but it is remediable at any time by clearing it.
- **Remedy:** keep the front yard open - no carport, no storage box, no solid gate screen across the full width. Low planting to the sides is fine.
- **Practical rationale:** this one is not merely symbolic. The front yard is the only place on the plot where cross-ventilation can enter the ground floor, and it is the buffer between a garage door and a footpath. Filling it costs both.
- **Conflict with safety/design:** none.
- **Evidence:** VERIFIED (measurements.md ground-floor table; IMG_9972 legend Ns).

**P-03 - Door D1 versus the stair: not actually aligned - and the fix belongs at the stair**

- **Where:** IMG_9972 chain: *noi de xe -> P. khach (3800/4000) -> thang*. D1 (2800 wide) sits in the front wall of the garage; the stair is 3800-4000 mm further back, in the core. The house is 25 000 long, so the door and the stair are **not** on one straight line - the entrance axis runs into the living room and is then turned sideways into the core. The rear door D2 is in the rear wall of the rear WC band.
- **Rule:** *cua chinh doi dien cau thang* (main door facing the stair) is a **dai ky** in Vietnamese practice. The stair is where qi gathers and is then driven straight up the shaft, so a door on the same axis is treated as a pump that pulls the incoming qi straight up the stairwell and out through the roof rather than distributing it into the rooms. The same logic makes a door in line with a rear door a **thong tam (xuyen tam)** - piercing the heart - because the qi enters at one end and leaves at the other without dwelling.
- **School:** general nha ong folk rule; Phi Tinh and Bat Trach do not state it.
- **Agreement:** COMMON as a rule; CONTESTED in severity - some practitioners treat a door-stair clash as a first-order defect and others as a curiosity for a house whose plot is already fixed.
- **Severity in the tradition:** MODERATE.
- **Remedy:** none is needed at the door - the geometry does not put the door and the stair on one axis. The cheap and recommended move is at the **stair**: close the stair's visual and qi link to the entry axis with a screen, a run of planting, or a solid balustrade panel at the core entry on the ground floor (see P-06).
- **Practical rationale:** the real problem in a 3.9 m-wide house is not metaphysics but draught and acoustic carry from the stair lobby into the living room. Screening the core solves both, and is exactly what the tradition asks for.
- **Conflict with safety/design:** the stair is the **only** escape stair in a 5-storey house (transcript IMG_9972, Five things for a safety or design reviewer, item 5) and the core band also carries the light wells. Any screen must not obstruct the stair discharge, the 8 mm tempered-glass balustrade, or the emergency-egress width. Screen the *lobby*, not the stair.
- **Evidence:** VERIFIED for the geometry (IMG_9972 chain and dims; measurements.md ground-floor table); the door-stair rule is CLAIMED but very widely repeated ([9], [12]).

**P-04 - The rear door D2 and the main door D1 are not on one axis - keep it that way**

- **Where:** D2 is the rear door of the rear WC band, per IMG_9972 (*WC (tags W1, Sb1, Dw, door D2 rear) -> san sau*). The front D1 is in the front wall of the garage. The WC band is 1600 deep (measurements.md), the garage 4000, the living room 4800 - the two doors are separated by 4800 + 4000 + 1600 = 10 400 mm of built depth, with the whole living room and the core band between them.
- **Rule:** *cua doi cua / xuyen tam* is a **dai ky** - the qi must not pass straight through. The remedy, when the geometry cannot change, is a screen or a plant at one of the two ends so the line is broken.
- **School:** general nha ong folk rule.
- **Agreement:** COMMON as a rule; CONTESTED as to whether it matters when the two doors are far apart. [22] argues explicitly that a *xuyen tam* only bites when the qi path is unobstructed end to end, and is harmless once anything interrupts it.
- **Severity in the tradition:** MINOR here, because the separation is large and several rooms and the whole core sit between the two doors.
- **Remedy:** none required. If the owner wants belt-and-braces, a low planting strip or a freestanding screen in the rear yard closes the sightline from D2 into the house - which also improves the rear privacy of a house whose rear yard backs onto a service alley.
- **Practical rationale:** a straight rear-yard sightline into the house is a privacy problem as well as a phong thuy one; screening the rear yard is worth doing on its own merits.
- **Conflict with safety/design:** none. Do not block the rear door's ventilation or its use as a service route.
- **Evidence:** VERIFIED for the geometry (IMG_9972 room chain; measurements.md); CLAIMED for the rule ([22] for the qualified form, [6] and [9] for the strict form).

### 3.2 The stair

**P-05 - 21 risers per storey: the Sinh-Lao-Benh-Tu cycle lands on Sinh for every flight**

- **Where:** stair treads numbered 1 to 21 on **every** plan (IMG_9972, IMG_9973, and the same on floors 2-5). The structural stair sheets give the risers precisely: IMG_0003 (tret) bottom +0.050 to top +3.750, rise **3700**, riser **176.2**, 3700 / 176.2 = 21.0; IMG_0004 (lung) +3.750 to +6.950, rise **3200**, riser **152.4**, 3200 / 152.4 = 21.0; IMG_0005 (tang 1, 2, 3) rise **3400**, riser **162**, 3400 / 162 = 21.0. Tread depth **250** on all three sheets. So: 21 risers per storey, five flights, 105 risers from the ground floor to the top floor.
- **Rule:** the classical rule is that the stair should end on **Sinh**, the first step of the Sinh-Lao-Benh-Tu four-cycle; counting from step 1 = Sinh, step 2 = Lao, step 3 = Benh, step 4 = Tu, step 5 = Sinh again. **21 mod 4 = 1, so the last step of every flight falls on Sinh.** This is why 21 is one of the most-cited good stair counts: [9] gives 17, 18, 21, 22; [11] gives 17, 19, 21, 23, 25 (odd, i.e. 4n+1); [12] gives 21 = 4 x 5 + 1 explicitly.
- **School:** general nha ong folk rule / Sinh-Lao-Benh-Tu cycle; also expressible in the Truong sinh (12-star) cycle, see P-06.
- **Agreement:** UNIVERSAL as a rule; the *form* of the count is CONTESTED - the 4n+1 version, the 12-star Truong sinh version, and the *house's own element* version are three versions in the sources, all in use.
- **Severity in the tradition:** MODERATE - but **in this house the condition is already satisfied**, so the finding is informational.
- **Remedy:** none needed for the count. Keep the treads unmodified; the numbering on the drawings should not be changed on site.
- **Practical rationale:** 21 risers with a 250 mm tread is a comfortable, generous proportion for a house with an older owner and small children, and it is below the *no more than 18 risers per flight* limit stated in [12]. The numbers and the tradition agree here.
- **Conflict with safety/design:** **none - but see P-06 and the safety review**: the three different risers (176.2 / 152.4 / 162) across the same stair are a consistency issue that belongs to the safety reviewer, not to this one.
- **Evidence:** VERIFIED (transcript-foundation-stairs.md, IMG_0003/0004/0005, with the transcript marking the riser arithmetic as its own arithmetic check; IMG_9972 tread numbers). VERIFIED for the rule ([9], [11], [12]).

**P-06 - The stair is in the middle of the house's length - the tradition's worst position, and here it is unavoidable**

- **Where:** the core band (stair + lift) sits at y = 12 300-16 300 in a 25 000 mm plot, i.e. **the middle 40 % of the depth** (measurements.md ground-floor table; the same band is byte-identical on all seven levels). The stair occupies the front-to-middle of the band, the lift the rear of it. The stair is the **only** stair in the building.
- **Rule:** *khong lam cau thang o giua nha* is the most emphatic single prohibition in the Vietnamese stair literature. The reason given in [12] is a Ngu hanh one: the stair is Moc, the centre of the house is Tho, and Moc khac Tho - the stair divides the house in two and sucks the energy out of the centre. [9] and [11] give the same rule and add: not in line with the main door; not at the rear of the house; not a spiral stair; not with open risers; not with a WC under it.
- **School:** general nha ong folk rule; Bat Trach does not address the stair.
- **Agreement:** UNIVERSAL as a rule - it is the one stair rule on which every source agrees. CONTESTED in its *cause*: some texts explain it energetically (Moc khac Tho, qi concentrated at the centre), others structurally (a mid-house stair splits the plan and forces circulation past it).
- **Severity in the tradition:** MAJOR. This is the tradition's biggest stair prohibition and this house commits it in the most literal way possible.
- **Remedy:** the position cannot be changed (it is set by the structure, the lift and the plot). What the tradition's own logic offers instead is **mitigation of the centre**: (a) keep the under-stair space **open and clear** - [9] says explicitly *khong gian duoi gam cau thang phai trong* and suggests a small rockery and a fish tank; (b) place a plant, a screen or a low light feature at the foot of the stair to soften the corner; (c) light the stair well warmly. Under-stair **storage** is the specific thing to avoid: a closed cupboard under the stair becomes the dense, dark, stagnant volume the rule is aimed at.
- **Practical rationale:** this is the strongest practical case in the whole report. The under-stair space in this house is a 3200 x 4000 mm volume with a 1250 mm flight hanging over it, reached through the core, in the middle of a five-storey plan. Turning it into an open, lit, visually interesting niche (planter, bench, washing area) instead of a cupboard is better for dust, for light, and for the feeling of the core. The tradition and the architecture agree for once.
- **Conflict with safety/design:** **the safety answer wins over the phong thuy answer here, in one respect.** Under-stair storage is attractive for exactly the reason the tradition dislikes it (a 3200 x 4000 void is the largest unsecured store in the house). If the owner wants the space, it must be a **locked, ventilated, fire-rated cupboard** or an open planter - not a walk-in store under a flight. The stair is the sole escape route for five storeys; nothing stored under it may impede egress, and the stair's fire-resistance and smoke behaviour must not be compromised by fixing (c) inside it.
- **Evidence:** VERIFIED for the position (measurements.md; JSON `stairwell` rect y=12 300 d=4 000; the core band is identical on all levels). VERIFIED for the rule ([9], [11], [12]).

**P-07 - The stair is a U-return with winders, not a spiral; that part is fine**

- **Where:** IMG_9972: *stair (U-shape with winder; 3000 wide as 1250+500+1250 (arithmetic check), 3200 between wall lines)*. IMG_0003: *U-shaped stair with a winder turn at the B-side end*. Flight widths: 1250 on the ground and mezzanine, **1350** on floors 2-4 (transcript IMG_9972, inconsistency note; IMG_0005 shows the upper stair at 1350 + 500 + 1350).
- **Rule:** the prohibitions are on **cau thang xoan oc** (spiral - the qi is said to wind around and shoot straight up) and on **cau thang bac ho** (open-riser - the stair is supposed to contain and lead qi, so an open-riser stair leaks it). A straight U-return with winders is neither. [12] lists both spiral and open-riser as ky.
- **School:** general nha ong folk rule.
- **Agreement:** COMMON (widely repeated in [9], [11], [12]).
- **Severity in the tradition:** MINOR (not applicable to this stair). This is a *checked and clear* finding, recorded so the owner is not told to change it.
- **Remedy:** none. Do **not** convert the U-return to a spiral to satisfy the rule - the rule exists to avoid spirals, and a spiral would be worse for the actual users.
- **Practical rationale:** the winders are a real ergonomic limitation for a 5-storey house - winders are narrow, turn sharply, and are the part of the stair most likely to cause a fall. That belongs to the safety review; from the phong thuy side there is nothing to change.
- **Conflict with safety/design:** n/a, but the winder geometry and the 1250/1350 width mismatch are flagged here only as a pointer to the safety review, not as a phong thuy finding.
- **Evidence:** VERIFIED (IMG_9972, IMG_0003, IMG_0005; transcript-foundation-stairs.md). VERIFIED for the rule ([12]).

**P-08 - The stair ends at a door: the top flight lands on the terrace lobby**

- **Where:** the stair continues to the top floor (IMG_9977: stair with 21 treads at the 5th-floor/terrace level; JSON `stairwell` present on the Roof Terrace storey with `direction: down`), discharging into a lobby with doors D6 (front terrace) and D7 (rear terrace) - transcript IMG_9977: *a stair/lift lobby (5200 long, 3200 + 1800 + 200) with floor tag SL5 and doors D6 (to the front terrace) and D7 (to the rear terrace)*.
- **Rule:** *cau thang cuoi cung dat doi dien cua* - the top of the stair landing directly on a door is treated as a fault of the same family as the door-stair clash: the qi arriving up the stair is driven straight out through the door instead of gathering. The related rule is that the stair should not end at a door but at a wall or an open space, so the arriving qi disperses.
- **School:** general nha ong folk rule.
- **Agreement:** COMMON as a stated rule; CONTESTED in severity - a door *beside* the stair head is much milder than a door *on* the axis of it, and this lobby has two doors either side of the landing rather than one dead ahead.
- **Severity in the tradition:** MINOR to MODERATE.
- **Remedy:** free - keep the landing clear of obstruction and place a plant or a low screen offset from the door axis so the straight line from the stair foot to the door is broken. No structural change.
- **Practical rationale:** on a roof terrace in HCMC the top landing is also a hot, exposed, unroofed place. A planter there does the phong thuy work (break the line) and the practical work (shade, soften the concrete, screen the lift head) at the same time.
- **Conflict with safety/design:** none - but note the roof terrace has **no parapet or balustrade note printed on sheet 9977** (transcript, ambiguity note) and the stair light well there is a **glass floor panel** whose load rating is not stated (same note). Anything added at the top of the stair must be ballast-safe and must not be mistaken for a guard. That is the safety review's point; the phong thuy point is only *don't block the landing*.
- **Evidence:** VERIFIED for the geometry (IMG_9977; JSON Roof Terrace storey `stairwell` + `direction: down`); CLAIMED for the rule (repeated across the folk literature, no single canonical source located).

**P-09 - No stair is over the altar, and no altar is over the stair: a clean pass**

- **Where:** the altar room P. THO is on the **5th floor at the FRONT** (y 4900-8900, 3960 x 4000 - measurements.md, *Tang 5*; JSON `tho_f5` x=0 y=4900 w=3960 d=4000), while the stair core is at y 12 300-16 300. They are 3400 mm apart in plan and 10 400 mm apart in level. There is no stair above or below the altar room on any storey.
- **Rule:** *ban tho khong dat duoi gam cau thang* and *khong dat ban tho tren cau thang* - the altar must not sit under a stair, and the stair must not run over it; the under-stair space is the darkest, most compressed, most stagnant volume in the house and is treated as unsuitable for worship. [9] and [12] both state the under-stair case.
- **School:** general nha ong folk rule / phong tho practice.
- **Agreement:** COMMON, and near-universal in practice - no source located that permits an altar under a stair.
- **Severity in the tradition:** MAJOR if broken.
- **Remedy:** none - the condition is already satisfied.
- **Practical rationale:** a stair overhead is loud, dark and hot; it is a poor place to pray regardless of doctrine.
- **Conflict with safety/design:** none.
- **Evidence:** VERIFIED (JSON `tho_f5` rect vs `stairwell` rect, all storeys).

### 3.3 The lift shaft and the vertical voids

**P-10 - A shaft punched through all five floors: *thung khi* - CONTESTED, and the safety answer overrides the tradition**

- **Where:** a lift shaft occupies the core on every storey. The transcript for IMG_9972 reads the shaft with an X, 1800 x 1600; the roof sheet (IMG_9978) carries an **O ky thuat thang may** (lift technical overrun) 2000 wide above the roof. **Important caveat:** `designs/contractor-as-drawn.fidelity.md` (c) records that **no residential floor plan labels a shaft** - the label appears once, on the roof sheet - and that the shaft's existence below roof level is an **inference**, to be confirmed with the contractor. The pit detail (IMG_9987) gives a 1600-wide clear pit, 1600 deep, with four corner piles.
- **Rule:** some schools treat a hole running the full height of the house as a **thung khi / thung long** - a chimney that carries qi straight out of the roof without ever circulating in the rooms. Others read a well-sited shaft as a *vertical ventilation spine*, especially in a 3.9 m-wide tube house where the whole depth is otherwise a single air tunnel.
- **School:** Phi Tinh / general nha ong folk rule. CONTESTED, and the disagreement is explicit in the sources: [12] treats the stair (a vertical void) as *the* qi-gathering element of a house while also forbidding it in the middle; the leak reading is the minority one.
- **Agreement:** CONTESTED.
- **Severity in the tradition:** MODERATE at most, and only under the minority reading.
- **Remedy:** if the owner wants the minority reading addressed, the traditional remedy is a **screen or a light-coloured, close-fitting door at each shaft opening** so the shaft is not a visually open hole from floor to floor - a lift door with a full-height screen behind it, or a dark screen on the shaft side. Cheap and non-structural.
- **Practical rationale:** this is a genuine and cheap improvement, but for a mundane reason: a lift shaft running five storeys is a **smoke and sound path** between floors. A tight shaft door and a shaft-side screen reduce both, and the screen also stops the shaft becoming a black hole in an otherwise narrow corridor.
- **Conflict with safety/design: safety wins.** Nothing may be added that reduces the lift shaft's clear dimensions, obstructs the lift car or its pit, or interferes with the **hoist-hook beam** (IMG_9988: a single 25 mm hook bar in a 120 mm slab with no stated rated load). Fire separation of the shaft is a structural and fire matter and any shaft-sealing work belongs to the engineer, not to a feng shui screen.
- **Evidence:** PARTIAL. The shaft's presence and size per the transcripts (IMG_9972, IMG_9978, IMG_9987, IMG_9988), but its **existence below the roof is an inference** per fidelity.md (c). CONTESTED / CLAIMED for the rule.

**P-11 - The light wells (o lay sang) are a genuine asset**

- **Where:** IMG_9974/9975/9976: an **O lay sang** (light well) 1600 wide sits next to the front bedroom's WC on floors 2, 3 and 4; on floor 5 it is 2100 long. On the roof (IMG_9978) two light wells are noted, one over the stair and one beside the lift shaft (sizes 1200 and 1300/1500, PARTIAL). The 5th-floor sheet (IMG_9977) carries **O lay sang gon kinh cuong luc, co khung inox bao ve** (light well in tempered glass with a protective stainless frame) - 2000 long x 1500 wide, over the stair. `fidelity.md` (b) records that the roof's glazed light-well cap sits **over the stair**, and that the model punches a void over the stairwell's own footprint instead of reproducing the narrower glazed insert.
- **Rule:** an intentional skylight or light well is a **thien tinh** - a heaven-window. The rule that is *not* in dispute is the practical one: a light well must bring light **and** air. A glazed, sealed light well is a light source; an unglazed one is also a ventilation shaft, which is what makes it useful in a house this narrow. The tradition's usual caveat is that a hole must not become a straight path for bad qi to enter, and that any well opening at the top must be protected - the *bao ve* framing the drawing already calls for.
- **School:** general nha ong folk rule + Phi Tinh (a well is read by its relationship to the star chart, not by a rule in itself).
- **Agreement:** COMMON for the practical part (light + air), CONTESTED for the symbolic reading.
- **Severity in the tradition:** MINOR - this is a positive feature, not a defect.
- **Remedy:** keep the light wells unglazed or openable where the drawings allow, so they ventilate; keep the stair light well's stainless protective frame intact; do not enclose the rear light well in a cupboard.
- **Practical rationale:** this is where the phong thuy advice and the building physics are most obviously the same advice. In a 3.9 x 25 m tube house with a single stair and a party wall on each side, the only way to get air to the rear bedroom is a vertical path. The light wells beside the stair are the reason the rear of the house is habitable at all.
- **Conflict with safety/design:** the stair's glass light well on the terrace has **no stated load rating and no fall protection** (IMG_9977 ambiguity note) - that is a safety-review item and it overrides any phong thuy preference for more glass.
- **Evidence:** VERIFIED (IMG_9973, 9974, 9977, 9978 notes; fidelity.md (b) for the over-the-stair reading).

**P-12 - The mezzanine double-height void (troi gieng) at the front**

- **Where:** the mezzanine (L1, +3.800) is void over the **front** - the front yard void (3900 wide) and an interior front void (2800 wide, tag K1 on the glass wall) - IMG_9973: *Front yard and the whole front interior (about 8140 long...) are marked Thong tang*. The only built part of L1 is the core and **P. Sinh hoat** at the rear (4400/1800 deep), plus a WC. The section IMG_9980 confirms the front double-height void with the K1 glass wall (1700 high, 600 + 600).
- **Rule:** a double-height void is traditionally read as a **troi gieng** - a shaft of space. Where the tradition and the drawing agree is on the *light* side: an open double-height slot is the best light source a deep plan can have. Where they differ: the tradition is markedly more comfortable with an open void in the **middle** of the plan than with a closed one, and the house has one at the front - but it is a **void at the front, above the entrance**, which is a different animal from the mid-house void the tradition warns about (P-06).
- **School:** general nha ong folk rule; Phi Tinh reads the void as an opening in the *star chart* of the floor.
- **Agreement:** COMMON that light wells and voids are favourable for daylight; CONTESTED on the symbolic weight.
- **Severity in the tradition:** MINOR - favourable, with one caution.
- **Remedy:** **none structural.** The one caution worth taking: a double-height void at the front of a house means the living room below is open to the front balcony and the garage door, so **the front-room privacy and the garage's heat and noise** need managing - a ceiling-level curtain or a slatted screen under the K1 glass wall is cheap and does the practical work.
- **Practical rationale:** the void is a light well for the ground floor and the mezzanine; keeping it visually open is the whole point. What the void does *not* do is separate the garage from the living room acoustically, and the drawing shows the garage and the living room sharing a 900 mm door only.
- **Conflict with safety/design:** the mezzanine slab edge facing the front void has **no guard-rail note** (IMG_9973 ambiguity note) - the section shows a short vertical element there, about 1100 high, PARTIAL. That is a safety-review item; the phong thuy point is only that the void itself should stay open.
- **Evidence:** VERIFIED (IMG_9973, IMG_9980; measurements.md mezzanine table).


### 3.4 Kitchen (bep)

**P-13 - The kitchen is at the REAR of the ground floor, and the tradition's own rule for rear kitchens is the weak one**

- **Where:** P. An + BEP is the rear-most built band on the ground floor. The two readings disagree on the order of the last two bands (see section 0): the transcript reads **kitchen then WC** front-to-rear; `measurements.md` rev.2 and the JSON read **WC then kitchen** (WC y 18100-19700, kitchen y 19700-23800). Both agree the kitchen band is 4100 deep and sits between the core and the rear yard, at the rear end of a 25 m plot.
- **Rule:** the kitchen is a **Hoa** element and is traditionally placed in a **hung** (bad) zone of the owner's cung, facing a **cat** (good) direction - the fire settles the bad qi [1], [3]. It is also traditionally kept out of the **centre** of the house and away from the main door (tai loc *thoat ra* - the wealth escapes out the front door) [1], [23].
- **School:** Bat Trach (position by cung) + general folk rule (not at the centre, not facing the main door).
- **Agreement:** UNIVERSAL on *not in the centre and not facing the main door*; CONTESTED on the toa-hung-huong-cat principle itself, which several modern sources treat as optional and some reject outright.
- **Severity in the tradition:** MODERATE.
- **Remedy:** the position is fixed. The cheap, widely-agreed fixes are: (a) **a solid backsplash / partition and a closed kitchen door** so the fire and the cooking smell are contained; [23] and [24] both recommend a curtain, a screen or a tall cabinet between the cooking zone and the door, precisely to break the direct line from the front door; (b) **a hood and good extraction** - the rear kitchen's only opening is a rear window, so the hood is doing real work; (c) keep the stove off the party wall where possible, because a party wall is where cooking odour and heat reach the neighbours.
- **Practical rationale:** the strongest argument for a closed kitchen in this house is not phong thuy at all. The plan puts the dining/kitchen at the **rear**, the front yard and the garage at the front, and the whole 25 m depth is a single air tube. A cooking smell that escapes at the rear travels the entire length of the house. A kitchen door is an acoustic and odour control measure.
- **Conflict with safety/design:** the kitchen is immediately **below the rear bedroom** (P. NGU at y 19700-23800 on floors 2-5 sits directly over the kitchen band) and **below the rear WC band** - see P-15, which is the more serious of the two overlaps. A kitchen door must not be confused with a fire-rated separation.
- **Evidence:** PARTIAL. The drawing facts (rear band, 4100 deep) are VERIFIED; the *order* of the WC and kitchen bands is CONTESTED between the two reads and is stated conditionally. VERIFIED for the rule ([1], [3], [23], [24]).

**P-14 - Stove versus sink, and stove versus WC**

- **Where:** IMG_9972 records *sink, hob and fridge drawn* in the P. An + BEP band. The **positions of the sink, the hob and the fridge relative to each other are not dimensioned in the transcript** - only their presence is recorded. There is no separate kitchen detail sheet in the photographed set.
- **Rule:** the standard kitchen rules are (a) **stove and sink should not be adjacent** - Hoa vs Thuy, they khac each other; where a small kitchen forces them together, the traditional remedy is a solid work surface or a cabinet between them [24], [25]; (b) the stove should not sit directly under a window (the draught blows the flame out, and the practice reads the window as a competing *mouth*) [25]; (c) the stove should not be against the kitchen's back door or immediately in front of the stair [23].
- **School:** general nha ong folk rule (Ngu hanh Hoa-Thuy); Bat Trach addresses the kitchen's *zone and facing*, not the internal layout.
- **Agreement:** COMMON.
- **Severity in the tradition:** MODERATE.
- **Remedy:** decide the kitchen layout at the joinery stage, before the units are cut: keep **at least one full worktop cabinet or a 600 mm tall upstand between the hob and the sink**, and keep the hob off the rear window. Both are free at this stage and cost nothing later.
- **Practical rationale:** a 600 mm gap between a gas hob and a sink is also what stops water from the sink getting into the hob, and it is where you put the drying rack. The window-draught point is genuine for a gas flame. The tradition is, unusually, giving good kitchen advice here.
- **Conflict with safety/design:** the gas or electric connection and the extraction duct are engineer's items. If the hob is electric induction, the *fire* element of the rule effectively disappears - several practitioners now treat an induction hob as not carrying the Hoa problem at all, which is a further reason to treat the rule as optional rather than load-bearing.
- **Evidence:** PARTIAL. The presence of sink, hob and fridge is VERIFIED (IMG_9972); their relative positions are **NOT FOUND** in the transcript. VERIFIED for the rule ([24], [25]).

**P-15 - A WC band and a kitchen band sit directly under the rear bedroom on floors 2-5 - the tradition's most serious overlap, and the drawing already confirms it**

- **Where:** the rear band is identical on **every** storey: at y 18100-19700 a WC, at y 19700-23800 the rear bedroom (P. NGU, 4100 deep) on floors 2, 3, 4 and 5. On the ground floor the same two y-bands hold the ground WC and the kitchen. So:
  - **the rear WC on each floor is directly above the ground-floor WC and directly below the rear bedroom above it** - i.e. a WC stack runs from the ground floor through floors 2, 3, 4 and 5, with a bedroom sitting on top of the topmost WC;
  - **the rear bedroom on each floor sits directly above the kitchen** (ground) or above the rear bedroom below it.
  Verified from `measurements.md` (ground, tang 2-4 and tang 5 tables) and from the JSON room rects, which are identical y-ranges on every storey.
- **Rule:** *nha ve sinh khong dat tren dau phong ngu* - a WC above a bedroom is one of the strongest and most consistently repeated prohibitions in Vietnamese folk practice. The stated reason is that the WC is the room where **ue khi** (impure qi) collects and is then pushed up into the room above by the stack effect; the bedroom above is then read as the room most harmed by it, because sleep is when the occupant is least able to resist it. *Nha ve sinh o cuoi nha* is also the least-favoured position, because the rear of the house is where the qi is weakest and where the house's exit is.
- **School:** general nha ong folk rule; Bat Trach addresses the WC's *zone and facing*, not the storey above it.
- **Agreement:** COMMON as a rule; the *severity* is CONTESTED - it is the most-cited prohibition, but its place in the hierarchy of *dai ky* varies between sources.
- **Severity in the tradition:** MAJOR. This is the tradition's sharpest finding against this particular house, and it is structural.
- **Remedy:** **no non-structural remedy is fully adequate, and the honest answer is that the owner cannot fix this cheaply.** The cheap mitigations that *do* help are: (a) **ventilation and odour control**: an exhaust fan ducted to the outside (not to the shaft), a floor drain, and a WC that is used with the door closed - [23] specifically advises keeping the WC door shut and the fan running; (b) **a ceiling void**: a 300-450 mm service plenum between the WC slab and the bedroom floor, so the two are not in direct acoustic and air contact - this is the one remedy that is close to free if it is decided *now*, before the slab is poured, and it is the single highest-value phong thuy-driven decision still open on this project; (c) **sealing**: a closable, sound-isolating WC door with an acoustic seal; (d) keep the **bed away from the WC wall** (see P-18) so the head of the sleeper is as far from the stack as the room allows.
- **Practical rationale:** this is the finding where the tradition is most obviously pointing at something real, and it is *also* a straightforward building-science problem. A five-storey stack of WCs directly under the bedrooms is exactly where stack-effect odour, sound transmission and (in a 100 mm slab) odour transmission through the slab occur. Remedy (a) is ordinary good practice; remedy (b) is ordinary good practice that happens to also be what the tradition asks for.
- **Conflict with safety/design: the safety answer wins on the ventilation detail.** The fan must be ducted **outside**, not into the light well and **not** into the lift shaft or the roof void. Ducting into the stair light well would push bathroom air into the stair, which is the main escape route - and this is exactly the kind of phong thuy adjacency (the light well as a pleasant feature) that must not override the fire strategy. The safety review owns this; the phong thuy layer only notes that the stacking is undesirable in the tradition's terms too.
- **Evidence:** VERIFIED (measurements.md per-floor tables; JSON room rects; IMG_9974, IMG_9975, IMG_9976, IMG_9977 rear chains). VERIFIED for the rule ([23], [25], [26]).

### 3.5 WC (nha ve sinh)

**P-16 - The WCs are in the core and at the rear, and they are not at the front**

- **Where:** every WC on the drawing is in the **middle-to-rear** third of the plan: ground WC at y 18100-19700 (rear band); the floor 2-4 front ensuite at y 8900-10500 (mid-plan, 1600 deep) and the rear WC at y 18100-19700; the floor 5 front WC under the light well. There is **no WC at the front** of the house and **no WC under the stair** (the under-stair volume is unbuilt on every storey).
- **Rule:** the two most-cited WC prohibitions are *WC o cuoi nha* and *WC o dau nha* - a WC at the front is said to let the house's incoming qi enter a dirty room first; a WC at the rear is said to sit where the house's qi has already spent itself, and is the position that makes *thong tam* from the main door to the rear door a real problem. *Nha ve sinh duoi gam cau thang* is the third [12].
- **School:** general nha ong folk rule.
- **Agreement:** COMMON.
- **Severity in the tradition:** MODERATE for the rear position, MAJOR for a front WC or a WC under the stair - neither of which occurs here.
- **Remedy:** the front-WC prohibition and the under-stair prohibition are both already satisfied - worth stating, because it is the part of the drawing a designer working from the folk rules would get right. For the rear WC, the mitigations in P-15 apply (vent out, close the door, acoustic seal, keep the bed off that wall).
- **Practical rationale:** keeping the WC out of the front third is also a hygiene and entertaining point: no guest ever walks past the WC to reach the living room in this house, because the WC is behind the core and the front is yard, garage, living room. That is a genuinely good plan decision that the folk rule happens to also endorse.
- **Conflict with safety/design:** the fire-safety point in P-15 (fan ducting, shaft separation) governs over any phong thuy reading of the WC's position.
- **Evidence:** VERIFIED (measurements.md per-floor tables; IMG_9972, 9974-9977). VERIFIED for the rule ([12], [23], [25]).

**P-17 - WC doors facing the beds and the stair**

- **Where:** the front ensuite on floors 2-4 opens from the hall (y 10500-12300) into the WC at y 8900-10500, i.e. the WC door faces down the corridor toward the front bedroom zone. On the rear side, the door between `wc_sau` and `ngu_sau` (JSON openings: `door ['wc_sau_f2','ngu_sau_f2'] 900`) means **the WC door opens directly into the rear bedroom** on every floor. The ground-floor rear WC is entered from the kitchen/dining band (`door ['wc_gf','bep_an'] 900`), and its rear door D2 opens to the rear yard.
- **Rule:** *cua nha ve sinh doi dien giuong ngu* - a WC door opening straight onto a bed is a **dai ky**; the two things share a line of sight and the rule says the impurity is carried directly at the sleeper. The related rule is that the WC door should not open directly onto the stair.
- **School:** general nha ong folk rule.
- **Agreement:** COMMON.
- **Severity in the tradition:** MODERATE.
- **Remedy:** **the cheapest and most effective fix in the whole report.** The rear bedroom and the rear WC are side by side, sharing a wall, and the door between them is a plain 900 mm leaf. If the WC is entered through the **hall** instead - i.e. the door between `wc_sau` and `ngu_sau` is replaced by a short offset or a 90-degree return so the WC door and the bed are **not** in line - the rule is satisfied. Options, in rising cost: (a) **keep the WC door closed and provide ventilation** - free, and a genuine improvement in a house where the WC is beside the master bedroom; (b) **change the swing** of the WC door so it opens against the wall rather than into the line of the bed - free if the door is not yet hung; (c) build a small **privacy return / dog-leg** in the opening - a modest masonry operation; (d) use a **sliding or pocket door** - [27] names this specifically as the standard remedy for a door facing a bed or another door.
- **Practical rationale:** the door-as-sightline argument is also a privacy argument, and in this plan the WC door is the only route between the ensuite and the bedroom it serves, so **it is also the en-suite**. A bedroom with an open WC door has no privacy at all. Making the door not line up with the bed improves both, at essentially no cost, and it is a decision that has to be taken **before the doors are ordered**.
- **Conflict with safety/design:** any alteration is a change to the WC's ventilation and to the bedroom's escape provision - a bedroom door that is the only door to its WC must remain usable as the bedroom's escape route. A sliding or pocket door is the safest variant here because it does not reduce the opening width.
- **Evidence:** VERIFIED for the adjacency and the direct door (JSON `openings` on floors 2-5: `door ['wc_sau_f*','ngu_sau_f*'] 900`; measurements.md tang 2-4 table). The *exact swing* is not recorded in the transcript - PARTIAL. VERIFIED for the rule ([27], [23]).

### 3.6 Bedrooms

**P-18 - Bed position relative to the door and to the party wall**

- **Where:** each bedroom is entered by a single door from the corridor, with the balcony door on the front bedroom and a window on the rear bedroom. The rear bedroom (P. NGU, 3960 wide x 4100 deep) has its only window on the **rear** wall (JSON `window ['ngu_sau_f*','exterior'] 1500`) and its door on the **WC** wall.
- **Rule:** the bed's head should be against a solid wall, and the bed should not be placed directly in line with the door (the *door sees the bed* arrangement), nor directly opposite a mirror, nor under a beam [28], [29].
- **School:** general nha ong folk rule; Bat Trach adds the *direction* of the bed head (a good direction of the owner's cung, usually Dien Nien).
- **Agreement:** COMMON as a rule.
- **Severity in the tradition:** MODERATE for the position; MINOR for the direction (the direction is a furniture move, and it is the one phong thuy rule that is genuinely free to comply with - see the summary).
- **Remedy:** free and fully within the owner's control - **the bed is furniture, and it can be re-oriented after handover without touching the building.** The one constraint the drawing imposes is that the rear bedroom has a single window at the rear wall, so the bed head must go on one of the **side** walls (the party wall or the WC wall). The tradition prefers the **solid** wall, so the head goes on the **party wall** (away from the WC), not on the WC wall; the tradition also prefers the head away from the door's sightline. Keep the mirror on the wall *beside* the bed, never opposite the head.
- **Practical rationale:** the practical case here is unusually strong. In a 3.96 m wide room with a door on one side and a window at the opposite end, the only arrangement that works is the bed along a side wall - and the side-wall choice decides whether the sleeper's head is against the party wall (solid, silent, best) or against the WC wall (noise, odour, P-15). The tradition and the acoustics agree: **head on the party wall**.
- **Conflict with safety/design:** the head must not be against a wall carrying a service riser or the kitchen flue - check before finalising. Keeping the bed away from the WC wall is also the phong thuy remedy for P-15 in the one place where it can be applied at zero cost.
- **Evidence:** VERIFIED for the plan (JSON room rects and openings for `ngu_sau_f2..f5`; measurements.md). The *bed's* actual position is not drawn - the bedroom layout is not in the photographed set. VERIFIED for the rule ([28], [29]).

**P-19 - Beams over the beds**

- **Where:** the structural sheets put a dense beam grid in the floor slabs: **DS5** transverse beams at the ends of the 1800 bay, **DS6** at every axis, **DS3** across the 3200 bay (the stair bay), and - most relevant here - the generic note on every floor sheet: **CHO NAY CO TUONG MA KHONG CO BO TRI DAM THI TA DAT THEM 2O16 HOAC 3O16 TAI VI TRI DO** (where a wall sits with no beam laid out, add 2O16 or 3O16 there), and **SAN BTCT** slabs 100 mm thick throughout (`transcript-beams-slabs.md`, IMG_9992/9993/9996). Beam depths are 500-700 mm for the grade beams (DK4/DK5 500, DG 300x700) and 100 mm-wide edge beams (DS7/DS6a) appear at the balcony end bay on every floor.
- **Rule:** a beam (xa ngang / dam) crossing directly over the head of a bed is called **huyen tram sat** - the beam presses on the sleeper - and is one of the most frequently-cited bedroom prohibitions [30], [31]. The related prohibitions are a bed under the stair, a mirror facing the bed, and a bed with its head at the foot of the bed.
- **School:** general nha ong folk rule; Phi Tinh treats the beam grid as the *star chart* of the floor, which is why an under-beam position is the traditional one to avoid - the logic of the two systems agrees here, which is unusual.
- **Agreement:** COMMON.
- **Severity in the tradition:** MODERATE.
- **Remedy:** **free and complete** - the beam positions are fixed by the structure, but the **bed is not**. The remedy is to place the bed so that no beam crosses over the sleeper's head. In a 3.96 m wide room with the beams running transversely at roughly 1.8-4.2 m centres, this is a drawing exercise, not a construction one. The owner should obtain the beam layout (which the structural set contains) at handover and lay out the beds against it. This is a genuine zero-cost phong thuy win.
- **Practical rationale:** the tradition's stated symptom - dizziness, headache, poor sleep - is the ordinary experience of trying to sleep under a low downstand in a hot climate, and the practical remedy (bed not under the lowest point of the ceiling) is the same one.
- **Conflict with safety/design:** none - this is a furniture-layout decision. Note for completeness that the beams in this structure are shallow (slabs 100 mm, beams 300-700 mm), so the effect is modest; the finding is a real but minor one.
- **Evidence:** VERIFIED for the structure (transcript-beams-slabs.md, beam schedule and the wall-note). The *bed positions* are NOT FOUND (no furniture layout in the set). VERIFIED for the rule ([30], [31]).

**P-20 - The master bedroom and the rear bedroom's window**

- **Where:** the rear bedroom (P. NGU, 4100 deep, one rear window 1500 wide, one door to the WC, on floors 2-5) is the most private room in the plan and is the obvious candidate for the master bedroom. The front bedroom has the balcony (S1 window and D5 balcony door) and faces the street. Floors 2, 3 and 4 are identical; floor 5 has the rear bedroom plus the front altar room.
- **Rule:** the master bedroom is traditionally given the **best** position in the house's own terms of qi, and its head-of-bed direction should be a good direction of the master occupant's cung [3]. There is no universal rule about front versus rear bedroom for a master; the folk preference is generally for the **quieter, more interior** room for the master, which in this house is the rear.
- **School:** Bat Trach (direction of the bed head) + general folk rule (master in the quietest room).
- **Agreement:** CONTESTED - no source states a fixed front/rear rule for the master bedroom; the tradition's own logic points to the quietest interior room.
- **Severity in the tradition:** MINOR (it is a furniture assignment, fully reversible).
- **Remedy:** put the master in the **rear bedroom** on floor 2 or 3 (not 5 - the top floor has the terrace and the plant room overhead, and the lift head is beside it), head on the **party wall**, away from the WC wall and away from the beam lines.
- **Practical rationale:** the rear bedroom is the quietest, and the front bedroom on floors 2-4 has a balcony door directly onto the street - a five-storey house's front bedrooms hear the street.
- **Conflict with safety/design:** none.
- **Evidence:** VERIFIED for the plan (JSON openings and rects; IMG_9974-9976). CONTESTED / CLAIMED for the master-bedroom rule.


### 3.7 The altar room (phong tho / ban tho)

**P-21 - The altar room is on the 5th floor at the FRONT, and the tradition would put it at the REAR of the top floor**

- **Where:** P. THO is at y 4900-8900 - the **front** of the 5th floor, 3960 x 4000, with the front balcony (BAN CONG, y 3500-4900) directly in front of it and the K1/K2 glazed front behind it (IMG_9976, IMG_9979: the 5th-floor front shows D6 and S2, a 1000-wide door and a 1200-wide window). Behind the altar room, at y 8900-12300, are the front hall and the front WC (JSON `wc_truoc_f5` x=1960 y=8900 w=2000 d=1900).
- **Rule:** the altar room is traditionally (i) on the **top floor** - the highest, quietest, most private place, closest to the heavens [32]; (ii) in the **interior**, not on the street front, because the front is where the house's incoming qi and the outside world are; (iii) **not facing the main door** and **not under a beam** and **not next to or above a WC** [25], [33].
- **School:** general nha ong folk rule + phong tho practice; Bat Trach adds toa cat huong cat - the altar faces one of the owner's four good directions [1].
- **Agreement:** UNIVERSAL on *top floor, quiet, not under a beam, not facing the WC door*; CONTESTED on *interior versus front* - see the dispute below.
- **Severity in the tradition:** MODERATE for the front position; the placement here is otherwise good.
- **Remedy:** the position is fixed by the structure, but **the altar's placement inside the room is free**, and that is where the tradition's actual requirements live: (a) put the altar table against a **solid interior wall**, not against the front glazing and not against the balcony wall - the front wall of this room is the most exposed wall in the house; (b) **do not put it against the WC wall** - the WC is immediately behind the altar room, sharing the wall at y 8900. Note this precisely: the WC is *behind and beside*, not *below*, so the tradition's worst case (WC above the altar) does not occur; (c) **do not put it under a beam** - check the floor-5 beam layout (DS5/DS6 grid) and place the altar clear of it; (d) the altar should face one of the owner's four good directions - this is a rotation of the altar table within the room, and it is free.
- **Practical rationale:** the front placement is a genuine loss, and it is a *practical* loss before it is a symbolic one: the room's outer wall is the exposed facade with the street on the other side of it. The trader's own instinct - put the altar against the quiet interior wall, with the back to the activity - is also how you make a small prayer room feel calm.
- **Conflict with safety/design:** the altar must not be fixed to or lean on the exterior wall in a way that damages the waterproofing, and the 5th floor is directly below the roof terrace - the room needs the waterproofing check more than most.
- **Evidence:** VERIFIED (JSON `tho_f5` rect and `wc_truoc_f5` rect; IMG_9976; IMG_9979 D6/S2). VERIFIED for the rule ([25], [32], [33]).

**P-22 - The house has a dedicated altar room, which is the better of the two arrangements**

- **Where:** the drawing **does** provide a dedicated P. THO on the 5th floor, which is better than the common fallback in a narrow house.
- **Rule:** where a tube house cannot hold a dedicated altar room, Vietnamese practice explicitly permits the altar in the living room or the family room, with a light partition or a curtain for privacy - [34] states this as one of two legitimate arrangements for a nha ong and says that the sincerity of the worship is the thing that matters, not the room.
- **School:** general folk rule / phong tho practice.
- **Agreement:** COMMON.
- **Severity in the tradition:** MINOR.
- **Remedy:** none - this house has the dedicated room, which is the better of the two arrangements. Worth telling the owner, because a common worry about narrow houses is that the altar must be compromised; here it need not be.
- **Practical rationale:** n/a.
- **Conflict with safety/design:** none.
- **Evidence:** VERIFIED (IMG_9976 labels P. THO); VERIFIED for the alternative arrangements ([34]).

**P-23 - The altar and the WC: *khong dat ban tho doi dien nha ve sinh* and *khong dat ban tho o noi co ue khi***

- **Where:** the front WC on the 5th floor (y 8900-10800) is immediately behind the altar room (y 4900-8900) and shares the wall at y = 8900. The altar's door is on the hall at y 8900-12300 (JSON `door ['tho_f5','hall_front_f5']`).
- **Rule:** *khong dat ban tho doi dien cua nha ve sinh* and *phia sau ban tho khong nen co nha ve sinh* - the rule is not merely about the line of sight; it is about the **ue khi** (impure qi) collecting behind the altar [35]. Some sources go further and forbid a WC **above** the altar outright.
- **School:** general nha ong folk rule / phong tho practice.
- **Agreement:** COMMON as a rule; CONTESTED as to whether *behind* and *opposite* both count - [35] states both, some sources only the facing rule.
- **Severity in the tradition:** MODERATE.
- **Remedy:** the room's use as an altar room is not in question, but the **altar's position within the room is**. The compliant arrangement is: the altar against the wall **furthest from the WC** - i.e. against the front-side interior wall or a side wall - and **not** against the WC's shared wall, so the altar's back is not to the WC. If the WC door's swing or position makes the altar face the WC door, rotate the altar 90 degrees to a side wall. Free, and it is exactly the *toa cat huong cat* rotation that P-21 asks for anyway - the direction and the WC rule can be satisfied together.
- **Practical rationale:** the shared wall is also the wall most likely to carry the WC's ventilation duct and the sound of the extract fan - a second reason to keep the altar off it.
- **Conflict with safety/design:** none. The fan duct and the WC door swing are the engineer's and the joiner's; the phong thuy constraint here happens to align with both of them.
- **Evidence:** VERIFIED for the adjacency (JSON `tho_f5` and `wc_truoc_f5` rects, shared wall at y = 8900). VERIFIED for the rule ([25], [33], [35]).

### 3.8 Roof terrace, plant room and the water tank

**P-24 - The water tank is not on the drawings, and the lift head is**

- **Where:** the roof plan (IMG_9978) shows five X-hatched rectangles, the stair/lift roof block in the middle, the **O ky thuat thang may** (lift technical overrun) 2000 wide, and **two light wells**. **No water tank (be nuoc) is drawn, and no tank position is annotated anywhere in the transcribed set.** Roof drainage arrows are shown at the core block, and the roof plan carries no level and no parapet height.
- **Rule:** the tank's *position* is a real traditional question, and the sources are specific: a tank in the **Doi (West)** cung is called *dao hoa phiem thuy* and is associated in the tradition with the household turning to dissipation and vice [36]; a tank in the **Ly (South)** cung is *thuy khac hoa* and is said to be bad for health; the safest general advice is the **centre (trung cung)** of the plot, which is what [36] recommends when the plot has no particular strength.
- **School:** general nha ong folk rule; Phi Tinh does not place tanks by cung.
- **Agreement:** COMMON as a folk rule; the *reasoning* (a tank is a body of water, and water in the wrong cung interacts badly with the cung's element) is the tradition's own.
- **Severity in the tradition:** MODERATE.
- **Remedy:** the tank is not yet located, so this is a **live decision**: place the tank in the **rear third of the roof, away from the lift overrun and away from the light wells**, on a raised plinth with a proper overflow and an access hatch. The rear of the roof terrace is the part with no stair-head light well in it. If the owner's cung is known and its Trung cung can be identified, the [36] advice is to prefer the centre. Cheap and reversible: the tank position is decided by the plinth, not by the structure.
- **Practical rationale:** a roof tank needs a level plinth, a screened overflow that discharges where it cannot erode the waterproofing, and access that does not require climbing over the parapet. Choosing the position *before* the plinth is built avoids redoing the waterproofing - which is the expensive version of this problem.
- **Conflict with safety/design:** the roof has **no parapet or balustrade note** on the plan sheets, and the stair's glass light well on the terrace has **no stated load rating** - the safety review owns both. A water tank is a permanent load: its position must be checked by the structural engineer, and it must not sit where it blocks the terrace's drainage arrows or the lift's maintenance access.
- **Evidence:** VERIFIED (IMG_9978 notes and legend; no tank anywhere in the transcript). VERIFIED for the rule ([36]).

**P-25 - The lift head (o ky thuat thang may) stands on the roof, over the core**

- **Where:** IMG_9978: *O ky thuat thang may* 2000 wide (plan 1800 + 900), in the middle of the roof, over the core; the section (IMG_9980) shows the overrun above +20.400, height 1300, PARTIAL. Sheet IMG_9988 gives the hoist-hook slab 2000 x 2000, 120 mm thick, with a single 25 mm hook bar.
- **Rule:** a solid mass in the centre of the plan is traditionally read as **trung cung bi chan** - the centre is blocked - and the traditional remedy is a void, a water feature, or planting at the centre rather than a solid block. The lift head is a solid block on the roof, at the centre of the core.
- **School:** general nha ong folk rule (the *trung cung* reading); Phi Tinh reads the core's position on the roof chart.
- **Agreement:** CONTESTED - the *blocked centre* reading is common, but the counter-claim (a solid centre is stable and the house's heart need not be open) is also made.
- **Severity in the tradition:** MINOR for a roof-level overrun, which no tradition treats as a dwelling-space problem; MODERATE if the reading is extended to the shaft below (see P-10, also CONTESTED).
- **Remedy:** none achievable - the lift head is where the lift has to be. If the owner wants to act on the reading, the traditional and pleasant move is to make the *roof* around the core a planted, shaded sitting area rather than a bare concrete deck, and to use the front and rear terraces as the usable outdoor rooms (they are 8800 and 5700 deep in the model, which is a large outdoor area for a 3.9 m-wide house).
- **Practical rationale:** the roof terraces are the best outdoor space the house has and they sit directly over the rear bedroom and the front altar room. Making them comfortable - planters, a table, a hose point, shade - is worth more than any symbolic correction, and it is the one place where the tradition's *plant the corners, keep the centre* instinct and the practical wish for a cool, green, private roof coincide.
- **Conflict with safety/design:** the lift overrun is a maintenance structure with a rated hoist hook; nothing may be placed on it or against it that impedes the maintainer. The terrace parapet question belongs to the safety review.
- **Evidence:** VERIFIED (IMG_9978, IMG_9980, IMG_9988). CLAIMED for the rule.

### 3.9 The facade, the number of floors, and the shape of the house

**P-26 - Five storeys plus a terrace: how many floors does the tradition count?**

- **Where:** the levels are +-0.000, +3.800, +7.000, +10.400, +13.800, +17.200, +20.400, +21.900 (transcript, level tags). The Vietnamese storey naming on the sheets is *tang N (lau N-1)*: *tang 1 (lau 0)* = tret, *tang 5 (lau 4)* = the top floor, and *san thuong (lau 4)* is the terrace at the same level as tang 5.
- **Rule:** the folk Vietnamese count is by **occupied storey**, and the terrace and roof are not counted as a floor; the lung (mezzanine) is counted. So this house is **five occupied floors**. Note that the *luc hao* (six harmony) figure in the folk literature applies to the *house's shape and elements*, not to its floor count: the six are Thuy (nha hinh nuoc), Hoa (nha hinh chop), Moc (nha hinh tru/cot), Kim (nha hinh tron/vom), Tho (nha hinh vuong/mai thang) and the wind/wood variant. **This house's shape is rectangular with a flat roof and a straight parapet - the *hinh Tho* (earth) form**, whose tr truong sinh step is the **5th** [12].
- **School:** general nha ong folk rule.
- **Agreement:** COMMON for the counting; CONTESTED for the *luc hao* element labels, which vary between sources and are frequently used loosely.
- **Severity in the tradition:** MINOR.
- **Remedy:** none required. The important consequence of the **Tho** classification is the *stair* rule in P-06: the tr truong sinh step for an earth-shaped house is the 5th, and the acceptable step counts for a Tho house are 1, 3, 5, 7, 8, 9, 13, 15, 17, 19, 20, **21**, 25, 27 [12]. **21 is on the list.** The stair passes under this rule too.
- **Practical rationale:** a flat-roofed, rectangular tube house in HCMC is thermally the hardest type to keep cool - the roof is the largest heat gain in the building, and the roof terrace above the rear bedroom is the worst place for it. The phong thuy advice (*plant the roof, make the terrace a green room*) and the cooling advice are the same advice.
- **Conflict with safety/design:** roof waterproofing, drainage, and the terrace's structural loading for planters are the engineer's; the safety review owns the parapet and the glass light well.
- **Evidence:** VERIFIED (level tags; IMG_9972 naming note *tang 5 (lau 4) is the top floor and san thuong (lau 4) is the terrace*). VERIFIED for the rule ([12]).

**P-27 - The facade is a flat rectangle: no sat khi from the house's own shape, but the neighbours' roof lines are the ones to look at**

- **Where:** the front elevation (IMG_9979) reads total width 3900 (550 + 2800 + 550 at the ground; 1900 + 2000 at the top) and total height 21 900, with the storey heights 3800 / 3200 / 3400 / 3400 / 3400 / 3200 / 1500. The facade is rectangular: a glazed ground-floor door, a 1700-high glass wall at the mezzanine, and balconies with arched window/door pairs on floors 2-4. The party walls are on both sides. `designs/contractor-as-drawn.json` gives the context: `neighbour_west_height_mm: 14000`, `neighbour_east_height_mm: 10500`, `opposite_height_mm: 12000`.
- **Rule:** **sat khi** (sha qi) is the term used for the sharp, intrusive energy the tradition attributes to corners, points and projections. A corner or a point that aims at the main door is the classic case (*tiem giac sat* - a needle-pointing sha); a neighbour's gable, a neighbour's parapet corner or a projecting slab aimed at the front door is read as *borrowed* sha. The remedies are: screen the point, plant it, round it off, or place a mirror to deflect it.
- **School:** general nha ong folk rule / Phi Tinh.
- **Agreement:** COMMON as a rule; CONTESTED in mechanism - some schools attribute sha to the *shape*, others to the *flow of qi* along the street, others simply to visual provocation, which is the version with the strongest practical support.
- **Severity in the tradition:** MODERATE where a point actually aims at the door; MINOR in general.
- **Remedy:** **none needed for the house itself** - a flat rectangular facade with a recessed, symmetrical front has no sha of its own, and there is nothing to round off. The check that *is* worth doing is the **neighbours'**: with a 14 000 mm house on one side and 10 500 mm on the other in a 3.9 m gap, the neighbours' parapets and any projecting balcony slabs are the sharp edges in this street. Two things the owner can actually do: (a) keep the front yard planting low and to the sides, so neither their edges nor the neighbours' form a straight corridor into the front door; (b) if the on-site compass reading (section 1.1) shows that a neighbour's projecting corner points at the front door, note it for the practitioner - the traditional remedies (a plant, a screen, a mirror) are all in the cheap category.
- **Practical rationale:** the visual-propagation version of the sha rule is the one with real support: a hard, bright, projecting corner aimed at a doorway is genuinely unpleasant to look at, and screening it improves the street and the frontage.
- **Conflict with safety/design: the mirror remedy should be skipped.** A mirror angled at the street at the front of a house in HCMC is a heat gain and a glare source for the neighbours, and at the top of a 5-storey facade it is a fall hazard during cleaning. Use planting or a screen instead; the tradition accepts both.
- **Evidence:** VERIFIED for the drawing facts (IMG_9979 elevation dimensions and storey heights; JSON `site.context` for the neighbour heights). CLAIMED for the rule ([37] for the point-and-needle form; [23] for the shared-wall/courtyard form).

**P-28 - The balconies project to the street and the frontage is only 3.9 m**

- **Where:** every upper floor has a front balcony (BAN CONG, 1400 deep, y 3500-4900), and floors 2-4 have a rear loggia (LO GIA) at the rear. The balconies are inside the building line, not cantilevered (fidelity.md (a) and the balcony notes). The glass balustrade is 8 mm tempered with a stainless handrail on every balcony, loggia and the mezzanine rear (IMG_9973, 9974, 9975, 9976).
- **Rule:** a balcony over the entry is read as a protective canopy - the *mai che* - and is generally favourable. The relevant prohibitions are about a balcony facing a neighbour's door or a sharp point, and about a balcony that traps heat.
- **School:** general nha ong folk rule.
- **Agreement:** COMMON.
- **Severity in the tradition:** MINOR - favourable.
- **Remedy:** none required. The balconies already do the job the tradition wants from a front canopy.
- **Practical rationale:** the front balconies shade the front bedroom glazing on floors 2-4 and 5 - which is the single most effective heat control available in this orientation - and they give the street a human scale. The 8 mm tempered glass with a stainless handrail is a sound choice for a 3.9 m-wide frontage where the balustrade cannot be a heavy wall.
- **Conflict with safety/design:** the balustrade specification is thin - no height is stated on any sheet, and there is no guard note at the mezzanine void edge or the terrace edges (transcript, *Five things for a safety or design reviewer*, item 1). The safety review owns that; the phong thuy point is only that the glass balustrade should be kept and not replaced with a solid parapet, which would help the sha reading slightly and hurt the light and the ventilation much more.
- **Evidence:** VERIFIED (IMG_9973-9976 notes; fidelity.md; JSON room rects).


### 3.10 Dimensions and the Lo Ban ruler

**P-29 - Which ruler, which element, and where the schools disagree**

- **Where:** the whole dimensional set of the project - the printed door and window sizes
  (IMG_9972, IMG_9974-9977, IMG_9979), the stair geometry (IMG_0003/0004/0005), the room
  widths in designs/contractor-as-drawn.measurements.md, and the altar room on the 5th
  floor (IMG_9976).
- **Rule:** each element is read on a specific ruler - 52.2 cm (thong thuy) for the *void*
  (door and window clear openings, light wells, ceiling heights), 42.9 cm (duong trach) for
  the *solid* (kitchen counter, steps, stair flights, beds, wardrobes, storey heights), and
  38.8 cm (am phan) for the *ritual* (altar table, ancestral cabinet, ritual tablet).
- **School:** Lo Ban.
- **Agreement:** COMMON as to which ruler measures what. CONTESTED as to the cung *names*
  on the 42.9 and 38.8 rulers, as to the **zero point** on those two rulers, and as to
  whether the 38.8 ruler has 8 cung or 10. All four disagreements are listed below.
- **Severity in the tradition:** MINOR for the building as a whole (the structure is fixed
  and most of its dimensions land on mixed cung, which is what the tradition expects of an
  existing building); MODERATE for the individual items that are still free to choose.
- **Remedy:** choose the free dimensions - the altar table, the door leaves, the cabinet
  sizes - on the ruler that applies to them, and use the *most favourable* of the two
  conventions where the reading flips (see the dispute 3 note below). Nothing structural.
- **Practical rationale:** the ruler is a selection tool for what is still free, not a
  reason to move a wall. Where a reading lands badly, the traditional and the practical
  answer is the same: change the thing by a few millimetres, or change the orientation.
- **Conflict with safety/design:** door clear widths, escape widths, stair geometry, slab
  thicknesses and storey heights are governed by the safety and structural codes, not by
  a ruler. **Where the ruler and the code disagree, the code wins and the ruler is dropped.**
- **Evidence:** VERIFIED for the ruler attributions ([7], [8], [9], [38], [39], [40], [16],
  [43]) and for the cung names ([4], [15], [38], [39]); VERIFIED as arithmetic for the
  readings in P-30 (script _scan1022/loban.py).

The three rulers and their conventional use, per [7], [8], [9] and [38]:

| ruler | cycle | cung | conventionally measures | good / bad cung names |
|---|---|---|---|---|
| **52.2 cm (thong thuy)** | 522 mm, 8 cung x 65.25 mm, each with 5 sub-cungs | 8 | **the void**: door and window clear widths, openings, light wells, ceiling heights | good: Quy Nhan, Thien Tai, Nhan Luc, Te Tuong - bad: Hiem Hoa, Thien Tai, Co Duc, Thien Tac |
| **42.9 cm (duong trach)** | 429 mm, 8 cung x 53.625 mm, each with 4 sub-cungs | 8 | **the solid**: kitchen counter, steps, stair flights, beds, wardrobes, cabinet heights, storey heights | good: Tai, Nghia, Quan, Ban (Mang) - bad: Benh, Ly, Kiep, Hai |
| **38.8 cm (am phan)** | 388 mm, 10 cung x 38.8 mm, each with 4 sub-cungs | 10 | **the yin/ritual**: altar tables, ancestral cabinets, the ritual tablet | good: Dinh, Vuong, Nghia, Quan, Hung, Tai - bad: Hai, Kho, Tu, That |

**Disagreements between schools, stated rather than hidden:**

1. **The 42.9 cung names.** The cung *order* is given as Tai-Benh-Ly-Nghia-Quan-...-Ban by
   [39] and [40], as ...-Nan-Hai-Mang by [38], and as ...-Kiep-Hai-Mang by [15]. Some sources
   call the 8th good cung **Ban** (the base, from Ben), others **Mang** (the fate/net); [39] and [40] both give the order Tai-Benh-Ly-Nghia-Quan-Kiep-Hai-Ban, [38] gives Tai-Benh-Ly-Nghia-Quan-Nan-Hai-Mang, [41] gives Tai-Benh-Ly-Nghia-Quan-Kiep-Hai-Mang, and [42] gives a *different set entirely* (Tai, Hai, Nhan, Kho, Loc, Tho, Tu, Hỷ) for the 42.9 ruler - which is the **38.8 ruler's** cung set. The naming is inconsistent across the Vietnamese literature; the *good/bad* pattern (4 good, 4 bad, alternating pairs) is not.
2. **The 38.8 ruler has 8 cung in some schools and 10 in others.** [38], [43], [16] and [7] all describe a 10-cung ruler with 38.8 mm per cung and 4 sub-cungs; [38] names the ten big cung Dinh-Hai-Kho-Nghia-Quan-Tu-That-Tai. The tables below use the **10-cung version**, because [4] publishes the complete 40-row numeric table for it.
3. **The zero point.** The published 42.9 tables start their first sub-cung at 13.40 mm from the ruler's end (the ruler begins in the *middle* of the Tai cung), while the 38.8 table begins at 9.70 mm. A reading that falls near a cung boundary can therefore come out differently depending on which end you start from. The findings below note every case where the answer flips.
4. **Which ruler for a door.** The 52.2 ruler is for the **clear (thong thuy) opening** - measured between the inner faces of the frame, ignoring the frame's own thickness [38], [9]. Some Vietnamese practice measures the *cover* (phu bi, outer dimension) for a door leaf instead and uses the 42.9 ruler [8].
5. **Whether a door has to be good at all.** [9] gives the popular rule *do thi dung, den thi bo* and [4] the more forgiving *two red, one black*. The two coexist.
6. **The 38.8 ruler's Vietnamese printings drift.** [7] notes that the Vietnamese 38.8 cm rulers are commonly printed 2 mm per ruler away from the Chinese original, and that the 52.2 cm ruler is rare in Vietnam - which is why most Vietnamese practitioners own a combined 42.9 + 38.8 steel rule and look the 52.2 cung up separately.

**P-30 - The printed sizes, read against the rulers**

- **Where:** every dimension printed on the architectural sheets that the Lo Ban is applied
  to - the D1 front door and the K1 mezzanine glass wall (IMG_9972, IMG_9979), the S1
  balcony window and the D5 / D6 doors (IMG_9979), the Dw WC door (IMG_9974), the stair
  treads and flights (IMG_0003/0004/0005), the frontage chains (IMG_9972), and the altar
  room on the 5th floor (IMG_9976).
- **Rule:** a measurement is reduced to the ruler cycle (522 / 429 / 388 mm), the remainder
  is located, and the cung it falls in is read as good or bad. The three tables below are
  the result of doing that to every dimension in the drawing set.
- **School:** Lo Ban.
- **Agreement:** COMMON as a method; the *results* are CONTESTED wherever the zero-point
  dispute applies, and each such row says so.
- **Severity in the tradition:** MINOR for the fixed building dimensions (they cannot be
  changed and, as the tradition itself says, a fixed dimension is not a defect); MODERATE
  for the door leaves and the altar table, which are free and are the ones worth acting on
  (see P-32 and P-21).
- **Remedy:** three things only, all of them free if they are decided now: the internal
  door leaves at **810 mm** rather than 900 (P-32), the WC leaf at **760 mm** rather than 700
  (P-32), and the altar table height at **1200 mm** rather than 900 (P-21, which also gives
  the altar the width of 800 and the depth of 600 that the sources already recommend). The
  main door D1 and the balcony windows are structural or joinery decisions already made
  and should not be disturbed for this.
- **Practical rationale:** the honest summary of this table is that **the ruler has almost
  nothing to say about this building**, because the building was designed to a 1000 mm
  structural module and the ruler cycles are 522 / 429 / 388 mm. The exceptions are exactly
  the dimensions that are still free. That is also what the tradition says: the ruler is a
  tool for choosing, and a completed building is not a thing to be chosen.
- **Conflict with safety/design:** **the table must never be used to narrow a door.** The
  clear widths that matter for egress and accessibility are set by the safety review and
  the building regulations; see P-32 and section 5, row 4.
- **Evidence:** VERIFIED for the printed dimensions (transcripts; measurements.md; the JSON
  openings list); VERIFIED as arithmetic for every cung reading, computed with the script
  _scan1022/loban.py from the cung tables of [4], [39] and [38].

Computed with the script `_scan1022/loban.py` from the cung tables of [4] (52.2, complete), [39]/[38] (42.9 and 38.8 cung order). *rem* is the position within the 522 / 429 / 388 mm cycle; the cung is the interval the remainder falls in.

**52.2 cm ruler (thong thuy) - doors, windows, openings**

| element | printed size | rem (mm) | cung | verdict |
|---|---|---|---|---|
| **D1 front door**, clear width | 2800 | 190.00 | Thien Tai | **HUNG** (bad) |
| **D1 front door**, clear height | 2800 | 190.00 | Thien Tai | **HUNG** |
| **K1 mezzanine glass wall**, width | 2800 | 190.00 | Thien Tai | **HUNG** |
| **K1 mezzanine glass wall**, height | 1700 | 134.00 | Thien Tai | **HUNG** |
| **S1 balcony window** | 2500 | 412.00 | Thien Tac | **HUNG** |
| **D5 balcony door** | 1100 | 56.00 | Quy Nhan | **CAT** (good) |
| **D6 top-floor door** | 1000 | 478.00 | Te Tuong | **CAT** |
| **S2 top-floor window** | 1200 | 156.00 | Thien Tai | **HUNG** |
| **Dw WC door** (transcript, floors 2-4) | 700 | 178.00 | Thien Tai | **HUNG** |
| internal door (as modelled) | 900 | 378.00 | Co Duc | **HUNG** |
| **frontage, overall** | 3900 | 246.00 | Thien Tai | **CAT** |
| frontage, internal between walls | 3200 | 68.00 | Hiem Hoa | **HUNG** |
| plot width | 3960 | 306.00 | Nhan Luc | **CAT** |
| front yard depth | 3500 | 368.00 | Co Duc | **HUNG** |

**42.9 cm ruler (duong trach) - the solid dimensions**

| element | printed size | rem (mm) | cung | verdict |
|---|---|---|---|---|
| stair tread depth | 250 | 250.00 | Quan | **CAT** |
| stair flight width, tret/lung | 1250 | 392.00 | Ban | **CAT** |
| stair flight width, tang 2-5 | 1350 | 63.00 | Benh | **HUNG** (but **CAT** under the 13.40 mm zero-point convention - see dispute 3 above) |
| stair landing | 1250 | 392.00 | Ban | **CAT** |
| kitchen counter run | 2400 | 255.00 | Quan | **CAT** |
| WC door (as modelled) | 900 | 42.00 | Tai | **CAT** |
| bed width | 1600 | 313.00 | Kiep | **HUNG** |
| bed length | 2100 | 384.00 | Ban | **CAT** (but **HUNG** under the 13.40 mm convention) |
| balcony depth | 1400 | 113.00 | Ly | **HUNG** |
| altar table width | 800 | 371.00 | Hai | **HUNG** |
| altar table length | 1200 | 342.00 | Hai | **HUNG** |
| storey height, ground | 3800 | 368.00 | Hai | **HUNG** |
| storey height, upper floors | 3400 | 397.00 | Ban | **CAT** |
| light well width | 1600 | 313.00 | Kiep | **HUNG** |
| lift shaft width | 1800 | 84.00 | Benh | **HUNG** |
| lift shaft depth | 1600 | 313.00 | Kiep | **HUNG** |
| rear bedroom depth | 4400 | 110.00 | Ly | **HUNG** (Benh under the other convention) |

**38.8 cm ruler (am phan) - the altar**

| element | size | rem (mm) | cung | verdict |
|---|---|---|---|---|
| altar table width | 800 | 24.00 | Dinh | **CAT** |
| altar table depth | 600 | 212.00 | Quan | **CAT** |
| altar table height | 900 | 124.00 | Kho | **HUNG** (Vuong under the 9.70 mm convention) |
| altar table height | 1200 | 36.00 | Dinh | **CAT** |
| ancestral cabinet width | 900 | 124.00 | Kho | **HUNG** (Vuong under the other convention) |
| ritual tablet width | 300 | 300.00 | Hung | **CAT** |
| altar room width | 3960 | 80.00 | Vuong | **CAT** |
| altar room depth | 4000 | 120.00 | Kho | **HUNG** (Vuong under the other convention) |

**Reading this table honestly.** The size of the altar table is not in the drawings - 800 / 600 / 900 / 1200 are the dimensions the sources use as examples - and the table shows that **800 wide and 600 deep are already good cung**; the altar's height is the one dimension worth choosing (900 lands on Kho, 1200 lands on Dinh - a 300 mm difference for a better cung, which is the whole point of the ruler). The building's own dimensions are fixed and mostly land on mixed cung, which is exactly what the tradition says to expect of an existing building: **the ruler is a tool for choosing what you still have the freedom to choose** (the altar, the door leaves, the cabinet sizes, the interior partition positions) and is not a reason to move a structural wall.

**P-31 - The frontage, 3.95 m, and the Lo Ban**

- **Where:** the frontage is printed as 3900 overall at the front, with 350 + 3200 + 350 wall zones; the plot is 3960 in the model (`measurements.md`: *frontage printed 3950 on every sheet; +10 mm orthogonal margin*).
- **Rule:** the frontage is measured with the **42.9 cm (duong trach)** ruler - it is a built, solid dimension of the house's face [8], [38]. A separate and very widely held folk rule is that the frontage should be an **odd** number of *units* (traditional Vietnamese *thuoc* of 30.3 cm and 30.4 cm, and in southern practice a *thuoc* of about 0.32 m) so that the house can be divided into an integral number of bays; an un-dividable frontage is called *cua hau* or *bat tien* in the trade.
- **School:** Lo Ban + general nha ong folk rule.
- **Agreement:** COMMON as a folk rule; the Lo Ban reading itself is contested in strength, and the *odd number of traditional thuoc* rule is a trade rule rather than a phong thuy one.
- **Severity in the tradition:** MINOR.
- **Remedy:** none available for the frontage - it is the plot. The trader's rule (frontage divisible into an integral number of bays) is actually **satisfied** here: 3900 = 350 + 3200 + 350, and the interior 3200 divides into the 1000 mm structural module the drawings use (chain: 350 | 3010 | 4240 | 4000 | 3200 | 1800 | 4500 | 1600). So the practical version of this rule passes.
- **Practical rationale:** the Lo Ban reading of the frontage on the 42.9 ruler gives 3900 -> rem 39.00 -> **Tai** (good), while the *plot* width 3960 -> rem 99.00 -> **Benh** (bad) and the *internal* 3200 -> rem 197.00 -> **Nghia** (good). The disagreement between the building line and the plot line is a 60 mm difference - a good illustration of why this rule is not worth arguing about at this level of precision.
- **Conflict with safety/design:** none.
- **Evidence:** VERIFIED for the dimensions (IMG_9972 frontage chains; measurements.md plot table). VERIFIED for the ruler attribution ([8], [38]). VERIFIED as arithmetic on [4]/[39]/[38] for the computed cung.

**P-32 - The internal 900 mm door leaves, and the 700 mm WC door**

- **Where:** the model has 900 mm internal doors throughout (JSON `openings`, `width_mm: 900`); the transcript reads Dw (WC door) at 700 on floors 2-4 (IMG_9974: *door Dw 700 / 750, 850 + 950 widths* - PARTIAL).
- **Rule:** a door's clear width is read on the 52.2 ruler. 900 -> Co Duc (bad); 700 -> Thien Tai (bad). The sources' own *so dep* lists for a 52.2 ruler are 750-810 (a single-leaf room door), 1070-1100 (a double-leaf or large door), 1270-1330 (a two-leaf main door), 1530 (three leaves), 1860 (three or four leaves), 2120 / 2330 (four-leaf main door height) - [43], [42], [44].
- **School:** Lo Ban.
- **Agreement:** COMMON.
- **Severity in the tradition:** MINOR.
- **Remedy:** essentially free, and **this is the one Lo Ban rule that is worth acting on**, because door leaves are made to measure at the end of the job: an internal leaf of **810** (Nhan Luc, good) rather than 900 (Co Duc) costs nothing but a different order quantity; the WC door at **760** (Thien Tai, good) rather than 700 costs 60 mm of clearance and one hinge adjustment. The main door D1 at 2800 sits in **Thien Tai**; **2810-2870** moves it into the next cung boundary as the table of [4] gives it, and **2880-2900** into Nhan Luc. A 10-100 mm change to a **clear** opening on a 2800 mm door is a joinery change, not a structural one - but it is only possible if it is decided now, before the frames are ordered.
- **Practical rationale:** none of this is about the door being lucky; it is about the fact that these are the *only* dimensions on this project that are still free and that the change is smaller than a tolerance. The honest caveat is that a 10 mm change to a 2800 mm opening changes nothing measurable about the house - which is exactly the point of the exercise for the owner: it is a free gesture, not a fix.
- **Conflict with safety/design: door width is a safety and accessibility matter.** The clear width of the main door and the stair doors is governed by egress and accessibility requirements, not by a ruler. **Do not narrow a door to improve its cung.** In particular, the bedroom doors must retain the clear width that the escape route needs, and the WC door must not be narrowed below what the layout needs. Where the ruler and the escape width conflict, the escape width wins and the ruler is dropped.
- **Evidence:** VERIFIED for the sizes (JSON openings; IMG_9974 Dw PARTIAL). VERIFIED as arithmetic for the ruler computation. VERIFIED for the *so dep* lists ([42], [43], [44]).

---


## 4. Owner-dependent layer: the questionnaire and the decision tree

The owner's birth data is **not given**, and it is not invented here. The following is a
one-page questionnaire the owner can fill in and hand back; the decision tree then turns
the answers into room assignments. Nothing in this section requires the owner to know
anything about feng shui - only their own birth date and who lives where.

### 4.1 The questionnaire (hand this to the owner)

**A. The household head**

1. Full name of the person whose name the house will be built under (the *chu nha*):
   ______________________
2. Date of birth (day / month / year, and the year in the lunar calendar if known):
   ______________________
3. Sex: ____ (needed because the cung phi formula differs by sex)
4. Where were you born (province / country)? ______________________
   *Needed only because the lunar-versus-solar year boundary differs by country; if you
   are unsure whether your birth was before or after Tet, answer this and it will be
   checked.*

**B. Everyone who will sleep in the house**

5. For each person: name, date of birth, and sex.
   ______________________ / ______________________ / ______
   (repeat for each person who sleeps here, including children and any elderly parent)
6. Who sleeps in the front bedroom and who in the rear bedroom, on each floor
   (tang 2, 3, 4, 5)? ______________________
7. Is anyone a shift worker, or does anyone need to wake at night and use the WC or the
   stair? Yes / No - if yes, who and how often? ______________________

**C. Practice and belief**

8. Does the household keep an ancestral altar (ban tho gia tien), a Buddha / Thien altar,
   or both? ______
9. Does the household place a Thien Tai / O Dia / Tho Than shrine? Yes / No
10. Are there any dates the family already avoids (a parent's death anniversary, a
    religious day, a family taboo)? ______________________
11. How much of the tradition does the household actually want applied? Choose one:
    (a) only the things that cost nothing and change nothing - bed direction, altar
    rotation, plants, a screen - *recommended*
    (b) the above plus the auspicious-date work for the topping-out and move-in
    (c) everything the tradition offers, including changing the layout
12. Is the owner willing to move the altar room, the bed positions, or the kitchen door
    swing **before construction starts** if the answer helps? Yes / No
13. Budget tolerance for phong thuy changes (excluding safety work):
    ______ VND (0 = free measures only)

**D. Site**

14. Compass bearing of the front facade (see the measurement instructions in section 1.1):
    ________ degrees, measured by ____ (phone compass / professional compass)
15. The street's own direction (the axis of the road in front of the house):
    ________ degrees
16. Which neighbours are taller than this house, and on which side (as seen from inside
    the house facing out)? ______________________
17. Any existing water tank, and where? ______________________

### 4.2 The decision tree

**Step 1 - Compute each person's cung phi.** For every person who sleeps here, using the
formula in section 2.1. Record the **cung** and the **group** (Dong tu menh or Tay tu
meneh) for each. Keep the *household head's* result as the primary one; the rest are used
to check for conflicts.

**Step 2 - Establish the four good directions.** Take the household head's cung and read
its four good directions from the table in section 2.2. Note that the four good
directions of any Dong tu menh owner are always Bac, Nam, Dong, Dong Nam, and of any Tay
tu menh owner always Tay, Tay Bac, Tay Nam, Dong Bac - so the group alone already fixes
the four directions, and only the *ranking* within the four needs the exact cung.

**Step 3 - If the household is split across the two groups.** This is the common case
(one Dong tu owner, one Tay tu owner) and it is not a crisis - [1] resolves it by
following the **head of the household**. The secondary occupant then gets the best
remaining option: usually the second-best good direction for them, or the master
bedroom's head turned to their own best direction while the other partner uses the
partner's second best. [1]'s worked example does exactly this (the wife's desk faces
Tay Bac, her Sinh Khi) while the house and altar follow the husband.

**Step 4 - The house direction.** If the measured facade bearing (question 14) falls in
one of the head's four good directions, the house is already well oriented and the Bat
Trach work reduces to the interior. If it does not, the plot is fixed and the
tradition's own fallback applies: **turn the interior** - the altar, the beds, the desk
and the stove - to the owner's good directions. Nothing about the building changes.

**Step 5 - Assign the floors.** The rule the tradition supports, and that the drawings
make easy:

| room | who | why |
|---|---|---|
| **Master bedroom** = rear bedroom on tang 2 or 3 | the head of the household, or the person whose cung is hardest to accommodate elsewhere | the rear bedroom is the quietest, has no street window, and has the party wall for the bed head; tang 2-3 is further from the lift head and the roof plant |
| **Second master / child's room** = front bedroom on tang 2 or 3 | whoever has the remaining group, or a child | the front bedroom has the balcony and the street light; a child's room benefits from that |
| **Rear bedroom, tang 4** | a child, a teenager, a guest, or a carer | it is the quietest of the four identical floors and directly above the kitchen and the WC stack - the family room that tolerates noise best |
| **Rear bedroom, tang 5** | the person with the least demanding direction, or a guest | the top floor is directly under the roof terrace: best cross-ventilation and the best roof access, but the most heat and the most water-tank noise |
| **P. Sinh hoat, mezzanine (lung)** | the family room | it is the only double-height room in the house and the one the tradition treats as the house's shared gathering qi |
| **P. Thu, tang 5 front** | the ancestor altar, plus a small altar for the household's own practice | it is a dedicated room on the top floor - the tradition's first choice - and it has a balcony for the family's use |

**Step 6 - Assign the directions inside each room.** Two rules, both free:

- **Altar (ban tho):** *toa cat huong cat*. Place it in the best zone of the room and
  rotate it so the person standing behind it faces one of the owner's four good
  directions. In this house the altar room's usable walls are the two side walls, plus
  the rear-side wall (y 8900, shared with the WC - avoid that one) and the front wall
  (exposed facade - avoid that one too), so the practical options are the **party wall**
  (x = 0) and the **stair-side wall**. If the head's Sinh Khi direction points toward the
  street, the altar goes against the party wall and faces the street; if it points
  toward the rear, it goes against the stair-side wall and faces the rear. Either way it
  is off the WC wall and off the front glazing, which satisfies P-21 and P-23 at once.
- **Bed heads:** the head goes against the **party wall** in the rear bedroom (solid,
  away from the WC stack, away from the window), and the head of the front bedroom goes
  against the **stair-side partition** rather than the outer wall, if the beam layout
  allows. Then rotate the bed so the head points at the sleeper's own Dien Nien (for a
  married couple) or Sinh Khi (for a child) direction.
- **Kitchen:** the cooking zone cannot move, but the **stove can be turned on the
  counter** so the cook's back faces one of the head's good directions - the *toa hung
  huong cat* rule, satisfied by rotating the hob within the run rather than by moving
  the kitchen.
- **The stair:** nothing to assign. It is the house's spine.

**Step 7 - Do the cheap works in this order.**

1. Beds: head against the party wall, no beam over the head, head toward the owner's
   good direction. (Free, and the biggest single win in the report.)
2. Altar: rotate within the room, off the WC wall, facing a good direction. (Free.)
3. Stove: turn the hob on the counter so the cook's back faces a good direction. (Free.)
4. WC doors: change the swing or use a pocket door so the WC door is not in line with
   the bed or the door opposite. (Nearly free - only if the doors are not yet ordered.)
5. Screen the stair lobby from the entry axis; keep the front yard open; plant the front
   corners and the roof. (Cheap.)
6. Door leaf sizes to the ruler: internal 810, WC 760, main door 2810-2870. (Free now,
   impossible later.)
7. If and only if the owner wants it: the auspicious-date work (section 4.3) and a Phi Tinh
   chart (section 4.4).

### 4.3 The timing layer (optional, short)

The following describes the checks and the formulas only. **No dates are selected here**,
because the owner's age is unknown and the checks below depend on it.

**Auspicious-date selection.** The four ceremonies are distinct and each has its own
rule set:

| ceremony | Vietnamese name | what it marks |
|---|---|---|
| breaking ground for construction | **cat noc** (also *dong tho*) | the start of the earth work; the owner's own age check governs |
| the raising of the roof / completion of the frame | **cat giao** (*lap dat / nen hoan thien*) | the point at which the house becomes a building rather than a hole |
| moving in | **nhap trach** | the owner's first night in the house; traditionally the wife enters first |
| the house's first full use / housewarming | **cat tich / khai trach** | the first gathering and the first offering |

The selection principle across all four is the same and is described in the sources as
the interaction of **the day's heavenly stem and earthly branch (can zhi ngay) with the
day's lunar month, the day's truc** (the twelve 30-day solar terms), **and the hour**,
combined with the avoidance days. The three parties to be reconciled are the day
chosen, the hour chosen, and the people involved.

**The three age checks on the builder-owner.** These are the checks the family will
actually ask for before they let a date be set, so they are worth stating precisely.
All three use the **tuoi mu** (the nominal age: year of the event minus year of birth,
plus one; some schools count by lunar year, which shifts the result by one for anyone
born before Tet).

1. **Tam Tai** (the Three Tribulations). Three consecutive years, keyed to the year of
   birth's *tam hop* (triple-harmony) group:
   - Thân - Ty - Than group -> in the years **Dan, Mao, Than**
   - Dan - Ngo - Tuat group -> in the years **Than, Dan, Tuat**
   - Hoi - Mao - Mui group -> in the years **Ty, Ngo, Mui**
   - Ty - Dan - Mau group -> in the years **Hoi, Ty, Mau**
   The rule as stated in [45] and [46] is that the tam tai years begin with the year whose
   earthly branch **opposes** the branch at the head of the group, then run for three
   consecutive years. [46] confirms this: *year 2026 is the second year of tam tai for
   the Hoi - Mao - Mui group*.
2. **Kim Lau** (the Golden Pavilion). Purely arithmetical: **divide the tuoi mu by 9;
   if the remainder is 1, 3, 6 or 8, the year is in kim lau.** [45] gives the meaning of
   each remainder: 1 = harm to oneself, 3 = harm to one's spouse, 6 = harm to one's
   children, 8 = harm to the family's affairs, work and property.
3. **Hoang Oc** (the Empty Tomb). Six cung cycling clockwise with the tuoi mu from age 10:
   **good** at Nhat Cat (10), Nhi Nghi (20), Tu Tan Tai (40); **bad** at Tam Dia Sat (30),
   Ngu Tho Tu (50), Luc Hoang Oc (60). [45] and [47] both give this six-cung cycle.

**The two years in question.**

| year | can chi | note |
|---|---|---|
| **2026** | **Binh Ngo** | the year of the Horse. Per [46], 2026 is the **second** year of tam tai for the Hoi - Mao - Mui group (Hoi, Mao, Mui born years) and the first year for the Than - Ty - Than group (Than, Ty, Than born years). The fourth group (Ty - Dan - Mau) is not in tam tai in 2026. |
| **2027** | **Dinh Mui** | the year of the Goat. It is the **third** year of tam tai for the Hoi - Mao - Mui group, and the first year for the Ty - Dan - Mau group. |

For the builder-owner the two checks that actually bite are **kim lau** (arithmetic, from
the owner's own birth year) and **hoang oc** (also from the owner's own birth year). The
tam tai check is a property of the birth *group*, so it can be read straight off the
owner's year of birth once it is known. The traditional remedies for a bad year are
*muon tuoi* (borrowing an age) and shifting the *ceremony* rather than the construction -
the construction can proceed, but the **cat noc** (breaking ground) and the **nhap
trach** (move-in) are the two that are normally moved. **Moving the move-in date is free;
moving the breaking-ground date costs a fortnight or two of site time.** That is the
practical shape of the whole timing layer: the expensive part is the delay, not the date
itself.

**What the timing layer cannot do.** It cannot fix a facing direction, a WC over a
bedroom, or a stair in the middle of the house. If the owner wants the auspicious work,
it should be layered on top of the interior decisions in the decision tree, not used to
justify moving the building.

### 4.4 Phi Tinh (Huyen Khong Phi Tinh) - a clearly separate optional layer

This system is **not** Bat Trach, and the two must not be mixed. [21] is explicit:
*this system is kept independent of Bat Trach*; it reads the house by the **year it was
built or substantially renovated** and the **degree bearing of the house**, and it does
not read the cung phi at all.

**How it works, in outline.**

1. **Determine the van (period) from the construction date.** [21] computes it from the
   completion date, using the Lập Xuân (Start of Spring) boundary rather than the Lunar
   New Year, and shows the reading directly: for a house completed in 2026 the period is
   **Van 9**, running **2024-2043**, with the central palace taking **Cuu Tu** (Nine, Fire).
2. **Place the nine stars in the Lo Shu bagua.** The van star sits in the centre; the
   remaining eight fly anticlockwise through the Lo Shu order (centre, Tay Bac, Tay, Dong
   Bac, Nam, Bac, Tay Nam, Dong, Dong Nam). For the example above the reading is Tay Bac
   = 1 (Nhat Bach, Water), Tay = 3 (Tam Bich, Wood), Dong Bac = 5 (Ngu Hoang, Earth),
   Trung cung = 9 (Cuu Tu, Fire), Dong = 7 (That Tich, Metal), Tay Nam = 6 (Luc Bach,
   Metal), Nam = 4 (Tu Luc, Wood), Bac = 2 (Nhi Hac, Earth), Dong Nam = 8 (Bat Bach,
   Earth).
3. **Add the annual and monthly flying stars.** The annual star changes at Lập Xuân, not
   at Tet; the monthly star changes at the twelve solar terms. [21] computes the 2026
   annual star as Nhat Bach entering the centre, and the October 2026 monthly star as Cuu
   Tu entering the centre.
4. **Read the sơn tinh and huong tinh**, which requires the house bearing in **degrees** to
   place the house in the correct one of the 24 son. This is why section 1.1 asks for a
   degree bearing and not just a compass name.
5. **Read the cung.**

**The two limits that matter here.** First, [21] itself separates the three layers and
warns against combining them into a single score: the **van layer** describes the
structure of the house, the **20-year comparison layer** is the context, and the
**annual and monthly flying stars** are the moving parts. Second, [21] does **not**
conclude cat/hung from the star combination, and does **not** offer a hoa giai (remedy)
procedure; [21] states plainly that it does not use the year-month-son-direction-van
combination to draw a cat/hung conclusion or to prescribe a remedy. A practitioner who
offers a single "your house is 7 stars" score has gone beyond what this layer claims.

**What it is good for, once the owner knows the year of completion and the bearing.** It
explains **why** two houses with the same floor plan and different completion years are
read differently, which Bat Trach cannot do at all. It is also the layer that would
justify the roof-terrace and light-well treatment in P-24 and P-25 (the position of the
lift head and the water tank are read as cells on the roof chart).

**Cost and honesty.** A Phi Tinh reading is a *whole-system* calculation from a
construction date and a degree bearing - it is not a set of interior tweaks, and it does
not produce a list of things to buy. For a house whose facing direction is not even known
yet, it cannot be done. **Recommendation: do not commission a Phi Tinh reading until the
compass bearing has been taken and the completion date is fixed.** If the owner then
wants one, it should be done as a standalone layer, reported separately, and it should
not be allowed to override anything in section 5 of this document.

---


## 5. Conflicts with safety and design

Every row is a phong thuy suggestion that a practitioner might make, and what it costs
in safety or design terms. **The verdict column is the recommendation of this review.**

| # | phong thuy suggestion | safety or design cost | verdict |
|---|---|---|---|
| 1 | Move the stair out of the middle of the house | the stair is the only escape stair in a 5-storey house; moving it means re-planning every floor, the lift shaft, the structure and the fire strategy | **SKIP** - the position is structural. Mitigate instead: keep the under-stair space open and lit (P-06) |
| 2 | Move the rear WC off the bedroom above it | the WC stack is shared with the drainage riser and the party-wall plumbing; relocating it means re-running the stacks and re-dimensioning every floor | **ADOPT A CHEAPER VARIANT** - keep the position, but (a) duct the fan outside, (b) add a 300-450 mm service plenum under the bedroom slab **if it is still possible**, (c) fit an acoustic WC door, (d) keep the bed off the WC wall (P-15, P-18) |
| 3 | Put the altar in the rear of the top floor instead of the front | the front zone of the 5th floor is the only place with a balcony and the only place the drawing gives a dedicated room; the rear of that floor is the rear bedroom and the lift head | **SKIP** the move; **ADOPT** the rotation - put the altar against the party or stair-side wall, off the WC wall and off the front glazing, facing a good direction (P-21, P-23) |
| 4 | Narrow a door leaf to land on a better Lo Ban cung | door clear width is an egress and accessibility matter; the bedroom doors are on the escape route | **SKIP** any narrowing. Where a ruler change is compatible with the required clear width (internal leaves, WC leaf), it is free, so **ADOPT** it there and nowhere else (P-32) |
| 5 | Duct the WC exhaust into the stair light well | the stair is the sole escape route; pushing bathroom air into it is a smoke and odour hazard | **SKIP** - this is a safety matter and safety wins. Fan goes outside (P-15) |
| 6 | Put a mirror at the top of the facade to deflect a neighbour sha | a mirror on a 5-storey facade is a glare source for the neighbours, a heat gain, and a fall hazard during cleaning | **SKIP** the mirror. Use planting or a screen, which the tradition also accepts (P-27) |
| 7 | Screen the stair lobby to break the door-stair line | the screen must not obstruct the stair discharge or reduce the egress width | **ADOPT A CHEAPER VARIANT** - screen the lobby, not the stair, and not the discharge (P-03, P-06) |
| 8 | Put a fish tank or a rockery under the stair (the classic folk remedy) | water and loose rock next to the sole escape stair is a slip, a leak and a load problem | **ADOPT A CHEAPER VARIANT** - a planter with robust, low, non-shedding plants and no water basin; the *tradition* only wants the space open and interesting, not specifically a pond (P-06) |
| 9 | Convert the U-return stair to a spiral (if the owner misreads the rule) | spirals are worse for the actual users, especially older people and children, and the winder geometry is already the stair weak point | **SKIP** - and see P-07: the rule is against spirals, not for them |
| 10 | Close the stair light well for tidiness, or leave it unglazed for a better view | the glass light well on the terrace has no stated load rating and no fall protection; the stair is the escape route | **SKIP** both - the safety review must resolve the glass light well load rating and fall protection. Keep the frame intact (P-11) |
| 11 | Add planters to the roof terrace | a permanent load on a roof slab in a building whose roof waterproofing is barely annotated; the terrace edges have no balustrade note | **ADOPT A CHEAPER VARIANT** - light planters only, positioned with the engineer approval, away from the drainage arrows and the lift overrun (P-24, P-25) |
| 12 | Move the water tank to the plot centre (the [32] advice) | a water tank is a permanent load; the plot centre here is the core, which carries the stair and the lift | **SKIP** the centre placement for this house. Put the tank on the rear roof, away from the lift overrun and the light wells, and note the cung question for the practitioner (P-24) |
| 13 | Widen or narrow the frontage to a lucky number | the frontage is the plot and the party walls | **SKIP** - and note the trader practical rule is already satisfied (P-31) |
| 14 | Enclose the front yard with a solid screen to stop the incoming qi | the front yard is the plot only cross-ventilation path to the ground floor, and a solid screen would block the garage ventilation | **ADOPT A CHEAPER VARIANT** - a slatted or planted screen at the sides, not a solid wall across the width (P-01, P-02) |
| 15 | Change the door swing on the WC so it does not face the bed | the WC door is the only route between the ensuite and the bedroom it serves, so it is also that bedroom escape door | **ADOPT** with a variant that preserves the opening width: a swing change or a pocket/sliding door rather than a narrowed door (P-17) |
| 16 | Add a service plenum under the WC slabs to separate them from the bedrooms above | it costs slab depth and headroom, and every millimetre of ceiling height is already tight at 3200-3400 mm storeys | **ADOPT ONLY IF THE SLABS ARE NOT YET BUILT** - the decision has a hard deadline; after that it is impossible. If the slabs are already cast, the free fallbacks (fan, acoustic door, bed position) apply (P-15) |
| 17 | Choose an auspicious date for the topping-out and move-in | delaying the move-in costs nothing but inconvenience; delaying the breaking ground costs site time | **ADOPT** if the owner wants it - but only as the last layer, on top of the interior decisions, and never as a reason to move the building (section 4.3) |
| 18 | Fit a feng shui object (mirror, crystal, coin, talisman) in each room to correct a bad direction | cost, clutter, and in some cases glare and objects that become a cleaning problem | **ADOPT A CHEAPER VARIANT** - the tradition own first remedies are physical: re-orient, re-screen, plant, light. Use the physical remedies first and treat objects as optional; this report recommends **skipping** objects entirely, because the sources used here are the ones that argue for the physical measures |

---

## 6. Plain-English summary for a skeptical but respectful owner

### 6.1 The eight cheap things worth doing

None of these cost more than a day work or a modest amount of money, and none of them touch
the structure. All are in the tradition own preferred remedies, and every one of them has a
plain practical reason as well.

1. **Put the bed head against the party wall, not against the WC wall, and turn it so no
   beam is over the sleeper head.** The bed is furniture. This costs nothing, it is free
   to change at any time, and it is the single highest-value phong thuy action available
   in this house - because the party wall is solid and silent and the WC wall is neither.
   (P-18, P-19, P-20)
2. **Rotate the altar in the prayer room so it faces one of your four good directions, and
   keep it off the WC wall and off the front glazing.** Also free, and it is the tradition
   *toa cat huong cat* rule, the most-cited Bat Trach instruction after the house
   direction itself. (P-21, P-23)
3. **Keep the front yard open.** It is 3.5 m deep and it is the only place air can enter
   the ground floor. No carport, no big storage box, no solid gate screen across the
   width. (P-02)
4. **Screen the stair lobby from the entry axis** - a planter, a slatted screen, or a
   solid balustrade panel at the core entrance. This is the tradition remedy for the
   door-stair clash, and it happens to be the right answer to the draught and the noise
   from the core as well. (P-03)
5. **Keep the under-stair space open, lit and interesting** - a bench, a planter, a
   washing area - rather than a cupboard. The tradition calls a closed under-stair store
   the worst thing you can do to a house centre; in a 5-storey tube house it is also the
   biggest dust trap and the fattest fire load. (P-06)
6. **Turn the hob on the kitchen counter** so that you stand with your back to one of
   your good directions, and keep at least 600 mm of solid worktop between the hob and
   the sink. (P-13, P-14)
7. **Change the WC door swing (or use a pocket door) so the WC door is not in line with
   the bed.** This has to be decided before the doors are ordered, and it is the change
   that most improves the actual privacy of the ensuite. (P-17)
8. **Take the compass bearing of the facade** - five minutes with a phone - and keep the
   front yard planting low and to the sides. The bearing unlocks the whole of the Bat
   Trach table for your family; the low planting is the tradition own answer to a
   neighbour sharp parapet corner. (section 1.1, P-27)

**One more that is free if it is decided now and impossible later:** the door leaf sizes.
Internal leaves at **810 mm** instead of 900, the WC leaf at **760 mm** instead of 700,
and the main door clear opening nudged 10-100 mm, all land on better Lo Ban cung at no
cost. It changes nothing measurable about the house - which is exactly the point. It is a
free gesture, not a fix. Do not narrow a door that the escape route needs. (P-32)

### 6.2 The four expensive things to ignore unless the owner cares deeply

1. **Moving the stair out of the middle of the house.** The tradition most emphatic
   prohibition and the reason this house is the most difficult by the tradition own
   standard. It is also a single escape stair in a five-storey building. Moving it would
   cost more than the rest of the phong thuy budget put together and would have to be
   re-drawn by the architect and the structural engineer. **Ignore it.** The mitigation
   (an open, lit under-stair space) is free. (P-06)
2. **Relocating the WCs so none sits under a bedroom.** The second-most-cited
   prohibition, and genuinely serious in the tradition terms. But the drainage and
   plumbing stacks are shared with the party walls, and re-running them means
   re-dimensioning every floor. The cheap mitigations - outside-vented fan, acoustic
   door, bed away from the wall, and a service plenum if the slabs are not yet cast - get
   most of the benefit for a fraction of the cost. **Ignore the relocation; do the
   mitigations.** (P-15)
3. **Moving the altar room to the rear of the top floor.** The 5th floor front zone is
   the only dedicated room the drawing offers, and the rear of that floor is the rear
   bedroom and the lift head. Rotating the altar inside the room satisfies the actual
   rule for about 1 % of the cost. **Ignore the move.** (P-21)
4. **Commissioning a full Phi Tinh chart, or buying remedies.** A Phi Tinh reading is a
   whole-system calculation from a completion date and a degree bearing - it is not a
   shopping list, and [21] (the source used here) explicitly declines to draw cat/hung
   conclusions or prescribe remedies from the star combination. It also cannot be done at
   all until the compass bearing is known. The tradition own first remedies are
   physical - re-orient, re-screen, plant, light - and they are the ones this report
   recommends. **Ignore the chart and the objects** unless the owner wants them for their
   own sake, and never let them override the physical measures. (section 4.4)

### 6.3 What a skeptical owner should take away anyway

The tradition has a reputation for vagueness, and much of what it says cannot be tested.
But strip it down and this house phong thuy reading is largely a **daylight, ventilation
and privacy** brief wearing older clothes:

- Keep the front yard open because it is the air supply.
- Keep the under-stair space open because it is dead space.
- Put the bed head on the solid wall because the other wall has a WC behind it.
- Keep the bedroom above the WC ventilated because the WC is below it.
- Break the line from the door to the stair because a straight line through the middle of
  a 25 m plan carries draught, noise and sight.
- Put the altar at the quiet end of the quietest room because that is where you would put
  it anyway.
- Turn the stove so the cook faces into the house rather than at a wall.

Where the tradition and the building science agree, follow both. Where they do not - the
mirror on the facade, the fish tank under the escape stair, narrowing a door - **safety
wins**, and this report says so in each case rather than hedging.

### 6.4 The three things this review could not determine

Stated plainly, because they change the answer:

1. **The facing direction.** No north arrow on the scanned ground-floor sheet, none in
   the transcripts, and the compass glyph on the stamped approval sheet is unreadable at
   its resolution. Every direction-dependent recommendation in this document is therefore
   conditional on the five-minute measurement in section 1.1.
2. **Whether a passenger lift exists below the roof.** The label *O ky thuat thang may*
   appears once, on the roof sheet; no residential floor plan labels a shaft, and the
   model in designs/contractor-as-drawn.json infers it. The lift-related findings
   (P-10, P-24, P-25) are conditional on that inference being confirmed.
3. **The order of the WC and the kitchen on the ground floor.** The phone-photo transcript
   and the earlier PDF read disagree; the bands are the same size either way, so the
   kitchen findings (P-13, P-15) are stated conditionally rather than picked silently.

---


## 7. What the sources agree on (5 bullets)

1. **The Bat Trach eight-cung table.** Four independent Vietnamese sources and one
   Chinese-language reference give the same Sinh Khi / Thien Y / Dien Nien / Phuc Vi /
   Tuyet Menh / Ngu Quy / Luc Sat / Hoa Hai assignment for all eight cung. Where they
   differ is only the *ranking inside* the four good directions, and the sources say so
   themselves. The one dissenting year-table found ([5]) disagrees on the cung for both
   sexes and is treated here as the outlier, not the standard.
2. **The Dong tu / Tay tu group split and its consequence.** The four good directions
   of any Dong tu owner are always Bac, Nam, Dong, Dong Nam; of any Tay tu owner, always
   Tay, Tay Bac, Tay Nam, Dong Bac. Every source agrees, and the Chinese reference states
   it as the geometric proof of the whole system.
3. **The stair must not be in the middle of the house.** Every source that mentions the
   stair says this, with the same corollaries (not in line with the main door, not at the
   rear of the house, not a spiral, not open-riser, no WC under it). It is the most widely
   held rule in the Vietnamese stair literature and it is also the one this house breaks
   most completely.
4. **The altar must not be under a stair, opposite a WC door, or under a beam, and should
   be on the top floor facing a good direction.** Universal across the folk and the Bat
   Trach sources, and the one part of the tradition where the rule and the room actual
   use of the space agree.
5. **A WC above a bedroom is a serious fault, and a WC at the front of the house or under
   the stair is worse.** The two WC prohibitions that recur most are the rear position and
   the storey above; the sources disagree on how much each costs, not on whether they
   matter.

---

## 8. Where schools disagree, or where the sources are thin

1. **The cung phi formula and one dissenting year-table.** The 11 - d / d + 4 digit-root
   method (or the equivalent 10 - r / 5 + r shortcut) is used by [1], [2], [3] and [19].
   [5] publishes a different method and a year-table that disagrees for both sexes in
   every year checked. Not used here. If the owner is given a table that contradicts
   section 2.2, that table is the one in error.
2. **The 42.9 cm ruler cung names, and the 38.8 cm ruler cung count.** The 42.9 cung set
   is given as Tai-Benh-Ly-Nghia-Quan-Kiep-Hai-Ban by [39] and [40], as
   ...-Nan-Hai-Mang by [38], as ...-Kiep-Hai-Mang by [41], and [42] gives the 42.9 ruler
   the 38.8 ruler cung set entirely. The 38.8 ruler is 10 cung in [38], [43], [7] and [4];
   other schools print 8. The good/bad pattern is stable; the names are not.
3. **The zero point on the 42.9 and 38.8 rulers** (P-29, dispute 3). Several readings in
   section 3.10 flip between good and bad depending on the convention, and each such case
   is flagged in place. **Any buyer of a physical ruler should check the reading against
   the ruler in hand** - and note [7] warning that Vietnamese 38.8 cm rulers are often
   printed 2 mm off the Chinese original.
4. **The kitchen hung direction** - whether the relevant direction is the cook back or
   the stove mouth. [1] names both readings and tells the reader to pick one.
5. **Whether the front yard should be open or screened**, and whether the altar position
   inside a room is governed by the owner cung or only by the rules about WC walls and
   beams. [1] and [3] treat the cung rule as primary; the folk sources treat the
   WC-and-beam rules as primary and the cung as a refinement.
6. **Whether a full-height shaft is a leak (thung khi) or a ventilation spine.** The
   disagreement is explicit: [10] treats the stair - also a vertical void - as the house
   qi-gathering element while forbidding it in the middle. Treated here as CONTESTED, and
   the remedy given is the version both readings can accept (a screen at the shaft
   opening), which is also the right answer for smoke and sound.
7. **The sat khi mechanism** - shape, flow, or visual provocation. The traditional sources
   split three ways and only the third has any support outside the tradition.
8. **The luc hao house-form labels** and their tr truong sinh steps ([10]). The label set
   varies; the rule applied here is the one the source states directly for the rectangular
   flat-roofed form, and it happens to favour the stair this house already has.
9. **The master bedroom position.** No source states a front/rear rule; the tradition own
   logic (the quietest room) is used, and labelled CONTESTED.
10. **Where the tradition is genuinely thin.** The following were **NOT FOUND** in any
    source that met the evidence bar: any rule about the specific 3.9 m frontage as a
    number; any rule about a 5-storey house floor count as such; any rule about a house
    with both a mezzanine and a roof terrace; any rule about the house party walls as
    such (only the courtyard version in [23] and [37]); any rule about a lift position in
    a tube house; and any published Vietnamese cung table for the year 2038+ or for the
    2000+ formula stated as a table rather than a formula. The last of these is why section
    2.1 gives the **formula** rather than a year-table: the formula is verifiable and
    survives past the last printed table.

---


## 9. Sources

Labels: **VERIFIED** = source seen with URL and access date, and the specific claim read in
it. **PARTIAL** = the source was read but supports only part of the claim, or the source
itself marks something as uncertain. **CLAIMED** = a single practitioner or site asserting
it, not corroborated. **UNVERIFIED** = a lead found in search results but not opened, so it
is cited as a lead only and never counted as evidence.

**Vietnamese and English-language practitioner and reference sources**

1. Gio Hoang Dao, *Cung phi Bat Trach: cach tinh cung phi va chon huong nha hop tuoi* -
   https://giohoangdao.vn/index.php/kien-thuc/cung-phi-bat-trach-huong-nha.html - accessed 2026-10-22 - **VERIFIED**: the full 8-cung x 8-direction table (Cung / Sinh Khi / Thien Y / Dien Nien / Phuc Vi / Tuyet Menh / Ngu Quy / Luc Sat / Hoa Hai) read from the page own HTML table; the cung phi formula with the 2000 breakpoint; the Dong tu / Tay tu split; the statement that the middle-star ranking varies between books; the kitchen and altar direction rules; the kitchen-direction reading dispute (cook back vs stove mouth); the 1990 / 1992 worked example.
2. Am Lich VN, *Xem huong nha theo cung phi (Bat trach)* -
   https://www.amlichvn.net/xem-huong-nha/ - accessed 2026-10-22 - **VERIFIED**: the formula *nam 11 - n, nu n + 4* with the number 5 going to Khon for men and Can for women; the eight cung names and numbers; and an explicit statement that Bat Trach has no scientific basis and that safety, structure, light and ventilation come first.
3. Cu Tien Sinh / tamlinh.cuthongthai.vn, *Cung phi (hay cung menh)* -
   https://tamlinh.cuthongthai.vn/blog/cung-phi-huong-nha - accessed 2026-10-22 - **VERIFIED**: the eight-cung table split into two four-column tables (Dong tu and Tay tu) read from the page HTML tables; the (100 - last two digits) / 9 and (last two digits - 4) / 9 formulas; the number-5 handling; the applications table (door / stove / bed head / altar / desk).
4. Akisa, *Thuoc lo ban: tra cuu online & cach do chuan xac nhat* -
   https://akisa.vn/thuoc-lo-ban - accessed 2026-10-22 - **VERIFIED**: the complete 40-row numeric table for the 52.2 cm ruler (all eight cycles, all forty sub-cung positions) read from the page HTML table; the 42.9 cm and 38.8 cm cung structures and sub-cung widths; the measured door-width example (82 cm -> 81 cm).
5. Meo Beo Studio, *Cung phi bat trach la gi? Cach tinh Dong tu menh - Tay tu menh va 8 du nien vo chong* -
   https://meobeostudio.com/blog/cung-phi-bat-trach-dong-tu-menh-tay-tu-menh - accessed 2026-10-22 - **PARTIAL / CONTESTED**: its 1985-2005 year-table is a usable lead but its method (reducing the full year, then subtracting 10 for men) disagrees with sources [1], [2], [3] and [19] for both sexes, so the table is **not used** in this report; the Dong tu / Tay tu split and the 8 du nien section are consistent with the other sources and were used as a cross-check only.
6. Cu Tien Sinh, *Su that it nguoi hay: Cua doi cua phong thuy - Hoa giai khi xung* -
   https://cuthongthai.vn/blog/su-that-it-nguoi-hay-cua-doi-cua-phong-thuy-hoa-giai-khi-xung - accessed 2026-10-22 - **VERIFIED (via search extract)**: the *cua doi cua, tat co khau thiet* formula and the remedies (sliding or hidden door, an object between the two leaves).
7. EBM (Cong ty CP Cua SUNSPACE), *Phan biet cac loai thuoc lo ban* -
   https://ebm.com.vn/phan-biet-cac-loai-thuoc-lo-ban/ - accessed 2026-10-22 - **VERIFIED**: which ruler measures what (52.2 = the void / doors and windows; 42.9 = the solid / furniture and building elements; 38.8 = the yin / altar and grave); the note that the 52.2 ruler is rare in Vietnam and that Vietnamese 38.8 rulers are commonly 2 mm off the Chinese original.
8. Tre Nghe, *Thuoc lo ban online cho xay dung va noi that* -
   https://trenghe.vn/thuoc-lo-ban - accessed 2026-10-22 - **VERIFIED**: the 52.2 cm good/bad cung ranges with their meanings (Quy Nhan, Hiem Hoa, Thien Tai, Thien Tai, Nhan Luc, Co Duc, Thien Tac, Te Tuong); the *do thi dung, den thi bo* maxim; the attribution of the three rulers to the void, the solid and the yin.
9. VnExpress, *Bo tri cau thang trong nha theo phong thuy* (10 Apr 2002) -
   https://vnexpress.net/bo-tri-cau-thang-trong-nha-theo-phong-thuy-2831884.html - accessed 2026-10-22 - **VERIFIED**: the rule that the stair must not be in the middle of the house; the rule against the stair in line with the main door; the under-stair space must be kept clear; the stair counts 17, 18, 21, 22; the 90 cm average stair width.
10. VietnamNet, *9 nguyen tac phong thuy cau thang can nho de tranh tan gia bai san* (19 May 2022) -
    https://vietnamnet.vn/9-nguyen-tac-phong-thuy-cau-thang-can-nho-de-tranh-tan-gia-bai-san-2020810.html - accessed 2026-10-22 - **VERIFIED**: the five stair prohibitions (mid-house, in line with the door, at the rear of the house, spiral, open-riser), the no-WC-under-the-stair rule; the Truong sinh cycle with the house-form starting steps and the acceptable stair-count lists per form (including 21 for the Tho form); the 18-riser-per-flight limit; the headroom and tread dimensions.
11. Tuoi Tre (PLO), *Dat cau thang, nhung dieu can luu y de tranh diem xau* -
    https://tuoitre.vn/plo/dat-cau-thang-nhung-dieu-can-luu-y-de-tranh-diem-xau-109409565.htm - accessed 2026-10-22 - **VERIFIED (via search extract)**: the Sinh-Lao-Benh-Tu counting with Sinh as the best final step; the prohibition on a spiral stair in the middle of the house or facing the front door; the plant remedy at the stair inner corner.
12. Dan tri, *Nhung luu y khi dat cau thang trong nha de dam bao phong thuy* -
    https://dantri.com.vn/bat-dong-san/nhung-luu-y-khi-dat-cau-thang-trong-nha-de-dam-bao-phong-thuy-20210131172715801.htm - accessed 2026-10-22 - **CLAIMED**: single site, no corroborating source located for the specific stair-count list.
13. Nhat Nguyet, *Son huong Mao trong phong thuy, cach luan* -
    https://nhatnguyet.org/kien-thuc/bai-viet/son-huong-mao-trong-24-son-huong-phong-thuy-7ec918 - accessed 2026-10-22 - **VERIFIED**: the 24-son structure (360 degrees into 24 x 15-degree divisions; 12 dia chi + 8 thien can + 4 que); the Miao band 82.5-97.5 degrees with its 90-degree centre; the chinh khi / kiem huong division of each son.
14. Nhat Nguyet, *Son huong Binh trong phong thuy* -
    https://nhatnguyet.org/kien-thuc/bai-viet/son-huong-binh-trong-24-son-huong-phong-thuy-y-nghia-va-cach-luan-807afe - accessed 2026-10-22 - **VERIFIED (via search extract)**: the full list of the 24 son names (Ty, Quy, Sui, Can, Dan, Giap, Mao, At, Thin, Ton, Ty, Binh, Ngo, Dinh, Mui, Khon, Than, Canh, Dau, Tan, That, Can, Hoi, Nham).
15. Soi Menh, *Thuoc Lo Ban & Thuoc Dinh Lan - Cach Do & Bang Tra* -
    https://soimenh.vn/thuoc-lo-ban-dinh-lan/ - accessed 2026-10-22 - **VERIFIED**: the 42.9 cm ruler eight cung with their catus/hung classification and their four sub-cungs (Tai / Benh / Ly / Nghia / Quan / Nan / Hai / Mang), and the reminder that a measurement can be good on one ruler and bad on another.
16. The Box, *Thuoc lo ban - Ung dung trong xay dung* -
    https://thebox.com.vn/thuoc-lo-ban-ung-dung-trong-xay-dung/ - accessed 2026-10-22 - **VERIFIED (via search extract)**: the 38.8 cm ruler as ten cung of 39 mm each with four sub-cungs of 9.75 mm, and its cung names (Dinh - Hai - Kho - Nghia - Quan - Tu - That - Tai).
17. Viet Thien Thu, *Cung phi Bat Trach (Quai menh)* -
    https://vietthienthu.com/phong-thuy/cung-phi/ - accessed 2026-10-22 - **VERIFIED**: all eight cung with hinh, phuong vi, nhom, the four good directions with their star names and the four bad directions with theirs - read from the page own listings and agreeing with [1], [3] and [19] cell for cell.
18. Dao Quan, *Bat Trach: bang tam cung phi va cach tra bon huong cat* -
    https://daoquan.vn/bai-viet/bat-trach-bang-tam-cung-phi-va-cach-tra-bon-huong-cat - accessed 2026-10-22 - **VERIFIED**: the cung phi / que trach distinction, the eight-cung four-good-direction table (read from the page HTML table), the statement that a good direction does not make a house bright or ventilated, and the explicit warning against moving a door or a technical route for a single cung.
19. Nine Palace Bagua (Chinese), *Ba Zhai Ji Xong Zong Lan - Ba Fang You Nian Xing Yu Zhai Ming Xiang Pei* -
    https://jiugongbagua.com/fengshui/bazhai/?lang=zh-TW - accessed 2026-10-22 - **VERIFIED**: the per-cung eight-star tables for all eight que, read from the page text; the Dong si / Xi si grouping; the Da You Nian formula (male 11 - d, female d + 4, the number 5 going to Kun for men and Gen for women); and the 1900-2100 year table, which agrees with [1], [2], [3] and [20] on every year checked.
20. Bazi Atlas (Chinese), *Ming Gua Ji Suan Qi - Ba Zhai Dong Xi Si Ming Yu Ba Fang Wei You Nian Xing* -
    https://bazi-atlas.com/zh/kua-number-calculator - accessed 2026-10-22 - **VERIFIED**: the 64-cell ming-zhai matching table (ming que down the side, zhai que across the top), read from the page HTML table, which agrees with the per-cung readings of [19].
21. Santa Lich, *Huyen Khong Phi Tinh - Tam Nguyen Cuu Van* -
    https://amlich.santajsc.vn/huyen-khong-phi-tinh.html - accessed 2026-10-22 - **VERIFIED**: the van determination from the completion date (2026 = Van 9, 2024-2043, CUU TU with Hoa in the centre); the Lo Shu anticlockwise star placement; the annual star at the 2026 Lich Xuan boundary and the monthly star at the October 2026 term; the statement that the system is kept independent of Bat Trach and does not read cung phi; and the explicit statement that it does not combine year, month, son, direction and van into a cat/hung conclusion or a remedy.
22. Phong Thuy Vuong, *Cach hoa giai loi phong thuy Xuyen Tam Sat khi cua va cong truc xung nhau* -
    https://phongthuyvuong.net/phong-thuy/cach-hoa-giai-loi-phong-thuy-xuyen-tam-sat-khi-cua-va-cong-truc-xung-nhau-615.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: the qualified form of the *xuyen tam sat* rule - that it only bites when the qi path is unobstructed from front to back - and the screening remedies.
23. Dogooccho.com.vn, *15 Kieng Ky Khi Lam Cua Nha Va Cach Hoa Giai* -
    https://dogooccho.com.vn/kieng-ky-khi-lam-cua-nha - accessed 2026-10-22 - **CLAIMED**: commercial site, single source: the *cua chinh doi dien nha ve sinh* rule and its reading of the front door as receiving pure qi while the WC releases ue khi; the screening remedies.
24. VietnamNet, *Nhung sai lam thuong gap ve phong thuy khi dat bep* -
    https://vietnamnet.vn/nhung-sai-lam-thuong-gap-ve-phong-thuy-khi-dat-bep-760851.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: the rule against the stove under or in front of a window; the worktop-between-hob-and-sink remedy; the *xa nha tren bep* rule.
25. VTC News, *Nhung kieng ky trong phong thuy nha bep* -
    https://vtcnews.vn/nhung-kieng-ky-trong-phong-thuy-nha-bep-ar220904.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: the stove not directly facing the main door; the separation remedies (worktop, island, screen, curtain); the *hoa khac thuy* reasoning for keeping the stove away from water storage and the WC.
26. Noi That Phu Quy, *Nhung dieu kieng ky va cach hoa giai khi dat giuong ngu* -
    https://noithatphuquy.com.vn/phong-thuy/nhung-dieu-kieng-ky-va-cach-hoa-giai-khi-dat-giuong-ngu--/144-305-87.aspx - accessed 2026-10-22 - **VERIFIED (via search extract)**: *huyen tram sat* for a beam over the bed head and the shift-the-bed remedy; the bed head against a solid wall, not against a kitchen or bathroom wall; the mirror rule.
27. Cu Tien Sinh, *98% Gia Chu Khong Bien: 5 Kieng Ky Cua Chinh Hut Van Xui* -
    https://cuthongthai.vn/blog/98-gia-chu-khong-biet-5-kieng-ky-cua-chinh-hut-van-xui - accessed 2026-10-22 - **VERIFIED (via search extract)**: the *cua doi cua, tat co khau thiet* formula; the sliding / hidden door remedy; the requirement that the main door be open and airy.
28. SHAC, *Tu van vi tri dat giuong ngu theo phong thuy* -
    https://shac.vn/tu-van-vi-tri-dat-giuong-ngu-theo-phong-thuy-va-cac-nguyen-tac-can-luu-y - accessed 2026-10-22 - **VERIFIED (via search extract)**: the bed head against a solid wall, not against a kitchen or bathroom wall; no mirror facing the bed head.
29. Kien truc DMC, *Nhung dieu nen tranh trong phong thuy giuong ngu* -
    https://kientrucdmc.com/tranh-trong-phong-thuy-giuong-ngu/ - accessed 2026-10-22 - **VERIFIED (via search extract)**: the bed-head-under-a-beam rule and its stated symptoms; the mirror rule.
30. VTC News, *Cach chon huong dat giuong trong phong thuy giuong ngu* -
    https://vtcnews.vn/cach-chon-huong-dat-giuong-trong-phong-thuy-giuong-ngu-ar743960.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: the bed head against a solid wall; avoiding dark corners and closed, still air; the mirror rule.
31. Phong Thuy Dai Nam, *Moi dieu can biet ve xa ngang trong phong thuy nha o* -
    https://phongthuydainam.vn/vi/tin-tuc/xa-ngang - accessed 2026-10-22 - **VERIFIED (via search extract)**: *huyen tram sat* defined as a beam cutting across the head or body of the sleeper; the rule against a beam over the altar table; the beam-over-the-kitchen rule.
32. VnExpress, *Vi tri dat be nuoc theo phong thuy* -
    https://vnexpress.net/vi-tri-dat-be-nuoc-theo-phong-thuy-4482029.html - accessed 2026-10-22 - **VERIFIED**: the *dao hoa phiem thuy* rule for a tank in the Doai (West) cung; the *thuy khac hoa* rule for the Ly (South) cung; and the general advice to place the tank in the trung cung.
33. 3TA Architecture, *Thiet ke phong tho hien dai va cach dat ban tho tranh cung xau* -
    https://kientruc3ta.com/vi-tri-dat-ban-tho-phong-thuy - accessed 2026-10-22 - **VERIFIED (via search extract)**: the altar room ideally on the top floor, away from the bedroom, kitchen and WC; the acknowledgement that a dedicated room is not always possible in a nha ong.
34. Ban Tho Da Nang, *Cach bo tri phong tho chuan phong thuy cho nha ong* (27 Feb 2023) -
    https://banthodanang.vn/tu-van/cach-bo-tri-phong-tho-chuan-phong-thuy-cho-nha-ong-tai-ban-tho-da-nang/ - accessed 2026-10-22 - **VERIFIED**: the five altar prohibitions (not facing the house direction, not under a beam, not opposite a door, not near the kitchen / WC / bedroom, not in direct sun or wind); the Lo Ban cung references for altar sizing; and the two legitimate arrangements for a nha ong, including the altar in the living room with a partition or curtain.
35. Noi That Diem Nhan, *Ban tho xung voi cua la nhu the nao? Co vi pham phong thuy khong?* -
    https://noithatdiemnhan.vn/ban-tho-xung-voi-cua-la-nhu-the-nao/ - accessed 2026-10-22 - **CLAIMED**: commercial site, single source: the rule that there should be no WC behind the altar and the reasoning about ue khi collecting there.
36. VietnamNet, *Nguyen tac vang cho phong thuy phong tho* -
    https://vietnamnet.vn/nguyen-tac-vang-khi-chon-vi-tri-dat-ban-tho-mang-tai-loc-cho-gia-chu-800138.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: the placement rules for the altar in a house, the prohibition against the altar being opposite a WC or under a beam.
37. Phong Thuy Minh Tuan, *Goc Nhon Chieu Thang Cua Chinh - Sat Khi Khien Gia Dinh De Bat Hoa* -
    https://phongthuyminhtuan.com/goc-nhon-chieu-thang-cua-chinh-sat-khi-khien-gia-dinh-de-bat-hoa/ - accessed 2026-10-22 - **CLAIMED**: single practitioner: the *tiem giac sat* form of the sharp-corner rule and the remedies (removing the point, screening, planting).
38. Hieu.asia, *Thuoc Lo Ban - 4 loai thuoc va cac cung tot xau* -
    https://hieu.asia/learn/thuoc-lo-ban - accessed 2026-10-22 - **VERIFIED**: the four rulers with their cycle, cung count and sub-cung width (52.2 / 42.9 / 38.8 and a fourth); the explicit warning that choosing the ruler to hear what you want makes the numbers meaningless; and the worked example showing 120 cm bad on 42.9 and good on 38.8.
39. Congdesign and Go Vi (two Vietnamese pages giving the same 42.9 table) -
    https://congdesign.vn/thuoc-lo-ban/ and https://govi.vn/thuoc-lo-ban-la-gi-nguon-goc-va-cach-su-dung/ - accessed 2026-10-22 - **VERIFIED (via search extract)**: the 42.9 cung order Tai - Benh - Ly - Nghia - Quan - Nan - Hai - Mang, the 53.625 mm cung length, and the four good cung named Tai, Nghia, Quan, Ban.
40. Bofii, *Bang tra cu the cua thuoc lo ban 42,9 hay con goi thuoc 43* -
    https://www.boffi.vn/2019/07/bang-tra-cu-cua-thuoc-lo-ban-429-hay.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: the 42.9 cycle length and the cung order Tai - Benh - Ly - Nghia - Quan - Kiep - Hai - Ban.
41. Namoc, *Kim Lau, Hoang Oc, Tam Tai* -
    https://nhamoc.net/kim-lau-hoang-oc-tam-tai/ - accessed 2026-10-22 - **VERIFIED (via search extract)**: the three checks as the folk literature frames them - Kim Lau for the person (tuoi mu divided by 9, remainder 1, 3, 6 or 8), Hoang Oc for the house (six cung), Tam Tai for the year van (the con giap); and the note that 2026 corresponds to the Hoi - Mao - Mui group.
42. Thac Nuoc Phong Thuy, *Huong dan dat ban tho Phat theo phong thuy* -
    https://thacnuocphongthuy.vn/ban-tho-phat-theo-phong-thuy/ - accessed 2026-10-22 - **VERIFIED (via search extract)**: the 42.9 cm cung as eight bands of 5.3625 cm and the altar-table sizing method. **Its cung-name set differs from [39]/[40] and is listed here as a documented disagreement, not as a competing table.**
43. Thanh Tung Glass, *Thuoc Lo Ban Online 52.2 / 42.9 / 38.8* -
    https://thanhtungglass.com/thuoc-lo-ban - accessed 2026-10-22 - **VERIFIED**: which ruler measures which element; the good-cung lists per ruler; and the *so dep* door-width list (75, 81, 107, 127, 133, 153, 186, 212, 233 cm) with their cung names.
44. PS Window, *Kich thuoc cua di 2 canh nhom kinh chuan phong thuy nhat* -
    https://pswindow.vn/kich-thuoc-cua-di-2-canh-nhom-kinh.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: the 52.2 ruler as the only one used for door and window clear openings; the worked division example (1500 / 522 = 2 remainder 456, cung Hai, bad) and the rule that only the clear opening is measured.
45. Tu Vi Hoi Quan, *Cach tinh han Tam Tai, Kim Lau, Hoang Oc chuan xac nhat* (13 Jun 2026) -
    https://tuvihoiquan.vn/blog/cach-tinh-tam-tai-kim-lau-hoang-oc/ - accessed 2026-10-22 - **VERIFIED**: the four tam-tai group tables and their three-year sets; the Kim Lau division rule with the meaning of each remainder (1, 3, 6, 8); and the Hoang Oc six-cung cycle from age 10 with the good cung at 10, 20, 40 and the bad at 30, 50, 60.
46. VTC News, *Bang tinh Tam tai, Hoang oc, Kim lau nam 2026 moi nhat* -
    https://vtcnews.vn/bang-tinh-tam-tai-hoang-oc-kim-lau-nam-2026-ar997017.html - accessed 2026-10-22 - **VERIFIED (via search extract)**: 2026 as the first year of tam tai for the Hoi - Mao - Mui group, and the per-year tables for 2026.
47. Huyen Co, *Tuoi Kim Lau, Tam Tai, Hoang Oc: cach tinh* -
    https://huyenco.vn/kien-thuc/xem-ngay/tuoi-kim-lau-tam-tai-hoang-oc - accessed 2026-10-22 - **VERIFIED (via search extract)**: the Kim Lau remainder rule, the Tam Tai three-year groups, and the statement that tam tai begins with the year whose earthly branch opposes the head of the group.
48. Nine Palace Bagua / Bazi Atlas, the Lo Shu 9-star structure and the Later Heaven bagua direction table -
    https://jiugongbagua.com/fengshui/bazhai/ and https://bazi-atlas.com/zh/kua-number-calculator - accessed 2026-10-22 - **VERIFIED**: the Later Heaven bagua direction assignments (Kham north, Can north-east, Zhen east, Xun south-east, Li south, Kun south-west, Dui west, Qian north-west) and the trigram element, family and animal correspondences.
49. Wikipedia, *Ba Gua* - https://en.wikipedia.org/wiki/Ba_Gua - accessed 2026-10-22 - **VERIFIED (secondary reference)**: the Later Heaven arrangement and the trigram correspondences only; not used for the Eight Mansions star table.

**Leads located but NOT opened, and therefore NOT counted as evidence** (listed because the
brief asks for them to be recorded): amlichvietnam.vn, vugioi.com, danguyencong.com,
phongthuy.khosachquy.com, xemboituvi.nexttop.org, blogphongthuy.com, 51wendang.com,
20579026.s21i.faiusr.com, scribd (24-son and Bat Chu Thu documents), and the SEO
*thuoc lo ban online* tool pages other than the ones opened above (loban.info.vn,
thuoclobanonline.com, ola88.com, lichdo.vn, vanthienlong.com, lka.com.vn,
kientrucnhacuagio.com, entercons.vn, namthinhphat.vn, thanhtungglass sibling pages). Several of
these copy one another and were therefore excluded from the evidence base under the brief
rules.

**Project documents relied on** (all read, all local):

- contractor/scan-2026-10-22/transcript-architecture.md - the nine architecture sheets.
- contractor/scan-2026-10-22/transcript-foundation-stairs.md - the foundation, lift-pit and stair sheets.
- contractor/scan-2026-10-22/transcript-beams-slabs.md - the beam and slab sheets.
- designs/contractor-as-drawn.json - the reconstructed model; used for the room rectangles, the opening list and the site context (neighbour heights).
- designs/contractor-as-drawn.measurements.md - the per-floor dimension tables and the core note.
- designs/contractor-as-drawn.fidelity.md - the fidelity ledger, in particular (a) the tapered plot, (b) the glazed light well over the stair, (c) the **inferred** lift shaft, (e) the balcony treatment, and the provenance note recording that the compass glyph on the stamped approval sheet is unreadable.
- _scan1022/loban.py - the Lo Ban lookup script used for every cung reading in section 3.10.

---

*End of review. 32 findings, P-01 to P-32. Section 5 lists 18 phong thuy suggestions with
their safety and design cost and a verdict on each; section 6.1 lists the 8 cheap fixes and
section 6.2 the 4 expensive ones to ignore.*

