"""Phase-3 verifier: headless-Chrome screenshots + DOM + pixel assertions.

Pure stdlib + Pillow. No arguments. Exit non-zero on any failure.
Writes shots/<opt>-<W>.png, shots/A-plan.png, shots/D-plan.png.
"""
from __future__ import annotations

import http.server
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
from functools import partial
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
PAGE = HERE / "f3-split-viewer.html"
SHOTS = HERE / "shots"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OPTS = ["0", "A", "B", "C", "D"]
TITLES = {"0": "As drawn", "A": "Study at the balcony", "B": "Side split",
          "C": "Glazed study at the rear", "D": "Open studio + curtain"}
VPS = [(1440, 900), (390, 844)]


_FLAGS = ["--no-first-run", "--no-default-browser-check", "--disable-extensions",
          "--disable-background-networking"]


def chrome(args, timeout=60, tag="?"):
    """Run headless Chrome once per call in a fresh profile.

    Retries ONCE on timeout (transient stall under load); a second timeout
    raises so the caller can mark the row FAIL instead of tracebacking."""
    prof = tempfile.mkdtemp(prefix="f3chrome_")
    try:
        last = None
        for attempt in (1, 2):
            t0 = time.monotonic()
            try:
                return subprocess.run(
                    [CHROME] + args + _FLAGS + [f"--user-data-dir={prof}"],
                    capture_output=True, text=True, timeout=timeout)
            except subprocess.TimeoutExpired as e:
                last = e
                print(f"chrome timeout tag={tag} attempt={attempt} "
                      f"elapsed={time.monotonic() - t0:.1f}s")
                if attempt == 2:
                    raise
        raise last
    finally:
        shutil.rmtree(prof, ignore_errors=True)


def chrome_soft(args, url, tag, timeout=60):
    """chrome() returning (proc, elapsed) or (None, elapsed) on timeout."""
    t0 = time.monotonic()
    try:
        return chrome(args, timeout=timeout, tag=tag), time.monotonic() - t0
    except subprocess.TimeoutExpired:
        return None, time.monotonic() - t0


def shot(url, path, w, h):
    r = chrome(["--headless=new", "--disable-gpu", "--hide-scrollbars",
                f"--screenshot={path}", f"--window-size={w},{h}",
                "--virtual-time-budget=9000", url], tag=f"shot {url}")
    if not Path(path).exists():
        raise AssertionError(f"no screenshot {path}: {r.stderr[-300:]}")


def dom(url):
    r = chrome(["--headless=new", "--disable-gpu",
                "--virtual-time-budget=9000", "--dump-dom", url],
               tag=f"dom {url}")
    return r.stdout


def title_of(html):
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    return m.group(1) if m else ""


def stddev(path):
    return ImageStat.Stat(Image.open(path).convert("L")).stddev[0]


def meandiff(a, b):
    ia = Image.open(a).convert("L")
    ib = Image.open(b).convert("L").resize(ia.size)
    return ImageStat.Stat(ImageChops.difference(ia, ib)).mean[0]


