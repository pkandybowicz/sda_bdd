#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v6 — poprawka v5 po audycie 'kominiarza'. Zmiany:
  (1) NOWA oś SCALE = wielkość rynku z reach (nagradza dużą bazę, nie karze jej);
  (2) WEDGE karany gdy obecny poziomy gigant FSM/SaaS (Jobber/Housecall/ServiceTitan/SafetyCulture...) — bo solo już obsłużone tanio;
  (3) model 'free' NIE jest dowodem popytu (było +1.4);
  (4) wysokie n (>=6 poważnych graczy) karze wedge (zatłoczenie);
  (5) artefakty augmentacji / puści konkurenci -> low-confidence, wypadają z topu.
"""
import json
from collections import Counter

def text(c):
    comp=c.get("competitors",[]); comp=comp if isinstance(comp,list) else [str(comp)]
    return (c["name"]+" "+" ".join(comp)).lower()
def comptext(c):
    comp=c.get("competitors",[]); comp=comp if isinstance(comp,list) else [str(comp)]
    return " ".join(comp).lower()

FAMS={
 "collection":["kolekcj","inwentarz","collection","catalog","kolekcjon"],
 "practice":["praktyk","practice","trening","postęp","progress","drill","rudiment","setlist","repertuar"],
 "calc":["kalkulator","calculator","ratio","proporcj","parametry","settings","reference","yield","percentage","estimator","kosztorys","cost","calc"],
 "fieldlog":["log","dziennik","journal","tracker","rejestr","sesj","session","inspekcj","inspection","checklist","compliance"],
 "formula":["formuł","receptur","recipe","mix","blend","protokół","protocol","dosing","nutrient"],
}
ADDRESS_HI=["kolekcj","collection","craft","rękodz","hobby","sport","klub","forum","reddit","cosplay","modelar","wędk","łow","pszczel","gildi","fan","enthusiast","narrator","voice","tattoo","tatuaż","aquasc","reef","bonsai","homebrew","piwo","whisky","sommelier","cicerone","disc golf","pickleball","kayak","wspina","ham radio","retro","vintage","luthier","quilt","knit","minia","warhammer","rpg","ttrpg","etsy","cricut"]
FREE_GIANT=["sleep","screen_time","menstrual","medication","step","weather","budget","todo","habit","pomodoro","note","calorie","water","fitness log","period","mood","gratitude","meditation"]
EXPENSIVE=["optymaliz","optimiz","route","sync","live","real-time","mapa","map ","gps","ai ","scan","ocr","bank","cloud","stream","multiplayer","social network"]
ENGINE=["kalkulator","calculator","ratio","proporcj","parametry","settings","reference","yield","percentage","speeds","feeds","heat","cure","dye","hydration","dosing","nutrient","estimator","kosztorys","scaler","converter"]
# poziomi giganci: jeśli obsługują niszę, solo NIE jest pominięte -> wedge słaby
HORIZ_GIANT=["jobber","housecall","servicetitan","service titan","service fusion","servicefusion","safetyculture","iauditor","field service","fieldservice","workiz","square","fresha","quickbooks","xero","monday.com","notion","jotform","gocanvas","go canvas","samsara","motive","geotab","procore","fieldwire","raken","upkeep","maintainx","kickserv","successware","servicem8","simpro","commusoft"]
# artefakty augmentacji / brak realnych danych
JUNKCOMP=["mutacj","demand-first","agent)","placeholder","(brak","tbd","n/a"]
# ZWERYFIKOWANE rynki gdzie istnieje świetna DARMOWA dominująca aplikacja (free_sub agentów bywa błędne)
SATURATED_FREE=["mileage","przebieg","roof pitch","spadek-dachu","spadek dachu","speeds & feeds","speeds and feeds","speeds-feeds","feeds-speeds","flight log","logbook","pilot log","beep test","vo2","unit conv","przelicznik jednost","tip calc","bmi","ohm"]

def lowconf(c):
    ct=comptext(c).strip()
    if not ct: return True
    if any(j in ct for j in JUNKCOMP): return True
    return False

def norm(s): return s.replace("_"," ").replace("-"," ")
def axes(c):
    s=text(c); sn=norm(s); ct=comptext(c); n=c.get("n",0); model=(c.get("model") or "").lower()
    reach=c.get("reach",3); demand=c.get("demand",2); free_sub=c.get("free_sub",True)
    # (a) demand_proof — płatny rynek = dowód WTP. 'free' = brak dowodu (FIX).
    dp=0.0
    if "sub" in model: dp+=2.0
    elif "freemium" in model: dp+=1.1
    elif model in ("onetime","one-time","mixed","paid","buy"): dp+=1.4
    elif model=="free": dp+=0.0          # FIX: darmowy != WTP
    else: dp+=0.5
    if n>=4: dp+=1.0
    elif n>=2: dp+=0.6
    elif n==1: dp+=0.2
    elif n==0: dp-=1.0                    # brak konkurentów = ryzyko braku rynku
    dp+=0.4*demand
    if any(g in s for g in FREE_GIANT): dp-=1.6
    dp=max(0,min(3,dp))
    # (b) wedge — tani offline one-time bije incumbenta?
    w=0.0
    if "sub" in model: w+=1.3
    if not free_sub: w+=0.9
    if any(e in s for e in ENGINE): w+=0.8
    if "freemium" in model and free_sub: w+=0.3
    if any(g in ct for g in HORIZ_GIANT): w-=1.2   # FIX: gigant FSM obsługuje solo -> słaby klin
    if n>=6: w-=0.6                                  # FIX: zatłoczenie poważnymi graczami
    if any(k in sn for k in SATURATED_FREE): w-=1.6  # FIX: zweryfikowana darmowa dominacja
    w=max(0,min(3,w))
    # (c) SCALE — wielkość dostępnego płacącego rynku z reach 1..6 (NOWE)
    scale=max(0,min(3,(reach-1)/5*3))
    # (d) addressability — czy tanio DOTRZEMY (skupiona społeczność). Usunięto bonus za mały rynek.
    a=0.7
    if any(k in s for k in ADDRESS_HI): a+=1.8
    a=max(0,min(3,a))
    # (e) build — prosty offline taniej
    b=1.5
    if any(e in s for e in ENGINE): b+=1.0
    if any(k in s for k in ["checklist","log","tracker","inventory","inwentarz","collection","kolekcj","reference","calculator","kalkulator"]): b+=0.8
    if any(x in s for x in EXPENSIVE): b-=1.5
    b=max(0,min(3,b))
    return dp,w,scale,a,b

def factory_fit(c,fc):
    s=text(c); best=0
    for fam,kw in FAMS.items():
        if any(k in s for k in kw):
            cnt=fc[fam]; best=max(best, 2.0 if cnt>=40 else 1.0 if cnt>=10 else 0.3)
    return best

def load_score(path="company/ideas/verified.json"):
    d=json.load(open(path)); cs=d["candidates"]
    fc=Counter()
    for c in cs:
        s=text(c)
        for fam,kw in FAMS.items():
            if any(k in s for k in kw): fc[fam]+=1
    for c in cs:
        dp,w,sc,a,b=axes(c); ff=factory_fit(c,fc); dur=c.get("durability",6)
        raw=0.24*dp+0.22*w+0.20*sc+0.10*a+0.12*b+0.12*ff
        v=100*raw/3 + min(dur,10)*0.5
        if lowconf(c): v-=18                      # FIX: artefakty/puste dane out of top
        if any(k in norm(text(c)) for k in SATURATED_FREE): v-=10   # FIX: darmowa dominacja
        c["v6"]=round(v,1)
        c["v6ax"]=dict(demand=round(dp,1),wedge=round(w,1),scale=round(sc,1),addr=round(a,1),build=round(b,1),fact=round(ff,1),lc=lowconf(c))
    return cs

if __name__=="__main__":
    cs=load_score(); cs.sort(key=lambda x:-x["v6"])
    print("TOP30 v6 — po audycie (scale+wedge-hardening)")
    print(f"{'v6':>5} {'dem':>3}{'wdg':>4}{'scl':>4}{'adr':>4}{'bld':>4}{'fac':>4} {'model':9} {'rch':>3} {'n':>2} fs lc  nisza")
    for c in cs[:30]:
        ax=c["v6ax"]; fs="F" if not c.get("free_sub") else "t"; lc="!" if ax["lc"] else " "
        print(f"{c['v6']:>5} {ax['demand']:>3}{ax['wedge']:>4}{ax['scale']:>4}{ax['addr']:>4}{ax['build']:>4}{ax['fact']:>4} {(c.get('model') or '')[:9]:9} {c.get('reach',0):>3} {c.get('n',0):>2} {fs}  {lc} {c['name'][:44]}")
