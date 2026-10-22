# -*- coding: utf-8 -*-
"""Part A: corrections banner, section 0, section 2.2 group-split fix."""
from fixlib import E, INS


CORRECTIONS = """## Corrections 2026-10-22

The first pass took the room positions from `designs/contractor-as-drawn.json`. That
reconstruction is **superseded by the scan**; the caller checked the photographs. The
three transcripts in `contractor/scan-2026-10-22/` are now the only authority for where
each room is. This pass rewrites the affected findings against those transcripts. The
previous text is kept verbatim in `_scan1022/out-phongthuy.before-fix.md`.

- **The altar room P. Thờ is on tầng 4 (+13.800), not on tầng 5.** It is the **front**
  room of tầng 4, behind the front balcony (ban công, door D5, window S1). Behind it is
  **P. Đọc sách** (reading room), separated by a **thin partition**; behind that a **WC
  with a light well**, then the stair, the lift, the rear bedroom P. Ngủ, a rear WC and
  the rear loggia. **The WC is not against the altar room wall.** (IMG_9976, sheet KT05.)
- **Tầng 5 (+17.200, KT06) has no rooms.** It is a stair/lift lobby (doors D6, D7), a
  glazed stair light well and two open terraces (sân thượng) at front and rear.
  (IMG_9977.)
- **The lift exists.** A lift shaft is drawn on every plan (1800 x 1600) with a pit detail
  sheet; the roof carries an *ô kỹ thuật thang máy*; the section shows a car at every
  floor. Only the exact size conflicts between sheets, which is a design-lane matter.
  Every statement that the lift is "only inferred" is withdrawn. (IMG_9972-9978,
  IMG_9987, IMG_9988.)
- **The ground floor is now known:** front yard -> garage -> P. Khách -> stair + lift ->
  **P. ăn + bếp** (in the 4500 band beside the core) -> **rear WC** (in the 1600 band at
  the rear, door D2 to the rear yard) -> rear yard. The earlier "WC then kitchen" reading
  is withdrawn. (IMG_9972.)
- **The rear WC band is at the very rear, not under the rear bedroom.** On tầng 2-4 the
  rear bedroom (the 4500 band) sits over the **kitchen** band; the rear WC (1600) has the
  rear loggia above it and the tầng 5 rear terrace above that. The tradition's sharpest
  prohibition (WC above a bedroom) therefore **does not bite in this house**. (IMG_9972,
  IMG_9974, IMG_9975, IMG_9976, IMG_9977.)
- **P-21, P-22 and P-23 are rewritten** for the real tầng 4 layout, including what a
  top-floor altar could be and what it would cost in weather, fall protection and load.
- **§2.2's East/West group note is corrected.** Tây, Tây Bắc, Tây Nam *and* Đông Bắc are
  all good for the whole Tây group and bad for the whole Đông group; the eight-row table
  above that note was already right and is left unchanged.
- **§6.4 is rewritten.** The lift question and the ground-floor kitchen/WC order are
  settled by the scan; only the **facing direction** remains unknown.
- Every finding, table row, summary line and sources entry that cited a JSON rectangle,
  a millimetre y-range or the superseded model has been rewritten against the
  transcripts, with IMG ids and transcript line numbers. **Finding IDs are unchanged**,
  and findings the scan does not touch are left exactly as they were.

---

"""

INS(11, CORRECTIONS, "corrections-banner", "## 0. Method and evidence limits")


# ------------------------------------------------------------------ section 0

E(20, 26,
  """**What the reviewer could and could not see.** The drawings were read through the three
transcripts in `contractor/scan-2026-10-22/` (`transcript-architecture.md`,
`transcript-foundation-stairs.md`, `transcript-beams-slabs.md`), which are the
**authoritative source for every room position, dimension chain and level** in this
document. The reconstructed spec `designs/contractor-as-drawn.json` and its companion
memos (`designs/contractor-as-drawn.measurements.md`,
`designs/contractor-as-drawn.fidelity.md`) are read only for what the scan does not carry
at all - the site context (neighbour heights) and a few model-only dimensions - and every
use of them is **labelled MODEL** where it appears. **No image was viewed.** Every
drawing fact below is labelled VERIFIED (transcript line), PARTIAL (the transcript itself
says so), or MODEL (superseded reconstruction). See *Corrections 2026-10-22* above for
what the scan changed.""",
  "s0-method",
  "**What the reviewer could and could not see.**")

E(45, 50,
  """- **The ground-floor order is settled: the kitchen is next to the core and the WC is
  at the rear.** IMG_9972 (KT01) reads the ground floor front-to-rear as *sân trước ->
  nơi để xe -> P. khách -> thang + thang máy -> **P. ăn + bếp** -> **WC** -> sân sau*, and
  its dimension chain `350 | 3010 | 4240 | 4000 | 5000 | 4500 | 1600 | 2650` puts the
  **kitchen in the 4500 band immediately behind the core** and the **WC in the 1600 band at
  the rear, with door D2 to the rear yard**. The earlier PDF read and the model put WC
  before kitchen; that reading is **withdrawn**, and the findings that depended on the swap
  have been rewritten.""",
  "s0-ground-order",
  "- **Two schools of the drawing-reading disagree on the ground floor.**")

E(151, 152,
  """that the *rear* of a tube house is the dark, still end (the rear yard is only 2300-2650
  deep, and the ground-floor rear rooms are the kitchen band and the rear WC band). The""",
  "s12-rearyard",
  "that the *rear* of a tube house is the dark, still end")


# ------------------------------------------------------------------ section 2.2

E(233, 240,
  """**Note on the East/West group split.** Đông tứ mệnh = Khảm, Ly, Chấn, Tốn; their four good
directions are always Bắc, Nam, Đông, Đông Nam. Tây tứ mệnh = Càn, Khôn, Cấn, Đoài; their
four good directions are always Tây, Tây Bắc, Tây Nam, Đông Bắc. **All four of the Tây
group's good directions - Tây, Tây Bắc, Tây Nam *and* Đông Bắc - are bad for the whole
Đông group, and all four of the Đông group's good directions - Bắc, Nam, Đông and Đông
Nam - are bad for the whole Tây group.** The two sets of four are disjoint and together
they cover the compass, so the split is perfectly symmetric: **every** direction is good
for one group and bad for the other. That is what the eight-row table above already says
cell by cell, and it is the geometric heart of Bat Trach: the four good directions of a
cung are always the four directions of its own group.

**Correction, 2026-10-22.** The earlier version of this paragraph singled out Đông Bắc as
"the only direction that is good for the whole Tây group and bad for the whole Đông
group". That was wrong: Đông Bắc is one of four, not the only one. The eight-row table
itself was always right and is left unchanged; this paragraph now matches it. The
practical consequence for a mixed-family house is unchanged but should be stated more
strongly: it is not that one direction is contentious - it is that the whole half of the
compass each half of the family prefers pulls against the other, and only the *ranking*
inside each half is a matter of school.""",
  "s22-groupsplit",
  "**Note on the East/West group split.**")
