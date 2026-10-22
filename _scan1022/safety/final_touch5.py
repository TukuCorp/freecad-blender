import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part1.md"

with open(path, encoding="utf-8") as fh:
    t = fh.read()

m = re.search(r'h\u1ea1ng m\u1ee5c "([^"]+)"', t)
print("current:", repr(m.group(1)) if m else None)
for ch in m.group(1):
    print("   ", ch, hex(ord(ch)))

src = open("contractor/scan-2026-10-22/transcript-architecture.md", encoding="utf-8").read()
mm = re.search(r'H\u1ea1ng m\u1ee5c: ([^,\n]+)', src)
good = mm.group(1).strip()
print("from transcript:", repr(good))

t = t[:m.start(1)] + good + t[m.end(1):]
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)

with open(path, encoding="utf-8") as fh:
    t2 = fh.read()
print("now:", repr(re.search(r'h\u1ea1ng m\u1ee5c "([^"]+)"', t2).group(1)))
