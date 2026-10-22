import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()

blocks = re.split(r"\n### S-(\d+)", t)
titles = {}
for i in range(1, len(blocks), 2):
    num = int(blocks[i])
    body = blocks[i + 1]
    m = re.search(r"\*\*Issue:\*\*\s*(.{0,110})", body, re.S)
    titles[num] = re.sub(r"\s+", " ", m.group(1)) if m else ""

for i in range(1, len(blocks), 2):
    num = int(blocks[i])
    body = blocks[i + 1]
    for m in re.finditer(r"(?:see |in |at |blocks |covered (?:in|at) |full treatment at |fix at |see also |from )\(?(S-\d+)\)?", body, re.I):
        tgt = int(m.group(1).split("-")[1])
        ctx = re.sub(r"\s+", " ", body[max(0, m.start() - 60):m.end() + 20])
        print("S-%02d -> S-%02d | %s" % (num, tgt, ctx[:110]))
        print("        target: " + titles.get(tgt, "?")[:100])
    print()
