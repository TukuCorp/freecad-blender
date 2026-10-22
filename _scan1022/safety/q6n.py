import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()


def show(label, pattern, span=2200, limit=1, before=0):
    print("################ " + label)
    n = 0
    for m in re.finditer(pattern, t):
        i = m.start()
        print("-----")
        print(t[max(0, i - before):i + span])
        n += 1
        if n >= limit:
            break
    if n == 0:
        print("(not found)")


show("STAIR TYPES 1/2/3 DEFS", r"C\u1ea7u thang b\u1ed9 lo\u1ea1i 1\s*:", 1000, 1, 900)
show("BUONG THANG BO LOAI N1", r"Bu\u1ed3ng thang b\u1ed9 lo\u1ea1i N1\s*:", 900, 1, 700)
show("APPENDIX D BODY", r"PH\u1ee4 L\u1ee4C D \(quy \u0111\u1ecbnh\) B\u1ea2O V\u1ec6 CH\u1ed8NG KH\u00d3I\s*\n", 3000, 1)
show("F1.3 requires stairwell", r"nh\u00e0 nh\u00f3m F1\.3[^\n]{0,300}c\u1ea7u thang", 700, 3)
