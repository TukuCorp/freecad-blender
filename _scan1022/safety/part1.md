# Independent life-safety and structural-safety review — contractor construction set

**Project:** NHÀ Ở RIÊNG LẺ, 506 ĐƯỜNG HỒNG BÀNG, PHƯỜNG MINH PHỤNG, TP.HCM ("HỒ SƠ THIẾT KẾ THI CÔNG", hạng mục "XÂY DỰNG MỚI")
**Drawing set reviewed:** contractor photo scan of 2026-10-22 (architecture KT01–KT07 + elevation + section A-A; structural KC01–KC24 subset)
**Review date:** 2026-10-22 (Asia/Ho_Chi_Minh)
**Lane:** safety only. Design-error and feng-shui issues are handled by other reviewers and are out of scope here.

---

## 1. Method and evidence limits

### 1.1 What I did

1. Read the four transcript/ledger files named in the brief and extracted every dimension, level, note and quoted Vietnamese string that bears on safety. Nothing in this report is read off the photographs — I have no access to the images.
2. Fetched and text-extracted four primary codes, and read the clauses that bear on this building: **QCVN 06:2022/BXD (as amended SĐ1:2023)**, **UK Approved Document B Volume 1 (Dwellings)**, **UK Approved Document K (2013 edition)**, and the **SCDF Fire Code 2013, Chapter 2**. Clause text quoted below was read from those documents, not from memory.
3. Cross-checked the current photo-scan transcripts against the earlier reading of the vector PDFs (`designs/contractor-as-drawn.measurements.md`, `.fidelity.md`) to find where the two sources disagree.
4. Screened the structural sheets for red flags only. **I am not a structural engineer and nothing in this report asserts that any element, foundation, connection or material is adequate or compliant.** Every structural item below is a "screening observation, to be confirmed by a licensed engineer".

### 1.2 The single most important determination in this report

**QCVN 06:2022 is probably not the legal floor for this building — but the owner asked for international best practice, so it is used here as the benchmark anyway.**

QCVN 06:2022 clause 1.1.2(2) applies to *nhà ở riêng lẻ* (single-family houses) at any of these scales:

> "cao từ 7 tầng trở lên (hoặc có chiều cao PCCC từ 25 m trở lên); hoặc có khối tích từ 5 000 m3 trở lên; hoặc có nhiều hơn 1 tầng hầm đến 3 tầng hầm."

On the transcript figures this house is: **6 occupied storeys** (trệt ±0.000, lửng +3.800, tầng 2 +7.000, tầng 3 +10.400, tầng 4 +13.800, tầng 5 +17.200) plus a **roof terrace at +20.400** and a 1500 parapet to +21.900; **PCCC ≈ 21.9 m** (per QCVN 06 clause 1.4.9 and its note 1, which counts the roof parapet when the roof is in use); and a gross enclosed volume of roughly **2 100 m³** (3.90 m × 25.0 m × 21.9 m, before deductions). All three triggers are therefore just below the threshold — but only just, and two of them turn on unresolved facts:

- if the roof terrace is counted as a **seventh storey**, QCVN 06 becomes mandatory outright;
- if the level data in `measurements.md` is the current design (**+23.800 roof slab, +25.800 plant room**), the PCCC is 25.8 m and QCVN 06 is mandatory outright.

QCVN 06's own scope note adds: *"Đối với các nhà đứng độc lập … có chiều cao dưới 7 tầng, chiều cao PCCC dưới 25 m và khối tích dưới 5 000 m3), nếu không thể tuân thủ các quy định của quy chuẩn này thì căn cứ trên công năng cụ thể của nhà cũng có thể áp dụng các tài liệu chuẩn để thiết kế an toàn cháy"* — i.e. a small house may use **published standards documents** instead. That is precisely the route the owner asked for.

**Consequence for the owner:** every Vietnamese clause cited below is marked LOCAL-MINIMUM. If the architect or the permitting authority concludes QCVN 06 *is* mandatory (7-storey or 25 m reading), **every finding below either stays the same or gets stricter**, and the single-stair and no-alarm findings become straight permit blockers rather than good-practice gaps. Owner must get this determination in writing before the first pour (Question 1).

### 1.3 What I could not do, and what that means for this report

