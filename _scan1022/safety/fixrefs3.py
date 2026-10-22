import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

EDITS = {
    "_scan1022/safety/part1.md": [
        (
            "**Lift usable in fire: cannot assess**, and it must not be. See S-11 and S-35.",
            "**Lift usable in fire: cannot assess**, and it must not be. See S-11, S-35 and S-52.",
        ),
        (
            "see S-01 and S-38, where the ADB para. 2.6(b) BS 9251 route is offered as the resolution to the single-stair problem.",
            "see S-01, where the ADB para. 2.6(b) BS 9251 route is offered as the resolution to the single-stair problem.",
        ),
    ],
}

for path, pairs in EDITS.items():
    with open(path, encoding="utf-8") as fh:
        t = fh.read()
    for old, new in pairs:
        if old not in t:
            print("MISS:", path, "|", old[:70])
            continue
        t = t.replace(old, new)
        print("OK  :", path, "|", old[:70])
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(t)
