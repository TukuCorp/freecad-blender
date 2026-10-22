import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def grab(t, label, needle, span=1600, before=0, limit=1):
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


scdf = open("_scan1022/safety/scdf_ch2.txt", encoding="utf-8", errors="ignore").read()
adb = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()

grab(scdf, "SCDF 2.3.3 exit staircase", r"2\.3\.3\s", 2600, 0, 1)
grab(scdf, "SCDF 2.2.13 smoke free", r"2\.2\.13\s", 2000, 0, 1)
grab(adb, "ADB 2.10 diagram 2.5", r"Diagram 2\.5", 1800, 200, 1)
grab(adb, "ADB 2.7 lift", r"2\.7\s+A passenger lift", 700, 0, 1)
