#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Idea Engine — generator kombinatoryczny.
Systematycznie mnoży NISZE x TYPY-NARZEDZI = ~15000 kombinacji,
filtruje pod ograniczenia (offline / zrob-raz / $5 / 1000 szt.) i scoruje.
To NIE jest LLM zgadujacy 15000 pomyslow — to wyczerpujace pokrycie
przestrzeni pomyslow + heurystyczny scoring. Twarda ocena nastepuje pozniej
na top-slice (agenci + 10-metodowa weryfikacja konkurencji).
"""
import csv, itertools, hashlib, os

# ── NISZE: (nazwa, bucket) ──────────────────────────────────────────────
# bucket: hobby/trade/prof/health/life/demo/relig
NICHES = []
def add(names, bucket):
    for n in names: NICHES.append((n, bucket))

add(["pszczelarze","akwaryści","piwowarzy domowi","winiarze domowi","piekarze zakwasowi",
     "dziewiarki","szydełkarki","makramistki","ceramicy","stolarze-hobbyści","modelarze kolejowi",
     "modelarze plastikowi","ptasiarze","wędkarze","wędkarze muchowi","disc golfiści","łucznicy",
     "biwakowicze","bushcrafterzy","geocacherzy","poszukiwacze z wykrywaczem","numizmatycy",
     "filateliści","kolekcjonerzy winyli","gracze planszówek","gracze RPG","malarze figurek",
     "cosplayerzy","quilterki","hafciarki","mydlarze","świecarze","jubilerzy-hobbyści",
     "kaligrafowie","bonsai-ści","storczykarze","ogrodnicy warzywni","sukulentowcy","grzybiarze",
     "degustatorzy whisky","miłośnicy cygar","astronomowie amatorzy","dronowcy","modelarze RC",
     "wspinacze","żeglarze","kajakarze","nurkowie","jeźdźcy konni","hodowcy kur",
     "hodowcy królików","terrarystów","aeromodelarze","fotografowie ptaków","biegacze górscy"], "hobby")

add(["elektrycy","hydraulicy","stolarze","malarze pokojowi","glazurnicy","dekarze","murarze",
     "spawacze","ślusarze","monterzy HVAC","ogrodnicy-firmy","arboryści","floryści","piekarze",
     "rzeźnicy","fryzjerzy","manicurzystki","tatuażyści","kolczykarze","groomerzy psów",
     "opiekunowie zwierząt","sprzątaczki","myjący okna","kominiarze","mobilni mechanicy",
     "tapicerzy","krawcowe","szewcy","kowale","brukarze","lakiernicy samochodowi"], "trade")

add(["pielęgniarki","ratownicy medyczni","położne","fizjoterapeuci","dietetycy","optometryści",
     "higienistki stomatologiczne","technicy weterynarii","nauczyciele","korepetytorzy",
     "instruktorzy nauki jazdy","nauczyciele muzyki","trenerzy personalni","instruktorzy jogi",
     "agenci nieruchomości","brokerzy ubezpieczeniowi","doradcy kredytowi","księgowi-mali",
     "notariusze","organizatorzy pogrzebów","organizatorzy eventów","wedding plannerzy",
     "fotografowie ślubni","kamerzyści","DJ-e","cateringowcy","food trucki","sprzedawcy na targu",
     "sprzedawcy Etsy","resellerzy eBay","tłumacze","bibliotekarze"], "prof")

add(["chorzy na IBS","chorzy na migrenę","alergicy","cukrzycy","z przewlekłym bólem pleców",
     "na diecie keto","na diecie FODMAP","na diecie carnivore","z celiakią","z nadciśnieniem",
     "po operacji bariatrycznej","z bezsennością","z ADHD","z dysleksją","z zaburzeniami odżywiania"], "health")

add(["nowi rodzice","planujący wesele","przeprowadzający się","dziedziczący spadek",
     "w trakcie rozwodu","opiekujący się seniorem","przygotowujący pogrzeb","oczekujący dziecka",
     "starający się o dziecko","w żałobie","remontujący mieszkanie","budujący dom"], "life")

add(["seniorzy","opiekunowie osób starszych","opiekunowie niepełnosprawnych","homeschoolerzy",
     "rodzice przedszkolaków","rodzice uczniów 1-3","studenci","emigranci uczący się języka",
     "Ukraińcy w Polsce","preppersi","minimaliści","vanliferzy","capsule-wardrobe"], "demo")

add(["muzułmanie w diasporze","Żydzi praktykujący","prawosławni","katolicy praktykujący",
     "buddyści świeccy"], "relig")

# ── ARCHETYPY NARZEDZI ──────────────────────────────────────────────────
# dur=durability(0-2), simp=build simplicity(0-2), pain(0-3), buckets=stosowalne
ALL = {"hobby","trade","prof","health","life","demo","relig"}
ARCH = {
 "reference":  dict(dur=2,simp=2,pain=2, buckets=ALL),
 "dosage":     dict(dur=2,simp=2,pain=3, buckets={"health","trade","prof","hobby"}),
 "calculator": dict(dur=2,simp=2,pain=2, buckets=ALL),
 "converter":  dict(dur=2,simp=2,pain=1, buckets=ALL),
 "estimator":  dict(dur=2,simp=1,pain=2, buckets={"trade","prof","life","hobby"}),
 "tracker":    dict(dur=1,simp=2,pain=2, buckets=ALL),
 "symptomdiary":dict(dur=2,simp=2,pain=3, buckets={"health","demo"}),
 "log":        dict(dur=1,simp=2,pain=1, buckets=ALL),
 "inventory":  dict(dur=1,simp=1,pain=2, buckets={"hobby","trade","prof"}),
 "checklist":  dict(dur=2,simp=2,pain=1, buckets={"trade","prof","life"}),
 "planner":    dict(dur=1,simp=1,pain=2, buckets={"life","prof","demo"}),
 "expiry":     dict(dur=2,simp=2,pain=2, buckets={"trade","prof","demo","life"}),
 "pricebook":  dict(dur=1,simp=1,pain=2, buckets={"trade","prof"}),
 "flashcard":  dict(dur=2,simp=2,pain=2, buckets={"demo","prof","relig"}),
 "generator":  dict(dur=2,simp=1,pain=1, buckets={"life","prof","demo","relig"}),
 "randomizer": dict(dur=2,simp=2,pain=1, buckets={"demo","life","hobby"}),
 "splitter":   dict(dur=2,simp=1,pain=3, buckets={"life","demo"}),
 "sizing":     dict(dur=2,simp=2,pain=2, buckets={"hobby","trade","prof","life"}),
 "rotation":   dict(dur=2,simp=2,pain=1, buckets={"demo","hobby","prof"}),
 "logbook":    dict(dur=1,simp=2,pain=2, buckets={"hobby","trade","prof"}),
}
# 100 konkretnych typow narzedzi: (label, archetype)
TASKS = []
def task(labels, arch):
    for l in labels: TASKS.append((l, arch))
task(["tabela referencyjna","ściąga norm/parametrów","lookup specyfikacji","podręczna baza wiedzy","tabela porównawcza"], "reference")
task(["kalkulator dawkowania","kalkulator proporcji mieszanki","kalkulator stężeń","przelicznik receptury","kalkulator składników"], "dosage")
task(["kalkulator kosztów","kalkulator materiałów","kalkulator opłacalności","kalkulator zużycia","kalkulator czasu"], "calculator")
task(["konwerter jednostek","przelicznik miar","konwerter formatów","przelicznik walut-stały","konwerter rozmiarów"], "converter")
task(["kosztorys/wycena","szacowanie nakładu","kalkulator oferty","wycena na papierze","estymacja czasu robót"], "estimator")
task(["tracker postępu","monitor nawyku","śledzenie wyników","tracker pomiarów","licznik serii"], "tracker")
task(["dziennik objawów → PDF dla lekarza","dziennik triggerów","log epizodów choroby","dziennik diety i reakcji","raport dla specjalisty"], "symptomdiary")
task(["dziennik aktywności","log zdarzeń","rejestr czynności","notatnik tematyczny","kronika"], "log")
task(["katalog kolekcji","ewidencja zasobów","inwentarz wyposażenia","baza sprzętu","spis zbiorów"], "inventory")
task(["lista kontrolna","checklist inspekcji","protokół odbioru","lista BHP","karta kontroli jakości"], "checklist")
task(["planer projektu","plan krok-po-kroku","organizator zadań","planer wydarzenia","harmonogram przygotowań"], "planner")
task(["tracker terminów ważności","alert wygasania uprawnień","przypominacz przeglądów","monitor dat odnowień","kalendarz obowiązków"], "expiry")
task(["cennik usług","książka cen","kalkulator marży","tabela stawek","kosztorys materiałowy"], "pricebook")
task(["fiszki/drill nauki","generator ćwiczeń","trening powtórek","quiz tematyczny","karty pamięciowe"], "flashcard")
task(["generator dokumentu","generator etykiet do druku","generator certyfikatów","generator planu","generator listy"], "generator")
task(["losowanie z regułami","picker decyzji","rotacyjny wybór","randomizer grupowy","koło wyboru"], "randomizer")
task(["kalkulator podziału","splitter kosztów/majątku","rozliczenie grupowe","podział równościowy","kalkulator wyrównań"], "splitter")
task(["kalkulator rozmiaru/ilości","kalkulator metrażu","przelicznik zapotrzebowania","kalkulator porcji","kalkulator wymiarów"], "sizing")
task(["rotacja/planer cykliczny","układacz harmonogramu","plan rotacji","grafik powtarzalny","rozkład tygodniowy"], "rotation")
task(["dziennik branżowy","logbook sesji","rejestr inspekcji","karta klienta","historia serwisowa"], "logbook")

# ── ATRYBUTY NISZ wg bucket ─────────────────────────────────────────────
BUCKET = {  # spend, recurring, techAverse(=mniej konkurencji), size
 "hobby": dict(spend=2,recur=1,averse=1,size=1),
 "trade": dict(spend=2,recur=2,averse=2,size=1),
 "prof":  dict(spend=2,recur=2,averse=1,size=1),
 "health":dict(spend=2,recur=2,averse=1,size=2),
 "life":  dict(spend=2,recur=0,averse=1,size=2),
 "demo":  dict(spend=1,recur=1,averse=1,size=2),
 "relig": dict(spend=1,recur=2,averse=1,size=1),
}

def score(nb, arch):
    b=BUCKET[nb]; a=ARCH[arch]
    return (b["spend"]+b["recur"]+b["averse"]+b["size"]
            + a["dur"]*2 + a["simp"] + a["pain"])

# ── GENERACJA GRIDU ─────────────────────────────────────────────────────
os.makedirs("company/ideas/iteration-2", exist_ok=True)
rows=[]
for (nname,nb),(tlabel,arch) in itertools.product(NICHES,TASKS):
    plausible = nb in ARCH[arch]["buckets"]
    s = score(nb,arch) if plausible else 0
    idea = f"{tlabel} dla: {nname}"
    rows.append((idea,nname,nb,tlabel,arch,int(plausible),s))

csvp="company/ideas/iteration-2/seed-corpus.csv"
with open(csvp,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["idea","nisza","bucket","narzedzie","archetyp","plausible","score"])
    w.writerows(rows)

total=len(rows)
plaus=[r for r in rows if r[5]==1]
plaus.sort(key=lambda r:(-r[6], r[0]))
top=plaus[:60]

mdp="company/ideas/iteration-2/AUTO-SHORTLIST.md"
with open(mdp,"w",encoding="utf-8") as f:
    f.write("# Iteracja 2 — Generator kombinatoryczny (auto)\n\n")
    f.write(f"- Nisze: **{len(NICHES)}** × Narzędzia: **{len(TASKS)}** = **{total}** kombinacji w gridzie.\n")
    f.write(f"- Sensownych (nisza pasuje do typu narzędzia): **{len(plaus)}**.\n")
    f.write(f"- Pełny korpus: `seed-corpus.csv` ({total} wierszy). Poniżej TOP 60 wg heurystyki.\n\n")
    f.write("> Heurystyka = spend+recurring+techAverse+size niszy + durability×2+simplicity+pain narzędzia.\n")
    f.write("> To pre-ranking do twardej weryfikacji (agenci + 10-metodowa konkurencja), NIE werdykt.\n\n")
    f.write("| # | Pomysł | bucket | score |\n|---|--------|--------|------|\n")
    for i,r in enumerate(top,1):
        f.write(f"| {i} | {r[0]} | {r[2]} | {r[6]} |\n")

print(f"GRID={total} PLAUSIBLE={len(plaus)} NICHES={len(NICHES)} TASKS={len(TASKS)}")
print("TOP5:", [(r[0],r[6]) for r in top[:5]])
