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
    ("qcvn03_tasfahn", "https://tasfahn.com/wp-content/uploads/2024/12/QCVN-03-2019-BXD.pdf"),
    ("qcvn03_tasfahn2", "https://tasfahn.com/wp-content/uploads/2024/12/QCVN03-2019-BXD-01-2025.pdf"),
    ("tcvn2737_tasfahn", "https://tasfahn.com/wp-content/uploads/2024/12/TCVN-2737-2023.pdf"),
    ("tcvn4451_tasfahn", "https://tasfahn.com/wp-content/uploads/2024/12/TCVN-4451-2012.pdf"),
    ("qcvn03_xaydung", "https://xaydung.gov.vn/vn/tin-tuc/"),
]

for key, url in TARGETS:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        raw = urllib.request.urlopen(req, context=ctx, timeout=120).read()
        name = key + (".pdf" if raw[:4] == b"%PDF" else ".html")
        with open("_scan1022/safety/" + name, "wb") as fh:
            fh.write(raw)
        print("OK " + name + " " + str(len(raw)))
    except Exception as exc:
        print("ERR " + key + " " + repr(exc)[:130])
