# -*- coding: utf-8 -*-
"""Structural verification of the corrected out-phongthuy.md."""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

PATH = "contractor/scan-2026-10-22/review/out-phongthuy.md"
raw = io.open(PATH, encoding="utf-8", newline="").read()
lines = raw.replace("\r\n", "\n").split("\n")

print("bytes            : %d" % len(raw.encode("utf-8")))
print("CRLF count       : %d" % raw.count("\r\n"))
print("bare LF count    : %d" % (raw.count("\n") - raw.count("\r\n")))
print("BOM              : %s" % (raw[:3] == "\xef\xbb\xbf"))
raw.encode("utf-8").decode("utf-8")
print("utf-8 round-trip : ok")

print()
print("=== headings ===")
for i, l in enumerate(lines, 1):
    if re.match(r"^#{1,3} ", l):
        print("%5d  %s" % (i, l))

print()
print("=== finding ids present ===")
ids = re.findall(r"\*\*(P-\d\d) -", "\n".join(lines))
for n in range(1, 33):
    tag = "P-%02d" % n
    print("  %s : %d" % (tag, ids.count(tag)))

print()
print("=== 2.2 eight-row table integrity ===")
i = next(k for k, l in enumerate(lines) if l.startswith("| Cung (quẻ)"))
rows = [l for l in lines[i + 2:i + 12] if l.startswith("| **")]
print("data rows        : %d" % len(rows))
for r in rows:
    print("  %s" % r.split("|")[1].strip())

print()
print("=== section 5 table row count ===")
i = next(k for k, l in enumerate(lines) if l.startswith("| # | phong thuy suggestion"))
rows = [l for l in lines[i + 2:] if re.match(r"^\| \d+ \|", l)]
print("rows             : %d" % len(rows))

print()
print("=== markdown table column consistency ===")
bad = 0
prev_cols = None
for i, l in enumerate(lines, 1):
    if l.startswith("|"):
        c = l.count("|")
        if prev_cols is not None and c != prev_cols:
            print("  line %d cols %d != %d : %s" % (i, c, prev_cols, l[:80]))
            bad += 1
        prev_cols = c
    else:
        prev_cols = None
print("inconsistent     : %d" % bad)

print()
print("=== evidence labels still in use ===")
for lab in ["VERIFIED", "PARTIAL", "CLAIMED", "NOT FOUND", "UNVERIFIED", "MODEL"]:
    print("  %-10s : %d" % (lab, len(re.findall(r"\b%s\b" % lab, "\n".join(lines)))))
