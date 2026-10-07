from PIL import Image, ImageDraw, ImageFont
W_MM, D_MM = 4000, 12000
S = 0.09
MAR = 90
cw, ch = int(W_MM*S), int(D_MM*S)
img = Image.new('RGB', (cw+2*MAR, ch+2*MAR+70), 'white')
dr = ImageDraw.Draw(img)
try:
    fnt = ImageFont.truetype('arial.ttf', 22)
    fnt_s = ImageFont.truetype('arial.ttf', 17)
except Exception:
    fnt = ImageFont.load_default()
    fnt_s = fnt
rooms = [
    ('LIVING|4.0 x 5.0 m', 0, 0, 4000, 5000, (219, 234, 248)),
    ('STAIRWELL|1.9 x 2.9 m', 0, 5000, 1900, 2900, (231, 229, 247)),
    ('HALL|2.1 x 2.9 m', 1900, 5000, 2100, 2900, (254, 240, 217)),
    ('BEDROOM|4.0 x 4.1 m', 0, 7900, 4000, 4100, (220, 243, 227)),
]
def mm(x, y):
    return (MAR + x*S, MAR + y*S)
order = [r[0] for r in rooms]
fillmap = {r[0]: r[5] for r in rooms}
geom = {r[0]: r[1:5] for r in rooms}
for label in order:
    x, y, w, d = geom[label]
    x0, y0 = mm(x, y)
    x1, y1 = mm(x+w, y+d)
    dr.rectangle([x0, y0, x1, y1], fill=fillmap[label], outline='black', width=3)
    cx, cy = (x0+x1)/2, (y0+y1)/2
    for i, line in enumerate(label.split('|')):
        bb = dr.textbbox((0, 0), line, font=fnt)
        dr.text((cx-(bb[2]-bb[0])/2, cy-22+i*28), line, fill='black', font=fnt)
x0, y0 = mm(0, 0)
x1, y1 = mm(W_MM, D_MM)
dr.rectangle([x0, y0, x1, y1], outline='#1d4ed8', width=5)
dr.text((MAR, 15), 'TUBEHOUSE-MINI  4.0m x 12.0m - ground floor (tubehouse-mini.json)', fill='black', font=fnt_s)
dr.text((MAR, 40), 'Front LIVING top / STAIRWELL+HALL middle / BEDROOM rear', fill='#444444', font=fnt_s)
dr.text((MAR, ch+2*MAR+10), 'Sketch saved in repo folder. Open in Paint to edit.', fill='#444444', font=fnt_s)
img.save('tubehouse-layout-sketch.png')
print('saved', img.size)
