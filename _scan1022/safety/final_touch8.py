import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part1.md"

with open(path, encoding="utf-8") as fh:
    t = fh.read()

m = re.search(r"\*\*Project:\*\* .*?\n", t, re.S)
print("before:", repr(m.group(0)[:240]))

good = (
    '**Project:** NHÀ Ở RIÊNG LẺ, 506 ĐƯỜNG HỒNG BÀNG, '
    'PHƯỜNG MINH PHỤNG, TP.HCM ("HỒ SƠ THIẾT KẾ THI CÔNG", '
    'hạng mục "XÂY DỰNG MỚI")\n'
)
t = t[:m.start()] + good + t[m.end():]

with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)

with open(path, encoding="utf-8") as fh:
    t2 = fh.read()
m2 = re.search(r"\*\*Project:\*\* .*?\n", t2, re.S)
print("after:", repr(m2.group(0)[:240]))
