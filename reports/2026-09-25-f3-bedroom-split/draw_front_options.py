"""Floor-3 rear-bedroom split study — scale drawings (SVG; PNG via MuPDF).

Source of truth:
  * designs/contractor-as-drawn.json  — compiled model (plot, core, stair, lobby)
  * contractor/MB 2-3-4-Model.pdf     — sheet "MẶT BẰNG TẦNG 2,3" (left plan),
    printed chain from the rear wall: 200 wall / 1600 WC+LÔ GIA / 4100 P.NGỦ /
    1800 lobby / 3200 stair.  The model as committed has the last two bands the
    other way round; this study uses the sheet's reading.

Outputs: f3-base-plan.svg / .png, f3-split-options.svg / .png
"""
from __future__ import annotations

import math
import os

A3W, A3H = 420.0, 297.0

# ---------------------------------------------------------------- geometry (mm)
PLOT_X0, PLOT_X1 = 0.0, 3960.0
IN_X0, IN_X1 = 200.0, 3760.0
WIDTH_CLEAR = IN_X1 - IN_X0                     # 3560
STAIR_Y0, STAIR_Y1 = 12300.0, 16300.0
LOBBY_Y0, LOBBY_Y1 = 16300.0, 17900.0
BED_Y0, BED_Y1 = 17900.0, 22000.0               # rear bedroom, gross = 4100
BAND_Y0, BAND_Y1 = 22000.0, 23600.0             # WC + lô gia band = 1600
REARW_Y1 = 23800.0
WC_X1 = 2200.0
LOGGIA_X0 = 2300.0
EXT, PART = 200.0, 100.0

DOOR_ENTRY = (300.0, 1200.0)      # lobby -> bedroom, front wall, west
DOOR_WC = (800.0, 1700.0)         # wc -> bedroom
DOOR_LOGGIA = (2500.0, 3400.0)    # bedroom -> lô gia

C_WALL, C_OLD = "#20242a", "#3d4247"
C_NEW, C_NEW_L = "#e8590c", "#fde3d3"
C_BED, C_WORK, C_STORE, C_FIX = "#cfe0f0", "#ffe9c9", "#e9e3d6", "#eef1f3"
C_GLASS = "#2f6fb0"
C_TXT, C_DIM, C_MUTE = "#15181b", "#6b7280", "#5a6167"
C_BG = "#ffffff"


class Sheet:
    def __init__(self) -> None:
        self.parts: list[str] = [f'<rect x="0" y="0" width="{A3W}" height="{A3H}" fill="{C_BG}"/>']

    def rect(self, x, y, w, h, fill, stroke="none", sw=0.12, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def line(self, x1, y1, x2, y2, stroke=C_WALL, sw=0.15, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}/>')

    def circle(self, cx, cy, r, fill=C_WALL, stroke="none", sw=0.1):
        self.parts.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" '
                          f'stroke="{stroke}" stroke-width="{sw}"/>')

    def text(self, x, y, s, size=2.4, fill=C_TXT, anchor="start", weight="normal", rot=None):
        tr = f' transform="rotate({rot} {x:.2f} {y:.2f})"' if rot else ""
        self.parts.append(
            f'<text x="{x:.2f}" y="{y:.2f}" font-family="Segoe UI,Arial,Helvetica" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"'
            f'{tr}>{s}</text>')

    def save(self, path: str) -> None:
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{A3W}mm" height="{A3H}mm" '
               f'viewBox="0 0 {A3W} {A3H}">\n' + "\n".join(self.parts) + "\n</svg>\n")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(svg)


