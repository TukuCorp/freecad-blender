import io, re, ssl, sys, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "vi,en;q=0.8",
}

URLS = {
    "qcvn06_luatvietnam": "https://luatvietnam.vn/tim-van-ban/van-ban-bao-dam-va-xay-dung/"
    "463437-qcvn-06-2022-bxd-cn-ban-hanh-quy-chuan-phong-chay-chua-chay-cho-cong-trinh-xay-dung.html",
    "qcvn06_vbpl": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=157072",
    "qcvn03_luatvietnam": "https://luatvietnam.vn/tim-van-ban/van-ban-bao-dam-va-xay-dung/"
    "421378-qcvn-03-2019-bxd-quy-chuan-ve-an-toan-kien-truc-xay-dung.html",
    "qcvn11_tcvn": "https://luatvietnam.vn/tim-van-ban/van-ban-bao-dam-va-xay-dung/"
    "504480-tcvn-4451-2012-thiet-ke-cauthanh-cong-trinh-xay-dung.html",
    "tcvn9386": "https://luatvietnam.vn/tim-van-ban/van-ban-bao-dam-va-xay-dung/"
    "293047-tcvn-9386-2012-xay-dung-phan-tich-va-thiet-ke-khung-chay-chua-chay.html",
    "scdf": "https://www.scdf.gov.sg/home/community-volunteers/fire-safety-for-residential/fire-code-2013",
    "nfpa101": "https://www.nfpa.org/codes-and-standards/nfpa-101-standard-development/51",
    "ibc": "https://codes.iccsafe.org/content/IBC2021P2/chapter-10-means-of-egress",
}

for key, url in URLS.items():
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        raw = urllib.request.urlopen(req, context=ctx, timeout=60).read()
        html = raw.decode("utf-8", "ignore")
        with open("_scan1022/safety/" + key + ".html", "w", encoding="utf-8") as fh:
            fh.write(html)
        body = re.sub(r"<[^>]+>", " ", html)
        body = re.sub(r"\s+", " ", body).strip()
        print("OK " + key + " " + str(len(html)) + " " + body[:180])
    except Exception as exc:
        print("ERR " + key + " " + repr(exc)[:140])
