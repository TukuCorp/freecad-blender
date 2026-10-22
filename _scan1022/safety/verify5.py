import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()

SRC = {
    "ADB": "_scan1022/safety/adb1.txt",
    "ADK": "_scan1022/safety/adk.txt",
    "QCVN06": "_scan1022/safety/qcvn06_sd1.txt",
    "SCDF": "_scan1022/safety/scdf_ch2.txt",
}
texts = {k: open(v, encoding="utf-8", errors="ignore").read() for k, v in SRC.items()}

NUMS = re.findall(r"\*\*(?:clause|para\.)\s*(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)\*\*", t)
NUMS += re.findall(r"(?<![\w.])clause\s+(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)", t)
NUMS += re.findall(r"(?<![\w.])para\.\s+(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)", t)

uniq = sorted(set(NUMS))
print("distinct clause numbers cited:", len(uniq))
bad = []
for n in uniq:
    bare = n.split("(")[0]
    where = [k for k, src in texts.items()
             if re.search(r"(?m)^\s*" + re.escape(bare) + r"\b", src)]
    if not where:
        bad.append((n, "NOT FOUND IN ANY SOURCE"))
    else:
        print("  OK ", n, "->", ",".join(where))
print()
print("PROBLEMS:", bad if bad else "none")

print()
print("=== cross-reference sanity ===")
blocks = re.split(r"\n### S-(\d+)", t)
defined = {int(blocks[i]) for i in range(1, len(blocks), 2)}
titles = {}
for i in range(1, len(blocks), 2):
    num = int(blocks[i])
    body = blocks[i + 1]
    m = re.search(r"\*\*Issue:\*\* (.{0,80})", body, re.S)
    titles[num] = (m.group(1).replace("\n", " ") if m else "")[:70]

for i in range(1, len(blocks), 2):
    num = int(blocks[i])
    body = blocks[i + 1]
    for ref in set(re.findall(r"\(S-(\d+)\)", body)):
        r = int(ref)
        if r not in defined:
            print("  MISSING TARGET S-" + ref, "cited in S-%02d" % num)

print()
print("=== cross-ref topic plausibility (spot check) ===")
for num in sorted(titles):
    print("  S-%02d" % num, titles[num])