class Panel:
    def __init__(self, sheet, win, dst):
        x0, y0, w, d = win
        px, py, pw, ph = dst
        self.s = min(pw / w, ph / d)
        self.ox = px + (pw - w * self.s) / 2.0
        self.oy = py + (ph - d * self.s) / 2.0
        self.win, self.sh = win, sheet

    def p(self, x, y):
        return (self.ox + (x - self.win[0]) * self.s,
                self.oy + (self.win[1] + self.win[3] - y) * self.s)

    def m(self, v):
        return v * self.s

    # world-space primitives
    def rect_mm(self, x, y, w, d, **kw):
        X, Y = self.p(x, y + d)
        self.sh.rect(X, Y, self.m(w), self.m(d), **kw)

    def line_mm(self, x1, y1, x2, y2, **kw):
        a, b = self.p(x1, y1), self.p(x2, y2)
        self.sh.line(a[0], a[1], b[0], b[1], **kw)

    def wall(self, x, y, w, d, fill=C_WALL):
        self.rect_mm(x, y, w, d, fill=fill)

    def circle_mm(self, cx, cy, r_mm, **kw):
        X, Y = self.p(cx, cy)
        self.sh.circle(X, Y, self.m(r_mm), **kw)

    def label(self, x, y, s, size=2.3, fill=C_TXT, weight="normal", anchor="middle"):
        X, Y = self.p(x, y)
        self.sh.text(X, Y, s, size=size, fill=fill, weight=weight, anchor=anchor)

    def label_rot(self, x, y, s, size=2.1, fill=C_TXT):
        X, Y = self.p(x, y)
        self.sh.text(X, Y + size * 0.35, s, size=size, fill=fill, anchor="start", rot=-90)

    def dim_h(self, x1, x2, y, label, off=380.0, size=1.9):
        X1, Y = self.p(x1, y)[0], self.p(x1, y)[1]
        X2 = self.p(x2, y)[0]
        Yd = Y - self.m(off)
        self.sh.line(X1, Yd, X2, Yd, stroke=C_DIM, sw=0.12)
        for X in (X1, X2):
            self.sh.line(X, Yd - self.m(110), X, Yd + self.m(110), stroke=C_DIM, sw=0.12)
        mid = (X1 + X2) / 2.0
        self.sh.rect(mid - 6.0, Yd - 2.0, 12.0, 3.4, fill=C_BG)
        self.sh.text(mid, Yd + 1.0, label, size=size, anchor="middle", fill=C_DIM)

    def dim_v(self, y1, y2, x, label, off=420.0, size=1.9, side=1):
        Y1 = self.p(x, y1)[1]
        Y2 = self.p(x, y2)[1]
        X = self.p(x, y1)[0] + self.m(off) * side
        self.sh.line(X, Y1, X, Y2, stroke=C_DIM, sw=0.12)
        for Y in (Y1, Y2):
            self.sh.line(X - self.m(110), Y, X + self.m(110), Y, stroke=C_DIM, sw=0.12)
        mid = (Y1 + Y2) / 2.0
        self.sh.rect(X - 2.0, mid - 6.0, 3.4, 12.0, fill=C_BG)
        self.sh.text(X + 1.0, mid, label, size=size, fill=C_DIM, anchor="middle", rot=-90)


# --------------------------------------------------------------- furnishings
def bed(p, x, y, w, d, head):
    p.rect_mm(x, y, w, d, fill=C_BED, stroke="#7d95ab", sw=0.1)
    t = 110.0
    if head == "east":
        p.rect_mm(x + w - t, y, t, d, fill="#a9c4dc", stroke="#7d95ab", sw=0.1)
        p.rect_mm(x + w - t - 430, y + 180, 430, (d - 3 * 180) / 2, fill=C_BG,
                  stroke="#9db3c7", sw=0.1)
        p.rect_mm(x + w - t - 430, y + d / 2 + 90, 430, (d - 3 * 180) / 2, fill=C_BG,
                  stroke="#9db3c7", sw=0.1)
    elif head == "west":
        p.rect_mm(x, y, t, d, fill="#a9c4dc", stroke="#7d95ab", sw=0.1)
        p.rect_mm(x + t + 60, y + 180, 430, (d - 3 * 180) / 2, fill=C_BG,
                  stroke="#9db3c7", sw=0.1)
        p.rect_mm(x + t + 60, y + d / 2 + 90, 430, (d - 3 * 180) / 2, fill=C_BG,
                  stroke="#9db3c7", sw=0.1)
    else:  # north
        p.rect_mm(x, y + d - t, w, t, fill="#a9c4dc", stroke="#7d95ab", sw=0.1)
        p.rect_mm(x + 180, y + d - t - 430, (w - 3 * 180) / 2, 430, fill=C_BG,
                  stroke="#9db3c7", sw=0.1)
        p.rect_mm(x + w / 2 + 90, y + d - t - 430, (w - 3 * 180) / 2, 430, fill=C_BG,
                  stroke="#9db3c7", sw=0.1)


def desk(p, x, y, w, d, chairs=2, face="north"):
    """face = side the user sits on."""
    p.rect_mm(x, y, w, d, fill=C_WORK, stroke="#c98f2e", sw=0.14)
    n = chairs
    if w >= d:
        for i in range(n):
            cx = x + w * (i + 1) / (n + 1)
            cy = (y + d + 330) if face == "north" else (y - 330)
            p.circle_mm(cx, cy, 240, fill="#cdd5dc", stroke="#8a939c", sw=0.1)
    else:
        for i in range(n):
            cy = y + d * (i + 1) / (n + 1)
            cx = (x + w + 330) if face == "north" else (x - 330)
            p.circle_mm(cx, cy, 240, fill="#cdd5dc", stroke="#8a939c", sw=0.1)


def wardrobe(p, x, y, w, d, doors_along="w"):
    p.rect_mm(x, y, w, d, fill=C_STORE, stroke="#a89a80", sw=0.14)
    if doors_along == "w":
        n = max(2, int(w / 600))
        for i in range(1, n):
            p.line_mm(x + i * w / n, y, x + i * w / n, y + d, stroke="#a89a80", sw=0.08)
    else:
        n = max(2, int(d / 600))
        for i in range(1, n):
            p.line_mm(x, y + i * d / n, x + w, y + i * d / n, stroke="#a89a80", sw=0.08)


