import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part1.md"
old = (
    '**Project:** NH\u00c0 \u1eceI RIA\u00caG L\u1ec6, 506 \u0110\u01af\u1ed0NG H\u1ed4NG B\u00c0NG, '
    'PH\u01af\u1ed2NG MINH PH\u1ee5NG, TP.HCM ("H\u1ed2 S\u01a0 THI\u1ebeT K\u1ebE THI C\u00d4NG")'
)
new = (
    '**Project:** NH\u00c0 \u1eceI RIA\u00caG L\u1ec6, 506 \u0110\u01af\u1ed0NG H\u1ed4NG B\u00c0NG, '
    'PH\u01af\u1ed2NG MINH PH\u1ee5NG, TP.HCM ("H\u1ed2 S\u01a0 THI\u1ebeT K\u1ebE THI C\u00d4NG", '
    'h\u1ea1ng m\u1ee5c "X\u00c2Y D\u1ef0NG M\u1ed4I")'
)

with open(path, encoding="utf-8") as fh:
    t = fh.read()
print("found:", old in t)
t = t.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)
print("done")
