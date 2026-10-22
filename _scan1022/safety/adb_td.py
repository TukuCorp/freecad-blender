import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()

for pat in [r"Table 3\.2", r"3\.3[0-9]\s", r"Dwellinghouse[^\n]{0,40}travel"]:
    print("#### " + pat)
    n = 0
    for m in re.finditer(pat, t):
        i = m.start()
        print("-----")
        print(t[i:i+1300])
        n += 1
        if n >= 3:
            break