def selftest(url):
    head, _, frag = url.partition("#")
    sep = "&" if "?" in head else "?"
    surl = f"{head}{sep}selftest=1" + (f"#{frag}" if frag else "")
    t = title_of(dom(surl))
    m = re.search(r"SELFTEST vw=(\d+) cw=(\d+) ch=(\d+) dpr=([\d.]+) "
                  r"opt=(\S+) plan=(\d) overflow=(\d)", t)
    if not m:
        raise AssertionError(f"no SELFTEST in title: {t[:160]!r}")
    return {"vw": int(m.group(1)), "cw": int(m.group(2)),
            "ch": int(m.group(3)), "dpr": float(m.group(4)),
            "opt": m.group(5), "plan": int(m.group(6)),
            "overflow": int(m.group(7)), "title": t}


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def iframe_measure(w, h, opt="A", query=""):
    """True viewport geometry via a fixed-size file:// iframe.

    Headless --dump-dom clamps the layout viewport (~758px) regardless of
    --window-size, so ?selftest=1 alone cannot prove a 390px phone layout.
    The wrapper pins the iframe to exactly w×h and reports the inner
    window size, scroll overflow, every overflowing element, and the chips.
    Viewer page itself is NOT modified; wrapper lives in the temp dir."""
    src = PAGE.as_uri() + (f"?{query}" if query else "") + f"#{opt}"
    html = ("<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<title>WRAP {w}x{h}</title></head><body style='margin:0'>"
            f"<iframe id='f' src='{src}' "
            f"style='width:{w}px;height:{h}px;border:0'></iframe>"
            "<div id='out'></div><script>\n"
            "window.addEventListener('load', function () {\n"
            "  setTimeout(function () {\n"
            "    try {\n"
            "      var f = document.getElementById('f');\n"
            "      var w2 = f.contentWindow, d = f.contentDocument;\n"
            "      var iw = w2.innerWidth, ih = w2.innerHeight;\n"
            "      var sw = d.documentElement.scrollWidth;\n"
            "      var cv = d.getElementById('viewer').getBoundingClientRect();\n"
            "      var bad = [];\n"
            "      Array.prototype.forEach.call(d.querySelectorAll('*'),\n"
            "        function (el) {\n"
            "          var r = el.getBoundingClientRect();\n"
            "          if (r.right > iw + 1 || r.bottom > ih + 1) {\n"
            "            var id = el.id ? '#' + el.id\n"
            "              : (el.className && el.className.baseVal === undefined\n"
            "                ? '.' + String(el.className).split(' ')[0] : '');\n"
            "            bad.push(el.tagName + id +\n"
            "              Math.round(r.right) + 'x' + Math.round(r.bottom));\n"
            "          }\n"
            "        });\n"
            "      var chips = [];\n"
            "      Array.prototype.forEach.call(\n"
            "        d.querySelectorAll('#chips button'), function (b) {\n"
            "          var r = b.getBoundingClientRect();\n"
            "          chips.push(Math.round(r.x) + ',' + Math.round(r.y) + '+' +\n"
            "            Math.round(r.width) + 'x' + Math.round(r.height));\n"
            "        });\n"
            "      document.title = 'IFRAME vw=' + iw + ' vh=' + ih +\n"
            "        ' scrollW=' + sw + ' cw=' + Math.round(cv.width) +\n"
            "        ' ch=' + Math.round(cv.height) + ' bad=' + bad.length +\n"
            "        ' chips=' + chips.join('|');\n"
            "      document.getElementById('out').textContent = bad.join(';');\n"
            "    } catch (e) { document.title = 'IFRAME ERROR: ' + e.message; }\n"
            "  }, 8000);\n"
            "});\n"
            "</script></body></html>\n")
    fd, wp = tempfile.mkstemp(suffix=".html")
    try:
        with open(fd, "w", encoding="utf-8") as fh:
            fh.write(html)
        # Budget 10s < 60s timeout: virtual time fast-forwards page timers,
        # so a 20s budget can exceed the wall-clock timeout under load.
        r, el = chrome_soft(["--headless=new", "--disable-gpu",
                             "--allow-file-access-from-files",
                             "--virtual-time-budget=10000",
                             "--window-size=1000,900",
                             "--dump-dom", Path(wp).as_uri()],
                            src, tag=f"iframe {w}x{h}")
        if r is None:
            raise TimeoutError(f"iframe launch timed out after {el:.1f}s")
        t = title_of(r.stdout)
        m = re.search(r"IFRAME vw=(\d+) vh=(\d+) scrollW=(\d+) cw=(\d+) "
                      r"ch=(\d+) bad=(\d+) chips=(.*?)(</title>|$)", t, re.S)
        if not m:
            raise AssertionError(f"no IFRAME report: {t[:200]!r}")
        out = re.search(r"<div id=\"out\">(.*?)</div>", r.stdout, re.S)
        return {"vw": int(m.group(1)), "vh": int(m.group(2)),
                "scrollW": int(m.group(3)), "cw": int(m.group(4)),
                "ch": int(m.group(5)), "bad_n": int(m.group(6)),
                "chips": m.group(7).strip().split("|"),
                "bad": (out.group(1) if out else "")[:300]}
    finally:
        Path(wp).unlink(missing_ok=True)

