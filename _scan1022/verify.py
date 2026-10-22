import sys,re,io
sys.stdout.reconfigure(encoding="utf-8")
p="contractor/scan-2026-10-22/review/out-design.md"
s=open(p,encoding="utf-8").read()
print("chars",len(s),"lines",s.count(chr(10))+1)
print("stray @@ count:", s.count("@@"))
ids=re.findall(r"^\*\*ID\*\* (D-\d+)", s, re.M)
print("finding blocks:",len(ids))
print(ids)
types=re.findall(r"\*\*Type\*\* (ERROR|INCONSISTENCY|RISK|IMPROVEMENT)", s)
from collections import Counter
print(Counter(types))
# unicode sanity: ensure no mojibake markers
for bad in ["Ã","â€","�"]:
    if bad in s: print("MOJIBAKE", bad, s.count(bad))
print("has vietnamese ok:", "P. Khách" in s, "Ô lấy sáng" in s)
