import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

WANT = [
    "3.4.2 ", "3.4.4 ", "3.4.5 ", "3.4.6 ", "3.4.7 ", "3.4.9 ", "3.4.10 ", "3.4.11 ",
    "3.4.12 ", "3.4.13 ",
]

for w in WANT:
    m = re.search(re.escape(w), t)
    if not m:
        print("== " + w + " NOT FOUND")
        continue
    i = m.start()
    print("==================== " + w)
    print(t[i:i+1600])
