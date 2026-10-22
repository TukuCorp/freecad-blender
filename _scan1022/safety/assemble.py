import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

parts = [
    "_scan1022/safety/part1.md",
    "_scan1022/safety/part2.md",
    "_scan1022/safety/part3.md",
    "_scan1022/safety/part4.md",
]

chunks = []
for p in parts:
    with open(p, encoding="utf-8") as fh:
        chunks.append(fh.read())

text = "\n".join(chunks)
text = re.sub(r"\n{4,}", "\n\n\n", text)

out = "contractor/scan-2026-10-22/review/out-safety.md"
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(text)

ids = re.findall(r"^- \*\*ID:\*\* (S-\d+)$", text, re.M)
inline = sorted(set(re.findall(r"\bS-(\d+)\b", text)))

print("chars", len(text))
print("declared finding blocks:", len(ids))
print("ids:", ", ".join(ids))

nums = sorted({int(i.split("-")[1]) for i in ids})
missing = [n for n in range(1, max(nums) + 1) if n not in nums]
print("max", max(nums), "missing", missing)

allref = sorted({int(i) for i in inline})
ghost = [n for n in allref if n not in nums]
print("referenced but not declared:", ghost)

for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
    print(sev, text.count("- **Severity:** " + sev))

for cls in ["LOCAL-MINIMUM", "BEYOND-LOCAL", "JUDGEMENT"]:
    print(cls, text.count("**Basis class:** " + cls))

for lab in ["VERIFIED", "PARTIAL", "CLAIMED", "NOT FOUND", "UNVERIFIED"]:
    print("label", lab, text.count("Evidence label:** " + lab))

print("--- headings ---")
for m in re.finditer(r"^#{1,3} .*$", text, re.M):
    print(m.group(0)[:110])
