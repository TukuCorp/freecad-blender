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


# ------------------------------------------------------------------- options
def opt_a(s, p: Panel):
    py_ = 20150.0          # new partition
    shell(s, p, new_walls=[(IN_X0, py_, IN_X1 - IN_X0, PART)])
    # study at the rear
    p.rect_mm(IN_X0, py_ + PART, IN_X1 - IN_X0, (BAND_Y1 - PART - 50) - (py_ + PART),
              fill="#fdf7ef")
    sliding(p, IN_X0, py_, IN_X1 - IN_X0, PART, vertical=False)
    cut(p, 250, py_ - 30, 1500, PART + 60)
    sliding(p, 250, py_, 1500, PART, vertical=False)
    p.label(1250, py_ + 700, "CỬA TRƯỢT 1500", size=1.9, fill=C_NEW)
    # desk under the lô gia
    desk(p, 2200, BAND_Y1 - PART - 50 - 650, 1460, 650, chairs=2, face="south")
    wardrobe(p, IN_X0 + 60, py_ + 350, 400, 1250, doors_along="d")
    p.label(1400, 21500, "BÀN LÀM VIỆC 5.9 m²", size=1.9, weight="bold")
    # bedroom at the front
    bed(p, 1760, 18600, 2000, 1600, head="east")
    wardrobe(p, 1300, 17950, 2460, 600, doors_along="w")
    p.label(760, 19300, "P. NGỦ 7.8 m²", size=1.9, weight="bold")


def opt_b(s, p: Panel):
    py_ = 19350.0
    shell(s, p, new_walls=[(IN_X0, py_, IN_X1 - IN_X0, PART)])
    p.rect_mm(IN_X0, LOBBY_Y1, IN_X1 - IN_X0, py_ - LOBBY_Y1, fill="#fdf7ef")
    # glazed upper band over the study side of the partition
    p.line_mm(IN_X0, py_ + PART / 2, 2200, py_ + PART / 2, stroke=C_GLASS, sw=0.25,
              dash="2.4 1.2")
    p.label(1350, py_ - 400, "KÍNH LẤY SÁNG 2200", size=1.8, fill=C_GLASS)
    cut(p, 250, py_ - 30, 1200, PART + 60)
    sliding(p, 250, py_, 1200, PART, vertical=False)
    desk(p, 1300, 18050, 2460, 650, chairs=2, face="north")
    p.rect_mm(IN_X0 + 60, 18800, 400, 480, fill=C_STORE, stroke="#a89a80", sw=0.14)
    p.label(700, 18550, "BÀN LÀM VIỆC", size=1.9, weight="bold")
    p.label(700, 18250, "5.0 m²", size=1.9, weight="bold", fill=C_MUTE)
    # bedroom at the rear
    bed(p, IN_X0, 19550, 2000, 1600, head="west")
    wardrobe(p, 2600, 19550, 1160, 600, doors_along="w")
    p.label(3000, 21600, "P. NGỦ 8.9 m²", size=1.9, weight="bold")


def opt_c(s, p: Panel):
    px_ = 1650.0
    shell(s, p, new_walls=[(px_, LOBBY_Y1, PART, (BAND_Y1 - PART - 50) - LOBBY_Y1)])
    p.rect_mm(IN_X0, LOBBY_Y1, px_ - IN_X0, (BAND_Y1 - PART - 50) - LOBBY_Y1, fill="#fdf7ef")
    cut(p, px_ - 30, 18700, PART + 60, 1500)
    sliding(p, px_, 18700, PART, 1500, vertical=True)
    p.label(px_ + 1500, 19450, "CỬA TRƯỢT 1500", size=1.8, fill=C_NEW, anchor="start")
    desk(p, IN_X0 + 80, 18600, 650, 2100, chairs=2, face="north")
    wardrobe(p, IN_X0 + 20, 17950, 400, 1400, doors_along="d")
    p.label(1150, 18450, "BÀN LÀM VIỆC", size=1.9, weight="bold")
    p.label(1150, 18150, "5.8 m²", size=1.9, weight="bold", fill=C_MUTE)
    # bedroom (east strip)
    bed(p, 1760, 19950, 2000, 1600, head="east")
    wardrobe(p, 2000, 17950, 1760, 600, doors_along="w")
    p.label(2800, 19300, "P. NGỦ 8.0 m²", size=1.9, weight="bold")


