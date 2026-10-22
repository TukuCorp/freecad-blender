import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = "_scan1022/safety/part4.md"

with open(path, encoding="utf-8") as fh:
    t = fh.read()

i = t.find("### S-51")
j = t.find("- **ID:** S-51")
print(repr(t[j:j + 1200]))
