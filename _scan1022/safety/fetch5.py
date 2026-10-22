import io, re, ssl, sys, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8",
    "Accept-Language": "en;q=0.9",
}

TARGETS = [
    ("nfpa101_free", "https://link.nfpa.org/free-access/publications/101/1012024"),
    ("ibc_upcodes10", "https://upcodes.com/viewer/hochi_2_ibc_2024/chapter/10-means-of-egress"),
    ("hcmc_flood", "https://hcmcportal.vn/"),
    ("hcmc_lloc", "https://www.google.com/search?q=site%3Ahcmcportal.vn+ngap+l%C5%BB1t"),
    ("qcvn07_2025", "https://luatvietnam.vn/tim-van-ban/van-ban-bao-dam-va-xay-dung/"
    "608450-qcvn-07-2025-bxd-quy-chuan-phan-tich-va-thiet-ke-khung-chay-chua-chay.html"),
    ("tcvn2737", "https://luatvietnam.vn/tim-van-ban/van-ban-bao-dam-va-xay-dung/"
    "502953-tcvn-2737-2023-thiet-ke-cauthanh-cong-trinh-xay-dung.html"),
]

for key, url in TARGETS:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        raw = urllib.request.urlopen(req, context=ctx, timeout=60).read()
        ctype = raw[:4]
        name = key + (".pdf" if ctype == b"%PDF" else ".html")
        with open("_scan1022/safety/" + name, "wb") as fh:
            fh.write(raw)
        print("OK " + name + " " + str(len(raw)) + " " + repr(raw[:4]))
    except Exception as exc:
        print("ERR " + key + " " + repr(exc)[:150])