def wc_fixtures(p, x, y, w, d):
    p.rect_mm(x, y, w, d, fill=C_FIX, stroke="#9aa3ab", sw=0.1)
    p.rect_mm(x + 250, y + 200, 420, 620, fill=C_BG, stroke="#9aa3ab", sw=0.1)
    p.circle_mm(x + 460, y + 300, 190, fill=C_BG, stroke="#9aa3ab", sw=0.08)
    p.rect_mm(x + w - 1050, y + 250, 800, 480, fill=C_BG, stroke="#9aa3ab", sw=0.1)


def leaf(p, hx, hy, w_mm, a0, a1):
    r = p.m(w_mm)
    X, Y = p.p(hx, hy)
    x1 = X + r * math.cos(math.radians(a0))
    y1 = Y - r * math.sin(math.radians(a0))
    x2 = X + r * math.cos(math.radians(a1))
    y2 = Y - r * math.sin(math.radians(a1))
    p.sh.line(X, Y, x2, y2, stroke=C_TXT, sw=0.18)
    large = 1 if abs(a1 - a0) > 180 else 0
    sweep = 1 if (a1 - a0) % 360 < 180 else 0
    p.sh.parts.append(
        f'<path d="M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 {large} {sweep} {x2:.2f} {y2:.2f}" '
        f'fill="none" stroke="{C_TXT}" stroke-width="0.13" stroke-dasharray="0.9 0.6"/>')


def cut(p, x, y, w, d):
    p.rect_mm(x, y, w, d, fill=C_BG)


def sliding(p, x, y, w, d, vertical):
    if vertical:
        cut(p, x - 40, y, d + 80, w)
        p.line_mm(y + d * 0.28, x - 30, y + d * 0.28, x + w * 0.55, stroke=C_NEW, sw=0.22)
        p.line_mm(y + d * 0.72, x + w * 0.45, y + d * 0.72, x + w + 30, stroke=C_NEW, sw=0.22)
    else:
        p.line_mm(x - 30, y + d * 0.28, x + w * 0.55, y + d * 0.28, stroke=C_NEW, sw=0.22)
        p.line_mm(x + w * 0.45, y + d * 0.72, x + w + 30, y + d * 0.72, stroke=C_NEW, sw=0.22)


def hinge_door(p, hx, hy, w_mm, a0, a1):
    cut(p, hx - 40, hy - 40, 80, 80) if False else None
    leaf(p, hx, hy, w_mm, a0, a1)


# ------------------------------------------------------------- shell drawing
def shell(sheet, p: Panel, new_walls=(), furn=True):
    """Walls in draw order: tints -> furniture(fixtures) -> walls -> doors."""
    # ---- room tints (drawn first so walls sit on top)
    p.rect_mm(0, LOBBY_Y0, 3960, LOBBY_Y1 - LOBBY_Y0, fill="#fbfbfc")
    p.rect_mm(0, LOBBY_Y1, 3960, BAND_Y1 - LOBBY_Y1, fill="#faf7f1")
    p.rect_mm(LOGGIA_X0, BAND_Y0, IN_X1 - LOGGIA_X0, BAND_Y1 - BAND_Y0, fill="#eaf3ea",
              stroke="#9ab89a", sw=0.1)
    # ---- fixtures / fixed furniture
    wc_fixtures(p, 260, BAND_Y0 + 90, WC_X1 - 260, BAND_Y1 - BAND_Y0 - 180)
    # ---- walls
    p.wall(0, STAIR_Y0 - 500, EXT, (BAND_Y1 - STAIR_Y0) + 500)
    p.wall(IN_X1, STAIR_Y0 - 500, EXT, (BAND_Y1 - STAIR_Y0) + 500)
    p.wall(0, BAND_Y1, 3960, EXT)                                   # rear wall
    p.wall(0, LOBBY_Y1 - PART / 2, IN_X1 + EXT, PART, fill=C_OLD)    # lobby | bedroom
    p.wall(IN_X0, BAND_Y1 - PART - 50, IN_X1 - IN_X0, PART, fill=C_OLD)  # bedroom | band
    p.wall(WC_X1, BAND_Y0, PART, BAND_Y1 - BAND_Y0, fill=C_OLD)      # wc | lô gia
    # ---- openings in the old walls
    cut(p, DOOR_ENTRY[0], LOBBY_Y1 - PART / 2 - 20, DOOR_ENTRY[1] - DOOR_ENTRY[0], PART + 40)
    leaf(p, DOOR_ENTRY[0], LOBBY_Y1, DOOR_ENTRY[1] - DOOR_ENTRY[0], 0, 90)
    cut(p, DOOR_WC[0], BAND_Y1 - PART - 70, DOOR_WC[1] - DOOR_WC[0], PART + 40)
    leaf(p, DOOR_WC[0], BAND_Y1 - PART - 50, DOOR_WC[1] - DOOR_WC[0], 0, 90)
    cut(p, DOOR_LOGGIA[0], BAND_Y1 - PART - 70, DOOR_LOGGIA[1] - DOOR_LOGGIA[0], PART + 40)
    leaf(p, DOOR_LOGGIA[1], BAND_Y1 - PART - 50, DOOR_LOGGIA[1] - DOOR_LOGGIA[0], 180, 90)
    # loggia railing
    p.line_mm(LOGGIA_X0, BAND_Y1 - 70, IN_X1, BAND_Y1 - 70, stroke="#2f7a2f", sw=0.3)
    # ---- new walls on top
    for (x, y, w, d) in new_walls or ():
        p.wall(x, y, w, d, fill=C_NEW)



