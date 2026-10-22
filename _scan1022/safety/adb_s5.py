import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()

i = t.find("Section 5: Internal fire spread")
while i != -1:
    seg = t[i:i+120]
    if "dwellinghouses" in seg:
        break
    i = t.find("Section 5: Internal fire spread", i + 1)

j = t.find("Section 6: Loadbearing elements")
print(t[i:j])
