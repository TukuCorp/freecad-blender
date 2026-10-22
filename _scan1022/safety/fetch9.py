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
    ("qcvn03_a", "https://datafiles.chinhphu.vn/cpp/files/vbpq/2019/12/28-qcvn-03-2019-bxd-1.pdf"),
    ("qcvn03_b", "https://datafiles.chinhphu.vn/cpp/files/vbpq/2019/12/qcvn-03-2019-bxd.pdf"),
    ("qcvn07_a", "https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/06/44-qcvn-07-2025-bxd.pdf"),
    ("qcvn07_b", "https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/06/qcvn-07-2025-bxd.pdf"),
    ("qcvn32_a", "https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/12/qcvn-32-2024-bxd.pdf"),
    ("tcvn2737_a", "https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/12/tcvn-2737-2023.pdf"),
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
        print("ERR " + key + " " + repr(exc)[:120])
