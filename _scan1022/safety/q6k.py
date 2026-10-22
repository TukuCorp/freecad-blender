import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

TARGETS = [
    ("BAO CHAY / CAM BAO", ["cảm báo", "báo cháy", "hệ thống báo", "còi báo"]),
    ("F1.3 GROUP", ["F1.3", "đơn nguyên"]),
    ("3.2.1", ["3.2.1 "]),
    ("ELEVATOR LOBBY", ["sảnh thang máy"]),
    ("3.4.6 lift", ["3.4.6"]),
]

for label, needles in TARGETS:
    for needle in needles:
        hits = [m.start() for m in re.finditer(re.escape(needle), t)]
        print("#### " + label + " [" + needle + "] " + str(len(hits)))
        for i in hits[:2]:
            print("  -----")
            print("  " + t[max(0, i - 700):i + 700].replace("\n", "\n  "))