# ============================================================== FRONT ROOM ===
# The FRONT bedroom of tầng 3 (the one with the ban công). Same helpers as the
# rear study; geometry below is read from MB 2-3-4-Model.pdf (left plan) and the
# compiled model's resolved openings.

BALC_Y0, BALC_Y1 = 3500.0, 4900.0
FB_Y0, FB_Y1 = 4900.0, 8900.0            # front bedroom, gross = 4000
FWC_Y0, FWC_Y1 = 8900.0, 10500.0         # WC + hall band = 1600
HF_Y0, HF_Y1 = 10500.0, 12300.0          # hall to the core = 1800
FWC_X1 = 1950.0
FSTOREY = 3400.0

BALC_DOOR = (200.0, 1100.0)              # balcony -> bedroom, west ('start')
BALC_WIN = (2360.0, 3760.0)              # balcony -> bedroom, east ('end'), 1400
WC_DOOR = (525.0, 1425.0)                # centred on the WC's 1950
HALL_DOOR = (2505.0, 3405.0)             # centred on the hall's 2010
FB_CLEAR = (200.0, 3760.0, 4950.0, 8850.0)   # x0, x1, y0, y1


def leaf_noarc(p, hx, hy, w_mm, a0, a1, arc=True):
    r = p.m(w_mm)
    X, Y = p.p(hx, hy)
    x2 = X + r * math.cos(math.radians(a1))
    y2 = Y - r * math.sin(math.radians(a1))
    p.sh.line(X, Y, x2, y2, stroke=C_TXT, sw=0.18)
    if arc:
        x1 = X + r * math.cos(math.radians(a0))
        y1 = Y - r * math.sin(math.radians(a0))
        p.sh.parts.append(
            f'<path d="M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 0 1 {x2:.2f} {y2:.2f}" '
            f'fill="none" stroke="{C_TXT}" stroke-width="0.13" stroke-dasharray="0.9 0.6"/>')


def shell_front(s, p: Panel, new_walls=(), base=False):
    """Balcony + front bedroom shell; walls on top of tint/furniture."""
    # tints
    p.rect_mm(0, BALC_Y0, 3960, BALC_Y1 - BALC_Y0, fill="#eef4ee")
    p.rect_mm(0, FB_Y0, 3960, FB_Y1 - FB_Y0, fill="#faf7f1")
    p.rect_mm(0, FWC_Y0, 3960, FWC_Y1 - FWC_Y0, fill="#f4f6f8")
    wc_fixtures(p, 220, FWC_Y0 + 90, FWC_X1 - 100 - 220, FWC_Y1 - FWC_Y0 - 180)
    # walls
    p.wall(0, BALC_Y0 - 200, EXT, (HF_Y1 - BALC_Y0) + 200)
    p.wall(IN_X1, BALC_Y0 - 200, EXT, (HF_Y1 - BALC_Y0) + 200)
    p.wall(0, BALC_Y0 - EXT, 3960, EXT)                      # balcony front wall
    p.wall(0, BALC_Y1 - PART / 2, IN_X1 + EXT, PART, fill=C_OLD)      # balcony | bedroom
    p.wall(IN_X0, FB_Y1 - PART / 2, IN_X1 - IN_X0, PART, fill=C_OLD)  # bedroom | band
    p.wall(FWC_X1 - PART / 2, FWC_Y0, PART, FWC_Y1 - FWC_Y0, fill=C_OLD)
    p.wall(0, FWC_Y1 - PART / 2, IN_X1 + EXT, PART, fill=C_OLD)       # band | hall_front
    # balcony openings: door (west) + window (east)
    cut(p, BALC_DOOR[0], BALC_Y1 - PART / 2 - 25, BALC_DOOR[1] - BALC_DOOR[0], PART + 50)
    leaf_noarc(p, BALC_DOOR[1], BALC_Y1, BALC_DOOR[1] - BALC_DOOR[0], 180, 90)
    cut(p, BALC_WIN[0], BALC_Y1 - PART / 2 - 25, BALC_WIN[1] - BALC_WIN[0], PART + 50)
    for o in (-60, 0, 60):
        p.line_mm(BALC_WIN[0], BALC_Y1 + o, BALC_WIN[1], BALC_Y1 + o, stroke=C_GLASS, sw=0.1)
    # band doors (leaf only — the swings land on furniture at this size)
    cut(p, WC_DOOR[0], FB_Y1 - PART / 2 - 25, WC_DOOR[1] - WC_DOOR[0], PART + 50)
    leaf_noarc(p, WC_DOOR[0], FB_Y1, WC_DOOR[1] - WC_DOOR[0], 0, 90, arc=base)
    cut(p, HALL_DOOR[0], FB_Y1 - PART / 2 - 25, HALL_DOOR[1] - HALL_DOOR[0], PART + 50)
    leaf_noarc(p, HALL_DOOR[1], FB_Y1, HALL_DOOR[1] - HALL_DOOR[0], 180, 90, arc=base)
    # balcony parapet on the open edge
    p.line_mm(0, BALC_Y0 - 30, 3960, BALC_Y0 - 30, stroke="#2f7a2f", sw=0.35)
    # new walls on top
    for (x, y, w, d) in new_walls or ():
        p.wall(x, y, w, d, fill=C_NEW)