| Gap | Consequence |
|---|---|
| **QCVN 03:2019/BXD** (architectural safety) — every fetch route returned HTTP 403/404; the text is not freely retrievable | No clause of QCVN 03 is cited. Stair geometry is instead checked against QCVN 06:2022 clause 3.4.2 (verified), ADK Table 1.1 (verified) and ADB (verified). QCVN 03 and TCVN 2737:2023 remain **required reading** — see Question 24. |
| **TCVN 4451:2012**, **TCVN 2737:2023**, **TCVN 9386:2012**, **QCVN 07:2025** — NOT FOUND | Not cited. Named in the questions list as documents the designer must produce. |
| **NFPA 101** — only the landing page was reachable; the free-access viewer is JavaScript-driven and the clause text was not obtained | **No NFPA 101 clause number or figure is quoted anywhere in this report.** NFPA 101 appears only as a code for the fire consultant to apply. |
| **IBC 2021 Chapter 10** — the ICC viewer is captcha-gated | **No IBC section number or figure is quoted anywhere in this report.** IBC appears only as a code for the fire consultant to apply. |
| **HCMC official flood levels** — `hcmcportal.vn` did not resolve from this environment and the search engine returned irrelevant results | **No flood level or tidal datum is quoted.** S-18 is written as a determination to obtain, not as a number. |
| **Geotechnical report** — none in the set | Foundation findings are screening observations only. No settlement, bearing or liquefaction figure is stated. |
| **Structural calculations** — none in the set | No capacity, stress, deflection or reinforcement adequacy is stated or implied. |
| **MEP drawings** — none in the set (no power, lighting, plumbing, drainage, gas or lightning-protection sheets) | Topic 7 findings are "cannot assess from the transcript" plus the specific gaps to close. |
| **Door/window schedule, fire notes, ceiling heights** — the transcripts record all of these as absent | S-07, S-11 and the smoke-control findings cannot be closed without them. |
| **Stair detail sheet** ("Xem chi tiết cầu thang") — referenced but not in the set | Headroom, landing sizes, handrails and the winder geometry cannot be verified. |

### 1.4 Evidence-label key used throughout

- **VERIFIED** — the source text or drawing line was seen, in a fetched document (URL and date given in §7) or in a transcript file (file and line quoted).
- **PARTIAL** — read, but the transcript itself flags the figure as uncertain (PARTIAL / ILLEGIBLE); not used as the sole basis of a CRITICAL finding.
- **CLAIMED** — asserted by the drawing set or the contractor without supporting evidence in the set.
- **NOT FOUND** — the document or clause was sought and could not be retrieved.
- **UNVERIFIED** — a standards clause quoted from memory or from a general reference without fetching the source. **No clause in this report carries the UNVERIFIED label, because every clause quoted was fetched and read.** Where a code could not be fetched (NFPA 101, IBC 2021), no clause is quoted at all.

### 1.5 Terminology

The Vietnamese transcripts mix *tầng* (storey) with the Hong Kong-style *lầu* used in the structural sheets (tầng 2 = lầu 1). This report uses the **architectural** naming throughout: trệt (ground), lửng (mezzanine), tầng 2, tầng 3, tầng 4, tầng 5, sân thượng (roof terrace).

---

## 2. Findings — Topic 1: Means of escape

### S-01

