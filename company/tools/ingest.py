#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wchłania wszystkie company/ideas/incoming/*.jsonl do verified.json (dedup po id i po nazwie)."""
import json, glob, os, re, unicodedata
V="company/ideas/verified.json"
d=json.load(open(V,encoding="utf-8"))
cands=d["candidates"]
by_id={c["id"] for c in cands}
def norm(s): 
    s=unicodedata.normalize("NFKD",s.lower()); return re.sub(r"[^a-z0-9]","",s)
by_name={norm(c["name"]) for c in cands}
added=0; bad=0; dup=0
for f in sorted(glob.glob("company/ideas/incoming/*.jsonl")):
    for line in open(f,encoding="utf-8"):
        line=line.strip()
        if not line or line.startswith("#"): continue
        try: o=json.loads(line)
        except: bad+=1; continue
        name=o.get("name","").strip()
        if not name: bad+=1; continue
        if norm(name) in by_name: dup+=1; continue
        i=o.get("id") or "X"+str(len(cands)+added+1)
        while i in by_id: i=i+"_"
        c={"id":i,"name":name,
           "verdict":o.get("verdict","SŁABO OBSŁUŻONA"),
           "competitors":o.get("competitors",["(bulk)"]) if isinstance(o.get("competitors"),list) else [str(o.get("competitors"))],
           "n":int(o.get("n",2)),"free_sub":bool(o.get("free_sub",True)),
           "model":o.get("model","mixed"),"durability":int(o.get("durability",7)),
           "reach":int(o.get("reach",3)),"demand":int(o.get("demand",2))}
        cands.append(c); by_id.add(i); by_name.add(norm(name)); added+=1
json.dump(d,open(V,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(f"dodano={added} duplikaty={dup} bledne={bad} | verified={len(cands)}")
# wyczysc incoming po wchlonieciu
for f in glob.glob("company/ideas/incoming/*.jsonl"): os.remove(f)
