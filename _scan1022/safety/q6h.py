import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()


def show(label, pattern, span=1500, limit=1, before=0):
    print("################ " + label)
    n = 0
    for m in re.finditer(pattern, t):
        i = m.start()
        print("-----")
        print(t[max(0, i - before):i + span])
        n += 1
        if n >= limit:
            break
    if n == 0:
        print("(not found)")


show("ALARM 3.4.x / 3.1.x", r"3\.4\.\d+\s+Hệ thống báo động", 1200, 2)
show("STAIRWELL TYPES DEF", r"Buồng thang bộ loại 1", 900, 1)
show("STAIR TYPE 2 DEF", r"Cầu thang bộ loại 2", 900, 1)
show("STAIR TYPE 3 DEF", r"Cầu thang bộ loại 3", 900, 1)
show("3.2.12", r"3\.2\.12\s", 1800, 1)
show("3.2.14", r"3\.2\.14\s", 1200, 1)
show("BALCONY GUARD", r"ban công[^.]{0,200}lan can", 700, 3)
