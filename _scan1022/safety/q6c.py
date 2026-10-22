import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

for pat in [
    r"3\.3\.\d\s",
    r"3\.4\.\d\s",
    r"3\.5\.\d\s",
]:
    print("=== " + pat)
    for m in re.finditer(pat, t):
        i = m.start()
        seg = t[i:i+220].split("\n")
        print(" | ".join(x.strip() for x in seg[:4] if x.strip())[:200])
