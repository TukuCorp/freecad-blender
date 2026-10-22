import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()


def show(label, pattern, span=1600, limit=1, before=0):
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


show("STAIR TYPE DEFS", r"1 \u2013 Cầu thang bộ loại 1|Cầu thang bộ loại 1:", 1200, 1, 400)
show("TABLE 4 FIRE RES", r"Bảng 4 ", 1800, 1, 300)
show("BALCONY GUARD HEIGHT", r"lan can[^\n]{0,80}1,1 m|1,1 m[^\n]{0,80}lan can", 700, 3)
show("LAN CAN 1,2", r"lan can cao 1,2 m|chiều cao lan can", 600, 2)
show("3.2.2 EXIT COUNT", r"3\.2\.2 ", 1200, 1)
show("APPENDIX D SMOKE", r"PHỤ LỤC D", 400, 1)
