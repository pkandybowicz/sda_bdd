#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v5 — soczewka komercyjna 'tysiące': demand_proof, wedge, addressability, build, factory.
CELOWO odwraca v4: konkurenci=dowód popytu; free_sub mniej istotny niż POWÓD niewystarczalności."""
import json,re
from collections import Counter

def text(c):
    comp=c.get("competitors",[]); comp=comp if isinstance(comp,list) else [str(comp)]
    return (c["name"]+" "+" ".join(comp)).lower()

# rodziny -> factory_fit
FAMS={
 "collection":["kolekcj","inwentarz","collection","catalog","kolekcjon"],
 "practice":["praktyk","practice","trening","postęp","progress","drill","rudiment","setlist","repertuar"],
 "calc":["kalkulator","calculator","ratio","proporcj","parametry","settings","reference","yield","percentage","estimator","kosztorys","cost","calc"],
 "fieldlog":["log","dziennik","journal","tracker","rejestr","sesj","session"],
 "formula":["formuł","receptur","recipe","mix","blend","protokół","protocol","dosing","nutrient"],
}
ADDRESS_HI=["kolekcj","collection","craft","rękodz","hobby","sport","klub","forum","reddit","cosplay","modelar","wędk","łow","pszczel","gildi","fan","enthusiast","narrator","voice","tattoo","tatuaż","aquasc","reef","bonsai","homebrew","piwo","whisky","sommelier","cicerone","disc golf","pickleball","kayak","wspina","ham radio","retro","vintage","luthier","quilt","knit","minia","warhammer","rpg","ttrpg"]
FREE_GIANT=["sleep","screen_time","menstrual","medication","step","weather","budget","todo","habit","pomodoro","note","calorie","water","fitness log","period","mood","gratitude","meditation"]
EXPENSIVE=["optymaliz","optimiz","route","sync","live","real-time","mapa","map ","gps","ai ","scan","ocr","bank","cloud","stream","multiplayer","social network"]
ENGINE=["kalkulator","calculator","ratio","proporcj","parametry","settings","reference","yield","percentage","speeds","feeds","heat","cure","dye","hydration","dosing","nutrient","estimator","kosztorys","scaler","converter"]

def axes(c):
    s=text(c); n=c.get("n",0); model=(c.get("model") or "").lower()
    reach=c.get("reach",3); demand=c.get("demand",2); dur=c.get("durability",6); free_sub=c.get("free_sub",True)
    # demand_proof: płatny rynek = dowód WTP; sub najsilniej; n>=3 aktywny; n==0 ryzyko braku rynku
    dp=0.0
    if "sub" in model: dp+=2.0
    elif "freemium" in model: dp+=1.1
    elif model in("onetime","mixed","paid","buy","free"): dp+=1.4
    if n>=4: dp+=1.0
    elif n>=2: dp+=0.6
    elif n==0: dp-=0.8
    dp+=0.4*demand
    if any(g in s for g in FREE_GIANT): dp-=1.6   # darmowy gigant wbudowany = fałszywy popyt
    dp=max(0,min(3,dp))
    # wedge_strength: one-time vs sub; brak darmowego substytutu; silnik
    w=0.0
    if "sub" in model: w+=1.5
    if not free_sub: w+=1.2
    if any(e in s for e in ENGINE): w+=1.0
    if "freemium" in model and free_sub: w+=0.3
    w=max(0,min(3,w))
    # addressability: skupiona społeczność
    a=0.5
    if any(k in s for k in ADDRESS_HI): a+=2.0
    if reach<=2: a+=0.5      # mała + skupiona = łatwo dosięgnąć
    if reach>=6 and any(g in s for g in FREE_GIANT): a-=0.5
    a=max(0,min(3,a))
    # build_cheapness: prosty offline taniej
    b=1.5
    if any(e in s for e in ENGINE): b+=1.0
    if any(k in s for k in ["checklist","log","tracker","inventory","inwentarz","collection","kolekcj","reference","calculator","kalkulator"]): b+=0.8
    if any(x in s for x in EXPENSIVE): b-=1.5
    b=max(0,min(3,b))
    return dp,w,a,b

def factory_fit(c,fam_counts):
    s=text(c); best=0
    for fam,kw in FAMS.items():
        if any(k in s for k in kw):
            cnt=fam_counts[fam]
            best=max(best, 2.0 if cnt>=40 else 1.0 if cnt>=10 else 0.3)
    return best

def load_score(path="company/ideas/verified.json"):
    d=json.load(open(path)); cs=d["candidates"]
    fc=Counter()
    for c in cs:
        s=text(c)
        for fam,kw in FAMS.items():
            if any(k in s for k in kw): fc[fam]+=1
    for c in cs:
        dp,w,a,b=axes(c); ff=factory_fit(c,fc)
        dur=c.get("durability",6)
        raw=0.28*dp+0.24*w+0.20*a+0.16*b+0.12*ff
        c["v5"]=round(100*raw/3 + min(dur,10)*0.6,1)
        c["v5ax"]=dict(demand=round(dp,1),wedge=round(w,1),addr=round(a,1),build=round(b,1),fact=round(ff,1))
    return cs

if __name__=="__main__":
    cs=load_score()
    cs.sort(key=lambda x:-x["v5"])
    print("TOP30 v5 — soczewka komercyjna 'tysiące'")
    print(f"{'v5':>5} {'dem':>3}{'wdg':>4}{'adr':>4}{'bld':>4}{'fac':>4}  {'model':8} fs  nisza")
    for c in cs[:30]:
        ax=c["v5ax"]; fs="F" if not c.get("free_sub") else "t"
        print(f"{c['v5']:>5} {ax['demand']:>3}{ax['wedge']:>4}{ax['addr']:>4}{ax['build']:>4}{ax['fact']:>4}  {(c.get('model') or '')[:8]:8} {fs}  {c['name'][:52]}")
