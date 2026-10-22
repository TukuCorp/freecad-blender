### 3.10 Dimensions and the Lo Ban ruler

**P-29 - Which ruler, which element, and where the schools disagree**

The three rulers and their conventional use, per [7], [8], [9] and [38]:

| ruler | cycle | cung | conventionally measures | good / bad cung names |
|---|---|---|---|---|
| **52.2 cm (thong thuy)** | 522 mm, 8 cung x 65.25 mm, each with 5 sub-cungs | 8 | **the void**: door and window clear widths, openings, light wells, ceiling heights | good: Quy Nhan, Thien Tai, Nhan Luc, Te Tuong - bad: Hiem Hoa, Thien Tai, Co Duc, Thien Tac |
| **42.9 cm (duong trach)** | 429 mm, 8 cung x 53.625 mm, each with 4 sub-cungs | 8 | **the solid**: kitchen counter, steps, stair flights, beds, wardrobes, cabinet heights, storey heights | good: Tai, Nghia, Quan, Ban (Mang) - bad: Benh, Ly, Kiep, Hai |
| **38.8 cm (am phan)** | 388 mm, 10 cung x 38.8 mm, each with 4 sub-cungs | 10 | **the yin/ritual**: altar tables, ancestral cabinets, the ritual tablet | good: Dinh, Vuong, Nghia, Quan, Hung, Tai - bad: Hai, Kho, Tu, That |

**Disagreements between schools, stated rather than hidden:**

1. **The 42.9 cung names.** Some sources call the 8th good cung **Ban** (the base, from Ben), others **Mang** (the fate/net); [39] and [40] both give the order Tai-Benh-Ly-Nghia-Quan-Kiep-Hai-Ban, [38] gives Tai-Benh-Ly-Nghia-Quan-Nan-Hai-Mang, [41] gives Tai-Benh-Ly-Nghia-Quan-Kiep-Hai-Mang, and [42] gives a *different set entirely* (Tai, Hai, Nhan, Kho, Loc, Tho, Tu, Hỷ) for the 42.9 ruler - which is the **38.8 ruler's** cung set. The naming is inconsistent across the Vietnamese literature; the *good/bad* pattern (4 good, 4 bad, alternating pairs) is not.
2. **The 38.8 ruler has 8 cung in some schools and 10 in others.** [38], [43] and [7] all describe a 10-cung ruler with 38.8 mm per cung and 4 sub-cungs; [38] names the ten big cung Dinh-Hai-Kho-Nghia-Quan-Tu-That-Tai. The tables below use the **10-cung version**, because [4] publishes the complete 40-row numeric table for it.
3. **The zero point.** The published 42.9 tables start their first sub-cung at 13.40 mm from the ruler's end (the ruler begins in the *middle* of the Tai cung), while the 38.8 table begins at 9.70 mm. A reading that falls near a cung boundary can therefore come out differently depending on which end you start from. The findings below note every case where the answer flips.
4. **Which ruler for a door.** The 52.2 ruler is for the **clear (thong thuy) opening** - measured between the inner faces of the frame, ignoring the frame's own thickness [38], [9]. Some Vietnamese practice measures the *cover* (phu bi, outer dimension) for a door leaf instead and uses the 42.9 ruler [8].
5. **Whether a door has to be good at all.** [9] gives the popular rule *do thi dung, den thi bo* and [4] the more forgiving *two red, one black*. The two coexist.
6. **The 38.8 ruler's Vietnamese printings drift.** [7] notes that the Vietnamese 38.8 cm rulers are commonly printed 2 mm per ruler away from the Chinese original, and that the 52.2 cm ruler is rare in Vietnam - which is why most Vietnamese practitioners own a combined 42.9 + 38.8 steel rule and look the 52.2 cung up separately.

**P-30 - The printed sizes, read against the rulers**

Computed with the script `_scan1022/loban.py` from the cung tables of [4] (52.2, complete), [39]/[38] (42.9 and 38.8 cung order). *rem* is the position within the 522 / 429 / 388 mm cycle; the cung is the interval the remainder falls in.

**52.2 cm ruler (thong thuy) - doors, windows, openings**

