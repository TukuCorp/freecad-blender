import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

t = open("contractor/scan-2026-10-22/review/out-safety.md", encoding="utf-8").read()

PROBES = [
    "MB ĐÀ GIẰNG",
    "P. NGỮ",
    "P. THỜ",
    "P. KHÁCH",
    "P. ĂN + BẾP",
    "P. SINH HOẠT",
    "Cầu thang bộ loại 3",
    "Cầu thang bộ loại 2",
    "HỒ SƠ THIẾT KẾ THI CÔNG",
    "ĐƯỜNG HỒNG BÀNG",
    "PHƯỜNG MINH PHỤNG",
    "XÂY DỰNG MỚI",
    "MẶT ĐỨNG CHÍNH",
    "MẶT CẮT A - A",
    "Ô KỸ THUẬT THANG MÁY",
    "Lan can kính cường lực dày 8 ly, gọn tay vịn inox",
    "TẤT CẢ CÁC SÀN DÀY 100 (mm)",
    "CHỖ NÀO CÓ TƯỜNG MÀ KHÔNG CÓ BỐ TRÍ DẦM THÌ TA ĐẶT THÊM 2Ø16 HOẶC 3Ø16 TẠI VỊ TRÍ ĐÓ",
    "MÓNG CỘT, ĐÀ KIỀNG VÀ TƯỜNG LÀM MỚI",
    "Xem chi tiết cầu thang",
    "Ô lấy sáng",
    "Nơi để xe",
    "Sân trước",
    "Sân sau",
    "Ban công",
    "Lô gia",
    "chống trượt",
    "vá trí phễu thu nước",
    "Vị trí do đơn vị cung cấp Thang máy chỉ định",
    "Móc treo 1Ø25",
    "KHI THI CÔNG NẾU SỨC CHỊU TẢI CỦA CỌC KHÔNG ĐÚNG PHẢI BÁO THIẾT KẾ ĐỂ CÓ BIỆN PHÁP XỬ LÝ",
    "ĐẦU CỌC CÓ HÀN MIẾNG THÉP BẢO VỆ",
    "PHẦN GHI CHÚ",
    "bậc chịu lửa",
    "cửa nắp hút khói",
]

missing = []
for p in PROBES:
    ok = p.lower() in t.lower()
    if not ok:
        missing.append(p)
    print(("OK  " if ok else "MISS"), p)

print()
print("missing count:", len(missing))
