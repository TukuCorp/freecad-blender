import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part1.md"
old = 'h\u1ea1ng m\u1ee5c "X\u00c2Y D\u1ef0NG M\u1ed4I"'
new = 'h\u1ea1ng m\u1ee5c "X\u00c2Y D\u1ef0NG M\u1ed0I"'

with open(path, encoding="utf-8") as fh:
    t = fh.read()
print("found:", old in t)
t = t.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)
print("done")
