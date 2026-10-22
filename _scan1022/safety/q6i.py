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


show("3.4.1 tail (khi khong bao dam)", r"Trong trường hợp không thể bảo đảm được các kí", 1400, 1)
show("LIFT SHAFT", r"giếng thang máy", 1000, 3)
show("FIRE LIFT", r"thang máy chữa cháy", 900, 2)
show("GARA", r"gara", 900, 2)
show("FIRE ALARM", r"báo động cháy", 900, 2)
show("SPRINKLER HOUSE", r"hệ thống chữa cháy tự động", 800, 2)
show("FLOOR COMPARTMENT", r"ngăn cháy giữa các tầng|tầng chống cháy lan|kết cấu ngăn cháy giữa", 900, 2)
