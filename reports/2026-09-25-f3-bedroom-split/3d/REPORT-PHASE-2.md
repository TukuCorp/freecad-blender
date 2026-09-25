# PHASE 2 REPORT — three.js viewer for options 0/A/B/C/D

Files (all under `3d/`): `f3split_model.py` (+`--viewer`, 1 HÀNH LANG label,
deviations docstring kept), `viewer_page_template.html` (editable page source),
`f3-split-viewer.html` (688470 B self-contained: three.min.js + OrbitControls
inlined as-is, model JSON embedded, only external-like string is the
w3.org-xmlns inside three.js), `f3_split_model.json` (kept), `VIEWER.md`,
`shots/` (A/D @1440×900 + 390×844, C over http).
Viewer: hash deep-link (#A), rebuild-on-switch + re-frame, 3D/MẶT BẰNG
(ortho, ceiling off), toggles walls/furniture/labels/ceiling-off-default/
1.2 m cut, canvas sprites with diacritics, orange = new work + legend, HUD
title + m², DPR≤2, pointer/touch input, try/catch + window.onerror red banner.
Commands: `--check` exit 0; `--out` 311 solids; `--viewer` embed; `chrome.exe
--headless=new --disable-gpu --screenshot=…png --window-size=…` ×4 + one over
`python -m http.server`; Pillow stddev check; `--dump-dom` title check.
Observed: check OK (same 5 lines as phase 1); screenshots A-1440 58712 B,
D-1440 57907 B, A-390 33953 B, D-390 33216 B, C-http 65026 B; stddev 44–63
(not blank); dump-dom titles `P.án A/D — T3 front split 3D`, no `ERROR:` title
(the only `ERROR:` hits are the handler's own source text); C over http
renders identically to file://. `git status` shows nothing touched outside
`reports/2026-09-25-f3-bedroom-split/` (plus pre-existing untracked
`docs/tubehouse-dream-light.html`, not mine).
Deviations: duplicate HÀNH LANG dropped (now 4/5 labels per option); mobile
tools panel collapses to a `? Tùy chọn` button; fixed desktop `#tools-btn`
leak and viewer-writer syntax slip during build; initial camera is a steep
high-angle oblique (street end nearest) — fine on both sizes. No blocker.
