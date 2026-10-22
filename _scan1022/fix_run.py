# -*- coding: utf-8 -*-
"""Driver: apply all correction parts to out-phongthuy.md."""
import sys

import fixlib

import fix_part_a
import fix_part_b
import fix_part_c
import fix_part_d
import fix_part_e
import fix_part_f
import fix_part_g

sys.stdout.reconfigure(encoding="utf-8")

lines = fixlib.load()
print("loaded %d lines" % len(lines))
lines = fixlib.apply(lines)
fixlib.save(lines)
fixlib.report()
