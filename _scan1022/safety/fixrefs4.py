import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part2.md"
old = "see S-01 and S-38, where the ADB para. 2.6(b) BS 9251 route is offered as the resolution to the single-stair problem."
new = "see S-01, where the ADB para. 2.6(b) BS 9251 route is offered as the resolution to the single-stair problem."

with open(path, encoding="utf-8") as fh:
    t = fh.read()
print("found:", old in t)
t = t.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)
print("done")
