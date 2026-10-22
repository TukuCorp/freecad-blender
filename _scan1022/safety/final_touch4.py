import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part1.md"

with open(path, encoding="utf-8") as fh:
    t = fh.read()

good = "XÂY DỰNG MỚI"
bad = "XÂY DỰNG MỔI"
print("bad present:", bad in t)
t = t.replace(bad, good)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)

with open(path, encoding="utf-8") as fh:
    t2 = fh.read()
print("good present:", good in t2)
i = t2.find("**Project:**")
print(repr(t2[i:i + 190]))
