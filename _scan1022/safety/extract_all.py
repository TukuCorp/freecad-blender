import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def grab(t, label, needle, span=1500, before=0, limit=1, raw=False):
    print("################ " + label)
    pat = re.escape(needle) if raw else needle
    n = 0
    for m in re.finditer(pat, t):
        i = m.start()
        print("-----")
        print(t[max(0, i - before):i + span])
        n += 1
        if n >= limit:
            break
    if n == 0:
        print("(not found)")


vn = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()
adb = open("_scan1022/safety/adb1.txt", encoding="utf-8", errors="ignore").read()
adk = open("_scan1022/safety/adk.txt", encoding="utf-8", errors="ignore").read()

grab(vn, "VN 2.2.13 smoke-free approach", r"2\.2\.13\s", 1500, 0, 2)
grab(vn, "VN stair type 2 def", "Cầu thang bộ loại 2\s*:", 700, 800, 1, raw=True)
grab(vn, "VN 3.4.8 stair lighting", r"3\.4\.8\s+Các buồng thang bộ", 1200, 0, 1)
grab(vn, "VN headroom stair", r"chiều cao thông thuầy[^\n]{0,120}thang", 900, 300, 2)
grab(vn, "VN balcony parapet height", r"ban công[^\n]{0,200}1,1 m", 700, 300, 3)
grab(vn, "VN ban cong lan can 1,2", r"lan can[^\n]{0,120}1,2 m", 600, 400, 3)
grab(adb, "ADB common stairs width", r"3\.60\s", 1600, 0, 1)
grab(adb, "ADB common stairs 3.61-3.65", r"3\.6[1-5]\s", 1400, 0, 5)
grab(adk, "ADK 1.6 headroom dwelling", r"1\.13\s", 1200, 0, 1)
grab(adk, "ADK 1.24 door across landing", r"1\.2[3-6]\s", 1200, 0, 4)
