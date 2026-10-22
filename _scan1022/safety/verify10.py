import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

arch = open("contractor/scan-2026-10-22/transcript-architecture.md", encoding="utf-8").read()
fid = open("designs/contractor-as-drawn.fidelity.md", encoding="utf-8").read()
t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()

print("=== fidelity.md THANG MÁY sentence ===")
for m in re.finditer(r"[^.]*THANG MÁY[^.]*\.", fid):
    print("  ", m.group(0).strip()[:230])

print()
print("=== transcript PHẦN GHI CHÚ sentence ===")
for m in re.finditer(r"[^.]*PHẦN GHI CHÚ[^.]*\.", arch):
    print("  ", m.group(0).strip()[:260])

print()
print("=== report usage of those two ===")
for m in re.finditer(r".{0,120}PHẦN GHI CHÚ.{0,160}", t):
    print("  ", m.group(0).replace("\n", " "))
print()
for m in re.finditer(r".{0,140}THANG MÁY.{0,140}", t):
    print("  ", m.group(0).replace("\n", " "))
print()
print("=== PHUONG AN usage ===")
for m in re.finditer(r".{0,100}PHƯƠNG ÁN AN TOÀN CHÁY.{0,100}", t):
    print("  ", m.group(0).replace("\n", " "))
