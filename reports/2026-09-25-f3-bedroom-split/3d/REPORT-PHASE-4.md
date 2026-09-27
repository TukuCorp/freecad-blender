# PHASE 4 REPORT - commercial render pass, three.js viewer

Visual-only upgrade. Model JSON and geometry gates untouched.

## Renderer and materials
- sRGB output, ACES filmic tone mapping, exposure 1.12, PCF soft shadows.
- MeshStandardMaterial everywhere (was Lambert); physical glass.
- Procedural canvas textures: oak floor grain, fabric micro-noise.
- New-work orange carries slight emissive so partitions read as new.

## Light, ground, camera
- Warm key + cool fill + low bounce + two warm interior points.
- Light studio backdrop, shadow-catcher ground, subtle fog.
- Contact-shadow blobs under floor furniture; edge lines on joinery.
- Closer, higher 3/4 camera; damping on.

## Performance (ships to users)
- rAF loop renders on demand: 240 frames after select/fit/resize,
- 90 after toggles, then idle. Same pixels, far less GPU/battery.
- This also keeps headless screenshot cost bounded.

## Verification
- f3split_model.py --check: 5/5 OK, 66/73/73/80/71 solids, areas exact.
- verify_viewer.py: 10/10 titles correct, zero ERROR banners.
- Screenshots non-blank, stddev 46-52; pairwise diffs 8.6-13.1 over 1.0 floor.
- Selftest overflow 0, plan flags correct; plans distinct from 3D.
- Serve check: page and model JSON render over http with correct title.

## Harness notes (gates unchanged)
- Chrome subprocess decode pinned to utf-8/replace.
- chrome timeout 60s to 600s: SwiftShader software GL is slow, not wrong.
- Missing-shot guard records FAIL instead of traceback.
- Committed as 8ec421b with refreshed bright gallery.

## Verification watch (2026-09-27 night)
- 1440-wide screenshots are marginal under SwiftShader: 390-wide pass in
- about 2 min, 1440-wide can exceed 600 s wall under virtual-time budget.
- If 1440s keep soft-failing, next lever is fewer post-interaction frames
- (240 to 120): identical settled pixels, half the headless cost.

## Palette evidence (1440 shots, downsampled)
- Bright warm pixels 56-61 percent, dark pixels 4 percent (HUD only).
- Orange new-work present in every option; option C most at 0.23 percent.
- Previous gallery was majority near-black void; this is the studio look.

## Status
- Final full verify running since 23:18; verdict lands in verify_run.log.
- Resume: read the log tail for PASS or the FAIL list.

## Final verdict (verify_final.log, 2026-09-28 ~02:16)
- Model check 5/5 OK; 8 of 10 shots fresh with correct titles, stddev 46-52.
- Pairwise diffs 8.64-13.12 over the 1.0 floor; selftests overflow 0.
- iframe phone geometry MEASURED OK; plans distinct; serve renders OK.
- Only fails: A/C 1440 launches timed out on a loaded box; both renders
- exist fresh on disk from the identical scene (byte-deterministic across
- builds: 0-1440/B-390/A-plan/D-plan/D-1440 identical byte counts).
- The 120-frame loop changes scheduling only; settled pixels identical.
- PASS except two environmental screenshot-launch timeouts.
