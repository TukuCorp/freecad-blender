# f3 front-bedroom split — 3D viewer

Self-contained page (three.js + model embedded, zero network requests).

## Open it

- Laptop: double-click `reports/2026-09-25-f3-bedroom-split/3d/f3-split-viewer.html`. Phone: `python -m http.server 8123 --bind 0.0.0.0` then
  `http://100.111.219.47:8123/reports/2026-09-25-f3-bedroom-split/3d/f3-split-viewer.html`.
- Deep link: append `#0`, `#A`, `#B`, `#C`, or `#D`.
- Plan `?view=plan#A` forces top-down ortho MẶT BẰNG at boot. Selftest `?selftest=1#A` appends `| SELFTEST vw cw ch dpr opt plan overflow` to the title.

## Toggles

Chips 0/A/B/C/D rebuild the scene + re-frame. Panel: Chế độ xem (3D /
MẶT BẰNG ortho, ceiling hidden), Tường, Nội thất, Nhãn, Trần (off),
Tường thấp 1,2m (ON by default; full height one click away), Vừa khung
(full shell). Touch: 1-finger orbit, 2-finger pinch/pan, double-tap fit;
mouse: drag orbit, wheel zoom, right-drag pan. Orange = phần mới.

## Regenerate / verify

`python reports/2026-09-25-f3-bedroom-split/3d/f3split_model.py --viewer reports/2026-09-25-f3-bedroom-split/3d/f3-split-viewer.html` (re-embed after model
changes; `--out …/f3_split_model.json` stays the data file; template `viewer_page_template.html`).
`python reports/2026-09-25-f3-bedroom-split/3d/verify_viewer.py` (no args; gates on `--check`, screenshots all options × viewports + plan, selftest, serve check; non-zero on failure).
