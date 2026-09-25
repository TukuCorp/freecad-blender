# PHASE 1 REPORT — f3 front-bedroom split 3D solid model

Built: `3d/f3split_model.py` (pure stdlib + `homedesign.rects.wall_face_fragments`,
mm, deterministic, importable+runnable); output `3d/f3_split_model.json`
(5 options 0/A/B/C/D, 311 solids; walls fragmented with real gaps, no decals).
Areas (m²): 0: –/13.9; A: 5.9/7.7; B: 5.7/7.8; C: 5.5/8.0; D: open 13.9.
Envelope check: all solids inside x0–3960/y3500–12300/z−200–3400; labels carry
diacritics (BÀN LÀM VIỆC, P. NGỦ, WC, BAN CÔNG, HÀNH LANG); UTF-8 JSON.
Ran: `python reports/2026-09-25-f3-bedroom-split/3d/f3split_model.py --check`
→ exit 0; `--out …/f3_split_model.json` → wrote 311 solids; two `--out` runs
sha1-identical (b4aff403…); `json.load` shows 5 options; import of module OK.
Observed check output verbatim:
0 As drawn (base): solids=55 study=0.0 bedroom=13.9 total=13.9 bbox=(0,3500,-200 +3960x8800x3600) outside=none OK
A Study at the balcony: solids=63 study=5.9 bedroom=7.7 total=13.5 bbox=(0,3500,-200 +3960x8800x3600) outside=none OK
B Side split: solids=63 study=5.7 bedroom=7.8 total=13.5 bbox=(0,3500,-200 +3960x8800x3600) outside=none OK
C Glazed study at the rear: solids=69 study=5.5 bedroom=8.0 total=13.5 bbox=(0,3500,-200 +3960x8800x3600) outside=none OK
D Open studio + curtain: solids=61 study=0.0 bedroom=13.9 total=13.9 bbox=(0,3500,-200 +3960x8800x3600) outside=none OK
Deviations (drawing file wins, noted in module docstring): C glass 110 thick
centred y7195–7305 (not 7250–7360); desk y5010 per brief (file 4960, neutral);
party walls from y3500 (file 3300); balcony front = slatted parapet 1100, not a
200 wall; C bed foot touches glass face 55 mm; base wardrobe back 50 mm in wall.
No geometry discrepancy beyond those; note H=3200 per brief (file FSTOREY=3400
is rear-study only, unused here). No other files touched; no blocker.
