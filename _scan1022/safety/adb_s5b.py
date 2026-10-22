import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()

hits = [m.start() for m in re.finditer(r"Section 5: Internal fire spread", t)]
print(hits)
for i in hits:
    seg = t[i:i+200]
    print("=====", repr(seg[:160]))

# find the body: paragraph 5.x
for pat in [r"5\.1\s+", r"5\.2\s+", r"5\.3\s+", r"5\.4\s+", r"5\.5\s+", r"5\.6\s+"]:
    m = re.search(pat, t)
    if m:
        print("----- " + pat)
        print(t[m.start():m.start()+1500])
