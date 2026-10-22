# -*- coding: utf-8 -*-
"""Part B: P-01 to P-08, P-09, P-10, P-11, P-12."""
from fixlib import E


# ------------------------------------------------------------------ P-02

E(292, 292,
  "- **Where:** the front yard is the **3360 deep band** in front of the building. The top "
  "dimension chain of IMG_9972 reads `350 | 3010 | 4240 | 4000 | 5000 | 4500 | 1600 | "
  "2650`, so the yard is 350 + 3010, and the running totals on that sheet are 3360 | 19340 "
  "| 2300. Its floor tag is **Ns** = *nen san, lat gach 30x60 cm, chong truot* (IMG_9972 "
  "finishes legend). The front is on the LEFT of every plan (transcript, plan convention) "
  "and the street is on that short side. (The superseded model carried 3500 for this "
  "depth; the scan says 3360.)",
  "p02-where",
  "- **Where:** san truoc is 3500 deep")

E(300, 300,
  "- **Evidence:** VERIFIED (IMG_9972 dimension chain and legend Ns).",
  "p02-evidence",
  "- **Evidence:** VERIFIED (measurements.md ground-floor table; IMG_9972 legend Ns).")


# ------------------------------------------------------------------ P-03

E(304, 304,
  "- **Where:** IMG_9972 chain: *noi de xe -> P. khach (3800/4000) -> thang*. D1 (2800 "
  "wide) sits in the front wall of the garage; the stair is a whole band further back - "
  "the P. khách band is 4000 on the grid - and sits in the core band (5000 = 3200 stair "
  "+ 1800 lift). The house is 25 000 long, so the door and the stair are **not** on one "
  "straight line - the entrance axis runs into the living room and is then turned sideways "
  "into the core. The rear door D2 is in the rear wall of the rear WC band.",
  "p03-where",
  "- **Where:** IMG_9972 chain: *noi de xe -> P. khach")

E(312, 312,
  "- **Evidence:** VERIFIED for the geometry (IMG_9972 room chain and dimension chains); "
  "the door-stair rule is CLAIMED but very widely repeated ([9], [12]).",
  "p03-evidence",
  "- **Evidence:** VERIFIED for the geometry (IMG_9972 chain and dims; measurements.md")


# ------------------------------------------------------------------ P-04

E(316, 316,
  "- **Where:** D2 is the rear door of the rear WC band, per IMG_9972 (*WC (tags W1, Sb1, "
  "Dw, door D2 rear) -> san sau*). The front D1 is in the front wall of the garage. The "
  "rear WC band is 1600 on the grid, the garage 4240 and the living room 4000 - the two "
  "doors are separated by 4240 + 4000 + 5000 (core) + 4500 (kitchen) + 1600 (WC) = 19 340 "
  "mm of built depth, with the living room, the whole core band and the kitchen band "
  "between them.",
  "p04-where",
  "- **Where:** D2 is the rear door of the rear WC band")

E(324, 324,
  "- **Evidence:** VERIFIED for the geometry (IMG_9972 room chain and dimension chains); "
  "CLAIMED for the rule ([22] for the qualified form, [6] and [9] for the strict form).",
  "p04-evidence",
  "- **Evidence:** VERIFIED for the geometry (IMG_9972 room chain; measurements.md)")


# ------------------------------------------------------------------ P-06

E(342, 342,
  "- **Where:** the core band (stair + lift) is the **5000-wide band at grid axes 4-5** of "
  "a 25 000 mm plot - the 3200 stair bay plus the 1800 lift bay - i.e. the middle fifth "
  "of the depth (IMG_9972 dimension chain `350 | 3010 | 4240 | 4000 | 5000 | 4500 | 1600 | "
  "2650`; the same axes 4-5 core band is drawn on every upper plan, IMG_9973-9977). The "
  "stair occupies the front-to-middle of the band, the lift the rear of it. The stair is "
  "the **only** stair in the building.",
  "p06-where",
  "- **Where:** the core band (stair + lift) sits at y = 12 300-16 300")

E(348, 348,
  "- **Practical rationale:** this is the strongest practical case in the whole report. The "
  "under-stair space in this house is a 3900 x 3200 mm volume (the stair well, A-B by axes "
  "3-3a, IMG_0003) with a 1250 mm flight hanging over it, reached through the core, in "
  "the middle of a five-storey plan. Turning it into an open, lit, visually interesting "
  "niche (planter, bench, washing area) instead of a cupboard is better for dust, for "
  "light, and for the feeling of the core. The tradition and the architecture agree for "
  "once.",
  "p06-practical",
  "- **Practical rationale:** this is the strongest practical case in the whole report.")

E(349, 349,
  "- **Conflict with safety/design:** **the safety answer wins over the phong thuy answer "
  "here, in one respect.** Under-stair storage is attractive for exactly the reason the "
  "tradition dislikes it (a 3900 x 3200 void is the largest unsecured store in the house). "
  "If the owner wants the space, it must be a **locked, ventilated, fire-rated cupboard** "
  "or an open planter - not a walk-in store under a flight. The stair is the sole escape "
  "route for five storeys; nothing stored under it may impede egress, and the stair's "
  "fire-resistance and smoke behaviour must not be compromised by fixing (c) inside it.",
  "p06-safety",
  "- **Conflict with safety/design:** **the safety answer wins over the phong thuy answer")