- **ID:** S-01
- **Severity:** CRITICAL
- **Where:** "MẶT BẰNG TẦNG 1", "MẶT BẰNG TẦNG LỬNG", "MẶT BẰNG TẦNG 2"…"TẦNG 5" — `contractor/scan-2026-10-22/transcript-architecture.md`: the room chain on every floor runs *"-> stair (U-shape with winder; 3000 wide as 1250+500+1250 (arithmetic check), 3200 between wall lines) -> lift"*, i.e. one stair, and `transcript-architecture.md` "Five things for a safety or design reviewer", item 5: *"one enclosed stair with the light wells (Sb1) adjacent to WCs on floors 2-4"*.
- **Issue:** There is a **single escape stair** serving a house whose occupied storeys reach +17.200 m (roof terrace +20.400 m, parapet +21.900 m), and there is **no second escape route of any kind**: no external escape stair, no balcony-to-balcony stair, no roof-ladder route, and no fire-resisting enclosure for the one stair that exists.
- **Why it matters:** The failure scenario is a fire in the rear half of an upper floor (most likely the rear bedroom, whose door D4 is 4.4–4.5 m from the stair on the *far* side of the lift) with smoke filling the single stair — the only route out. Occupants on that floor have exactly one egress, and if that egress is the fire's path (the stair is open to the mezzanine void and glazed over at the head — see S-05 and S-16) there is no second option. Above +7.5 m this is the specific situation UK and international practice refuses to accept without either a protected alternative route or sprinklers.
- **Basis:** UK Approved Document B Vol. 1 (2019 ed. with 2020/2022/2025/2026 amendments, retrieved 2026-10-22) **para. 2.5** — for a dwellinghouse with storeys more than 4.5 m above ground level, *"The dwellinghouse should have either of the following. a. Protected stairway – a stair separated by fire resisting construction (minimum REI 30) at all storeys"* … *"b. Alternative escape route – a top storey separated from lower storeys by fire resisting construction (minimum REI 30) and with an alternative escape route leading to its own final exit."* And **para. 2.6**: *"Dwellinghouses with two or more storeys more than 4.5m above ground level … should comply with either of the following. a. Provide an alternative escape route from each storey more than 7.5m above ground level … b. Provide a sprinkler system throughout, designed and installed in accordance with BS 9251."* QCVN 06:2022 **clause 3.2.6.1(c)** — an F1.3 unit with only one exit and a storey area ≤ 500 m² *"phải có một lối ra khẩn cấp theo quy định tại 3.2.13"* from each unit above 15 m. SCDF Fire Code 2013 Ch. 2 **clause 2.2.13** — in any building more than four storeys above ground level, entry to an exit staircase *"shall be through … an external exit passageway or external corridor … or a lobby that is separated from the adjoining areas of the building by a wall having a fire resistance of 1 hour"* with a half-hour self-closing door.
- **Basis class:** BEYOND-LOCAL
- **Fix:** Adopt one of three routes and record it on the drawings: **(a)** provide a second, protected escape route from every storey above +7.500 (an external escape stair on the rear/party-wall line, or a protected second stair), with the top storey separated by REI 30 construction per ADB 2.5(b)/2.6(a); **or (b)** fit a BS 9251 residential sprinkler/mist system throughout, which is the ADB 2.6(b) alternative and also satisfies the QCVN 06 clause 3.2.6.2(a)3) requirement for *"hệ thống báo cháy và chữa cháy tự động"* at 21–25 m PCCC; **or (c)** re-plan the core so the single stair becomes a protected stairway serving a re-planned floor plate, and re-issue the fire strategy. Option (b) is the pragmatic route for a 3.95 m tube house and should be priced before anything else.
- **Who decides:** owner (strategy and budget), architect (re-plan), fire consultant (the escape strategy itself).
- **Evidence label:** VERIFIED (drawing line quoted from transcript; ADB 2.5/2.6, QCVN 06 3.2.6.1(c) and 3.2.13, SCDF 2.2.13 read from the fetched documents listed in §15).

### S-02

- **ID:** S-02
- **Severity:** HIGH
- **Where:** "MẶT BẰNG TẦNG 2" (and mirrored on 3, 4) — `transcript-architecture.md`: *"Ban công (front balcony, door D5, window S1, floor SB2; depth 1400 on the grid)"*, and the front elevation IMG_9979: *"tags D5 (balcony door) and S1 (window)"* with *"1000 + 2500 + 200 / 200 + 2500 + 1000 chains alternating left-right per floor"*.
- **Issue:** The front balconies are drawn at 1400 mm deep on floors 2–5, but **nothing connects them** — no external stair between balconies, no floor hatch, and no indication that D5/S1 form an emergency-escape opening. As drawn, a person on the front balcony of tầng 5 has nowhere to go: the terrace above is reached only through the core.
- **Why it matters:** The balcony is the only place on the front of the house from which a 17 m fall could be arrested, and it is the natural candidate for the second escape route or the emergency exit that QCVN 06 clause 3.2.13 and ADB para 2.10 both need. If the balconies are not connected, the emergency exit has to be manufactured somewhere else (or the house gets sprinklers instead).
- **Basis:** QCVN 06:2022 clause **3.2.13(c)** — *"Lối ra ban công hoặc lô gia có chiều rộng không nhỏ hơn 0,6 m, mà ở đó có trang bị thang bên ngoài nối các ban công hoặc lô gia theo từng tầng, hoặc có cửa nắp trên sàn ban công hoặc lô gia, kích thước tối thiểu 0,6 x 0,8 m, có thông xuống ban công hoặc lô gia tầng dưới"*. Clause **3.2.13(a)** additionally requires, for a balcony used as an emergency exit, *"một khoảng tường đặc với chiều rộng không nhỏ hơn 1,2 m tính từ mép ban công (lô gia) tới ô cửa sổ … hoặc không nhỏ hơn 1,6 m giữa các ô cửa kính mở ra ban công"*, a balcony width ≥ 0.6 m, natural ventilation, and separation from the room by *"vách ngăn (có các lối cửa) từ sàn đến trần"*. UK ADB **para. 2.14** — *"A balcony or flat roof intended to form part of an escape route should be provided with guarding etc. in accordance with Approved Document K."*
- **Basis class:** LOCAL-MINIMUM (QCVN 06 3.2.13) reinforced by BEYOND-LOCAL (ADB 2.14)
- **Fix:** Fit a stainless external escape stair on the front face linking the four balcony levels (or a vertical ladder/hoist per floor), **or** fit floor hatches ≥ 600 × 800 mm in each balcony slab with a ladder, **or** accept the balcony as a non-escape feature and rely on the BS 9251 sprinkler route in S-01. If the balcony is to count as an emergency exit, the 1200 mm solid-wall or 1600 mm between-pane condition of clause 3.2.13(a) must be designed in from the start — on a 1400 mm deep balcony with full-height glazing this is geometrically very tight and will probably fail, which is itself worth knowing before the facade is fixed.
- **Who decides:** architect (with the structural engineer for the balcony cantilever and any stair fixings), owner.
- **Evidence label:** VERIFIED (balcony depth and tags from the transcript; QCVN 06 3.2.13 and ADB 2.14 read from the fetched documents). Whether a connecting stair was intended is **PARTIAL** — the transcripts describe the balconies in isolation and do not mention one.

