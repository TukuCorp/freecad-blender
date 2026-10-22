import io, re, ssl, sys, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8",
    "Accept-Language": "vi,en;q=0.8",
}

FILES = {
    "qcvn06_2022.pdf": "https://datafiles.chinhphu.vn/cpp/files/vbpq/2022/12/06-bxd.pdf",
    "scdf_ch2.pdf": "https://www.scdf.gov.sg/docs/default-source/fire-safety-docs/downloads/"
    "fire-code-2013/chapter-2-%28prescriptive-provisions%29.pdf",
}

for name, url in FILES.items():
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        data = urllib.request.urlopen(req, context=ctx, timeout=120).read()
        with open("_scan1022/safety/" + name, "wb") as fh:
            fh.write(data)
        print("OK " + name + " " + str(len(data)))
    except Exception as exc:
        print("ERR " + name + " " + repr(exc)[:160])
