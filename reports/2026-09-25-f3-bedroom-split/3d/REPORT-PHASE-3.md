# PHASE 3 REPORT — fidelity + verifier

Fidelity (same schema/envelopes): bed = plinth + frame + mattress + 2
pillows + headboard on study side (0/E, A/N 1000..2600/6800..8800, B/E,
C/S y5195..7195 55 off glass, D/N); desk = top + 4 legs + seat + back;
wardrobe = 2400 carcass + doors; WC = tank/bowl/seat + basin + tray/curb.
`stack_on` declares stacks; `--check` fails on undeclared overlap, any
furniture-in-wall hit, envelope/area drift, or manifest miss (0: bed6 +
2 tables + ward; A–D: bed6 + ward + desk5 + chair2; bed == study x/y).
Viewer: hemi 1.25 + fill 0.30, low-cut ON, fit + plan on full shell x0..3960/y3500..12300, `?view=plan` pre-first-frame.
Verifier: 5×2 title/stddev; pairwise floor 1.0; plan non-blank AND vs3D
bbox + mean>3; serve 200 + render (selftest clamped, iframe authoritative).
Real final output (exit 0, PASS):
0 As drawn: solids=66 0.0/13.9 bbox=(0,3500,-200 +3960x8800x3600) manifest=ok furn_overlap=none wall_hit=none OK
A Study at the balcony: solids=73 5.9/7.7 manifest=ok furn_overlap=none wall_hit=none OK
B Side split: solids=73 5.7/7.8 manifest=ok furn_overlap=none wall_hit=none OK
C Glazed study at the rear: solids=80 5.5/8.0 manifest=ok furn_overlap=none wall_hit=none OK
D Open studio + curtain: solids=71 0.0/13.9 manifest=ok furn_overlap=none wall_hit=none OK
0 1440x900 68094 58.3 True / 0 390x844 42879 79.4 True / A 1440x900 82245 57.5 True / A 390x844 52623 79.9 True
B 1440x900 77185 57.3 True / B 390x844 48396 78.5 True / C 1440x900 83442 57.2 True / C 390x844 54481 79.0 True
D 1440x900 81262 55.0 True / D 390x844 50199 75.6 True
0~A 8.07 / A~B 5.39 / B~C 5.62 / C~D 5.95 / 0~D 7.50 (floor 1.0; same shell, contents-only deltas)
selftest rows are clamped (vw=758, vacuous at 390); MEASURED iframe row
is the authority: 390x844 vw=390 vh=844 scrollW=390 cw=390 ch=844 bad=0,
chips 48x44 at x=59/115/171/227/283 (right=331, bottom=834). Desktop via
1440 screenshot + clamped selftest (1440 iframe dropped: flaky in 1000px
window under load). Fix r3: 60s timeout + retry-once + fresh profile per
launch, soft-FAIL rows (no traceback); two back-to-back PASS exit=0
(run1 08:26, run2 08:32, zero chrome-timeout lines in either).
