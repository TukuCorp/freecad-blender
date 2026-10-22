import io, re, sys, html as htmlmod

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

KEYS = ["qcvn06", "qcvn03", "tcvn4451", "tcvn9386", "scdf", "nfpa101", "ibc"]

for key in KEYS:
    path = "_scan1022/safety/search_%s_bing.html" % key
    try:
        doc = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        continue
    print("== " + key)
    for m in re.finditer(r'<li class="b_algo".*?</li>', doc, re.S):
        block = m.group(0)
        cite = re.search(r'<cite[^>]*>(.*?)</cite>', block, re.S)
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', block, re.S)
        if not cite:
            continue
        url = re.sub(r"<[^>]+>", "", cite.group(1)).strip()
        title = re.sub(r"<[^>]+>", "", h2.group(1)).strip() if h2 else ""
        print("   " + htmlmod.unescape(title)[:80] + " | " + htmlmod.unescape(url)[:140])
