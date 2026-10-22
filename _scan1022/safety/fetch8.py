import io, ssl, sys, urllib.request

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
    ("qcvn03_lamdao", "https://lamdao.vn/qcvn-03-2019-bxd-quy-chuan-ve-an-toan-kien-truc-xay-dung-263573d.html"),
    ("qcvn03_mocgov", "https://xaydung.gov.vn/Images/editor/files/QuyChuan/QCVN%2003-2019.pdf"),
    ("qcvn03_luatvn", "https://luatvietnam.vn/tim-van-ban/van-ban-bao-dam-va-xay-dung/"
    "421378-qcvn-03-2019-bxd-quy-chuan-ve-an-toan-kien-truc-xay-dung.html"),
    ("luatvn_home", "https://luatvietnam.vn"),
    ("chinhphu_qcvn", "https://vanban.chinhphu.vn/?pageid=27160&docid=207687"),
]

for key, url in TARGETS:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        raw = urllib.request.urlopen(req, context=ctx, timeout=90).read()
        name = key + (".pdf" if raw[:4] == b"%PDF" else ".html")
        with open("_scan1022/safety/" + name, "wb") as fh:
            fh.write(raw)
        print("OK " + name + " " + str(len(raw)))
    except Exception as exc:
        print("ERR " + key + " " + repr(exc)[:140])
