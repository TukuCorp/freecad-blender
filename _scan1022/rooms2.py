import json,sys
sys.stdout.reconfigure(encoding="utf-8")
d=json.load(open("designs/contractor-as-drawn.json",encoding="utf-8"))
for st in d["storeys"]:
    print("ST", st.get("name"), "base_z", st.get("base_z"), "h", st.get("height_mm"))
    for r in st.get("rooms",[]):
        rc=r.get("rect") or {}
        print("  ", r.get("id"), r.get("type"), rc.get("x"), rc.get("y"), rc.get("w"), rc.get("d"))
    for v in st.get("voids") or []:
        print("   VOID", v)
print("SITE", d["site"])
print("META", json.dumps(d["meta"],ensure_ascii=False)[:800])
