import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

i = t.find("3.2.6.2 Cho phép bố trí một lối ra thoát nạn")
j = t.find("3.2.7", i)
print(t[i:j])
