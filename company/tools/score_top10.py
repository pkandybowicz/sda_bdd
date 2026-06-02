#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scoring TOP 10 — czyta company/ideas/verified.json, stosuje ALGORYTM oceny
i wypisuje TOP 10 (md + json + stdout). Zmiana algorytmu => bump ALGO i
re-run na CALEJ bazie (re-walidacja TOP10).
"""
import json, datetime, sys

ALGO = "v3"
# B2B / nisze zawodowe poza app-storem (discovery nie zabija) — lekki bonus.
B2B = {"FoodTemp","DyeRatio","HairColorRecord","ChemLabel","ContinuingEdTracker",
       "EstimateSlip","CaregiverHandover","MealCost"}
# Wagi v3 — DWA tory wygranej:
#  (A) REALNY BLUE OCEAN: verdict 'PUSTA Z OKAZJI' = jest popyt, NIE ma apki -> moze 70+.
#  (B) KLIN CENOWY w zatloczonym: droga subskrypcja bez darmowej alternatywy.
# 'demand' (0-3): sila sygnalu popytu (prosby/wyszukiwania/arkusze), domyslnie z verdiktu.
def score(c):
    v = c["verdict"]; n = c["n"]; free = c["free_sub"]; model = c["model"]
    dem = c.get("demand", 2 if n > 0 else 1)
    dur = c["durability"]; reach = c["reach"]
    b2b = 6 if c["id"] in B2B else 0
    if v == "PUSTA Z OKAZJI":
        # blue ocean: popyt potwierdzony, brak/minimum apek
        s = 50 + dem*9 - min(4*n, 12) - (15 if free else 0) + dur + reach + b2b
    elif v == "SŁABO OBSŁUŻONA":
        wedge = 12 if (model in ("sub","enterprise","mixed") and not free) else 0
        s = 38 + dem*5 - min(2*n, 16) - (18 if free else 0) + wedge + dur + reach + b2b
    elif v == "ZATŁOCZONA":
        wtp = 15 if model in ("onetime","sub","mixed","enterprise") else 0
        comp = -min(3*n, 27)
        freep = -28 if free else 0
        wedge = 28 if (model in ("sub","enterprise") and not free) else (10 if (model=="mixed" and not free) else 0)
        s = 35 + wtp + comp + freep + wedge + b2b + dur + reach
    else:  # PUSTA Z PRZYCZYNY
        s = 20 - (10 if free else 0) + dur + reach
    return max(0, min(100, s))

def main():
    data = json.load(open("company/ideas/verified.json", encoding="utf-8"))
    cs = data["candidates"]
    for c in cs: c["score"] = score(c)
    cs.sort(key=lambda c: (-c["score"], c["id"]))
    top = cs[:10]
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # JSON dla portalu
    json.dump({"algo":ALGO,"updated":ts,"verified":len(cs),
               "top10":[{"id":c["id"],"name":c["name"],"score":c["score"],
                         "verdict":c["verdict"],"n":c["n"]} for c in top]},
              open("company/ideas/top10.json","w",encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # Markdown
    L=[]
    L.append(f"# 🏆 TOP 10 pomysłów — żywy ranking\n")
    L.append(f"> Algorytm: **{ALGO}** · Zweryfikowanych realnie: **{len(cs)}** · Aktualizacja: {ts}\n")
    L.append("> Każdy pomysł przeszedł weryfikację konkurencji w sieci PRZED oceną.\n")
    L.append("\n| # | Pomysł | Score | Werdykt niszy | #konkur. |")
    L.append("|---|--------|:-----:|---------------|:--------:|")
    for i,c in enumerate(top,1):
        L.append(f"| {i} | {c['name']} | **{c['score']}** | {c['verdict']} | {c['n']} |")
    L.append(f"\n_Pełna baza: company/ideas/verified.json · Scoring: company/tools/score_top10.py_\n")
    open("company/ideas/TOP10.md","w",encoding="utf-8").write("\n".join(L))

    # stdout (zwiezla tabela do czatu)
    print(f"TOP10 | algo={ALGO} | verified={len(cs)} | {ts}")
    print(f"{'#':>2}  {'SCORE':>5}  {'WERDYKT':<18}  POMYSL")
    for i,c in enumerate(top,1):
        print(f"{i:>2}  {c['score']:>5}  {c['verdict']:<18}  {c['name']}")

if __name__ == "__main__":
    main()
