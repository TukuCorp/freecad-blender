import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "contractor/scan-2026-10-22/review/out-safety.md"
raw = open(path, "rb").read()
print("bytes", len(raw))
print("has BOM", raw[:3] == b"\xef\xbb\xbf")
print("CRLF count", raw.count(b"\r\n"))

t = raw.decode("utf-8")
print("decoded utf-8 OK, chars", len(t))

for probe in [
    "lan can kính cường lực dày 8 ly",
    "ĐƯỜNG HỒNG BÀNG",
    "XEM CHI TIẾT CẦU THANG",
    "TẤT CẢ CÁC SÀN DÀY 100 (mm)",
    "Chỗ nào có tường",
    "HỒNG BÀNG",
    "kính cường lực",
    "ĐÀ GIẰNG",
    "Ô lấy sáng",
    "bậc chịu lửa",
]:
    print(("OK  " if probe in t else "MISS"), probe[:56])

print("--- hygiene ---")
print("raw html tags:", len(re.findall(r"<html|<body|<div|<script", t, re.I)))
print("phone numbers:", re.findall(r"(?:\+?84|0)\d{9,10}", t))
print("emails:", re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", t))
print("dollar signs:", t.count("$"))
print("lines over 400 chars:", sum(1 for ln in t.splitlines() if len(ln) > 400))

print("--- required sections ---")
need = [
    "Method and evidence limits",
    "Top 10 actions before pouring concrete",
    "Questions for the contractor",
    "What the sources agree on",
    "Where the sources conflict",
    "Sources",
]
for n in need:
    print(("OK  " if n in t else "MISS"), n)

print("--- field completeness per finding ---")
blocks = re.split(r"\n### S-\d+", t)[1:]
fields = ["**ID:**", "**Severity:**", "**Where:**", "**Issue:**", "**Why it matters:**",
          "**Basis:**", "**Basis class:**", "**Fix:**", "**Who decides:**", "**Evidence label:**"]
bad = []
for i, b in enumerate(blocks, 1):
    missing = [f for f in fields if f not in b]
    if missing:
        bad.append((i, missing))
print("blocks", len(blocks), "incomplete:", bad if bad else "none")

print("--- severity vocabulary ---")
print(sorted(set(re.findall(r"\*\*Severity:\*\* ([A-Z]+)", t))))
print("--- basis class vocabulary ---")
print(sorted(set(re.findall(r"\*\*Basis class:\*\* ([A-Z\-]+)", t))))
print("--- top10 table rows ---")
for m in re.finditer(r"^\| (\d+) \| (.{0,90})", t, re.M):
    print("  ", m.group(1), m.group(2))
print("--- numbered contractor questions ---")
q = re.findall(r"^(\d+)\. \*\*", t, re.M)
print(len(q), "questions")
