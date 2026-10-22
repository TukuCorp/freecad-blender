import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

for m in re.finditer(r"lan can", t):
    i = m.start()
    print("----")
    print(t[max(0, i - 1200): i + 1500])
