import sys,hashlib,glob,os
sys.stdout.reconfigure(encoding="utf-8")
h={}
for f in glob.glob("contractor/scan-2026-10-22/jpg/*.jpg"):
    d=hashlib.md5(open(f,"rb").read()).hexdigest()
    h.setdefault(d,[]).append(os.path.basename(f))
for k,v in h.items():
    if len(v)>1: print("DUP",v)
print("total",len(glob.glob("contractor/scan-2026-10-22/jpg/*.jpg")))