| element | printed size | rem (mm) | cung | verdict |
|---|---|---|---|---|
| **D1 front door**, clear width | 2800 | 190.00 | Thien Tai | **HUNG** (bad) |
| **D1 front door**, clear height | 2800 | 190.00 | Thien Tai | **HUNG** |
| **K1 mezzanine glass wall**, width | 2800 | 190.00 | Thien Tai | **HUNG** |
| **K1 mezzanine glass wall**, height | 1700 | 134.00 | Thien Tai | **HUNG** |
| **S1 balcony window** | 2500 | 412.00 | Thien Tac | **HUNG** |
| **D5 balcony door** | 1100 | 56.00 | Quy Nhan | **CAT** (good) |
| **D6 top-floor door** | 1000 | 478.00 | Te Tuong | **CAT** |
| **S2 top-floor window** | 1200 | 156.00 | Thien Tai | **HUNG** |
| **Dw WC door** (transcript, floors 2-4) | 700 | 178.00 | Thien Tai | **HUNG** |
| internal door (as modelled) | 900 | 378.00 | Co Duc | **HUNG** |
| **frontage, overall** | 3900 | 246.00 | Thien Tai | **CAT** |
| frontage, internal between walls | 3200 | 68.00 | Hiem Hoa | **HUNG** |
| plot width | 3960 | 306.00 | Nhan Luc | **CAT** |
| front yard depth | 3500 | 368.00 | Co Duc | **HUNG** |

**42.9 cm ruler (duong trach) - the solid dimensions**

| element | printed size | rem (mm) | cung | verdict |
|---|---|---|---|---|
| stair tread depth | 250 | 250.00 | Quan | **CAT** |
| stair flight width, tret/lung | 1250 | 392.00 | Ban | **CAT** |
| stair flight width, tang 2-5 | 1350 | 63.00 | Benh | **HUNG** (but **CAT** under the 13.40 mm zero-point convention - see dispute 3 above) |
| stair landing | 1250 | 392.00 | Ban | **CAT** |
| kitchen counter run | 2400 | 255.00 | Quan | **CAT** |
| WC door (as modelled) | 900 | 42.00 | Tai | **CAT** |
| bed width | 1600 | 313.00 | Kiep | **HUNG** |
| bed length | 2100 | 384.00 | Ban | **CAT** (but **HUNG** under the 13.40 mm convention) |
| balcony depth | 1400 | 113.00 | Ly | **HUNG** |
| altar table width | 800 | 371.00 | Hai | **HUNG** |
| altar table length | 1200 | 342.00 | Hai | **HUNG** |
| storey height, ground | 3800 | 368.00 | Hai | **HUNG** |
| storey height, upper floors | 3400 | 397.00 | Ban | **CAT** |
| light well width | 1600 | 313.00 | Kiep | **HUNG** |
| lift shaft width | 1800 | 84.00 | Benh | **HUNG** |
| lift shaft depth | 1600 | 313.00 | Kiep | **HUNG** |
| rear bedroom depth | 4400 | 110.00 | Ly | **HUNG** (Benh under the other convention) |

**38.8 cm ruler (am phan) - the altar**

| element | size | rem (mm) | cung | verdict |
|---|---|---|---|---|
| altar table width | 800 | 24.00 | Dinh | **CAT** |
| altar table depth | 600 | 212.00 | Quan | **CAT** |
| altar table height | 900 | 124.00 | Kho | **HUNG** (Vuong under the 9.70 mm convention) |
| altar table height | 1200 | 36.00 | Dinh | **CAT** |
| ancestral cabinet width | 900 | 124.00 | Kho | **HUNG** (Vuong under the other convention) |
| ritual tablet width | 300 | 300.00 | Hung | **CAT** |
| altar room width | 3960 | 80.00 | Vuong | **CAT** |
| altar room depth | 4000 | 120.00 | Kho | **HUNG** (Vuong under the other convention) |

**Reading this table honestly.** The size of the altar table is not in the drawings - 800 / 600 / 900 / 1200 are the dimensions the sources use as examples - and the table shows that **800 wide and 600 deep are already good cung**; the altar's height is the one dimension worth choosing (900 lands on Kho, 1200 lands on Dinh - a 300 mm difference for a better cung, which is the whole point of the ruler). The building's own dimensions are fixed and mostly land on mixed cung, which is exactly what the tradition says to expect of an existing building: **the ruler is a tool for choosing what you still have the freedom to choose** (the altar, the door leaves, the cabinet sizes, the interior partition positions) and is not a reason to move a structural wall.

**P-31 - The frontage, 3.95 m, and the Lo Ban**

