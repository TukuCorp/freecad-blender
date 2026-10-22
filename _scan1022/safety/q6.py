import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

TERMS = [
    "cầu thang chữa cháy",
    "Cầu thang chữa cháy",
    "cao độ chuyển tầng",
    "khoảng cách",
    "lối thoát hiểm",
    "bậc chắp",
    "lan can",
    "mặt kính",
    "báo động",
    "cảm báo",
    "tường chắn",
    "sân thượng",
    "mái",
]

for term in TERMS:
    hits = [m.start() for m in re.finditer(re.escape(term), t)]
    print("== %s : %d" % (term, len(hits)))
