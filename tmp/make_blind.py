from PIL import Image
import pathlib

def cover_crop(img, target_w, target_h):
    """Resize to cover target, then center crop."""
    iw, ih = img.size
    # scale to cover
    scale = max(target_w / iw, target_h / ih)
    nw, nh = int(round(iw * scale)), int(round(ih * scale))
    img = img.resize((nw, nh), Image.LANCZOS)
    # center crop
    left = (nw - target_w) // 2
    top = (nh - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))

def make_blind(bar_path, cand_path, out_path, total_w, total_h, divider=3):
    bar = Image.open(bar_path).convert("RGB")
    cand = Image.open(cand_path).convert("RGB")
    pane_w = (total_w - divider) // 2
    pane_h = total_h
    # if odd width, make right pane 1px wider
    pane_w2 = total_w - divider - pane_w
    bar_pane = cover_crop(bar, pane_w, pane_h)
    cand_pane = cover_crop(cand, pane_w2, pane_h)
    out = Image.new("RGB", (total_w, total_h), (255,255,255))
    out.paste(bar_pane, (0, 0))
    # divider
    for x in range(pane_w, pane_w + divider):
        for y in range(total_h):
            out.putpixel((x, y), (255,255,255))
    out.paste(cand_pane, (pane_w + divider, 0))
    out.save(out_path, "PNG")
    print(f"wrote {out_path} {out.size} from bar {bar_path} {bar.size} cand {cand_path} {cand.size}")

# Desktop blind: 1280x720
make_blind("tmp/bar-0.jpg", "tmp/critic-1280x720.png", "tmp/blind-desktop-1280.png", 1280, 720, divider=2)
make_blind("tmp/bar-0.jpg", "tmp/critic-1280x720.png", "reports/gloop-critic-viewer-desktop-blind-round2.png", 1280, 720, divider=3)

# Mobile blind: 750x812 (two 375 halves) - previous was 750
make_blind("tmp/bar-0.jpg", "tmp/critic-375x812.png", "tmp/blind-mobile-375.png", 750, 812, divider=4)
make_blind("tmp/bar-0.jpg", "tmp/critic-375x812.png", "reports/gloop-critic-viewer-mobile-blind-round2.png", 750, 812, divider=4)

# Also save individual copies for forensics
import shutil
shutil.copy2("tmp/bar-0.jpg", "reports/gloop-critic-viewer-bar-0-round2.jpg")
shutil.copy2("tmp/critic-1280x720.png", "reports/gloop-critic-viewer-critic-1280x720-round2.png")
shutil.copy2("tmp/critic-375x812.png", "reports/gloop-critic-viewer-critic-375x812-round2.png")
print("done")
