import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()
src = ""
for p in ["contractor/scan-2026-10-22/transcript-architecture.md",
          "contractor/scan-2026-10-22/transcript-foundation-stairs.md",
          "contractor/scan-2026-10-22/transcript-beams-slabs.md",
          "designs/contractor-as-drawn.fidelity.md",
          "designs/contractor-as-drawn.measurements.md"]:
    src += open(p, encoding="utf-8").read()

print("=== quoted sheet names / drawing titles used in the report ===")
names = set()
for m in re.finditer(r'"([^"]{4,70})"', t):
    s = m.group(1)
    if re.search(r"[A-ZĐÁÀẢÃẠĂẰẮẲẴẶÂẤẦẨẪẬ]{3,}", s) and re.search(r"[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠƯ]{2,}", s):
        names.add(s)

bad = []
for n in sorted(names):
    inrep = n in t
    insrc = n.lower() in src.lower()
    if inrep and not insrc:
        bad.append(n)
        print("  NOT-IN-TRANSCRIPT:", repr(n))
    else:
        print("  OK  ", repr(n))

print()
print("quoted strings not found verbatim in any transcript:", len(bad))
for b in bad:
    print("   ", repr(b))
