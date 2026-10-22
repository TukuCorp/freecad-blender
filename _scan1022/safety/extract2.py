import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def grab(t, label, needle, span=1500, before=0, limit=1):
    print("################ " + label)
    n = 0
    for m in re.finditer(needle, t):
        i = m.start()
        print("-----")
        print(t[max(0, i - before):i + span])
        n += 1
        if n >= limit:
            break
    if n == 0:
        print("(not found)")


vn = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()
adb = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()

grab(vn, "VN glass balustrade", r"mặt kính[^\n]{0,80}lan can|lan can[^\n]{0,80}mặt kính", 900, 400, 3)
grab(vn, "VN balcony height rail", r"1,05 m|0,95 m|1,1 m[^\n]{0,60}lan can", 700, 400, 4)
grab(vn, "VN 4.x balcony balcony", r"4\.\d+\s+[^\n]{0,40}ban công", 1400, 200, 3)
grab(adb, "ADB 3.10-3.14 upper storeys dwellings", r"3\.1[0-4]\s", 1400, 0, 5)
grab(adb, "ADB 2.11 balcony escape roof", r"2\.1[1-4]\s", 1200, 0, 4)