def front_base_furniture(p: Panel):
    bed(p, 1760, 5000, 2000, 1600, head="east")
    p.rect_mm(1200, 5000, 450, 450, fill=C_STORE, stroke="#a89a80", sw=0.1)
    p.rect_mm(1200, 6150, 450, 450, fill=C_STORE, stroke="#a89a80", sw=0.1)
    wardrobe(p, 200, 8300, 1400, 600, doors_along="w")


# ------------------------------------------------------------------- options
def opt_a2(s, p: Panel):
    """Study at the balcony (stud wall)."""
    py_ = 6600.0
    shell_front(s, p, new_walls=[(IN_X0, py_, IN_X1 - IN_X0, PART)])
    p.rect_mm(IN_X0, FB_Y0, IN_X1 - IN_X0, py_ - FB_Y0, fill="#fdf7ef")
    cut(p, 300, py_ - 30, 1200, PART + 60)
    p.line_mm(300 + 1200 * 0.28, py_ + PART * 0.3, 300 + 1200 * 0.55, py_ + PART * 0.3,
              stroke=C_NEW, sw=0.22)
    p.line_mm(300 + 1200 * 0.45, py_ + PART * 0.7, 300 + 1200 + 30, py_ + PART * 0.7,
              stroke=C_NEW, sw=0.22)
    p.label(700, 6100, "CỬA TRƯỢT 1200", size=1.8, fill=C_NEW)
    desk(p, 2300, FB_Y0 + 60, 1400, 650, chairs=1, face="north")
    p.label(800, FB_Y0 + 1250, "BÀN LÀM VIỆC", size=1.9, weight="bold")
    p.label(800, FB_Y0 + 850, "5.9 m²", size=1.9, weight="bold", fill=C_MUTE)
    bed(p, 1000, 6800, 1600, 2000, head="north")
    wardrobe(p, 3160, 6800, 600, 1000, doors_along="d")
    p.label(800, 8400, "P. NGỦ 7.7 m²", size=1.9, weight="bold")


def opt_b2(s, p: Panel):
    """Side split — study east with the window and the entry."""
    px_ = 2200.0
    shell_front(s, p, new_walls=[(px_, FB_Y0, PART, FB_Y1 - FB_Y0)])
    p.rect_mm(px_ + PART, FB_Y0, IN_X1 - (px_ + PART), FB_Y1 - FB_Y0, fill="#fdf7ef")
    cut(p, px_ - 30, 7600, PART + 60, 900)
    leaf_noarc(p, px_, 7600 + 900, 900, 0, -90)
    desk(p, 2500, FB_Y0 + 60, 1260, 650, chairs=1, face="north")
    p.label(3100, 7500, "BÀN LÀM VIỆC", size=1.9, weight="bold")
    p.label(3100, 7150, "5.7 m²", size=1.9, weight="bold", fill=C_MUTE)
    bed(p, IN_X0, 5700, 2000, 1600, head="east")
    wardrobe(p, 1240, FB_Y0 + 60, 960, 600, doors_along="w")
    p.label(800, 8300, "P. NGỦ 7.8 m²", size=1.9, weight="bold")


