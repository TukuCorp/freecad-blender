import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part1.md"

with open(path, encoding="utf-8") as fh:
    t = fh.read()

m = re.search(r'h\u1ea1ng m\u1ee5c "[^"]+"', t)
print("before:", repr(m.group(0)))

good = 'h\u1ea1ng m\u1ee5c "X\u00c2Y D\u1ef0NG M\u1ed0I"'
t = t[:m.start()] + good + t[m.end():]

with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)

with open(path, encoding="utf-8") as fh:
    t2 = fh.read()
print("after:", repr(re.search(r'h\u1ea1ng m\u1ee5c "[^"]+"', t2).group(0)))
