import json,sys
sys.stdout.reconfigure(encoding="utf-8")
d=json.load(open("designs/contractor-as-drawn.json",encoding="utf-8"))
print(list(d.keys()))
for st in d.get("storeys",[]):
    print("STOREY", st.get("id"), st.get("name"), st.get("base_z"), st.get("height_mm"), "voids", len(st.get("voids") or []))
    for r in st.get("rooms",[]):
        print("   ", r.get("id"), "|", r.get("name"), "|", r.get("type"), "| x",r.get("x"),"y",r.get("y"),"w",r.get("w"),"d",r.get("d"))
