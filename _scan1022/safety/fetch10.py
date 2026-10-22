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
    ("ibc_upcodes", "https://upcodes.com/viewer/hochi_2_ibc_2024/chapter/10-means-of-egress"),
    ("ibc_codes2", "https://codes.iccsafe.org/content/IBC2021P1/chapter-10-means-of-egress"),
    ("nfpa101_link", "https://link.nfpa.org/publications/101/1012024"),
    ("nfpa_fact", "https://www.nfpa.org/education-and-research/research/nfpa-research/fire-statistics"),
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
        print("ERR " + key + " " + repr(exc)[:130])
