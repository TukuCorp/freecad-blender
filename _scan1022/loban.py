# Lo Ban ruler lookup, cycle tables from sources 4 (akisa.vn 52.2 full table),
# 15 (soimenh.vn / congdesign 42.9 cung order), 16 (thebox.com.vn 38.8 cung order).
import math

C52 = [('QUY NHAN',True),('HIEM HOA',False),('THIEN TAI',False),('THIEN TAI',True),
       ('NHAN LUC',True),('CO DUC',False),('THIEN TAC',False),('TE TUONG',True)]
C429 = [('TAI',True),('BENH',False),('LY',False),('NGHIA',True),
        ('QUAN',True),('KIEP',False),('HAI',False),('BAN',True)]
C388 = [('DINH',True),('HAI',False),('VUONG',True),('KHO',False),('NGHIA',True),
        ('QUAN',True),('TU',False),('HUONG',True),('THAT',False),('TAI',True)]

def look(mm, cung, length):
    n = math.floor(mm / length)
    rem = mm - n * length
    i = int(rem // (length / len(cung)))
    name, good = cung[i]
    return n, name, good, rem

def rule52(mm): return look(mm, C52, 522)
def rule429(mm): return look(mm, C429, 429)
def rule388(mm): return look(mm, C388, 388)
