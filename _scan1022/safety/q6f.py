import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()


def show(label, pattern, span=2000, limit=2):
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


show("3.2.6.2 continued", r"2\) Đối với nhà có chiều cao PCCC lớn hơn 15 m", 2600, 1)
show("PHU LUC G", r"PHỤ LỤC G", 200, 1)
show("Bang G travel", r"Bảng G\.\d", 300, 12)
show("F1.3 dinh nghia", r"ĐƠN NGUYÊN NHÀ Ở", 1200, 1)
