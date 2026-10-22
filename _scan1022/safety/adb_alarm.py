import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()

i = t.find("Requirement B1")
print("### B1 section")
for m in re.finditer(r"1\.\d+\s+[^\n]{0,60}\n\s{5}[^\n]{0,200}", t):
    pass

j = t.find("1.1 ")
print(t[j - 2500:j + 3500])
