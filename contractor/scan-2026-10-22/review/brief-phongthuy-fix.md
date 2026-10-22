# Brief phongthuy-fix: correction pass on out-phongthuy.md

Folder: the project root. File to correct IN PLACE: `contractor/scan-2026-10-22/review/out-phongthuy.md` (about 1300 lines). Back it up first to `_scan1022/out-phongthuy.before-fix.md`. Today is 2026-10-22.

Why: the first pass took room positions from `designs/contractor-as-drawn.json`. That spec is SUPERSEDED by the scan. The caller checked the photos. The facts below are authoritative; the transcript `contractor/scan-2026-10-22/transcript-architecture.md` has the supporting lines (search it, do not guess).

## Facts from the scan
1. Altar room (P. Thờ) is on tầng 4 (+13.800; sheet KT05, IMG_9976), at the FRONT behind the front balcony (ban công, door D5, window S1). Behind it (toward the core) is P. Đọc sách (reading room), separated by a thin partition. Behind that: a WC with a light well (ô lấy sáng), then the stair (21 treads), the lift, the rear bedroom P. Ngủ (+13.800), a rear WC, and the rear loggia (lô gia). The WC is NOT against the altar room wall. The old claim that P. Thờ is on the 5th floor is wrong.
2. Tầng 5 (+17.200; KT06, IMG_9977) has NO rooms: a stair/lift lobby (doors D6, D7), a glazed stair light well, and two open terraces (Sân thượng) at front and rear.
3. A lift shaft IS drawn on every plan (about 1800 x 1600) with a pit detail sheet. So "does a lift exist" is resolved; its exact size conflicts across sheets and is a design-lane matter. Remove statements that the lift is only inferred.
4. Ground floor, front to rear: front yard (sân trước), garage (nơi để xe), P. Khách, stair, lift, P. ăn + bếp, then the WC at the rear next to the rear yard. This differs from the older spec (it had WC before kitchen).
5. Levels: 0, +3.800, +7.000, +10.400, +13.800, +17.200, roof slab +20.400, parapet top +21.900.
6. The street is on the short side at the top/left of the plans. There is NO north arrow in the scan: facing direction stays unknown (keep that part as is).

## Tasks
1. Find every finding, table row, summary line and sources entry that cites the JSON rects (ids such as `tho_f5`, `wc_truoc_f5`, `hall_front_f5`, `san_thuong_*`, y-ranges in mm, "JSON") or says the altar is on the 5th floor, or says the lift is only inferred, or places rooms where the old spec did. Rewrite each against the transcript, citing IMG ids and transcript line numbers, not JSON rects. List them first in `_scan1022/fix-worklist.md`.
2. Rewrite P-21, P-22 and P-23 from scratch for the real layout: altar room at the front of tầng 4 with balcony and glazing in front of it, reading room behind, WC position per the transcript, beams unknown unless the beam transcript shows them (`transcript-beams-slabs.md`). Cover: front-position issue, the tradition's preference for the top floor or the interior, what the owner can do inside the room, and where a top-floor altar could go instead (tầng 5 is only a lobby and terraces; a rooftop altar nook costs what in safety: weather, fall protection, loads). Keep the safety/design conflict line.
3. Fix section 2.2: the paragraph claiming Đông Bắc is the ONLY direction good for the whole Tây group and bad for the whole Đông group is wrong. Tây, Tây Bắc, Tây Nam and Đông Bắc are all good for the Tây group and bad for the Đông group. Correct it; the eight-row table itself is right, leave it.
4. Fix section 6.4 (the three things not determined): the lift question is now resolved; the facing direction remains unknown; the ground-floor kitchen/WC order is now known from the scan (kitchen next to the core, WC at the rear).
5. Add a short section at the top titled `## Corrections 2026-10-22` listing what changed, in bullet form. Keep every unaffected finding as is. Keep finding IDs stable.
6. Sanity grep at the end: no remaining occurrence of `tho_f5`, `wc_truoc_f5` or "5th floor" in the sense of an altar room. Print only counts.

## Hard rules
No raw dumps; UTF-8 everywhere (Python: encoding="utf-8"); no dollar sign in shell text; edit only `out-phongthuy.md` and files under `_scan1022/`; do not overstate; label evidence VERIFIED / PARTIAL / CLAIMED / NOT FOUND / UNVERIFIED as before.

## Last action (mandatory)
As your very last action run:
herdr agent prompt w3D:p1 "phongthuy-fix finished: N findings changed, file contractor/scan-2026-10-22/review/out-phongthuy.md"
(replace N with the real number; do not use --wait; if you could not finish, say partial).
