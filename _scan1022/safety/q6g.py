import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("_scan1022/safety/qcvn06_sd1.txt", encoding="utf-8", errors="ignore").read()

i = t.find("Bảng G.1 – Khoảng cách giới hạn cho phép từ cửa ra vào của căn hộ hay của phòng ở")
print(t[i - 400:i + 4500])
