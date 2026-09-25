# Tầng 3 — splitting a bedroom into bedroom + workspace

Layout study, 2026-09-25. 2D only, one desk. Four options, drawn to scale over
the real geometry of the house.

## Start here

| file | what it is |
|---|---|
| `f3-front-base-plan_web.png` | **the front bedroom (ban công) as drawn** — dimensions, doors, light, and what it means for a split |
| `f3-front-split-options_web.png` | **options A–D for the front bedroom**, 1:56 |
| `3d/f3-split-viewer.html` | **the four options in 3D** — one self-contained three.js page, opens on a laptop and on a phone (see below) |
| `f3-base-plan_web.png`, `f3-split-options_web.png` | the same pair for the REAR bedroom (4100) — kept for reference; the answer was the front room |
| `*_print.png` | print resolution (A3, ~350 dpi) |
| `*.svg` | vector originals |
| `draw_options.py`, `draw_front_options.py` | generators — pure stdlib, mm coordinates |

## Sources — and one thing to confirm

* `contractor/MB 2-3-4-Model.pdf`, left plan **“MẶT BẰNG TẦNG 2,3”** (floors 2–4
  identical). Front bedroom printed **4000** deep, balcony **1400**, rear band
  **1600** with WC **1950** + hall beside it; room width printed **3950**.
* `designs/contractor-as-drawn.json` (compiled model) for the plot, core, stair,
  lobby and the resolved door positions.

**Discrepancy worth confirming.** In the model the two rear bands of the plan —
the rear bedroom and the rear WC/lô gia band — are the wrong way round versus the
sheet (the sheet reads `1600` WC+LÔ GIA first from the rear wall, then `4100`
bedroom; the model does the reverse and gives the bedroom the rear wall with a
1500 window). This affects the 3D renders and the viewer for floors 2–5. Left
open by choice; the front bedroom studied below is **not** affected.

## The front bedroom, as drawn

* Printed **4000 × 3560** outer → lọt lòng **~3900 × 3560 ≈ 13.9 m²**.
* **Ban công 1400** deep at the street, recessed, with a 900 door (west) + a
  1400 window (east) — together the room's only daylight, since both long walls
  are party walls.
* Rear band 1600: **WC 1950** west (door into the bedroom) + **hall 2010** east
  (the room's only entry, from the core).
* In the drawing: bed head on the east wall with two bedside tables, wardrobe
  against the WC wall.

**The constraint any split has to live with:** light is at the street end, the
single entry is at the core end. A front/rear split therefore always makes one
zone a walk-through — the zone without the entry. Only a side (front-to-rear)
split can give each zone its own door.

## Options for the front bedroom

| | split | workspace | bedroom | idea |
|---|---|---|---|---|
| **A** | stud wall 1650 from the balcony | 5.9 m² | 7.7 m² | desk straight on the window — the only option with direct daylight |
| **B** | partition at x 2200, front-to-rear | 5.7 m² | 7.8 m² | each zone its own door: the east strip takes the window **and** the entry, the west strip the balcony door and the WC |
| **C** | glass partition 1550 from the rear wall | 5.5 m² | 8.0 m² | bedroom keeps balcony + window + WC at full size; the study is a glazed box at the core taking the entry and the WC |
| **D** | none — track curtain | 13.9 m² open | | desk at the window, bed at the core, cheapest build |

**A — study at the balcony.** The desk faces the window with nothing between it
and the light; the bedroom keeps its own WC. Costs: the bedroom drops to 2150
deep, and you cross the bedroom to reach the study.

**B — side split.** The cleanest circulation of the four: the east strip holds
the window *and* the entry, so the study is entered straight from the hall and
the bedroom (west) keeps the balcony door and the WC, with a new door from the
study. Costs: the study is only 1460 clear and the bedroom 2000 wide, so the bed
spans it front to back.

**C — glazed study at the rear.** The bedroom keeps everything it has — balcony,
window, WC, full depth — and the study is a 1550-deep glazed box at the core
that takes the entry and the WC. Costs: the desk has no window (light is borrowed
through the glass) and it is acoustically open.

**D — open studio + curtain.** Nothing is walled off: desk at the window, bed at
the core, one track curtain between them. Cheapest, most light, nothing lost if
the plan changes. Costs: no acoustic separation at all.

## Rear-room set (reference)

`f3-base-plan_web.png` / `f3-split-options_web.png` cover the rear bedroom
(4100 × 3560 → ~4000 × 3560 ≈ 13.9 m²). Its only daylight is the open **LÔ GIA**
1660 wide at the rear-east, and its entry is a 900 door from the lobby at the
front-west. Options there: A study at the rear on the lô gia (5.9 / 7.8 m²),
B study at the entry (5.0 / 8.9 m²), C long desk wall side split (5.8 / 8.0 m²),
D platform bed + track curtain (14.2 m² open).

## The four options in 3D (three.js)

`3d/f3-split-viewer.html` is one self-contained page — three.js and the model are
embedded, nothing is fetched, so it works offline:
- **Laptop:** double-click the file. **Phone:** serve the repo
  (`python -m http.server 8123 --bind 0.0.0.0`) and open
  `http://100.111.219.47:8123/reports/2026-09-25-f3-bedroom-split/3d/f3-split-viewer.html`
  (Tailscale IP; add `#A`…`#D` to deep-link an option).
- Chips `0/A/B/C/D` switch the option; the panel toggles view (3D / MẶT BẰNG
  top-down), walls, furniture, labels, ceiling, and a 1.2 m wall cut; touch is
  one-finger orbit, two-finger pinch/pan, double-tap to re-fit. Orange = the new
  work, matching the 2D sheets.
- Model + geometry: `3d/f3split_model.py` (pure stdlib, mm) → `3d/f3_split_model.json`;
  regenerate the page with `--viewer`. `3d/verify_viewer.py` re-proves it
  (screenshots every option at 1440×900 and 390×844, measured phone layout,
  plan-vs-3D difference, http serve) and exits non-zero on any failure.

## Open

* WC and hall door positions are drawn as the sheet has them; both can shift
  ±300 mm inside their wall, which helps options A and C.
* Nothing is modelled in the pipeline yet — no spec variant, no 3D render. Once
  an option is picked: author `designs/contractor-as-drawn-<tag>.json`, run
  `homedesign plans` (SVG/DXF), then `homedesign build` for the EEVEE preview
  and the viewer.
