import io, json, re, ssl, sys, urllib.parse, urllib.request

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


def get(url, timeout=45):
    req = urllib.request.Request(url, headers=HEADERS)
    return urllib.request.urlopen(req, context=ctx, timeout=timeout).read().decode("utf-8", "ignore")


def strip(html):
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    return re.sub(r"\s+", " ", body).strip()


QUERIES = [
    ("qcvn06", "QCVN 06:2022 BXD quy chuan phong chay chua chay toan van ban"),
    ("qcvn03", "QCVN 03:2019 BXD quy chuan an toan kien truc xay dung"),
    ("tcvn4451", "TCVN 4451:2012 thiet ke cau thang"),
    ("tcvn9386", "TCVN 9386:2012 phan tich va thiet ke khung chay chua chay"),
    ("scdf", "SCDF Fire Code 2013 shophouse escape staircase width travel distance"),
    ("nfpa101", "NFPA 101 residential one or two family dwelling means of escape travel distance"),
    ("ibc", "IBC 2021 1007 egress width stairs residential 1029 travel distance"),
]

for key, q in QUERIES:
    for engine, tmpl in (
        ("bing", "https://www.bing.com/search?q={q}&count=15"),
        ("mojeek", "https://www.mojeek.com/search?q={q}"),
    ):
        url = tmpl.format(q=urllib.parse.quote(q))
        try:
            html = get(url)
            with open("_scan1022/safety/search_%s_%s.html" % (key, engine), "w", encoding="utf-8") as fh:
                fh.write(html)
            links = re.findall(r'href="(https?://[^"]+)"', html)
            out = [l for l in links if not re.search(r"bing\.com|microsoft|mojeek|google|w3\.org|schema", l)]
            print("== %s %s len=%d" % (key, engine, len(html)))
            for l in out[:14]:
                print("   " + l[:160])
            if out:
                break
        except Exception as exc:
            print("ERR %s %s %r" % (key, engine, exc)[:120])