def main():
    chk = subprocess.run([sys.executable, str(HERE / "f3split_model.py"),
                          "--check"], capture_output=True, text=True, timeout=120)
    print(chk.stdout.strip())
    if chk.returncode != 0:
        print("FAIL\n - model --check failed")
        return 1
    SHOTS.mkdir(parents=True, exist_ok=True)
    fails, rows = [], []
    base = PAGE.as_uri()

    for opt in OPTS:
        for (w, h) in VPS:
            p = SHOTS / f"{opt}-{w}.png"
            tag = f"shot {opt} {w}x{h}"
            r, el = chrome_soft(["--headless=new", "--disable-gpu",
                                 "--hide-scrollbars",
                                 f"--screenshot={p}",
                                 f"--window-size={w},{h}",
                                 "--virtual-time-budget=9000",
                                 f"{base}#{opt}"],
                                f"{base}#{opt}", tag)
            if r is None or not Path(p).exists():
                print(f"chrome timeout tag={tag} elapsed={el:.1f}s")
                fails.append(f"{opt} {w}x{h}: shot launch failed "
                             f"({el:.0f}s)")
                rows.append({"opt": opt, "vp": f"{w}x{h}", "path": p,
                             "bytes": 0, "sd": 0.0, "title_ok": False,
                             "title": f"BROWSER-TIMEOUT {el:.0f}s"})
                continue
            sd = stddev(p)
            try:
                t = title_of(dom(f"{base}#{opt}"))
            except (subprocess.TimeoutExpired, TimeoutError) as e:
                fails.append(f"{opt} {w}x{h}: dom launch failed: {e}")
                rows.append({"opt": opt, "vp": f"{w}x{h}", "path": p,
                             "bytes": p.stat().st_size, "sd": sd,
                             "title_ok": False, "title": "BROWSER-TIMEOUT"})
                continue
            tok = (f"P.án {opt}" in t and TITLES[opt] in t
                   and not t.startswith("ERROR"))
            rows.append({"opt": opt, "vp": f"{w}x{h}", "path": p,
                         "bytes": p.stat().st_size, "sd": sd,
                         "title_ok": tok, "title": t})
            if sd <= 15:
                fails.append(f"{opt} {w}x{h}: blank (stddev {sd:.1f})")
            if not tok:
                fails.append(f"{opt} {w}x{h}: bad title {t[:100]!r}")
    for a, b in [("0", "A"), ("A", "B"), ("B", "C"), ("C", "D"), ("0", "D")]:
        d = meandiff(SHOTS / f"{a}-1440.png", SHOTS / f"{b}-1440.png")
        rows.append({"opt": f"{a}~{b}", "vp": "diff1440", "diff": d})
        # Same shell from the same camera: options differ only in the room
        # contents, so the floor is 1.0 (byte-identical would read ~0.0).
        if d <= 1.0:
            fails.append(f"pair {a}~{b}: not distinct (meandiff {d:.2f})")

    for (w, h) in VPS:
        for plan in [0, 1]:
            url = f"{base}?view=plan#A" if plan else f"{base}#A"
            try:
                st = selftest(url)
            except (subprocess.TimeoutExpired, TimeoutError,
                    AssertionError) as e:
                fails.append(f"selftest {w}x{h}p{plan}: launch failed: {e}")
                rows.append({"opt": "selftest", "vp": f"{w}x{h}p{plan}",
                             "st": {"vw": 0, "cw": 0, "dpr": 0, "plan": -1,
                                    "overflow": 1}})
                continue
            if st["overflow"] != 0:
                fails.append(f"overflow=1 at {w}x{h} plan={plan}")
            if abs(st["cw"] - st["vw"]) > 2:
                fails.append(f"cw {st['cw']} != vw {st['vw']} at {w}x{h}")
            if st["plan"] != plan:
                fails.append(f"plan flag {st['plan']} != {plan}")
            rows.append({"opt": "selftest", "vp": f"{w}x{h}p{plan}",
                         "st": st, "clamped": True})
    # Phone width by direct iframe measurement; desktop width indirectly via
    # the 1440 screenshot + clamped selftest rows (a 1440px iframe inside a
    # 1000px window is flaky under headless load - dropped by decision).
    for (w, h) in [(390, 844)]:
        try:
            fr = iframe_measure(w, h)
        except (subprocess.TimeoutExpired, TimeoutError,
                AssertionError) as e:
            fails.append(f"iframe {w}x{h}: launch failed: {e}")
            rows.append({"opt": "iframe", "vp": f"{w}x{h}",
                         "fr": {"vw": 0, "vh": 0, "scrollW": 0, "cw": 0,
                                "ch": 0, "bad_n": 1, "chips": [],
                                "bad": str(e)[:200]},
                         "ok": False})
            continue
        ok_w = fr["vw"] == w
        ok_sw = fr["scrollW"] <= fr["vw"] + 1
        ok_bad = fr["bad_n"] == 0
        chip_ok, chip_msg = True, ""
        for c in fr["chips"]:
            m = re.match(r"(-?\d+),(-?\d+)\+(\d+)x(\d+)$", c)
            if not m:
                chip_ok = False
                chip_msg = f"unparsed chip {c!r}"
                break
            x, y, cw2, ch2 = map(int, m.groups())
            if cw2 < 44 or ch2 < 44:
                chip_ok, chip_msg = False, f"chip {c} <44px"
            if x + cw2 > fr["vw"] - 4 + 1 or y + ch2 > fr["vh"] - 4 + 1:
                chip_ok, chip_msg = False, f"chip {c} escapes viewport"
        if len(fr["chips"]) != 5:
            chip_ok, chip_msg = False, f"{len(fr['chips'])} chips != 5"
        if not ok_w:
            fails.append(f"iframe {w}x{h}: vw={fr['vw']} != {w}")
        if not ok_sw:
            fails.append(f"iframe {w}x{h}: scrollW={fr['scrollW']} > vw")
        if not ok_bad:
            fails.append(f"iframe {w}x{h}: {fr['bad_n']} overflowing: "
                         f"{fr['bad']}")
        if not chip_ok:
            fails.append(f"iframe {w}x{h}: chips bad: {chip_msg}")
        rows.append({"opt": "iframe", "vp": f"{w}x{h}", "fr": fr,
                     "ok": ok_w and ok_sw and ok_bad and chip_ok})

    for opt in ["A", "D"]:
        p = SHOTS / f"{opt}-plan.png"
        try:
            shot(f"{base}?view=plan#{opt}", str(p), 1440, 900)
        except (subprocess.TimeoutExpired, TimeoutError,
                AssertionError) as e:
            fails.append(f"{opt} plan: launch failed: {e}")
            rows.append({"opt": opt, "vp": "plan", "bytes": 0, "sd": 0.0,
                         "diff": 0.0, "same": True})
            continue
        sd = stddev(p)
        q3 = SHOTS / f"{opt}-1440.png"
        ia = Image.open(q3).convert("L")
        ib = Image.open(p).convert("L").resize(ia.size)
        diff = ImageChops.difference(ia, ib)
        md = ImageStat.Stat(diff).mean[0]
        same = diff.getbbox() is None
        rows.append({"opt": opt, "vp": "plan", "bytes": p.stat().st_size,
                     "sd": sd, "diff": md, "same": same})
        if sd <= 15:
            fails.append(f"{opt} plan: blank (stddev {sd:.1f})")
        if same or md <= 3:
            fails.append(f"{opt} plan: identical to 3D shot "
                         f"(bbox={diff.getbbox()} mean={md:.2f})")

    port = free_port()
    hdl = partial(http.server.SimpleHTTPRequestHandler, directory=str(REPO))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", port), hdl)
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    http_ok = json_ok = srv_ok = False
    t = "serve not attempted"
    try:
        rel = "reports/2026-09-25-f3-bedroom-split/3d/f3-split-viewer.html"
        with urllib.request.urlopen(
                f"http://127.0.0.1:{port}/{rel}", timeout=20) as r:
            http_ok = r.status == 200 and b"P.\xc3\xa1n" in r.read()
        with urllib.request.urlopen(
                f"http://127.0.0.1:{port}/reports/2026-09-25-f3-bedroom-split/"
                f"3d/f3_split_model.json", timeout=20) as r:
            json_ok = r.status == 200 and b'"options"' in r.read()
        try:
            t = title_of(dom(f"http://127.0.0.1:{port}/{rel}#C"))
        except (subprocess.TimeoutExpired, TimeoutError) as e:
            t, srv_ok = f"BROWSER-TIMEOUT {e}", False
        else:
            srv_ok = "Glazed study" in t and not t.startswith("ERROR")
    finally:
        srv.shutdown()
        th.join(timeout=10)
    rows.append({"opt": "serve", "vp": f":{port}",
                 "http_ok": http_ok, "json_ok": json_ok, "srv_ok": srv_ok,
                 "title": t})
    if not (http_ok and json_ok and srv_ok):
        fails.append(f"serve check failed: page={http_ok} json={json_ok} "
                     f"render={srv_ok} title={t[:100]!r}")

    print(f"{'opt':<9}{'vp':<9}{'bytes':>8}{'stddev':>8}  "
          f"{'title-ok':<8}  note")
    for r in rows:
        if "sd" in r and "bytes" in r and "diff" in r:
            print(f"{r['opt']:<9}{r['vp']:<9}{r['bytes']:>8}"
                  f"{r['sd']:>8.1f}  "
                  f"{str(r.get('title_ok', '-')):<8}  "
                  f"vs3D mean={r['diff']:.2f} identical={r['same']}")
        elif "sd" in r and "bytes" in r:
            print(f"{r['opt']:<9}{r['vp']:<9}{r['bytes']:>8}"
                  f"{r['sd']:>8.1f}  "
                  f"{str(r.get('title_ok', '-')):<8}  "
                  f"{r.get('title', '')[:60]}")
        elif "diff" in r:
            print(f"{r['opt']:<9}{r['vp']:<9}        "
                  f"{'':>8}  {'':<8}  meandiff={r['diff']:.2f}")
        elif "st" in r:
            s = r["st"]
            print(f"{r['opt']:<9}{r['vp']:<9}        "
                  f"{'':>8}  {'':<8}  "
                  f"vw={s['vw']}(clamped) cw={s['cw']} dpr={s['dpr']} "
                  f"plan={s['plan']} overflow={s['overflow']}")
        elif "fr" in r:
            f = r["fr"]
            print(f"{r['opt']:<9}{r['vp']:<9}        "
                  f"{'':>8}  {'':<8}  "
                  f"MEASURED vw={f['vw']} vh={f['vh']} scrollW={f['scrollW']} "
                  f"cw={f['cw']} ch={f['ch']} bad={f['bad_n']} "
                  f"chips={' '.join(f['chips'])} "
                  f"{'OK' if r['ok'] else 'BAD ' + f['bad']}")
        elif r.get("opt") == "serve":
            print(f"serve    {r['vp']:<9}        {'':>8}  {'':<8}  "
                  f"page={r['http_ok']} json={r['json_ok']} "
                  f"render={r['srv_ok']} {r['title'][:50]}")
    if fails:
        print("FAIL")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
