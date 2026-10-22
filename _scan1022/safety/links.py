import io, re, sys, urllib.parse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

KEYS = ["qcvn06", "qcvn03", "tcvn4451", "tcvn9386", "scdf", "nfpa101", "ibc"]

for key in KEYS:
    path = "_scan1022/safety/search_%s_bing.html" % key
    try:
        html = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        continue
    print("== " + key)
    hits = re.findall(r'href="(https?://[^"]+)"[^>]*>(.{0,120}?)</a>', html, re.S)
    seen = set()
    for url, label in hits:
        label = re.sub(r"<[^>]+>", "", label)
        label = re.sub(r"\s+", " ", label).strip()
        if "bing.com" in url or "microsoft" in url:
            continue
        base = url.split("?")[0]
        if base in seen:
            continue
        seen.add(base)
        print("   " + label[:70] + " | " + base[:140])
