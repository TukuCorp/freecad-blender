import sys,glob,os
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image
for f in sorted(glob.glob("contractor/scan-2026-10-22/jpg/sheet*.jpg")):
    im=Image.open(f); print(f, im.size)
for f in ["contractor/scan-2026-10-22/jpg/IMG_9972.jpg","contractor/scan-2026-10-22/jpg/IMG_0005.jpg"]:
    im=Image.open(f); print(f, im.size)
