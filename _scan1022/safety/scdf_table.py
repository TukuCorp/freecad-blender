import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/scdf_ch2.txt", encoding="utf-8", errors="ignore").read()

i = t.find("Table 2.2A")
while i != -1:
    seg = t[i:i+200]
    if "Travel" in seg or "Occupancy" in seg or "Width" in seg:
        print("=====", i)
        print(t[i:i+4200])
        break
    i = t.find("Table 2.2A", i + 1)

print("\n#### search travel distance table")
for m in re.finditer(r"Maximum travel distance", t):
    print(t[max(0, m.start() - 1500):m.start() + 2000])
    break
