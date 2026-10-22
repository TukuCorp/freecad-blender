# -*- coding: utf-8 -*-
"""Sanity checks on the corrected out-phongthuy.md. Prints counts only."""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

PATH = "contractor/scan-2026-10-22/review/out-phongthuy.md"
text = io.open(PATH, encoding="utf-8").read()
lines = text.splitlines()


def count(pattern, flags=0):
    return len(re.findall(pattern, text, flags))


print("=== forbidden ids ===")
print("tho_f5                : %d" % count(r"tho_f5"))
print("wc_truoc_f5           : %d" % count(r"wc_truoc_f5"))
print("hall_front_f5         : %d" % count(r"hall_front_f5"))
print("san_thuong_* ids      : %d" % count(r"san_thuong_"))
print("wc_sau_f* ids         : %d" % count(r"wc_sau_f"))
print("ngu_sau_f* ids        : %d" % count(r"ngu_sau_f"))
print("wc_gf ids             : %d" % count(r"wc_gf"))
print("bep_an ids            : %d" % count(r"bep_an"))
print("openings ids          : %d" % count(r"JSON `openings`"))
print("stairwell ids         : %d" % count(r"`stairwell`"))

print("=== altar on 5th floor ===")
print("altar + 5th floor     : %d" % count(
    r"(?is)(altar|ban tho|P\. THO|P\. Thờ)[^.]{0,200}5th floor"))
print("5th floor + altar     : %d" % count(
    r"(?is)5th floor[^.]{0,200}(altar|ban tho|P\. THO|P\. Thờ)"))
print("'tang 5'/'tầng 5' altar: %d" % count(
    r"(?is)(altar|ban tho)[^.]{0,200}(tang 5|tầng 5)"))
print("P. Thờ on tầng 5      : %d" % count(
    r"(?is)P\. Thờ[^.]{0,120}tầng 5"))
print("'P. Thu, tang 5'      : %d" % count(r"P\. Thu, tang 5"))

print("=== lift inference withdrawn ===")
print("'lift is only inferred': %d" % count(r"(?i)lift[^.]{0,120}only inferred"))
print("'existence ... infer'  : %d" % count(r"(?i)existence below the roof"))
print("'shaft ... inference'  : %d" % count(r"(?i)shaft[^.]{0,160}inference"))
print("'model ... infers it'  : %d" % count(r"(?i)infers it"))

print("=== JSON / measurements citations ===")
print("'JSON' mentions        : %d" % count(r"JSON"))
print("'measurements.md'      : %d" % count(r"measurements\.md"))
print("'y 18100' style bands  : %d" % count(r"y 1[0-9]{4}"))
print("'y = 12 300' style     : %d" % count(r"y = \d[\d ]\d\d\d"))

print("=== structure ===")
print("lines                 : %d" % len(lines))
print("finding ids P-01..P-32: %d" % len(
    set(re.findall(r"\*\*(P-\d\d) -", text))))
print("corrections section   : %d" % count(r"## Corrections 2026-10-22"))
print("P-21 title            : %d" % count(r"\*\*P-21 - "))
print("P-22 title            : %d" % count(r"\*\*P-22 - "))
print("P-23 title            : %d" % count(r"\*\*P-23 - "))
print("s6.4 heading          : %d" % count(r"### 6\.4 "))
print("safety-wins line      : %d" % count(r"safety wins"))
