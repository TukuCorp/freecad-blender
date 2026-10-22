import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()


def show(label, pattern, span=2000, limit=1, before=0):
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


show("STAIR TYPES DEF", "Cầu thang bộ loại 1\s*:", 900, 1, 1100)
show("N1 DEF", "Buồng thang bộ loại N1\s*:", 800, 1, 900)
show("APPENDIX D HEAD", "PHỤ LỤC D \(quy định\)", 3000, 1, 200)
show("F1.3 STAIR", "F1\.3[^\n]{0,200}cầu thang", 600, 3)
show("2.2 BANG 6", "Bảng 6 ", 2200, 1, 200)
