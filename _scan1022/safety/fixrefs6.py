import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part2.md"
old = (
    "This is Question 4b in the list below (folded into the rear-boundary question)."
)
new = (
    "This is covered by Question 4 in the list below \u2014 please ask the contractor what the "
    "2600 mm rear boundary element is and whether the rear yard is enclosed or open."
)
with open(path, encoding="utf-8") as fh:
    t = fh.read()
print("found:", old in t)
t = t.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)

path2 = "_scan1022/safety/part4.md"
old2 = (
    "4. **What is the design flood level and the design groundwater level for this plot?** "
    "Please supply the official HCMC flood and tidal inundation mapping for ward Minh Ph\u1ee5ng "
    "and 506 H\u1ed3ng B\u00e0ng, the historic high-water mark, and a site levels survey "
    "establishing what \u00b10.000 means in street level."
)
new2 = (
    "4. **What is the design flood level and the design groundwater level for this plot, and what "
    "is the 2600 mm element at the rear boundary?** Please supply the official HCMC flood and "
    "tidal inundation mapping for ward Minh Ph\u1ee5ng and 506 H\u1ed3ng B\u00e0ng, the "
    "historic high-water mark, and a site levels survey establishing what \u00b10.000 means in "
    "street level. Please also state whether the rear boundary is a fence, a wall or a gate, and "
    "whether the rear yard is enclosed \u2014 this decides whether the rear door D2 is a usable "
    "final exit at all."
)
with open(path2, encoding="utf-8") as fh:
    t2 = fh.read()
print("found2:", old2 in t2)
t2 = t2.replace(old2, new2)
with open(path2, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t2)
print("done")
