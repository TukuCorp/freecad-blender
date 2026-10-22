import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part4.md"

with open(path, encoding="utf-8") as fh:
    t = fh.read()

old = (
    'records that *"No sheet prints \'THANG MÁY\' next to a shaft on any floor plan"* '
    'and that the label appears once, on the roof sheet, as *"Ô KỸ THUẬT THANG MÁY"*, '
    'and concludes that the shaft\'s very existence *"is an inference, not a read"*.'
)

new = (
    'records that the three residential floor-plan sheets *"show the stair block followed '
    'by an unlabelled walled void, then a light well, then WC — never a shaft marked '
    '\'THANG MÁY\'"*, and that the label *"Ô KỸ THUẬT THANG MÁY"* *"appears exactly once, on '
    'the roof sheet"*. The ledger\'s own conclusion is that the shaft is *"an inference, not '
    'a read"*.'
)

print("found:", old in t)
t = t.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(t)

with open(path, encoding="utf-8") as fh:
    t2 = fh.read()
i = t2.find("Scope note.")
print(repr(t2[i:i + 800]))