E(350, 350,
  "- **Evidence:** VERIFIED for the position (IMG_9972 dimension chain and core band; "
  "IMG_9973-9977 draw the same axes 4-5 core on every upper plan; the stair well 3900 x "
  "3200 from IMG_0003). VERIFIED for the rule ([9], [11], [12]).",
  "p06-evidence",
  "- **Evidence:** VERIFIED for the position (measurements.md; JSON `stairwell` rect")


# ------------------------------------------------------------------ P-08

E(366, 366,
  "- **Where:** the stair continues to the top level, **tầng 5 (+17.200)** - IMG_9977: "
  "*stair with 21 treads at the 5th-floor/terrace level* - discharging into a lobby with "
  "doors D6 (front terrace) and D7 (rear terrace): transcript IMG_9977: *a stair/lift "
  "lobby (5200 long, 3200 + 1800 + 200) with floor tag SL5 and doors D6 (to the front "
  "terrace) and D7 (to the rear terrace)*.",
  "p08-where",
  "- **Where:** the stair continues to the top floor (IMG_9977")

E(374, 374,
  "- **Evidence:** VERIFIED for the geometry (IMG_9977 - tầng 5 lobby, doors D6 and D7, "
  "stair with 21 treads); CLAIMED for the rule (repeated across the folk literature, no "
  "single canonical source located).",
  "p08-evidence",
  "- **Evidence:** VERIFIED for the geometry (IMG_9977; JSON Roof Terrace storey")


# ------------------------------------------------------------------ P-09 (376-386)

E(376, 386,
  """**P-09 - No stair is over the altar, and no altar is over the stair: a clean pass**

- **Where:** P. Thờ is the **front room of tầng 4 (+13.800)**, sitting behind the front
  balcony - IMG_9976 (KT05): *Ban công (front balcony, D5, S1, SB4) -> P. Thờ (altar room)
  -> P. Đọc sách (reading room; thin partition wall between the two, 3010 + 4240 grid)*.
  The stair and the lift sit in the **core band at grid axes 4-5** (the 3200 stair bay plus
  the 1800 lift bay) on the same plan, four bands further back, and the same axes 4-5 core
  is drawn on every other level (IMG_9972-9977). No storey draws a stair over the altar
  bay, and the altar bay has no stair below it. The vertical section agrees: at +13.800
  the long section lists *P. Ngủ, P. Đọc sách, P. Thờ* (IMG_9980).
- **Rule:** *ban tho khong dat duoi gam cau thang* and *khong dat ban tho tren cau thang* - the
  altar must not sit under a stair, and the stair must not run over it; the under-stair
  space is the darkest, most compressed, most stagnant volume in the house and is treated
  as unsuitable for worship. [9] and [12] both state the under-stair case.
- **School:** general nha ong folk rule / phong tho practice.
- **Agreement:** COMMON, and near-universal in practice - no source located that permits an
  altar under a stair.
- **Severity in the tradition:** MAJOR if broken.
- **Remedy:** none - the condition is already satisfied.
- **Practical rationale:** a stair overhead is loud, dark and hot; it is a poor place to
  pray regardless of doctrine.
- **Conflict with safety/design:** none.
- **Evidence:** VERIFIED (IMG_9976 room chain for tầng 4; IMG_9972-9977 dimension chains
  putting the core at axes 4-5 on every level; IMG_9980 section, +13.800 level).""",
  "p09-block",
  "**P-09 - No stair is over the altar")


# ------------------------------------------------------------------ P-10 (390-400)

