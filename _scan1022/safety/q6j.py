import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

TARGETS = [
    ("FIRE ALARM SYSTEM", "báo động cháy"),
    ("SPRINKLER", "hệ thống chụa cháy tự động"),
    ("FIRE LIFT", "thang máy chữa cháy"),
    ("GARAGE", "gara"),
    ("COMPARTMENT BETWEEN FLOORS", "ngăn cháy giữa các tầng"),
    ("LIFT HOISTWAY FIRE", "giếng thang máy"),
    ("BALCONY 1.2", "ban công"),
    ("ROOF TERRACE", "sân thượng"),
]

for label, needle in TARGETS:
    hits = [m.start() for m in re.finditer(re.escape(needle), t)]
    print("################ " + label + " : " + str(len(hits)))
    for i in hits[:2]:
        print("-----")
        print(t[max(0, i - 900):i + 900])