def opt_d(s, p: Panel):
    shell(s, p, new_walls=[])
    # new opening in the lobby wall for this scheme
    cut(p, 2400, LOBBY_Y1 - PART / 2 - 20, 900, PART + 40)
    leaf(p, 2400, LOBBY_Y1, 900, 0, 90)
    p.label(2850, LOBBY_Y1 - 700, "CỬA MỚI", size=1.8, fill=C_NEW)
    # platform
    plat = (IN_X0, LOBBY_Y1, 2100.0, 2200.0)
    p.rect_mm(*plat, fill="#f0e7db", stroke=C_NEW, sw=0.3)
    bed(p, IN_X0 + 250, LOBBY_Y1 + 200, 1600, 2000, head="west")
    p.label(1250, 18400, "SÀN NÂNG +1400", size=2.0, weight="bold", fill="#8a5a22")
    p.label(1250, 18050, "kho/bàn dưới sàn", size=1.7, fill="#8a5a22")
    for i in range(3):
        p.rect_mm(1700 + i * 340, LOBBY_Y1 + 2200, 340, 330, fill="#dfd3c2",
                  stroke="#b08c5a", sw=0.12)
    p.label(2250, 20600, "3 bậc", size=1.7, fill="#8a5a22", anchor="start")
    desk(p, IN_X1 - 760, 19000, 660, 2150, chairs=2, face="west")
    p.label(2300, 19300, "BÀN LÀM VIỆC 650 × 2150", size=1.8, fill=C_MUTE)
    p.label(2100, 21600, "KHU LÀM VIỆC MỞ — 14.2 m²", size=2.1, weight="bold")
    p.line_mm(IN_X0, LOBBY_Y1 + 2350, 2100, LOBBY_Y1 + 2350, stroke="#7a4bd0", sw=0.25,
              dash="3 1.5")
    p.label(1050, 20950, "RÈM / VÁCH DI ĐỘNG", size=1.8, fill="#7a4bd0")