E(390, 400,
  """**P-10 - A shaft punched through all five floors: *thung khi* - CONTESTED, and the safety answer overrides the tradition**

- **Where:** **a lift shaft is drawn on every plan.** IMG_9972 reads it as an X-hatched
  shaft **1800 wide x 1600 deep** in the core, and the same 1800 x 1600 shaft is drawn on
  IMG_9973, IMG_9974, IMG_9975, IMG_9976 and IMG_9977 (the tầng 5 lobby). The roof sheet
  (IMG_9978) carries the **ô kỹ thuật thang máy** (lift technical overrun) 2000 wide
  (plan 1800 + 900), and the long section (IMG_9980) draws a lift car with its doors at
  every floor (door gap 300 + 1000 + 300). The pit detail (IMG_9987) gives a **1600 clear
  width** between wall inner faces, 200 thick walls, 2000 overall, pit floor at -1.650,
  with four corner piles (M4, M5, M6). **The lift is not an inference.** What is not
  settled is its **exact size**, which conflicts between sheets - 1800 x 1600 on the
  plans, 1600 clear in the pit detail, 2000 wide for the roof overrun - and that is a
  design-lane matter for the architect, the structural engineer and the lift supplier,
  not a feng shui one.
- **Rule:** some schools treat a hole running the full height of the house as a **thung
  khi / thung long** - a chimney that carries qi straight out of the roof without ever
  circulating in the rooms. Others read a well-sited shaft as a *vertical ventilation
  spine*, especially in a 3.9 m-wide tube house where the whole depth is otherwise a
  single air tunnel.
- **School:** Phi Tinh / general nha ong folk rule. CONTESTED, and the disagreement is
  explicit in the sources: [12] treats the stair (a vertical void) as *the* qi-gathering
  element of a house while also forbidding it in the middle; the leak reading is the
  minority one.
- **Agreement:** CONTESTED.
- **Severity in the tradition:** MODERATE at most, and only under the minority reading.
- **Remedy:** if the owner wants the minority reading addressed, the traditional remedy is
  a **screen or a light-coloured, close-fitting door at each shaft opening** so the shaft
  is not a visually open hole from floor to floor - a lift door with a full-height screen
  behind it, or a dark screen on the shaft side. Cheap and non-structural.
- **Practical rationale:** this is a genuine and cheap improvement, but for a mundane
  reason: a lift shaft running the full height of the house is a **smoke and sound path**
  between floors. A tight shaft door and a shaft-side screen reduce both, and the screen
  also stops the shaft becoming a black hole in an otherwise narrow corridor.
- **Conflict with safety/design: safety wins.** Nothing may be added that reduces the lift
  shaft's clear dimensions, obstructs the lift car or its pit, or interferes with the
  **hoist-hook beam** (IMG_9988: a single 25 mm hook bar in a 120 mm slab with no stated
  rated load). Fire separation of the shaft is a structural and fire matter and any
  shaft-sealing work belongs to the engineer, not to a feng shui screen.
- **Evidence:** VERIFIED for the shaft's existence and its drawn size (IMG_9972, IMG_9973,
  IMG_9974, IMG_9975, IMG_9976, IMG_9977 - shaft 1800 x 1600 on every plan; IMG_9978 -
  overrun 2000 wide; IMG_9980 - car and doors at every level; IMG_9987 - pit 1600 clear;
  IMG_9988 - hoist slab 2000 x 2000). The **size conflict between sheets** is PARTIAL and
  is referred to the design review. CONTESTED / CLAIMED for the rule.""",
  "p10-block",
  "**P-10 - A shaft punched through all five floors")


# ------------------------------------------------------------------ P-11 (402-412)

E(402, 412,
  """**P-11 - The light wells (o lay sang) are a genuine asset**

- **Where:** an **ô lấy sáng** (light well) sits beside the WC on the front side of
  **every upper floor**: 1600 wide on tầng 2 and tầng 3 (IMG_9974, IMG_9975), and
  **2100 long** on tầng 4 beside the WC behind the reading room (IMG_9976). The **tầng 5**
  sheet (IMG_9977) carries **ô lấy sáng gắn kính cường lực, có khung inox bảo vệ** (light
  well in tempered glass with a protective stainless-steel frame) - 2000 long x 1500 wide -
  **over the stair**, with tag S2 on the stair-side window. On the roof (IMG_9978) **two**
  light wells are noted, one at the stair and one beside the lift shaft (sizes 1200 and
  1300/1500, PARTIAL).
- **Rule:** an intentional skylight or light well is a **thien tinh** - a heaven-window. The
  rule that is *not* in dispute is the practical one: a light well must bring light **and**
  air. A glazed, sealed light well is a light source; an unglazed one is also a ventilation
  shaft, which is what makes it useful in a house this narrow. The tradition's usual caveat
  is that a hole must not become a straight path for bad qi to enter, and that any well
  opening at the top must be protected - the *bao ve* framing the drawing already calls for.
- **School:** general nha ong folk rule + Phi Tinh (a well is read by its relationship to the
  star chart, not by a rule in itself).
- **Agreement:** COMMON for the practical part (light + air), CONTESTED for the symbolic
  reading.
- **Severity in the tradition:** MINOR - this is a positive feature, not a defect.
- **Remedy:** keep the light wells unglazed or openable where the drawings allow, so they
  ventilate; keep the stair light well's stainless protective frame intact; do not enclose
  the rear light well in a cupboard.
- **Practical rationale:** this is where the phong thuy advice and the building physics are
  most obviously the same advice. In a 3.9 x 25 m tube house with a single stair and a party
  wall on each side, the only way to get air to the rear bedroom is a vertical path. The
  light wells beside the stair are the reason the rear of the house is habitable at all.
- **Conflict with safety/design:** the stair's glass light well on the terrace has **no stated
  load rating and no fall protection** (IMG_9977 ambiguity note) - that is a safety-review
  item and it overrides any phong thuy preference for more glass.
- **Evidence:** VERIFIED (IMG_9974, IMG_9975, IMG_9976, IMG_9977, IMG_9978 notes, including
  the glazed stair light well on tầng 5 and the 2100 long well on tầng 4).""",
  "p11-block",
  "**P-11 - The light wells (o lay sang) are a genuine asset")


# ------------------------------------------------------------------ P-12 evidence

E(424, 424,
  "- **Evidence:** VERIFIED (IMG_9973, IMG_9980).",
  "p12-evidence",
  "- **Evidence:** VERIFIED (IMG_9973, IMG_9980; measurements.md mezzanine table).")
