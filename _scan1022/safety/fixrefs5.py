import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part2.md"
old = (
    "(iv) make the rear door D2 a second final exit to the rear yard and confirm the rear boundary wall "
    "does not trap occupants \u2014 the rear yard is 2.3\u20132.5 m deep and the boundary is drawn as a "
    "2600 mm-high wall, so D2 is not a usable exit unless the rear boundary is treated accordingly "
    "(see S-19)."
)
new = (
    "(iv) establish what the 2600 mm rear boundary element actually is \u2014 a fence, a wall or a gate "
    "\u2014 and make D2 discharge to a space a person can be rescued from. The rear yard is only "
    "2.3\u20132.5 m deep, so a solid 2600 mm boundary would make D2 a trap rather than an exit."
)

with open(path, encoding="utf-8") as fh:
    t = fh.read()
print("found:", old in t)
t = t.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)
print("done")
