import io, ssl, sys, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/pdf,text/html,*/*;q=0.8",
    "Accept-Language": "vi,en;q=0.8",
}

FILES = {
    "qcvn06_sd1_2023.pdf": "https://tasfahn.com/wp-content/uploads/2024/12/"
    "QCVN06-2022-SUA-DOI-01-2023.pdf",
    "qcvn06_moc.pdf": "https://moc.gov.vn/Images/editor/files/Tailieu/Tai%20lieu%20Hoi%20thao%20"
    "Sua%20doi%201_2023%20QCVN%2006-2022_22_4_2024.pdf",
    "qcvn06_moc2.pdf": "https://xaydung.gov.vn/Images/editor/files/Quy%20Chu%E1%BA%A9n/QCVN%2006-2022.pdf",
}

for name, url in FILES.items():
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        data = urllib.request.urlopen(req, context=ctx, timeout=180).read()
        with open("_scan1022/safety/" + name, "wb") as fh:
            fh.write(data)
        print("OK " + name + " " + str(len(data)))
    except Exception as exc:
        print("ERR " + name + " " + repr(exc)[:160])
