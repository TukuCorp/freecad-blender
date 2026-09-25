"""Tang-3 front-bedroom split study - PHASE 1: deterministic 3D solid model.

Pure stdlib (+ read-only import of homedesign.rects for wall fragments).
Units: mm. x=0 west party wall (+x east); y=0 street (+y rear); z up,
z=0 finished floor of tang 3.

Geometry transcribed from reports/2026-09-25-f3-bedroom-split/
draw_front_options.py (front-room part). Where that file and the task brief
disagree, the DRAWING FILE wins - see DISCREPANCIES below.

Usage (run from the repo root):
    python reports/2026-09-25-f3-bedroom-split/3d/f3split_model.py --out <dir>/f3_split_model.json
    python reports/2026-09-25-f3-bedroom-split/3d/f3split_model.py --check
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from homedesign.rects import wall_face_fragments
except ImportError:  # runnable without an installed package: fall back to src/
    _REPO = Path(__file__).resolve().parent.parent.parent.parent
    sys.path.insert(0, str(_REPO / "src"))
    from homedesign.rects import wall_face_fragments

# ---------------------------------------------------------------- constants
H = 3200.0            # clear ceiling height (task value; file's FSTOREY=3400 is rear-study only)
SLAB = 200.0
IN_X0, IN_X1 = 200.0, 3760.0
CLEAR_W = IN_X1 - IN_X0                       # 3560
BALC_Y0, BALC_Y1 = 3500.0, 4900.0
FB_Y0, FB_Y1 = 4900.0, 8900.0
CLEAR_Y0, CLEAR_Y1 = 4950.0, 8850.0           # bedroom clear interior
FWC_Y0, FWC_Y1 = 8900.0, 10500.0
HF_Y0, HF_Y1 = 10500.0, 12300.0
FWC_X1 = 1950.0
ENV = (0.0, 3500.0, -SLAB, 3960.0, 12300.0, 3400.0)  # shell envelope x0,y0,z0,x1,y1,z1

# DISCREPANCIES (drawing file vs task brief; drawing file used throughout):
# 1. Glazed partition C: file draws it 110 thick CENTRED on y=7250 (7195..7305);
#    brief says 7250..7360. Only the file geometry reproduces the published
#    areas (study (8850-7305)*3560=5.50, bedroom (7195-4950)*3560=7.99).
# 2. Desk/wardrobe y for A,B,D: file uses FB_Y0+60=4960; brief says 5010.
#    Brief value (5010) used - 50 mm, area-neutral.
# 3. Party walls: file runs them from y=3300 (BALC_Y0-200); brief says
#    3500..12300. Brief value used; balcony front edge is parapet, not wall.
# 4. File draws a solid 200 wall at the balcony front edge (y3300..3500);
#    brief says open edge with 1100 slatted parapet. Parapet built instead.
# 5. File's band|hall_front wall (y10450..10550, no opening) is reproduced
#    as drawn, so the hall pocket is reachable only via the bedroom hall door.
# 6. C bed vs glass (phase-1 note said a 55 mm foot touch): phase 3 moves the
#    bed 55 south (y5195..7195) so NOTHING intersects the glass - the check
#    now fails on any furniture-in-wall hit.
# 7. Base wardrobe (phase-1 note said back 50 mm inside the wall): phase 3
#    moves it to y8240..8840 (10 clear of the band wall face at 8850).

EXPECTED = {  # (study, bedroom, total) m2, 1 dp
    "0": (0.0, 13.9, 13.9),
    "A": (5.9, 7.7, 13.5),
    "B": (5.7, 7.8, 13.5),
    "C": (5.5, 8.0, 13.5),
    "D": (0.0, 13.9, 13.9),
}
TITLES = {
    "0": "As drawn (base)", "A": "Study at the balcony", "B": "Side split",
    "C": "Glazed study at the rear", "D": "Open studio + curtain",
}


# ---------------------------------------------------------------- builders
def solid(sid, kind, x, y, z, w, d, h, material, label=None, stack_on=None):
    s = {"id": sid, "kind": kind, "x": x, "y": y, "z": z, "w": w, "d": d,
         "h": h, "material": material}
    if label is not None:
        s["label"] = label
    if stack_on is not None:
        s["stack_on"] = stack_on
    return s


def _frags(span, openings):
    """Face fragments of a wall via homedesign.rects (REAL gaps, no decals)."""
    holes = [(o[0], o[1], o[2], o[3] - o[1]) for o in openings]
    return wall_face_fragments(float(span), float(H), holes)


def wall_solids_h(opt, wid, x, y, w, t, kind, mat, openings):
    out = []
    for i, (fs, ft, fw, fh) in enumerate(_frags(w, openings)):
        out.append(solid(f"{opt}_wall_{wid}_{i}", kind, x + fs, y, ft, fw, t,
                         fh, mat))
    return out


def wall_solids_v(opt, wid, x, y, t, d, kind, mat, openings):
    out = []
    for i, (fs, ft, fw, fh) in enumerate(_frags(d, openings)):
        out.append(solid(f"{opt}_wall_{wid}_{i}", kind, x, y + fs, ft, t, fw,
                         fh, mat))
    return out


def opening(oid, kind, host, x, y, sill, head, width, swing):
    return {"id": oid, "kind": kind, "host": host, "x": x, "y": y,
            "sill": sill, "head": head, "width": width, "swing": swing}


def bed_solids(opt, x, y, w, d, head):
    """Readable bed inside the exact x/y/w/d envelope: plinth + mattress
    (inset ~30) + two pillows at the head end + headboard on `head` side."""
    PH, PW = 100.0, 1000.0      # headboard thickness / pillow width
    PL, PT = 300.0, 25.0        # plinth height / top slab thickness
    MZ0 = PL + PT                # mattress base
    MH = 220.0
    s = [solid(f"{opt}_bed_base", "furniture", x, y, 0, w, d, PL, "wood"),
         solid(f"{opt}_bed_frame", "furniture", x, y, PL, w, d, PT, "wood",
               stack_on=f"{opt}_bed_base")]
    base = f"{opt}_bed_frame"
    if head == "north":
        s.append(solid(f"{opt}_bed_head", "furniture", x, y + d - PH, 0, w,
                       PH, PW, "wood", stack_on=base))
        s.append(solid(f"{opt}_bed_mattress", "furniture", x + 30,
                       y + 30, MZ0, w - 60, d - 60 - PH, MH, "fabric",
                       stack_on=base))
        for i, px in enumerate([x + 90, x + w / 2 + 30]):
            s.append(solid(f"{opt}_bed_pillow{i}", "furniture", px,
                           y + d - PH - 430, MZ0 + MH, w / 2 - 120, 400, 140,
                           "fabric", stack_on=f"{opt}_bed_mattress"))
    elif head == "south":
        s.append(solid(f"{opt}_bed_head", "furniture", x, y, 0, w, PH, PW,
                       "wood", stack_on=base))
        s.append(solid(f"{opt}_bed_mattress", "furniture", x + 30,
                       y + 30 + PH, MZ0, w - 60, d - 60 - PH, MH, "fabric",
                       stack_on=base))
        for i, px in enumerate([x + 90, x + w / 2 + 30]):
            s.append(solid(f"{opt}_bed_pillow{i}", "furniture", px, y + PH + 60,
                           MZ0 + MH, w / 2 - 120, 400, 140, "fabric",
                           stack_on=f"{opt}_bed_mattress"))
    elif head == "east":
        s.append(solid(f"{opt}_bed_head", "furniture", x + w - PH, y, 0, PH,
                       d, PW, "wood", stack_on=base))
        s.append(solid(f"{opt}_bed_mattress", "furniture", x + 30, y + 30,
                       MZ0, w - 60 - PH, d - 60, MH, "fabric",
                       stack_on=base))
        for i, py in enumerate([y + 90, y + d / 2 + 30]):
            s.append(solid(f"{opt}_bed_pillow{i}", "furniture",
                           x + w - PH - 430, py, MZ0 + MH, 400, d / 2 - 120,
                           140, "fabric", stack_on=f"{opt}_bed_mattress"))
    else:  # west
        s.append(solid(f"{opt}_bed_head", "furniture", x, y, 0, PH, d, PW,
                       "wood", stack_on=base))
        s.append(solid(f"{opt}_bed_mattress", "furniture", x + 30 + PH, y + 30,
                       MZ0, w - 60 - PH, d - 60, MH, "fabric",
                       stack_on=base))
        for i, py in enumerate([y + 90, y + d / 2 + 30]):
            s.append(solid(f"{opt}_bed_pillow{i}", "furniture", x + PH + 60,
                           py, MZ0 + MH, 400, d / 2 - 120, 140, "fabric",
                           stack_on=f"{opt}_bed_mattress"))
    return s


def desk_solids(opt, x, y, w, d, prefix="desk"):
    """25 mm top on four legs; chair = seat + back on the north side."""
    cx, cy = x + w / 2, y + d + 330  # chair centre, north side (as drawn)
    leg, top1 = 50, 750
    s = [solid(f"{opt}_{prefix}_top", "furniture", x, y, top1 - 25, w, d, 25,
               "wood")]
    for i, (lx, ly) in enumerate([(x + 25, y + 25),
                                  (x + w - 25 - leg, y + 25),
                                  (x + 25, y + d - 25 - leg),
                                  (x + w - 25 - leg, y + d - 25 - leg)]):
        s.append(solid(f"{opt}_{prefix}_leg{i}", "furniture", lx, ly, 0, leg,
                       leg, top1 - 25, "wood"))
    seat, back = f"{opt}_chair_seat", f"{opt}_chair_back"
    s.append(solid(seat, "furniture", cx - 240, cy - 240, 0, 480, 480, 450,
                   "wood"))
    s.append(solid(back, "furniture", cx - 240, cy + 180, 450, 480, 60, 500,
                   "wood", stack_on=seat))
    return s


def wardrobe_solids(opt, x, y, w, d, n_doors=3):
    """2400-high wardrobe inside the exact footprint; door slabs stack on the
    carcass so the overlap check allows them. Door split lines read as doors."""
    carcass = f"{opt}_ward_carcass"
    s = [solid(carcass, "furniture", x, y, 0, w, d, 2400, "wood")]
    dw = w / n_doors
    for i in range(n_doors):
        s.append(solid(f"{opt}_ward_door{i}", "furniture", x + i * dw + 8,
                       y + d - 24, 0, dw - 16, 24, 2200, "wood",
                       stack_on=carcass))
    return s


def shell(opt):
    """Shell solids + openings shared by every option."""
    solids, openings = [], []
    solids += wall_solids_v(opt, "party_w", 0, BALC_Y0, 200, HF_Y1 - BALC_Y0,
                            "wall", "concrete", [])
    solids += wall_solids_v(opt, "party_e", IN_X1, BALC_Y0, 200,
                            HF_Y1 - BALC_Y0, "wall", "concrete", [])
    solids += wall_solids_h(opt, "balc_bed", IN_X0, BALC_Y1 - 50,
                            CLEAR_W, 100, "wall", "concrete",
                            [(0, 0, 900, 2100), (2160, 900, 1400, 2200)])
    openings += [opening(f"{opt}_op_balcdoor", "door", "balc_bed", 200, 4850,
                         0, 2100, 900, "in"),
                 opening(f"{opt}_op_balcwin", "window", "balc_bed", 2360, 4850,
                         900, 2200, 1400, "none")]
    solids += wall_solids_h(opt, "bed_band", IN_X0, FB_Y1 - 50, CLEAR_W, 100,
                            "wall", "concrete",
                            [(325, 0, 900, 2100), (2305, 0, 900, 2100)])
    openings += [opening(f"{opt}_op_wcdoor", "door", "bed_band", 525, 8850, 0,
                         2100, 900, "in"),
                 opening(f"{opt}_op_halldoor", "door", "bed_band", 2505, 8850,
                         0, 2100, 900, "in")]
    solids += wall_solids_v(opt, "wc_hall", FWC_X1 - 50, FWC_Y0, 100,
                            FWC_Y1 - FWC_Y0, "wall", "concrete", [])
    solids += wall_solids_h(opt, "band_hall", IN_X0, FWC_Y1 - 50, CLEAR_W, 100,
                            "wall", "concrete", [])
    for sid, y0, y1 in [("balc", BALC_Y0, BALC_Y1), ("bed", FB_Y0, FB_Y1),
                        ("band", FWC_Y0, FWC_Y1), ("hall", HF_Y0, HF_Y1)]:
        solids.append(solid(f"{opt}_slab_{sid}", "slab", 0, y0, -SLAB, 3960,
                            y1 - y0, SLAB, "concrete"))
    solids.append(solid(f"{opt}_slab_roof", "slab", 0, BALC_Y0, H, 3960,
                        HF_Y1 - BALC_Y0, SLAB, "concrete"))
    # slatted parapet on the open y=3500 edge: 29 slats + top rail, 1100 high
    n, pitch, sw = 29, CLEAR_W / 29, 60.0
    for i in range(n):
        x = IN_X0 + i * pitch + (pitch - sw) / 2
        solids.append(solid(f"{opt}_parapet_slat{i:02d}", "parapet", x,
                            BALC_Y0, 0, sw, 30, 1040, "wood"))
    solids.append(solid(f"{opt}_parapet_rail", "parapet", IN_X0, BALC_Y0,
                        1040, CLEAR_W, 60, 60, "wood"))
    # WC fixtures: toilet (tank + bowl + seat) + basin (pedestal + bowl),
    # against the west wall; shower tray + curb in the east remainder.
    wct = f"{opt}_wc_toilet"
    solids.append(solid(wct, "fixture_wc", 240, 9320, 0, 420, 200, 750,
                        "porcelain", "tank"))
    solids.append(solid(f"{opt}_wc_bowl", "fixture_wc", 240, 9520, 0, 420,
                        480, 400, "porcelain", "bowl", stack_on=wct))
    solids.append(solid(f"{opt}_wc_seat", "fixture_wc", 260, 9530, 400, 380,
                        440, 60, "porcelain", stack_on=f"{opt}_wc_bowl"))
    ped = f"{opt}_wc_pedestal"
    solids.append(solid(f"{opt}_wc_basin", "fixture_wc", 940, 9920, 750, 600,
                        480, 180, "porcelain", "basin"))
    solids.append(solid(ped, "fixture_wc", 1150, 10050, 0, 180, 220, 750,
                        "porcelain"))
    solids.append(solid(f"{opt}_wc_tray", "fixture_wc", 760, 8990, 0, 900,
                        900, 80, "porcelain", "shower tray"))
    solids.append(solid(f"{opt}_wc_curb", "fixture_wc", 760, 9890, 0, 900,
                        60, 150, "porcelain", stack_on=f"{opt}_wc_tray"))
    return solids, openings


def labels_common():
    # One HÀNH LANG label per option - the band hall and hall_front share one
    # zone, so the second label drawn there in phase 1 is dropped (review 1).
    return [ {"text": "BAN CÔNG", "x": 1980, "y": 4200, "z": 1600},
             {"text": "WC", "x": 975, "y": 9700, "z": 1600},
             {"text": "HÀNH LANG", "x": 1980, "y": 11400, "z": 1600}]


def build_option(oid):
    solids, openings = shell(oid)
    if oid == "0":
        solids += bed_solids(oid, 1760, 5000, 2000, 1600, "east")
        solids.append(solid("0_table1", "furniture", 1200, 5000, 0, 450, 450,
                            500, "wood"))
        solids.append(solid("0_table2", "furniture", 1200, 6150, 0, 450, 450,
                            500, "wood"))
        solids += wardrobe_solids(oid, 200, 8240, 1400, 600, n_doors=3)
        labels = labels_common() + [{"text": "P. NGỦ", "x": 1980, "y": 6900,
                                     "z": 1600}]
    elif oid == "A":
        solids += wall_solids_h(oid, "newA", IN_X0, 6600, CLEAR_W, 100,
                                "new_partition", "stud", [(100, 0, 1200, 2100)])
        openings.append(opening("A_op_slider", "slider", "newA", 300, 6600, 0,
                                2100, 1200, "slide"))
        solids += desk_solids(oid, 2300, 5010, 1400, 650)
        solids += bed_solids(oid, 1000, 6800, 1600, 2000, "north")
        solids += wardrobe_solids(oid, 3160, 6800, 600, 1000, n_doors=2)
        labels = (labels_common()
                  + [{"text": "BÀN LÀM VIỆC", "x": 1980, "y": 5775, "z": 1600},
                     {"text": "P. NGỦ", "x": 1980, "y": 7775, "z": 1600}])
    elif oid == "B":
        solids += wall_solids_v(oid, "newB", 2200, FB_Y0, 100, FB_Y1 - FB_Y0,
                                "new_partition", "stud", [(2700, 0, 900, 2100)])
        openings.append(opening("B_op_door", "door", "newB", 2200, 7600, 0,
                                2100, 900, "in"))
        solids += desk_solids(oid, 2500, 5010, 1260, 650)
        solids += bed_solids(oid, 200, 5700, 2000, 1600, "east")
        solids += wardrobe_solids(oid, 1240, 5010, 960, 600, n_doors=2)
        labels = (labels_common()
                  + [{"text": "BÀN LÀM VIỆC", "x": 3030, "y": 6900, "z": 1600},
                     {"text": "P. NGỦ", "x": 1200, "y": 6900, "z": 1600}])
    elif oid == "C":
        solids += wall_solids_h(oid, "newC", IN_X0, 7195, CLEAR_W, 110,
                                "glass", "glass", [(1300, 0, 900, 2400)])
        openings.append(opening("C_op_glassdoor", "door", "newC", 1500, 7195,
                                0, 2400, 900, "in"))
        for i, mx in enumerate([793, 1387, 1500, 2400, 2573, 3167]):
            h = 2400 if mx in (1500, 2400) else H
            solids.append(solid(f"C_mullion{i}", "mullion", mx - 20, 7195, 0,
                                40, 110, h, "wood"))
        solids += desk_solids(oid, 2300, 7450, 1400, 650)
        solids += bed_solids(oid, 1250, 5195, 1600, 2000, "south")
        solids += wardrobe_solids(oid, 3160, 5500, 600, 1650, n_doors=3)
        labels = (labels_common()
                  + [{"text": "BÀN LÀM VIỆC", "x": 1980, "y": 8105, "z": 1600},
                     {"text": "P. NGỦ", "x": 1980, "y": 6072, "z": 1600}])
    elif oid == "D":
        solids.append(solid("D_curtain", "curtain", IN_X0, 6690, 0, CLEAR_W,
                            20, 2200, "fabric", "track curtain"))
        solids += desk_solids(oid, 2300, 5010, 1400, 650)
        solids += bed_solids(oid, 1250, 6850, 1600, 2000, "north")
        solids += wardrobe_solids(oid, 1200, 5010, 1100, 600, n_doors=2)
        labels = (labels_common()
                  + [{"text": "BÀN LÀM VIỆC", "x": 3000, "y": 6100, "z": 1600},
                     {"text": "P. NGỦ", "x": 1980, "y": 7900, "z": 1600}])
    else:
        raise ValueError(oid)
    xs = [s["x"] for s in solids] + [s["x"] + s["w"] for s in solids]
    ys = [s["y"] for s in solids] + [s["y"] + s["d"] for s in solids]
    zs = [s["z"] for s in solids] + [s["z"] + s["h"] for s in solids]
    bbox = {"x": min(xs), "y": min(ys), "z": min(zs), "w": max(xs) - min(xs),
            "d": max(ys) - min(ys), "h": max(zs) - min(zs)}
    exp = EXPECTED[oid]
    areas = {"study_m2": exp[0], "bedroom_m2": exp[1], "total_m2": exp[2]}
    return {"id": oid, "title": TITLES[oid], "areas": areas, "solids": solids,
            "openings": openings, "labels": labels, "bbox": bbox}


def zone_areas(oid):
    """Measured clear zones (m2), same convention as the 2D study."""
    if oid == "0":
        return (0.0, CLEAR_W * (CLEAR_Y1 - CLEAR_Y0) / 1e6)
    if oid == "A":
        return ((6600 - CLEAR_Y0) * CLEAR_W / 1e6,
                (CLEAR_Y1 - 6700) * CLEAR_W / 1e6)
    if oid == "B":
        d = CLEAR_Y1 - CLEAR_Y0
        return ((IN_X1 - 2300) * d / 1e6, (2200 - IN_X0) * d / 1e6)
    if oid == "C":
        return ((CLEAR_Y1 - 7305) * CLEAR_W / 1e6,
                (7195 - CLEAR_Y0) * CLEAR_W / 1e6)
    if oid == "D":
        return (0.0, CLEAR_W * (CLEAR_Y1 - CLEAR_Y0) / 1e6)
    raise ValueError(oid)


def build_model():
    return {"units": "mm", "up": "z",
            "storey": {"level": 3, "height_mm": 3200, "slab_mm": 200},
            "options": [build_option(oid) for oid in ["0", "A", "B", "C", "D"]]}


WALL_KINDS = {"wall", "new_partition", "glass", "mullion", "parapet", "slab"}
FURN_KINDS = {"furniture", "fixture", "fixture_wc", "curtain"}


def _aabox(s):
    return (s["x"], s["y"], s["z"], s["x"] + s["w"], s["y"] + s["d"],
            s["z"] + s["h"])


def _overlap(a, b, eps=1.0):
    ax0, ay0, az0, ax1, ay1, az1 = a
    bx0, by0, bz0, bx1, by1, bz1 = b
    return (min(ax1, bx1) - max(ax0, bx0) > eps
            and min(ay1, by1) - max(ay0, by0) > eps
            and min(az1, bz1) - max(az0, bz0) > eps)


def overlap_pairs(solids):
    """(id_a, id_b) for AABB intersections, ignoring declared stack_on pairs.

    A solid carrying "stack_on": "<parent id>" may intersect exactly that
    parent (mattress on base, pillow on mattress, door slab on carcass, seat
    parts, WC seat on bowl / curb on tray). Anything else is a failure."""
    boxes = {s["id"]: _aabox(s) for s in solids}
    kinds = {s["id"]: s.get("kind") for s in solids}
    stacks = {(s["id"], s["stack_on"]) for s in solids if s.get("stack_on")}
    ids = [s["id"] for s in solids]
    bad = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            if (a, b) in stacks or (b, a) in stacks:
                continue
            if _overlap(boxes[a], boxes[b]):
                bad.append((a, b))
    return bad, kinds


BED_ENV = {  # study bed envelope per option: (x, y, w, d, head)
    "0": (1760, 5000, 2000, 1600, "east"),
    "A": (1000, 6800, 1600, 2000, "north"),
    "B": (200, 5700, 2000, 1600, "east"),
    "C": (1250, 5195, 1600, 2000, "south"),
    "D": (1250, 6850, 1600, 2000, "north"),
}


def manifest_errors(opt):
    """Required furniture parts per option; missing/wrong-envelope = errors.

    0: bed (6 parts), 2 tables, wardrobe (carcass + >=2 doors). No desk/chair.
    A/B/C/D: bed (6), wardrobe (carcass + >=2), desk (top + 4 legs),
    chair (seat + back). Bed envelope must equal BED_ENV exactly."""
    oid, errs = opt["id"], []
    ids = {s["id"] for s in opt["solids"]}
    byid = {s["id"]: s for s in opt["solids"]}
    bed_ids = [f"{oid}_bed_base", f"{oid}_bed_frame", f"{oid}_bed_mattress",
               f"{oid}_bed_head", f"{oid}_bed_pillow0", f"{oid}_bed_pillow1"]
    for b in bed_ids:
        if b not in ids:
            errs.append(f"missing {b}")
    n_doors = sum(1 for i in ids if i.startswith(f"{oid}_ward_door"))
    if f"{oid}_ward_carcass" not in ids:
        errs.append(f"missing {oid}_ward_carcass")
    if n_doors < 2:
        errs.append(f"wardrobe doors={n_doors} <2")
    bx, by, bw, bd, head = BED_ENV[oid]
    base = byid.get(f"{oid}_bed_base")
    if base and (base["x"], base["y"], base["w"], base["d"]) != (bx, by, bw, bd):
        errs.append(f"bed envelope {(base['x'], base['y'], base['w'], base['d'])}"
                    f" != {(bx, by, bw, bd)}")
    if oid == "0":
        for t in ("0_table1", "0_table2"):
            if t not in ids:
                errs.append(f"missing {t}")
        for bad in [f"{oid}_desk_top", f"{oid}_chair_seat"]:
            if bad in ids:
                errs.append(f"unexpected {bad} in option 0")
    else:
        for need in [f"{oid}_desk_top"] + [f"{oid}_desk_leg{i}" for i in range(4)] \
                + [f"{oid}_chair_seat", f"{oid}_chair_back"]:
            if need not in ids:
                errs.append(f"missing {need}")
    return errs


def run_check():
    """Returns (lines, ok). Prints per-option counts/areas/bbox; asserts areas
    within +/-0.1 m2, every solid inside the shell envelope, required parts
    manifest, no undeclared furniture interpenetration, and no
    furniture-in-wall intersection."""
    model = build_model()
    lines, ok = [], True
    x0, y0, z0, x1, y1, z1 = ENV
    for opt in model["options"]:
        oid = opt["id"]
        study, bed = zone_areas(oid)
        total = study + bed if oid in "ABC" else bed
        exp = EXPECTED[oid]
        got = (round(study, 1), round(bed, 1), round(total, 1))
        area_ok = all(abs(g - e) <= 0.1 + 1e-9 for g, e in zip(got, exp))
        area_ok = area_ok and opt["areas"] == {
            "study_m2": exp[0], "bedroom_m2": exp[1], "total_m2": exp[2]}
        outside = [s["id"] for s in opt["solids"]
                   if not (s["x"] >= x0 - 1e-9 and s["y"] >= y0 - 1e-9
                           and s["z"] >= z0 - 1e-9
                           and s["x"] + s["w"] <= x1 + 1e-9
                           and s["y"] + s["d"] <= y1 + 1e-9
                           and s["z"] + s["h"] <= z1 + 1e-9)]
        bad, kinds = overlap_pairs(opt["solids"])
        furn_bad, wall_bad = [], []
        for a, b in bad:
            ka, kb = kinds[a], kinds[b]
            if ka in WALL_KINDS and kb in WALL_KINDS:
                continue  # coplanar wall fragments / parapet slats butt-join
            if ({ka, kb} <= FURN_KINDS
                    and (a, b) in {(f"{oid}_bed_base", f"{oid}_bed_head"),
                                  (f"{oid}_bed_head", f"{oid}_bed_base")}):
                continue  # headboard butt-joins the plinth panel (declared)
            (wall_bad if (ka in WALL_KINDS or kb in WALL_KINDS)
             else furn_bad).append(f"{a}~{b}")
        b = opt["bbox"]
        manifest = manifest_errors(opt)
        status = ("OK" if (area_ok and not outside and not furn_bad
                           and not wall_bad and not manifest) else "FAIL")
        if status == "FAIL":
            ok = False
        lines.append(
            f"{oid} {opt['title']}: solids={len(opt['solids'])} "
            f"study={got[0]:.1f} bedroom={got[1]:.1f} total={got[2]:.1f} "
            f"bbox=({b['x']:.0f},{b['y']:.0f},{b['z']:.0f} +"
            f"{b['w']:.0f}x{b['d']:.0f}x{b['h']:.0f}) "
            f"outside={outside if outside else 'none'} "
            f"manifest={manifest if manifest else 'ok'} "
            f"furn_overlap={furn_bad if furn_bad else 'none'} "
            f"wall_hit={wall_bad if wall_bad else 'none'} {status}")
    return lines, ok


def write_viewer_html(out_path):
    """Regenerate the self-contained viewer with the model JSON embedded.

    Reads three.min.js + OrbitControls.js from src/homedesign/assets (as-is,
    never modified) and viewer_page_template.html from this directory, then
    substitutes __THREE_JS__ / __ORBIT_CONTROLS__ / the model JSON. The page
    makes no external requests, so it works from file:// and over http."""
    here = Path(__file__).resolve().parent
    repo = here.parent.parent.parent
    assets = repo / "src" / "homedesign" / "assets"
    template = (here / "viewer_page_template.html").read_text(encoding="utf-8")
    three = (assets / "three.min.js").read_text(encoding="utf-8")
    orbit = (assets / "OrbitControls.js").read_text(encoding="utf-8")
    model = build_model()
    for marker in ("__THREE_JS__", "__ORBIT_CONTROLS__",
                   "/*__MODEL_JSON__*/var MODEL = null;"):
        if marker not in template:
            raise SystemExit(f"template marker missing: {marker}")
    html = template.replace("__THREE_JS__", three)
    html = html.replace("__ORBIT_CONTROLS__", orbit)
    payload = json.dumps(model, ensure_ascii=False, separators=(",", ":"))
    html = html.replace("/*__MODEL_JSON__*/var MODEL = null;",
                        "var MODEL = " + payload + ";")
    Path(out_path).write_text(html, encoding="utf-8")
    print(f"wrote {out_path}: {len(html)} bytes, "
          f"{len(model['options'])} options embedded")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--viewer", default=None,
                    help="write self-contained viewer HTML to this path")
    args = ap.parse_args(argv)
    if args.check:
        lines, ok = run_check()
        print("\n".join(lines))
        return 0 if ok else 1
    if args.viewer:
        write_viewer_html(args.viewer)
        return 0
    if args.out:
        model = build_model()
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(model, fh, ensure_ascii=False, indent=1)
        print(f"wrote {args.out}: "
              f"{len(model['options'])} options, "
              f"{sum(len(o['solids']) for o in model['options'])} solids")
        return 0
    ap.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
