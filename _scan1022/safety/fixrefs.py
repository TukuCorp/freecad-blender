import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

EDITS = {
    "_scan1022/safety/part2.md": [
        (
            "There is no second exit from the rear yard at ground level to step into (D2 leads to a rear yard that is enclosed by a boundary wall \u2014 see S-08 fix note).",
            "There is no second exit from the rear yard at ground level to step into \u2014 D2 leads to a rear yard that is enclosed by a 2600 mm boundary element, which may not be a usable final exit at all.",
        ),
        (
            "and the garage-to-house door (see S-10).",
            "and the garage-to-house door (S-09).",
        ),
        (
            "the construction must be coordinated with the neighbours (see S-16, S-17).",
            "the construction must be coordinated with the neighbours (S-28, S-29).",
        ),
    ],
}

for path, pairs in EDITS.items():
    with open(path, encoding="utf-8") as fh:
        t = fh.read()
    for old, new in pairs:
        if old not in t:
            print("MISS:", old[:70])
            continue
        t = t.replace(old, new)
        print("OK  :", old[:70])
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(t)
