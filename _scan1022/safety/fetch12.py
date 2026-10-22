import io, re, ssl, sys, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8",
    "Accept-Language": "vi,en;q=0.9",
}

TARGETS = [
    ("hcmc_flood_dc", "https://www.bing.com/search?q=ngap+l%E1%BB%81t+TP.HCM+2024+tr%C3%ADch+t%E1%BB%A1i+%C4%91%E1%BB%99+th%E1%BB%A5p+tr%C3%AAng+b%E1%BB%81t"),
    ("hcmc_hdong_b", "https://www.bing.com/search?q=Ho%CC%80ng+ngap+l%E1%BB%BB1t+TP.HCM+2024+tr%C3%ADch+t%E1%BB%A1i+thu%E1%BB%99+n%E1%BB%AFi+%C4%91%E1%BB%99+th%E1%BB%A5p+tr%C3%AAng+b%E1%BB%81t"),
    ("scdf_ref", "https://www.scdf.gov.sg/home/community-volunteers/fire-safety-for-residential/fire-code-2013"),
    ("moj_qcvn06", "https://thuvienphapluat.vn/van-ban/Xay-dung/499237-qcvn-06-2022-bxd-quy-chuan-ky-thuat-quoc-gia-ve-an-toan-chay-cho-nha-va-cong-trinh-2022"),
]

for key, url in TARGETS:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        raw = urllib.request.urlopen(req, context=ctx, timeout=60).read()
        with open("_scan1022/safety/" + key + ".html", "wb") as fh:
            fh.write(raw)
        print("OK " + key + " " + str(len(raw)))
    except Exception as exc:
        print("ERR " + key + " " + repr(exc)[:130])
