import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()

m = re.search(r"5\.8\s+", t)
print(t[m.start():m.start()+5200])
