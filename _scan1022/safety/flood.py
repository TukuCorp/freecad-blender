import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

for key in ["hcmc_flood_dc", "hcmc_hdong_b"]:
    html = open("_scan1022/safety/" + key + ".html", encoding="utf-8", errors="ignore").read()
    print("############ " + key)
    for m in re.finditer(r'<li class="b_algo".*?</li>', html, re.S):
        block = m.group(0)
        cite = re.search(r"<cite[^>]*>(.*?)</cite>", block, re.S)
        h2 = re.search(r"<h2[^>]*>(.*?)</h2>", block, re.S)
        cap = re.search(r'<p[^>]*>(.*?)</p>', block, re.S)
        if not cite:
            continue
        url = re.sub(r"<[^>]+>", "", cite.group(1)).strip()
        title = re.sub(r"<[^>]+>", "", h2.group(1)).strip() if h2 else ""
        snippet = re.sub(r"<[^>]+>", "", cap.group(1)).strip() if cap else ""
        print("  * " + title[:90])
        print("    " + url[:130])
        print("    " + snippet[:260])
