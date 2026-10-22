# -*- coding: utf-8 -*-
"""Diff the corrected file against the backup, finding-wise, to confirm what changed."""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

BEFORE = "_scan1022/out-phongthuy.before-fix.md"
AFTER = "contractor/scan-2026-10-22/review/out-phongthuy.md"


def findings(path):
    text = io.open(path, encoding="utf-8").read()
    parts = re.split(r"\n\n(?=\*\*P-\d\d - )", text)
    out = {}
    for p in parts:
        m = re.match(r"\*\*(P-\d\d) -", p)
        if m:
            out[m.group(1)] = p
    return out


b = findings(BEFORE)
a = findings(AFTER)

print("before findings: %d   after findings: %d" % (len(b), len(a)))
print("ids missing after : %s" % sorted(set(b) - set(a)))
print("ids added after   : %s" % sorted(set(a) - set(b)))
print()
print("=== per-finding changed / unchanged ===")
changed = []
same = []
for k in sorted(b, key=lambda s: int(s[2:])):
    if k not in a:
        continue
    if b[k].strip() == a[k].strip():
        same.append(k)
    else:
        changed.append(k)
print("CHANGED   (%d): %s" % (len(changed), ", ".join(changed)))
print("UNCHANGED (%d): %s" % (len(same), ", ".join(same)))

print()
print("=== whole-document diff stats ===")
import difflib

bl = io.open(BEFORE, encoding="utf-8").read().splitlines()
al = io.open(AFTER, encoding="utf-8").read().splitlines()
sm = difflib.SequenceMatcher(None, bl, al, autojunk=False)
added = removed = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ("replace", "delete"):
        removed += i2 - i1
    if tag in ("replace", "insert"):
        added += j2 - j1
print("lines removed/replaced: %d" % removed)
print("lines added/replaced  : %d" % added)
print("before lines: %d  after lines: %d" % (len(bl), len(al)))