# ------------------------------------------------------------------- sheets
def base_sheet(path):
    sh = Sheet()
    sh.text(12, 13.5, "TẦNG 3 — rear bedroom, as drawn (corrected reading)",
            size=4.4, weight="bold")
    sh.text(12, 19.0, "Source: contractor/MB 2-3-4-Model.pdf, left plan “MẶT BẰNG TẦNG 2,3”.  "
                      "From the rear wall the printed chain reads 200 wall / 1600 WC+LÔ GIA / "
                      "4100 P.NGỦ / 1800 lobby / 3200 stair.", size=2.3, fill=C_MUTE)
    win = (-1500.0, 12200.0, 3960 + 3000, 12000.0)
    p = Panel(sh, win, (14.0, 24.0, 76.0, 150.0))
    p.rect_mm(0, LOBBY_Y1, 3960, BAND_Y1 - LOBBY_Y1, fill="#faf7f1")
    p.rect_mm(LOGGIA_X0, BAND_Y0, IN_X1 - LOGGIA_X0, BAND_Y1 - BAND_Y0, fill="#eaf3ea",
              stroke="#9ab89a", sw=0.1)
    wc_fixtures(p, 260, BAND_Y0 + 90, WC_X1 - 260, BAND_Y1 - BAND_Y0 - 180)
    bed(p, 900, 19950, 1600, 2000, head="north")
    p.rect_mm(300, 21450, 450, 450, fill=C_STORE, stroke="#a89a80", sw=0.1)
    p.rect_mm(2650, 21450, 450, 450, fill=C_STORE, stroke="#a89a80", sw=0.1)
    wardrobe(p, 3160, 18100, 600, 2400, doors_along="d")
    p.rect_mm(0, STAIR_Y0, 3005, 4000, fill="#f4f5f6")
    for i in range(10):
        p.line_mm(300 + i * 250, STAIR_Y0 + 200, 300 + i * 250, STAIR_Y0 + 1900,
                  stroke="#c3c9ce", sw=0.1)
    p.rect_mm(1960, STAIR_Y0 + 4000, 2000, 1800, fill="#f0f1f2", stroke="#b9c0c6", sw=0.12)
    p.label(2960, 17200, "THANG MÁY", size=1.8, fill="#8a939c")
    p.wall(0, STAIR_Y0 - 300, EXT, (BAND_Y1 - STAIR_Y0) + 300)
    p.wall(IN_X1, STAIR_Y0 - 300, EXT, (BAND_Y1 - STAIR_Y0) + 300)
    p.wall(0, BAND_Y1, 3960, EXT)
    p.wall(0, STAIR_Y0 - 100, 3005, PART, fill=C_OLD)
    p.wall(2955, STAIR_Y0, PART, LOBBY_Y1 - STAIR_Y0, fill=C_OLD)
    p.wall(0, LOBBY_Y1 - PART / 2, IN_X1 + EXT, PART, fill=C_OLD)
    p.wall(IN_X0, BAND_Y1 - PART - 50, IN_X1 - IN_X0, PART, fill=C_OLD)
    p.wall(WC_X1, BAND_Y0, PART, BAND_Y1 - BAND_Y0, fill=C_OLD)
    p.wall(1910, LOBBY_Y0, PART, LOBBY_Y1 - LOBBY_Y0, fill=C_OLD)
    cut(p, DOOR_ENTRY[0], LOBBY_Y1 - PART / 2 - 20, DOOR_ENTRY[1] - DOOR_ENTRY[0], PART + 40)
    leaf(p, DOOR_ENTRY[0], LOBBY_Y1, DOOR_ENTRY[1] - DOOR_ENTRY[0], 0, 90)
    cut(p, DOOR_WC[0], BAND_Y1 - PART - 70, DOOR_WC[1] - DOOR_WC[0], PART + 40)
    leaf(p, DOOR_WC[0], BAND_Y1 - PART - 50, DOOR_WC[1] - DOOR_WC[0], 0, 90)
    cut(p, DOOR_LOGGIA[0], BAND_Y1 - PART - 70, DOOR_LOGGIA[1] - DOOR_LOGGIA[0], PART + 40)
    leaf(p, DOOR_LOGGIA[1], BAND_Y1 - PART - 50, DOOR_LOGGIA[1] - DOOR_LOGGIA[0], 180, 90)
    p.line_mm(LOGGIA_X0, BAND_Y1 - 70, IN_X1, BAND_Y1 - 70, stroke="#2f7a2f", sw=0.3)
    p.label(1700, 19200, "P. NGỦ (hậu) 4100 × 3560", size=2.3, weight="bold")
    p.label(1700, 18800, "lọt lòng ~4000 × 3560 ≈ 13.9 m²", size=1.9, fill=C_MUTE)
    p.label(1150, BAND_Y0 + 700, "WC 2200", size=1.9, fill="#4c6b8a")
    p.label(3000, BAND_Y0 + 900, "LÔ GIA 1660", size=1.9, fill="#2f7a2f")
    p.label(1000, 17300, "HÀNH LANG", size=1.7, fill="#8a939c")
    p.dim_v(BED_Y0, BED_Y1, IN_X1, "4100", off=520)
    p.dim_v(BAND_Y0, BAND_Y1, IN_X1, "1600", off=520)
    p.dim_v(LOBBY_Y0, LOBBY_Y1, IN_X1, "1800", off=520)
    p.dim_h(IN_X0, IN_X1, REARW_Y1, "3560", off=420)
    p.dim_h(0, WC_X1, BAND_Y1, "2200", off=380)

    # ---------------- right-hand reading block ----------------
    bx = 106.0
    sh.line(bx - 8, 26, bx - 8, 176, stroke="#e2e6ea", sw=0.3)
    y = 34.0
    sh.text(bx, y, "What the sheet gives", size=3.0, weight="bold")
    y += 6.0
    for ln in [
        "· Rear bedroom 4100 (printed) × 3560 outer, lọt lòng",
        "   ~4000 × 3560 ≈ 13.9 m²  (the larger of the two",
        "   bedrooms: the front one is 4000 deep).",
        "· Entry door 900 from the lobby, front-west.",
        "· WC 2200 × 1600 at the rear-west — its door opens",
        "   into the bedroom.",
        "· LÔ GIA 1660 × 1600 at the rear-east, open — the",
        "   room's ONLY daylight and air, reached by a 900 door.",
        "· Wardrobe wall on the east; bed head on the WC wall.",
    ]:
        sh.text(bx, y, ln, size=2.3, fill=C_MUTE)
        y += 4.2
    y += 3.0
    sh.text(bx, y, "What that means for any split", size=3.0, weight="bold")
    y += 6.0
    for ln in [
        "· Daylight is a single resource at one corner: a",
        "   workspace only works if it takes the rear-east,",
        "   otherwise it is a dark box or needs borrowed light.",
        "· The WC door sits on the rear wall, so it lands in",
        "   whichever zone touches that wall.",
        "· Practical band for a new partition: 1500–1900 from",
        "   the rear wall, or a front-to-rear side partition.",
        "· No second window is available: both side walls are",
        "   party walls shared with the neighbours.",
    ]:
        sh.text(bx, y, ln, size=2.3, fill=C_MUTE)
        y += 4.2
    y += 3.0
    sh.rect(bx, y - 1, 300, 26, fill="#fff6ef", stroke="#f0c3a1", sw=0.3)
    sh.text(bx + 3, y + 5, "MODEL vs SHEET — designs/contractor-as-drawn.json has the last two",
            size=2.3, fill="#b34700", weight="bold")
    sh.text(bx + 3, y + 9.6, "rear bands the other way round: it puts the 1600 WC band IN FRONT of the",
            size=2.3, fill="#b34700")
    sh.text(bx + 3, y + 14.2, "bedroom and gives the bedroom the rear wall with a 1500 window. The sheet",
            size=2.3, fill="#b34700")
    sh.text(bx + 3, y + 18.8, "reads 1600 first from the rear (WC+LÔ GIA), then 4100. Worth confirming.",
            size=2.3, fill="#b34700")
    sh.text(12, 192, "This sheet is the base for the four split options; all four keep the WC, the lô gia "
                     "and the entry door where the drawing puts them.", size=2.3, fill=C_MUTE)
    sh.save(path)


