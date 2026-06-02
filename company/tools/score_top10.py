#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scoring TOP 10 — czyta company/ideas/verified.json, stosuje ALGORYTM oceny
i wypisuje TOP 10 (md + json + stdout). Zmiana algorytmu => bump ALGO i
re-run na CALEJ bazie (re-walidacja TOP10).
"""
import json, datetime, sys

ALGO = "v2"
# B2B / nisze zawodowe poza app-storem (discovery nie zabija) — lekki bonus.
B2B = {"FoodTemp","DyeRatio","HairColorRecord","ChemLabel","ContinuingEdTracker",
       "EstimateSlip","CaregiverHandover","MealCost"}
# Wagi v2 — najmocniej nagradzamy REALNY KLIN: droga subskrypcja BEZ darmowej
# alternatywy. Darmowy/OSS substytut i 'pusta z przyczyny' = zabojcy.
def score(c):
    base = 35 if c["n"] > 0 else 25
    wtp  = 15 if c["model"] in ("onetime","sub","mixed","enterprise") else 0
    comp = -min(3*c["n"], 27)                  # gestosc konkurencji (lagodniej — klin bije gestosc)
    free = -28 if c["free_sub"] else 0         # silny darmowy/OSS substytut = glowny zabojca
    if c["model"] in ("sub","enterprise") and not c["free_sub"]:
        wedge = 28                              # pelny arbitraz: subskrypcja -> $5 jednorazowo
    elif c["model"] == "mixed" and not c["free_sub"]:
        wedge = 10
    else:
        wedge = 0
    b2b  = 6 if c["id"] in B2B else 0
    reason = -12 if c["verdict"] == "PUSTA Z PRZYCZYNY" else 0
    s = base+wtp+comp+free+wedge+b2b+reason+c["durability"]+c["reach"]
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
