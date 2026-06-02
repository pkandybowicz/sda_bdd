#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scoring TOP 10 — czyta company/ideas/verified.json, stosuje ALGORYTM oceny
i wypisuje TOP 10 (md + json + stdout). Zmiana algorytmu => bump ALGO i
re-run na CALEJ bazie (re-walidacja TOP10).
"""
import json, datetime, sys

ALGO = "v4"
# B2B / nisze zawodowe poza app-storem (discovery nie zabija) — lekki bonus do openness.
B2B = {"FoodTemp","DyeRatio","HairColorRecord","ChemLabel","ContinuingEdTracker",
       "EstimateSlip","CaregiverHandover","MealCost"}
# Wagi v4 — score = 100 * MARKET * DURFACTOR * OPENNESS (mnozniki, nie sumy).
#  MARKET   = jak duzy/glodny rynek (reach 0-6, demand 0-3). Maly rynek => niski wynik
#             niezaleznie od pustki niszy (pusta nisza bez ludzi = bezwartosciowa).
#  DURFACTOR= trwalosc popytu (dur 0-10) skaluje 0.65..1.0.
#  OPENNESS = jak otwarta konkurencyjnie (verdict + free_sub + model[klin cenowy] + n).
def score(c):
    v = c["verdict"]; n = c["n"]; free = c["free_sub"]; model = c["model"]
    dem = c.get("demand", 2 if n > 0 else 1)
    dur = c["durability"]; reach = c["reach"]
    # --- MARKET (0..1): zasieg i popyt jako mnozniki ---
    market = 0.55*(min(reach,6)/6.0) + 0.45*(min(dem,3)/3.0)
    # --- DURFACTOR (0.65..1.0) ---
    durfactor = 0.65 + 0.35*(min(max(dur,0),10)/10.0)
    # --- OPENNESS (0..~1) ---
    b2b = 0.06 if c["id"] in B2B else 0.0
    if v == "PUSTA Z OKAZJI":
        openness = 0.95 - 0.06*min(n,6) - (0.35 if free else 0.0) + b2b
    elif v == "SŁABO OBSŁUŻONA":
        wedge = 0.18 if (model in ("sub","enterprise","mixed") and not free) else 0.0
        openness = 0.62 + wedge - (0.32 if free else 0.0) - 0.03*min(n,8) + b2b
    elif v == "ZATŁOCZONA":
        wedge = 0.22 if (model in ("sub","enterprise") and not free) else (0.10 if (model=="mixed" and not free) else 0.0)
        openness = 0.38 + wedge - (0.30 if free else 0.0) - 0.04*min(n,9) + b2b
    else:  # PUSTA Z PRZYCZYNY (popyt nie istnieje / strukturalnie martwa)
        openness = 0.15 - (0.05 if free else 0.0)
    openness = max(0.0, min(1.0, openness))
    s = 100.0 * market * durfactor * openness
    return int(round(max(0, min(100, s))))

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
