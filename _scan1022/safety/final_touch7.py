import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part1.md"

with open(path, encoding="utf-8") as fh:
    t = fh.read()

m = re.search(r'hạng mục "[^"]*"', t)
print("before:", repr(m.group(0)))

good = 'hạng mục "XÂY DỰNG MỚI"'
t = t[:m.start()] + good + t[m.end():]

with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)

with open(path, encoding="utf-8") as fh:
    t2 = fh.read()

m2 = re.search(r'hạng mục "[^"]*"', t2)
print("after:", repr(m2.group(0)))
for ch in m2.group(0):
    if ord(ch) > 127:
        print("   ", ch, hex(ord(ch)))
