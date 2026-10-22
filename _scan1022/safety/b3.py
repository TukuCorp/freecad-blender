import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()
ms = [m.start() for m in re.finditer(r"Table B3", t)]
print("hits", len(ms))
for idx in (5, 6, 7, 8):
    i = ms[idx]
    seg = t[i - 2600:i + 1200]
    if "Minimum" in seg or "minutes" in seg or "REI" in seg or "60" in seg:
        print("=========== idx", idx)
        print(seg)
        break
else:
    print(t[ms[5] - 2000:ms[5] + 2000])