def opt_c2(s, p: Panel):
    """Glazed study at the rear; bedroom keeps the balcony and the light."""
    py_ = 7250.0
    shell_front(s, p, new_walls=[])
    # glazed partition: two blue lines with hatch ticks
    for o in (-55, 55):
        p.line_mm(IN_X0, py_ + o, IN_X1, py_ + o, stroke=C_GLASS, sw=0.3)
    for i in range(24):
        x = IN_X0 + 60 + i * 150
        p.line_mm(x, py_ - 55, x, py_ + 55, stroke="#bcd4ea", sw=0.12)
    p.label(1100, py_ - 900, "VÁCH KÍNH", size=1.8, fill=C_GLASS)
    p.rect_mm(0, py_, 3960, FWC_Y0 - py_, fill="#eef5fb")
    cut(p, 1500, py_ - 40, 900, 80)
    leaf_noarc(p, 1500, py_ + 55, 900, 0, -85)
    desk(p, 2300, py_ + 200, 1400, 650, chairs=1, face="north")
    p.label(900, 8200, "BÀN LÀM VIỆC", size=1.9, weight="bold")
    p.label(900, 7850, "5.5 m² · sáng qua kính", size=1.7, weight="bold", fill=C_MUTE)
    bed(p, 1250, 5250, 1600, 2000, head="south")
    wardrobe(p, 3160, 5500, 600, 1650, doors_along="d")
    p.label(1100, 6300, "P. NGỦ 8.0 m²", size=1.9, weight="bold")


def opt_d2(s, p: Panel):
    """Open studio + track curtain, desk at the window."""
    shell_front(s, p, new_walls=[])
    desk(p, 2300, FB_Y0 + 60, 1400, 650, chairs=1, face="north")
    p.label(1150, FB_Y0 + 1500, "BÀN LÀM VIỆC", size=1.9, weight="bold")
    bed(p, 1250, 6850, 1600, 2000, head="north")
    wardrobe(p, 1200, FB_Y0 + 60, 1100, 600, doors_along="w")
    p.line_mm(IN_X0, 6700, IN_X1, 6700, stroke="#7a4bd0", sw=0.3, dash="3 1.5")
    p.label(1750, 6350, "RÈM / VÁCH DI ĐỘNG", size=1.7, fill="#7a4bd0")
    p.label(750, 8400, "P. NGỦ 13.9 m²", size=1.9, weight="bold")


