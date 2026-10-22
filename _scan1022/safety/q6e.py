import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()


def show(label, pattern, span=1800, limit=3):
    print("################ " + label)
    n = 0
    for m in re.finditer(pattern, t):
        i = m.start()
        print("-----")
        print(t[i:i+span])
        n += 1
        if n >= limit:
            break
    if n == 0:
        print("(not found)")


show("F1.3 GROUP DEF", r"F1\.3\s+ĐƠN NGUYÊN NHÀ Ở")
show("TRAVEL DISTANCE APPENDIX G", r"Phụ lục G\s*$|PHỤ LỤC G\s*$")
show("3.2.13 EMERGENCY EXIT", r"3\.2\.13\s", 1500, 2)
show("3.2.6 ALTERNATIVE ESCAPE", r"3\.2\.6\.\d", 1400, 2)
