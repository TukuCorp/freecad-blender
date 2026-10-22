import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()

sec = t.split("## 12. Questions for the contractor")[1].split("## 13.")[0]
nums = re.findall(r"^(\d+)\. ", sec, re.M)
print("questions:", len(nums), "->", ",".join(nums))
print("contiguous:", nums == [str(i) for i in range(1, len(nums) + 1)])

print("--- quoted Vietnamese strings present ---")
for q in [
    "Xem chi tiết cầu thang",
    "CHỖ NÀO CÓ TƯỜNG MÀ KHÔNG CÓ BỐ TRÍ DẦM THÌ TA ĐẶT THÊM 2Ø16 HOẶC 3Ø16 TẠI VỊ TRÍ ĐÓ",
    "MB ĐÀ KIỀNG",
    "MÓNG CỘT, ĐÀ KIỀNG VÀ TƯỜNG LÀM MỚI",
    "Ô kỹ thuật thang máy",
    "TẦNG CẦU THANG TRỆT",
    "ĐƯỜNG HỒNG BÀNG",
    "chống trượt",
    "máu sáng",
    "gồn kính cường lực, có khung inox bảo vệ",
    "Vị trí do đơn vị cung cấp Thang máy chỉ định",
    "Móc treo 1Ø25",
    "KHI THI CÔNG NẾU SỨC CHỊU TẢI CỦA CỌC KHÔNG ĐÚNG PHẢI BÁO THIẾT KẾ ĐỂ CÓ BIỆN PHÁP XỬ LÝ",
    "lan can kính cường lực dày 8 ly, gọn tay vịn inox",
    "PHẦN GHI CHÚ",
]:
    print(("OK  " if q in t else "MISS"), q[:70])

print("--- longest lines (sample) ---")
for ln in sorted(t.splitlines(), key=len, reverse=True)[:3]:
    print(len(ln), repr(ln[:120]))

print("--- code refs quoted ---")
for c in ["ADB **para. 2.5", "ADB **para. 2.6", "ADB **para. 5.6", "ADB **para. 5.7",
          "ADB **para. 1.1", "ADB **para. 2.10", "ADB **para. 2.13", "ADB **para. 2.14",
          "ADB **para. 3.39", "ADB **para. 3.107", "ADB **para. 3.38",
          "ADK (2013) **para. 1.11", "ADK (2013) **para. 1.39", "ADK (2013) **para. 1.34",
          "ADK (2013) **para. 1.20", "ADK (2013) **para. 3.3",
          "SCDF clause **2.2.13", "SCDF **para", "SCDF clause **2.4.5",
          "clause **3.2.13", "clause **3.4.4", "clause **3.4.7", "clause **3.4.3",
          "clause **3.2.6.1(c)", "clause **3.4.13", "clause **3.4.8", "clause **3.4.11",
          "clause **3.4.6", "clause **3.3.7", "clause **3.3.4", "clause **4.33.1",
          "Table G.1", "Table 4", "Table 1.1", "Table 2.2A"]:
    print(("OK  " if c in t else "MISS"), c)

print("--- forbidden invented numbers check ---")
print("NFPA 101 clause refs:", re.findall(r"NFPA 101[^.]{0,40}\d+\.\d+", t))
print("IBC section refs:", re.findall(r"IBC 2021[^.]{0,30}\d{4}\.\d+", t))
print("QCVN 03 clause refs:", re.findall(r"QCVN 03[^.]{0,30}\d+\.\d+\.\d+", t))
print("TCVN clause refs:", re.findall(r"TCVN \d+[^.]{0,40}\d+\.\d+\.\d+", t))
print("any NFPA/IBC clause numbers at all:", re.findall(r"(NFPA|IBC)\s*\d+\.\d+", t))