### S-03

- **ID:** S-03
- **Severity:** HIGH
- **Where:** `transcript-architecture.md`, IMG_9974 "MẶT BẰNG TẦNG 2": *"WC (tag WL2, door Dw 700 / 750, 850 + 950 widths) next to Ô lấy sáng (light well, tag Sb1, X, 1600 wide)"*; IMG_9972: *"Rear WC: 1600 wide, 2100 long, tags W1, Sb1, Dw (READ)"*; and the same file: *"No door/window schedule is in this set of nine photos."*
- **Issue:** **No window in the set is documented as openable.** S1 (balcony window), Sb1 (light-well window), K2 (WC window) and the front D5 doors are dimensioned as glazed openings with no opening device, no operable area, no sill height and no grille detail. Whether any of them can be used as an emergency escape window — and whether a burglar/security grille is fitted over them, which is near-universal on Vietnamese ground-to-first-floor openings and would defeat the escape entirely — is **not determinable from the transcript**.
- **Why it matters:** If S-01 is resolved by "emergency escape windows" rather than sprinklers, and every window is either fixed or grilled, the house has no second escape route at all and the strategy in S-01 collapses. A window that looks like an escape window and is not is worse than one that is obviously fixed, because the occupant tries it.
- **Basis:** UK ADB **para. 2.10** — *"Windows or external doors providing emergency escape should comply with all of the following. a. Windows should have an unobstructed openable area that complies with all of the following. i. A minimum area of 0.33m2. ii. A minimum height of 450mm and a minimum width of 450mm … iii. The bottom of the openable area is a maximum of 1100mm above the floor."* Plus *"d. Windows should be capable of remaining open without being held."* ADB **para. 2.6** (escape from storeys above 7.5 m must be an alternative route or sprinklers). QCVN 06 clause **3.2.13(d)** — direct external exit from a room whose finished floor is between −4.5 m and +5.0 m via a window or door *"không nhỏ hơn 0,75 m × 1,5 m"*, with a ladder.
- **Basis class:** BEYOND-LOCAL
- **Fix:** Produce a window and door schedule for every external opening stating, per opening: type, opening device, unobstructed openable area (mm²), sill height above finished floor, and whether any security grille is fitted. Design at least one **unobstructed, ungrilled, openable** opening on each of floors 3, 4 and 5 that meets the 0.33 m² / 450 × 450 / 1100 mm rule, with the grille (if the owner wants one) as a key-released or removable type. If none can be achieved on the front, the rear loggia and the light-well windows must be examined — a light-well window opening onto a 1600 mm shaft is not an escape route but may be an extraction route.
- **Who decides:** architect (schedule and openings), owner (accepts ungrilled openings or pays for a compliant grille), fire consultant (confirms the escape strategy that depends on them).
- **Evidence label:** PARTIAL (the absence of a door/window schedule and the window tags are VERIFIED from the transcript, and ADB 2.10/2.6 were read from the fetched document; but the openability and grille status of every window is **not stated either way** in the set, so the *conclusion* that a compliant escape opening may or may not exist is PARTIAL).

