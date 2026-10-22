import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()
adk = open("_scan1022/safety/adk.txt", encoding="utf-8", errors="ignore").read()
adb = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()
vn = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()
scdf = open("_scan1022/safety/scdf_ch2.txt", encoding="utf-8", errors="ignore").read()

print("=== ADK clauses cited, present in source? ===")
for n in sorted(set(re.findall(r"ADK[^.\n]{0,14}\*\*para\. (\d+\.\d+)", t))):
    hit = re.search(r"\n\s*" + re.escape(n) + r"\s", adk)
    print(("OK  " if hit else "MISS"), n)

print("=== ADB clauses cited, present in source? ===")
for n in sorted(set(re.findall(r"ADB[^.\n]{0,14}\*\*para\. (\d+\.\d+)", t))):
    hit = re.search(r"\n" + re.escape(n) + r"\s", adb)
    print(("OK  " if hit else "MISS"), n)

print("=== QCVN clauses cited, present in source? ===")
for n in sorted(set(re.findall(r"clause \*\*(\d+\.\d+(?:\.\d+)?)", t))):
    hit = re.search(r"(?m)^\s*" + re.escape(n) + r"\b", vn)
    print(("OK  " if hit else "MISS"), n)

print("=== SCDF clauses cited, present in source? ===")
for n in sorted(set(re.findall(r"SCDF clause \*\*(\d+\.\d+(?:\.\d+)?)", t))):
    hit = re.search(r"(?m)^\s*" + re.escape(n) + r"\b", scdf)
    print(("OK  " if hit else "MISS"), n)

print("=== formatting probes ===")
probes = ["ADK **para. 1.34", "ADK **para. 1.20", "ADK **para. 3.3", "3.4.11", "3.3.7", "CẦU THANG TRỆT", "SCDF **"]
for p in probes:
    print(("OK  " if p in t else "MISS"), p)

print("=== Table B3 mentions ===")
for m in re.findall(r"Table B3[^|]{0,60}", t):
    print("  ", m)
