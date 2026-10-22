import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()

SRC = {
    "QCVN": "_scan1022/safety/qcvn06_sd1.txt",
    "SCDF": "_scan1022/safety/scdf_ch2.txt",
    "ADB": "_scan1022/safety/adb1.txt",
    "ADK": "_scan1022/safety/adk.txt",
}
texts = {k: open(v, encoding="utf-8", errors="ignore").read() for k, v in SRC.items()}

DOCS = {
    "ADB": r"Approved Document B|ADB",
    "ADK": r"Approved Document K|ADK",
    "QCVN": r"QCVN 06",
    "SCDF": r"SCDF",
}

problems = []
for m in re.finditer(r"(?:ADB|ADK|QCVN 06:2022|SCDF)[^.\n]{0,40}?\*\*?(?:clause|para\.?)\s*\*?\*?\s*(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)", t):
    ctx = t[max(0, m.start() - 120):m.start()]
    num = m.group(1)
    doc = None
    for name, pat in DOCS.items():
        hits = re.findall(pat, ctx)
        if hits:
            doc = name
    if doc is None:
        doc = "ADB" if "Approved Document B" in ctx else ("ADK" if "Approved Document K" in ctx else None)
    if doc is None:
        problems.append(("NO-DOC", num, ctx[-90:].replace("\n", " ")))
        continue
    src = texts[doc]
    bare = num.split("(")[0]
    if not re.search(r"(?m)^\s*" + re.escape(bare) + r"\b", src):
        problems.append(("NOT-IN-SOURCE", doc, num, ctx[-70:].replace("\n", " ")))

print("problems:", len(problems))
for p in problems:
    print("  ", p)

print()
print("=== all clause-style citations with context ===")
seen = set()
for m in re.finditer(r"\*\*?(?:clause|para\.)\s*\*?\*\s*(\d+\.\d+(?:\.\d+)?(?:\([a-z]\))?)", t):
    ctx = t[max(0, m.start() - 150):m.start()].replace("\n", " ")
    doc = "?"
    for name, pat in DOCS.items():
        if re.search(pat, ctx):
            doc = name
    key = (doc, m.group(1))
    if key in seen:
        continue
    seen.add(key)
    print("  ", doc, m.group(1))