# ------------------------------------------------------------------- sheets
def front_base_sheet(path):
    sh = Sheet()
    sh.text(12, 13.5, "TẦNG 3 — front bedroom (with ban công), as drawn",
            size=4.4, weight="bold")
    sh.text(12, 19.0, "Source: contractor/MB 2-3-4-Model.pdf, left plan “MẶT BẰNG TẦNG 2,3”.  "
                      "Printed depth 4000; balcony 1400 recessed; rear band 1600 with WC 1950 "
                      "+ hall beside it.", size=2.3, fill=C_MUTE)
    win = (-1700.0, 3200.0, 3960 + 2900, 9400.0)
    p = Panel(sh, win, (14.0, 24.0, 78.0, 152.0))
    p.rect_mm(0, BALC_Y0, 3960, BALC_Y1 - BALC_Y0, fill="#eef4ee")
    p.rect_mm(0, FB_Y0, 3960, FB_Y1 - FB_Y0, fill="#faf7f1")
    p.rect_mm(0, FWC_Y0, 3960, HF_Y1 - FWC_Y0, fill="#f4f6f8")
    wc_fixtures(p, 220, FWC_Y0 + 90, FWC_X1 - 100 - 220, FWC_Y1 - FWC_Y0 - 180)
    front_base_furniture(p)
    p.rect_mm(0, HF_Y0, 3960, HF_Y1 - HF_Y0, fill="#fbfbfc")
    p.label(1000, 11400, "HÀNH LANG", size=1.8, fill="#8a939c")
    p.wall(0, BALC_Y0 - 500, EXT, (HF_Y1 - BALC_Y0) + 500)
    p.wall(IN_X1, BALC_Y0 - 500, EXT, (HF_Y1 - BALC_Y0) + 500)
    p.wall(0, BALC_Y0 - EXT, 3960, EXT)
    p.wall(0, BALC_Y1 - PART / 2, IN_X1 + EXT, PART, fill=C_OLD)
    p.wall(IN_X0, FB_Y1 - PART / 2, IN_X1 - IN_X0, PART, fill=C_OLD)
    p.wall(FWC_X1 - PART / 2, FWC_Y0, PART, FWC_Y1 - FWC_Y0, fill=C_OLD)
    p.wall(0, FWC_Y1 - PART / 2, IN_X1 + EXT, PART, fill=C_OLD)
    cut(p, BALC_DOOR[0], BALC_Y1 - PART / 2 - 25, BALC_DOOR[1] - BALC_DOOR[0], PART + 50)
    leaf(p, BALC_DOOR[1], BALC_Y1, BALC_DOOR[1] - BALC_DOOR[0], 180, 90)
    cut(p, BALC_WIN[0], BALC_Y1 - PART / 2 - 25, BALC_WIN[1] - BALC_WIN[0], PART + 50)
    for o in (-60, 0, 60):
        p.line_mm(BALC_WIN[0], BALC_Y1 + o, BALC_WIN[1], BALC_Y1 + o, stroke=C_GLASS, sw=0.1)
    cut(p, WC_DOOR[0], FB_Y1 - PART / 2 - 25, WC_DOOR[1] - WC_DOOR[0], PART + 50)
    leaf(p, WC_DOOR[0], FB_Y1, WC_DOOR[1] - WC_DOOR[0], 0, 90)
    cut(p, HALL_DOOR[0], FB_Y1 - PART / 2 - 25, HALL_DOOR[1] - HALL_DOOR[0], PART + 50)
    leaf(p, HALL_DOOR[1], FB_Y1, HALL_DOOR[1] - HALL_DOOR[0], 180, 90)
    p.line_mm(0, BALC_Y0 - 30, 3960, BALC_Y0 - 30, stroke="#2f7a2f", sw=0.35)
    p.label(1700, 8000, "P. NGỦ (trước)", size=2.3, weight="bold")
    p.label(1700, 7600, "lọt lòng ~3900 × 3560 ≈ 13.9 m²", size=1.9, fill=C_MUTE)
    p.label(2050, 4200, "BAN CÔNG 1400", size=1.9, fill="#2f7a2f")
    p.label(950, 9700, "WC 1950", size=1.9, fill="#4c6b8a")
    p.label(2900, 9700, "HÀNH LANG", size=1.8, fill="#8a939c")
    p.dim_v(FB_Y0, FB_Y1, IN_X1, "4000", off=520)
    p.dim_v(FWC_Y0, FWC_Y1, IN_X1, "1600", off=520)
    p.dim_h(BALC_DOOR[0], BALC_WIN[1], FB_Y1, "door 900 + window 1400", off=560)
    p.dim_h(IN_X0, IN_X1, BALC_Y0, "3560", off=420)

    bx = 104.0
    sh.line(bx - 8, 26, bx - 8, 176, stroke="#e2e6ea", sw=0.3)
    y = 34.0
    sh.text(bx, y, "What the sheet gives", size=3.0, weight="bold")
    y += 6.0
    for ln in [
        "· Front bedroom 4000 (printed) × 3560 outer → lọt",
        "   lòng ~3900 × 3560 ≈ 13.9 m².",
        "· Balcony (ban công) 1400 deep at the street, recessed,",
        "   with a 900 door (west) + a 1400 window (east).",
        "· Together they are the room's daylight — the only",
        "   light source, since both side walls are party walls.",
        "· Rear band: WC 1950 wide (west) + hall 2010 (east),",
        "   both 1600 deep, both doors opening into the bedroom.",
        "· Entry comes from that hall, at the rear-EAST: the",
        "   stair core and the lift sit behind it.",
        "· In the drawing: bed head on the east wall with the",
        "   bedside tables, wardrobe on the WC wall.",
    ]:
        sh.text(bx, y, ln, size=2.3, fill=C_MUTE)
        y += 4.2
    y += 3.0
    sh.text(bx, y, "What that means for a split", size=3.0, weight="bold")
    y += 6.0
    for ln in [
        "· Light lives at the STREET end: any desk wants the",
        "   balcony side (window + door), not the core side.",
        "· There is only ONE way in, at the rear-east, so a",
        "   front/rear split makes one zone a walk-through —",
        "   whichever zone you do not put the entry in.",
        "· The WC door is at the rear-west, the entry at the",
        "   rear-east: the middle of the rear wall is the only",
        "   place furniture can stand against it.",
        "· A side (front-to-rear) split can give each zone its",
        "   own door: the east strip takes the entry, the west",
        "   strip keeps the balcony door and the WC.",
    ]:
        sh.text(bx, y, ln, size=2.3, fill=C_MUTE)
        y += 4.2
    sh.text(12, 192, "This sheet is the base for the four front-room split options; all four keep "
                     "the balcony, the WC and the entry door where the drawing puts them.",
            size=2.3, fill=C_MUTE)
    sh.save(path)


