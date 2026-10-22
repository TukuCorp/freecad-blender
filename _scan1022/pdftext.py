import sys,glob
sys.stdout.reconfigure(encoding="utf-8")
try:
    import fitz
    print("pymupdf ok", fitz.__doc__)
except Exception as e:
    print("no pymupdf:", e)
    fitz=None
if fitz:
    for f in sorted(glob.glob("contractor/*.pdf")):
        doc=fitz.open(f)
        t="".join(p.get_text() for p in doc)
        print("---", f, "pages", doc.page_count, "chars", len(t.strip()))
        print(repr(t.strip()[:600]))
