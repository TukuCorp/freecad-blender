# -*- coding: utf-8 -*-
"""Shared helpers for the out-phongthuy.md correction pass.

Edits are applied by 1-based inclusive line range in the ORIGINAL file, applied from the
bottom upwards so the line numbers are stable and auditable. Each edit carries a guard
string that must appear on its first line, so a drifted edit fails loudly instead of
silently writing the wrong thing.
"""
import io
import sys

sys.stdout.reconfigure(encoding="utf-8")

PATH = "contractor/scan-2026-10-22/review/out-phongthuy.md"

EDITS = []
INSERTS = []
REPS = []
LOG = []


def E(start, end, text, label, expect=None):
    """Replace original lines [start, end] with text."""
    EDITS.append((start, end, text, label, expect))


def INS(before_line, text, label, expect=None):
    """Insert text immediately before original line before_line."""
    INSERTS.append((before_line, text, label, expect))


def REP(old, new, label):
    """Exact-substring replacement, must match exactly once."""
    REPS.append((old, new, label))


def load():
    with io.open(PATH, encoding="utf-8", newline="") as fh:
        raw = fh.read()
    assert "\r\n" in raw, "expected CRLF source"
    return raw.replace("\r\n", "\n").split("\n")


def apply(lines):
    for start, end, text, label, expect in sorted(EDITS, key=lambda e: -e[0]):
        got = lines[start - 1]
        if expect is not None:
            assert expect in got, (
                "edit %s: line %d lacks %r -> %r" % (label, start, expect, got[:90]))
        lines[start - 1:end] = text.split("\n")
        LOG.append("edit   %-28s lines %d-%d" % (label, start, end))
    for before_line, text, label, expect in sorted(INSERTS, key=lambda e: -e[0]):
        got = lines[before_line - 1]
        if expect is not None:
            assert expect in got, (
                "insert %s: line %d lacks %r -> %r"
                % (label, before_line, expect, got[:90]))
        lines[before_line - 1:before_line - 1] = text.split("\n")
        LOG.append("insert %-28s before line %d" % (label, before_line))
    text = "\n".join(lines)
    for old, new, label in REPS:
        n = text.count(old)
        assert n == 1, "rep %s: expected 1 match, got %d" % (label, n)
        text = text.replace(old, new)
        LOG.append("rep    %-28s (1 match)" % label)
    lines = text.split("\n")
    return lines


def save(lines):
    out = "\n".join(lines)
    with io.open(PATH, "w", encoding="utf-8", newline="\r\n") as fh:
        fh.write(out)
    LOG.append("wrote %s (%d lines)" % (PATH, len(lines)))


def report():
    for row in LOG:
        print(row)