- **Where:** the frontage is printed as 3900 overall at the front, with 350 + 3200 + 350 wall zones; the plot is 3960 in the model (`measurements.md`: *frontage printed 3950 on every sheet; +10 mm orthogonal margin*).
- **Rule:** the frontage is measured with the **42.9 cm (duong trach)** ruler - it is a built, solid dimension of the house's face [8], [38]. A separate and very widely held folk rule is that the frontage should be an **odd** number of *units* (traditional Vietnamese *thuoc* of 30.3 cm and 30.4 cm, and in southern practice a *thuoc* of about 0.32 m) so that the house can be divided into an integral number of bays; an un-dividable frontage is called *cua hau* or *bat tien* in the trade.
- **School:** Lo Ban + general nha ong folk rule.
- **Agreement:** COMMON as a folk rule; the Lo Ban reading itself is contested in strength, and the *odd number of traditional thuoc* rule is a trade rule rather than a phong thuy one.
- **Severity in the tradition:** MINOR.
- **Remedy:** none available for the frontage - it is the plot. The trader's rule (frontage divisible into an integral number of bays) is actually **satisfied** here: 3900 = 350 + 3200 + 350, and the interior 3200 divides into the 1000 mm structural module the drawings use (chain: 350 | 3010 | 4240 | 4000 | 3200 | 1800 | 4500 | 1600). So the practical version of this rule passes.
- **Practical rationale:** the Lo Ban reading of the frontage on the 42.9 ruler gives 3900 -> rem 39.00 -> **Tai** (good), while the *plot* width 3960 -> rem 99.00 -> **Benh** (bad) and the *internal* 3200 -> rem 197.00 -> **Nghia** (good). The disagreement between the building line and the plot line is a 60 mm difference - a good illustration of why this rule is not worth arguing about at this level of precision.
- **Conflict with safety/design:** none.
- **Evidence:** VERIFIED for the dimensions (IMG_9972 frontage chains; measurements.md plot table). VERIFIED for the ruler attribution ([8], [38]). VERIFIED as arithmetic on [4]/[39]/[38] for the computed cung.

**P-32 - The internal 900 mm door leaves, and the 700 mm WC door**

- **Where:** the model has 900 mm internal doors throughout (JSON `openings`, `width_mm: 900`); the transcript reads Dw (WC door) at 700 on floors 2-4 (IMG_9974: *door Dw 700 / 750, 850 + 950 widths* - PARTIAL).
- **Rule:** a door's clear width is read on the 52.2 ruler. 900 -> Co Duc (bad); 700 -> Thien Tai (bad). The sources' own *so dep* lists for a 52.2 ruler are 750-810 (a single-leaf room door), 1070-1100 (a double-leaf or large door), 1270-1330 (a two-leaf main door), 1530 (three leaves), 1860 (three or four leaves), 2120 / 2330 (four-leaf main door height) - [43], [42], [44].
- **School:** Lo Ban.
- **Agreement:** COMMON.
- **Severity in the tradition:** MINOR.
- **Remedy:** essentially free, and **this is the one Lo Ban rule that is worth acting on**, because door leaves are made to measure at the end of the job: an internal leaf of **810** (Nhan Luc, good) rather than 900 (Co Duc) costs nothing but a different order quantity; the WC door at **760** (Thien Tai, good) rather than 700 costs 60 mm of clearance and one hinge adjustment. The main door D1 at 2800 sits in **Thien Tai**; **2810-2870** moves it into the next cung boundary as the table of [4] gives it, and **2880-2900** into Nhan Luc. A 10-100 mm change to a **clear** opening on a 2800 mm door is a joinery change, not a structural one - but it is only possible if it is decided now, before the frames are ordered.
- **Practical rationale:** none of this is about the door being lucky; it is about the fact that these are the *only* dimensions on this project that are still free and that the change is smaller than a tolerance. The honest caveat is that a 10 mm change to a 2800 mm opening changes nothing measurable about the house - which is exactly the point of the exercise for the owner: it is a free gesture, not a fix.
- **Conflict with safety/design: door width is a safety and accessibility matter.** The clear width of the main door and the stair doors is governed by egress and accessibility requirements, not by a ruler. **Do not narrow a door to improve its cung.** In particular, the bedroom doors must retain the clear width that the escape route needs, and the WC door must not be narrowed below what the layout needs. Where the ruler and the escape width conflict, the escape width wins and the ruler is dropped.
- **Evidence:** VERIFIED for the sizes (JSON openings; IMG_9974 Dw PARTIAL). VERIFIED as arithmetic for the ruler computation. VERIFIED for the *so dep* lists ([42], [43], [44]).

---