def options_sheet(path):
    sh = Sheet()
    sh.text(10, 12.5, "TẦNG 3 — rear bedroom 14.2 m² split into bedroom + workspace",
            size=4.4, weight="bold")
    sh.text(10, 18.0, "Four options, same scale.  Orange = new work.  Rear (LÔ GIA + WC) at top; "
                      "the room's only opening to daylight is the lô gia door, rear-east.",
            size=2.3, fill=C_MUTE)
    xs = [10.0, 112.0, 214.0, 316.0]
    win = (-700.0, 17100.0, 3960 + 1500, 7100.0)
    fns = [("A", "Study at the rear, on the lô gia", opt_a),
           ("B", "Study at the entry, bed at the rear", opt_b),
           ("C", "Long desk wall — side split", opt_c),
           ("D", "Platform bed, open studio", opt_d)]
    caps = {
        "A": [("BÀN LÀM VIỆC 5.9 m² · P.NGỦ 7.8 m²", C_TXT),
              ("Desk sits on the only daylight the", C_MUTE),
              ("room has; the WC stays with the", C_MUTE),
              ("study, so it is out of the bed zone.", C_MUTE),
              ("Partition can slide between", C_MUTE),
              ("1500 and 1900 from the rear wall.", C_MUTE),
              ("− Bedroom drops to 2200 deep and", "#8a4b2a"),
              ("   you cross the study to reach the WC.", "#8a4b2a")],
        "B": [("BÀN LÀM VIỆC 5.0 m² · P.NGỦ 8.9 m²", C_TXT),
              ("Work zone at the door — no crossing", C_MUTE),
              ("the bedroom for a guest or delivery.", C_MUTE),
              ("Bedroom keeps both the lô gia and", C_MUTE),
              ("the WC, at its best size.", C_MUTE),
              ("", C_MUTE),
              ("− No daylight in the study: needs the", "#8a4b2a"),
              ("   glazed upper band, or a screen wall.", "#8a4b2a")],
        "C": [("BÀN LÀM VIỆC 5.8 m² · P.NGỦ 8.0 m²", C_TXT),
              ("One 2.1 m desk wall front-to-rear for", C_MUTE),
              ("two people; study gets the WC, the", C_MUTE),
              ("bedroom keeps the lô gia.", C_MUTE),
              ("", C_MUTE),
              ("", C_MUTE),
              ("− Bedroom only 2010 clear: the bed", "#8a4b2a"),
              ("   must sit against the partition.", "#8a4b2a")],
        "D": [("KHU MỞ 14.2 m² — no floor lost", C_TXT),
              ("Bed raised +1400 on a platform with", C_MUTE),
              ("storage under it; nothing is walled", C_MUTE),
              ("off, just a track curtain.", C_MUTE),
              ("Cheapest build, most daylight, the", C_MUTE),
              ("longest desk wall.", C_MUTE),
              ("− Platform cost; 1400 headroom under", "#8a4b2a"),
              ("   the bed; reads as a single room.", "#8a4b2a")],
    }
    for (tag, title, fn), x in zip(fns, xs):
        p = Panel(sh, win, (x + 4.0, 24.0, 92.0, 152.0))
        fn(sh, p)
        sh.text(x + 3, 22.0, f"OPTION {tag}", size=3.2, weight="bold", fill=C_NEW)
        sh.text(x + 20.0, 22.0, title, size=2.6, weight="bold")
        for i, (ln, col) in enumerate(caps[tag]):
            sh.text(x + 3, 190.0 + i * 4.1, ln, size=2.2, fill=col)
        sh.rect(x, 10.5, 98.0, 182.0, fill="none", stroke="#d3d8dc", sw=0.25)
    # key
    sh.rect(10, 264, 400, 26, fill="#fbfcfd", stroke="#e2e6ea", sw=0.25)
    kx = 16
    sh.rect(kx, 269, 5, 5, fill=C_WALL)
    sh.text(kx + 7, 273, "tường / wall", size=2.1, fill=C_MUTE)
    sh.rect(kx + 40, 269, 5, 5, fill=C_NEW)
    sh.text(kx + 47, 273, "vách mới / new partition", size=2.1, fill=C_MUTE)
    sh.line(kx + 130, 271.5, kx + 140, 271.5, stroke=C_GLASS, sw=0.25, dash="2.4 1.2")
    sh.text(kx + 143, 273, "kính / glazing", size=2.1, fill=C_MUTE)
    sh.rect(kx + 185, 269, 5, 5, fill=C_BED, stroke="#7d95ab", sw=0.1)
    sh.text(kx + 192, 273, "giường 1600 × 2000", size=2.1, fill=C_MUTE)
    sh.rect(kx + 255, 269, 5, 5, fill=C_WORK, stroke="#c98f2e", sw=0.14)
    sh.text(kx + 262, 273, "bàn làm việc 650 sâu", size=2.1, fill=C_MUTE)
    sh.rect(kx + 335, 269, 5, 5, fill=C_STORE, stroke="#a89a80", sw=0.14)
    sh.text(kx + 342, 273, "tủ 600 sâu", size=2.1, fill=C_MUTE)
    sh.text(10, 293, "Scale ≈ 1:50 (1 m = 20 mm).  Walls: party 200, partitions 100, new partition "
                     "shown 100 stud hoặc kính.  Furniture indicative.  Sources: "
                     "contractor/MB 2-3-4-Model.pdf + designs/contractor-as-drawn.json.",
            size=2.1, fill="#7a8288")
    sh.save(path)


if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    base_sheet(os.path.join(out, "f3-base-plan.svg"))
    options_sheet(os.path.join(out, "f3-split-options.svg"))
    print("wrote svg ->", out)
