import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()

PROBES = [
    "Xem chi tiết cầu thang",
    "Chỗ nào có tường",
    "MB Đà giằng",
    "Ô kỹ thuật thang máy",
    "Sàn tầng lửng",
    "Ban công",
    "Lô gia",
    "Phòng ngủ",
    "Phòng thờ",
    "Ô lấy sáng",
    "Nơi để xe",
    "Sân trước",
    "Sân sau",
    "HỒ SƠ THIẾT KẾ THI CÔNG",
    "XÂY DỰNG MỚI",
    "Phường Minh Phụng",
]

print("=== Vietnamese quote check (case-insensitive) ===")
for p in PROBES:
    print(("OK  " if p.lower() in t.lower() else "MISS"), p)

texts = {
    "ADB": open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read(),
    "ADK": open("_scan1022/safety/adk.txt", encoding="utf-8", errors="ignore").read(),
    "QCVN06": open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read(),
    "SCDF": open("_scan1022/safety/scdf_ch2.txt", encoding="utf-8", errors="ignore").read(),
}
nums = set(re.findall(r"\*\*(?:clause|para\.)\s*(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)\*\*", t))
nums |= set(re.findall(r"(?<![\w.])clause\s+(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)", t))
nums |= set(re.findall(r"(?<![\w.])para\.\s+(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)", t))
bad = []
for n in sorted(nums):
    bare = n.split("(")[0]
    if not any(re.search(r"(?m)^\s*" + re.escape(bare) + r"\b", src) for src in texts.values()):
        bad.append(n)
print()
print("distinct clause numbers:", len(nums), "| not found in any source:", bad if bad else "none")

print()
print("=== invented clause numbers for unretrieved codes ===")
print("NFPA:", re.findall(r"NFPA[^.\n]{0,30}\b\d+\.\d+(?:\.\d+)?", t))
print("IBC:", re.findall(r"\bIBC[^.\n]{0,30}\b\d{4}\.\d+(?:\.\d+)?", t))
print("QCVN03:", re.findall(r"QCVN 03[^.\n]{0,30}\b\d+\.\d+\.\d+", t))
print("QCVN07:", re.findall(r"QCVN 07[^.\n]{0,30}\b\d+\.\d+\.\d+", t))
print("TCVN:", re.findall(r"TCVN \d+[^.\n]{0,40}\b\d+\.\d+\.\d+", t))

print()
print("=== overstatement scan ===")
for m in re.finditer(r"[^.\n]{0,90}\b(?:is|are|was|were)\s+(?:structurally\s+)?(?:adequate|compliant|safe)\b[^.\n]{0,60}", t, re.I):
    print("  ", m.group(0).strip()[:170])

print()
print("=== counts ===")
print("words:", len(t.split()))
print("findings:", len(re.findall(r"^- \*\*ID:\*\*", t, re.M)))
print("questions:", len(re.findall(r"^\d+\. \*\*", t.split("## 12.")[1].split("## 13.")[0], re.M)))
print("top10 rows:", len(re.findall(r"^\| \d+ \|", t, re.M)))
print("sources rows:", len(re.findall(r"^\| \d+ \| ", t, re.M)))
print("agree-on bullets:", len(re.findall(r"^\d+\. \*\*", t.split("## 13.")[1].split("## 14.")[0], re.M)))
