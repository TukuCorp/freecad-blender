import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

EDITS = {
    "_scan1022/safety/part2.md": [
        (
            'and *"PHẦN GHI CHÚ (remarks) box is blank on every sheet."*',
            'and *"PHẦN GHI CHÚ" (remarks) box is blank on every sheet.*',
        ),
        (
            '**Fix:** Add a **fire-safety sheet (a "PHƯƠNG ÁN AN TOÀN CHÁY" / fire strategy sheet)** to the set,',
            '**Fix:** Add a **fire-safety sheet** (a fire-strategy sheet; the Vietnamese title the owner\'s authority will expect is "PHƯƠNG ÁN AN TOÀN CHÁY", which is a name this review proposes, not one read from the drawings) to the set,',
        ),
    ],
}

for path, pairs in EDITS.items():
    with open(path, encoding="utf-8") as fh:
        t = fh.read()
    for old, new in pairs:
        print(("OK  " if old in t else "MISS"), path, "|", old[:60])
        t = t.replace(old, new)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(t)