### S-04

- **ID:** S-04
- **Severity:** MEDIUM
- **Where:** `transcript-architecture.md`, IMG_9977 "MẶT BẰNG TẦNG 5": *"this floor has no rooms except a stair/lift lobby (5200 long, 3200 + 1800 + 200) with floor tag SL5 and doors D6 (to the front terrace) and D7 (to the rear terrace)"*; and IMG_9978 "MẶT BẰNG MÁI": *"Ô kỹ thuật thang máy = lift technical shaft/overrun (2000 wide, READ; plan 1800 + 900)"*.
- **Issue:** The stair and lift form a **single 3200 + 1800 = 5000 mm core** on every level, and the 1800 mm lift band has no lobby of its own — the lift doors open directly onto the stair. There is no smoke-stop lobby, no protected lobby, no buffer. The only separation between the lift lobby and the rest of the floor is the lift's own doors.
- **Why it matters:** With a fire on an upper floor, the people waiting at the lift are standing in the smoke path of the single stair (S-01). A lift lobby that is part of the escape stair is a trap: the doors fail or the car is on another floor, and the waiting occupants are in the stair enclosure with the fire.
- **Basis:** SCDF Fire Code 2013 Ch. 2 **clause 2.2.13** — for buildings more than four storeys above ground level, exit-staircase entry *"shall be through: (a) an external exit passageway or external corridor … or (b) a lobby that is separated from the adjoining areas of the building by a wall having a fire resistance of 1 hour. The exit access door shall have fire resistance of half an hour fitted with automatic self closing device … The floor area of a smoke-stop lobby shall be not less than 3m2"*. QCVN 06:2022 **clause 3.4.7** — stairwells *"phải có lối ra ngoài trực tiếp tới khu đất liền kề nhà hoặc qua tiền sảnh được ngăn cách với các hành lang và các gian phòng tiếp giáp bằng các vách ngăn cháy loại 1 có cửa đi với cơ cấu tự đóng"*. UK ADB **para. 2.7** — a passenger lift serving any storey more than 4.5 m above ground level should be *"in either of the following. a. The enclosure to the protected stairway … b. A fire resisting lift shaft (minimum REI 30)."* QCVN 06:2022 **clause 3.4.3** — the landing in front of a lift door must be *"không nhỏ hơn tổng chiều rộng bản thang và một nửa chiều rộng cánh cửa của thang máy, nhưng không nhỏ hơn 1,6 m"*.
- **Basis class:** BEYOND-LOCAL (SCDF and ADB) and LOCAL-MINIMUM (QCVN 06 3.4.7)
- **Fix:** Enclose the lift lobby on each floor in a fire-rated enclosure (REI 30 walls, self-closing E 20 doors) with a smoke-stop lobby at the stair, and make the lift shaft REI 30. On a 3.9 m plot this is a spatial problem, not a detailing problem — the 1800 mm lift band has to become a 1800 mm protected lobby with the shaft inside it, which the owner should be told about now because it changes the core and therefore the whole floor plate. Verify against QCVN 06 clause 3.4.3 that the landing keeps the required 1.6 m minimum once the doors are in.
- **Who decides:** architect (core re-plan), fire consultant (enclosure type and rating), owner (cost and whether to keep the lift).
- **Evidence label:** VERIFIED (core dimensions from the transcript; SCDF 2.2.13, ADB 2.7, QCVN 06 3.4.3 and 3.4.7 read from the fetched documents). Whether the shaft is enclosed on each floor is **PARTIAL** — the transcripts show the shaft X-hatched with a lobby, not a rated enclosure.

### S-05

