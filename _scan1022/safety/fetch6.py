import io, ssl, sys, urllib.request

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
    ("ibc2021_ch10", "https://codes.iccsafe.org/content/IBC2021P2/chapter-10-means-of-egress"),
    ("nfpa101_2021", "https://www.nfpa.org/codes-and-standards/nfpa-101-standard-development/51"),
    ("nfpa101_pdf", "https://docinfofiles.nfpa.org/files/AboutTheCodes/101/101_A2023_NFPA_101_SD_P1.pdf"),
    ("hcmc_floodpdf", "https://hcmcportal.vn/wp-content/uploads/2023/"),
    ("hcmc_quiz", "https://www.google.com/search?q=%22H%E1%BB%A3i+Ch%C3%AD+Minh+Th%C3%A0nh%22+ngap+l%E1%BB%BB1t+tr%C3%ADch+t%E1%BB%A1i+%C4%91%E1%BB%99+th%E1%BB%A5p+2024"),
]

for key, url in TARGETS:
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        raw = urllib.request.urlopen(req, context=ctx, timeout=90).read()
        ctype = raw[:4]
        name = key + (".pdf" if ctype == b"%PDF" else ".html")
        with open("_scan1022/safety/" + name, "wb") as fh:
            fh.write(raw)
        print("OK " + name + " " + str(len(raw)))
    except Exception as exc:
        print("ERR " + key + " " + repr(exc)[:150])