def front_options_sheet(path):
    sh = Sheet()
    sh.text(10, 12.5, "TẦNG 3 — front bedroom (ban công) 13.9 m² split into bedroom "
                      "+ workspace", size=4.4, weight="bold")
    sh.text(10, 18.0, "Four options, one desk, same scale.  Orange = new work; the balcony "
                      "(ban công) and the street are at the BOTTOM, the hall/stair at the top.",
            size=2.3, fill=C_MUTE)
    xs = [10.0, 112.0, 214.0, 316.0]
    win = (-600.0, 3250.0, 5160.0, 8100.0)
    fns = [("A", "Study at the balcony", opt_a2),
           ("B", "Side split — desk by the window", opt_b2),
           ("C", "Glazed study at the rear", opt_c2),
           ("D", "Open studio + curtain", opt_d2)]
    caps = {
        "A": [("BÀN LÀM VIỆC 5.9 m² · P.NGỦ 7.7 m²", C_TXT),
              ("Desk gets the window straight on — the", C_MUTE),
              ("only room in the set with direct light.", C_MUTE),
              ("Bedroom keeps its own WC; bedroom is", C_MUTE),
              ("the walk-through to the study.", C_MUTE),
              ("", C_MUTE),
              ("− Bedroom 2150 deep, and the WC/hall", "#8a4b2a"),
              ("   door swings land close to the bed.", "#8a4b2a")],
        "B": [("BÀN LÀM VIỆC 5.7 m² · P.NGỦ 7.8 m²", C_TXT),
              ("Each zone gets its own door: the east", C_MUTE),
              ("strip takes the window AND the entry,", C_MUTE),
              ("the west strip the balcony door and", C_MUTE),
              ("the WC. No crossing a bedroom.", C_MUTE),
              ("", C_MUTE),
              ("− Study only 1460 clear; bedroom 2000", "#8a4b2a"),
              ("   wide, so the bed spans it.", "#8a4b2a")],
        "C": [("BÀN LÀM VIỆC 5.5 m² · P.NGỦ 8.0 m²", C_TXT),
              ("Bedroom keeps balcony, window and WC", C_MUTE),
              ("at full size; the study is a 1500-deep", C_MUTE),
              ("glazed box at the core, taking the", C_MUTE),
              ("entry and the WC.", C_MUTE),
              ("", C_MUTE),
              ("− Desk has no window: light is borrowed", "#8a4b2a"),
              ("   through the glass; calls are exposed.", "#8a4b2a")],
        "D": [("13.9 m² kept whole — no wall", C_TXT),
              ("Desk at the window, bed at the core,", C_MUTE),
              ("one track curtain between them.", C_MUTE),
              ("Cheapest build, most light, nothing", C_MUTE),
              ("lost if the plan changes.", C_MUTE),
              ("", C_MUTE),
              ("− No acoustic separation: the desk is", "#8a4b2a"),
              ("   visible from the bed day and night.", "#8a4b2a")],
    }
    for (tag, title, fn), x in zip(fns, xs):
        p = Panel(sh, win, (x + 4.0, 24.0, 92.0, 152.0))
        fn(sh, p)
        sh.text(x + 3, 22.0, f"OPTION {tag}", size=3.2, weight="bold", fill=C_NEW)
        sh.text(x + 20.0, 22.0, title, size=2.5, weight="bold")
        for i, (ln, col) in enumerate(caps[tag]):
            sh.text(x + 3, 190.0 + i * 4.1, ln, size=2.2, fill=col)
        sh.rect(x, 10.5, 98.0, 182.0, fill="none", stroke="#d3d8dc", sw=0.25)
    sh.rect(10, 264, 400, 26, fill="#fbfcfd", stroke="#e2e6ea", sw=0.25)
    kx = 16
    sh.rect(kx, 269, 5, 5, fill=C_WALL)
    sh.text(kx + 7, 273, "tường / wall", size=2.1, fill=C_MUTE)
    sh.rect(kx + 40, 269, 5, 5, fill=C_NEW)
    sh.text(kx + 47, 273, "vách mới / new partition", size=2.1, fill=C_MUTE)
    sh.line(kx + 130, 271.5, kx + 140, 271.5, stroke=C_GLASS, sw=0.3)
    sh.text(kx + 143, 273, "kính / glazing", size=2.1, fill=C_MUTE)
    sh.line(kx + 176, 271.5, kx + 186, 271.5, stroke="#7a4bd0", sw=0.3, dash="3 1.5")
    sh.text(kx + 189, 273, "rèm / curtain", size=2.1, fill=C_MUTE)
    sh.rect(kx + 230, 269, 5, 5, fill=C_BED, stroke="#7d95ab", sw=0.1)
    sh.text(kx + 237, 273, "giường 1600 × 2000", size=2.1, fill=C_MUTE)
    sh.rect(kx + 300, 269, 5, 5, fill=C_WORK, stroke="#c98f2e", sw=0.14)
    sh.text(kx + 307, 273, "bàn 650 sâu", size=2.1, fill=C_MUTE)
    sh.rect(kx + 355, 269, 5, 5, fill=C_STORE, stroke="#a89a80", sw=0.14)
    sh.text(kx + 362, 273, "tủ 600", size=2.1, fill=C_MUTE)
    sh.text(10, 293, "Scale ≈ 1:56.  Party walls 200, partitions 100; new partition shown 100 "
                     "stud or glass.  Furniture indicative; WC and hall door positions can shift "
                     "±300 inside their wall.", size=2.1, fill="#7a8288")
    sh.save(path)


if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    front_base_sheet(os.path.join(out, "f3-front-base-plan.svg"))
    front_options_sheet(os.path.join(out, "f3-front-split-options.svg"))
    print("wrote front sheets ->", out)