- **ID:** S-05
- **Severity:** MEDIUM
- **Where:** `transcript-architecture.md`, IMG_9977: *"Ô lấy sáng gồn kính cường lực, có khung inox bảo vệ = light well fitted with tempered glass and a protective stainless-steel frame (over the stair; 2000 long x 1500 wide, READ; tag S2 on the stair-side window)"*; IMG_9978: *"Notes … 'Ô lấy sáng' (x2: one at the stair light well, one over the inner well next to the lift shaft)"*.
- **Issue:** The stair is lit by a **glazed light well over its own head, at every level**, with no smoke-venting provision, no smoke control, and no shaft running to the roof identified as a smoke outlet. The glazed panel sits directly over the only escape stair.
- **Why it matters:** Smoke that enters the stair has nowhere to go: the light well is glazed (closed to the fire flow unless it breaks), the roof over the stair is a glazed floor panel, and no smoke outlet is shown. In a fire on an upper floor the stair fills from the bottom and occupants are trapped. This is the "stair open to the void" failure mode in its most literal form.
- **Basis:** QCVN 06 clause **3.4.13** — for an ordinary (non-smoke-proof) stairwell, *"phải bố trí các lối thoát khói trên tum thang với tổng diện tích tối thiểu bằng 10 % diện tích phủ bì (tính cả tường bao che) của sàn buồng thang"* unless the house has at least two escape stairs *"hoặc một cầu thang thoát nạn nhưng có các lối thoát nạn khẩn cấp khác như quy định tại 3.2.6.2"*. QCVN 06 clause **3.4.8(a)** — stairwells must have natural or artificial lighting; natural lighting requires *"các lỗ lấy ánh sáng với diện tích không nhỏ hơn 1,2 m2 trên các tường ngoài ở mỗi tầng"* (L2 stairwells instead require a roof opening ≥ 4 m² with a ≥ 0.7 m gap between flights, or a full-height light well of ≥ 2 m² section). UK ADB **para. 2.9** — air-circulation systems serving a storey more than 4.5 m above ground level must not *"serve other areas as well"* and must shut down on smoke detection, so a mechanical extract serving the stair cannot double as house ventilation.
- **Basis class:** LOCAL-MINIMUM (QCVN 06 3.4.8, 3.4.13) and BEYOND-LOCAL (ADB 2.9)
- **Fix:** Decide one of: **(a)** make the stair a genuine **L1 stairwell** (QCVN 06 clause 3.4.11 — *"Các buồng thang bộ loại L1 và cầu thang bộ loại 3 được phép bố trí trong các nhà … có chiều cao PCCC tới 28 m"*) with fire-resisting construction, self-closing fire doors at each level, and a smoke outlet at the roof of ≥ 10 % of the stair floor area; or **(b)** run the light well as an open, permanently-ventilated shaft from the stair head to the roof with an automatically-opening smoke vent at the top and a ≥ 2 m² clear section, which also serves the ventilation purpose the earlier design review identified; or **(c)** rely on the BS 9251 sprinkler route (S-01) and confirm the stair enclosure is at least REI 30 with fire doors. Whichever is chosen, the glazed panel over the stair must be specified as **not part of the escape provision** and must have a stated fire and load rating.
- **Who decides:** fire consultant (smoke control strategy), architect (core), owner (cost).
- **Evidence label:** VERIFIED (light-well note and dimensions from the transcript; QCVN 06 3.4.8/3.4.11/3.4.13 and ADB 2.9 read from the fetched documents). Whether the glazed panel is fixed or openable is **PARTIAL** — the transcript reads the note but the fixity is not stated, so the severity of the smoke-trapping is bounded by that uncertainty.

**Topic 1 — no issue found / cannot assess:**

- **Travel distance within the unit: no issue found.** The farthest occupied points are the rear bedroom door D4 and the front bedroom door D5; on the drawn chains both are within roughly 3.5 m of the stair. QCVN 06 Appendix G **Table G.1** allows 40 m (bậc chịu lửa I–II, S0) down to 20 m (bậc IV, S1/S2) depending on fire-resistance grade, and SCDF Table 2.2A gives *"NR"* (no requirement) for *"Detached, semi-detached & terrace house, including townhouses"* and 20 m for maisonettes — the house is comfortably inside all of these. **The travel distance is not this building's problem; the single point of failure is.**
- **Exit door widths: no issue found.** The front door D1 is 2800 × 2800 (four-leaf glazed with transom); the lift doors are drawn at 1000 mm clear. SCDF clause 2.2.7(a) requires a minimum clear width of 850 mm at an exit door and caps a single-leaf swing door at 1250 mm; ADK para. 1.23 requires a landing of at least 1200 mm unobstructed.
- **Final exit to the street: no issue found.** The front yard ("Sân trước", −0.200) connects to D1 and the street; there is no exit dispute at the boundary.
- **Roof refuge/access: cannot assess.** Whether the roof terrace is used as an escape route is not stated, and the terrace is reached only through the core.
- **Lift usable in fire: cannot assess**, and it must not be. See S-11, S-35 and S-52.
