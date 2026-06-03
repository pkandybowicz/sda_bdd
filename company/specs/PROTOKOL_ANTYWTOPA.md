# Protokół ANTY-WTOPA — weryfikacja-first (v7)

## Problem
Wcześniej agenci ZGADYWALI konkurencję i `free_sub`. Stąd „brak konkurencji", które user obala w minutę.
Skala (4071) była płytka. Teraz: GŁĘBIA i DOWODY zamiast wszerz.

## Żelazna zasada
ZAKAZ pisania „brak konkurencji" bez dowodu szukania. Każdy wpis MUSI wylistować co sprawdzono
(App Store, Google Play, web) i co znaleziono — z linkami i cenami. Luka = KONKRETNY powód
(„wszystko sub >$30/mc i tylko online; segment solo/offline/one-time niezaspokojony"), nie „nikt tego nie robi".

## Twarda przewaga (czego solo-dev-freemium NIE podgryzie)
Lekcja Candle Studio/Soapmaking Friend: hobby-kalkulatory są commoditizowane przez freemium w weekend.
TRWAŁY klin = deliverable to REKORD REGULACYJNY (compliance), nie „miły kalkulator":
przymus prawny + znajomość normy = bariera. Stąd przeważamy na COMPLIANCE + głębię wertykalną.

## Pipeline
1. SHORTLIST (~80) z v6, przeważona na compliance + costing-z-głębią, bez free-dominated.
2. DEEP-VERIFY (worker-pixel ×N): każdy bierze ~12 nisz, robi REALNE szukanie:
   - App Store ("site:apps.apple.com <nisza>"), Google Play, "<nisza> app/software pricing", reddit/forum (popyt).
   - zapisuje found_competitors[{name,url,price,model}], czy segment solo/offline/one-time obsłużony,
     gap_statement, demand_evidence, market_size, geo, verdict, confidence, killer_risk.
3. RED-TEAM (worker-nova, Opus): próbuje OBALIĆ każdą ocalałą lukę — szuka konkurenta,
   którego user znalazłby w minutę ("<nisza> app", "free <nisza>"). Znajdzie killer → demote.
4. SYNTEZA: ranking ocalałych, TOP 20 PDF — każdy z realnymi konkurentami+linkami, luką, popytem, rynkiem, pewnością.

## Schemat JSONL (company/ideas/verify/*.jsonl) — jeden obiekt/linia
{"niche","cluster","definition",
 "found":[{"name","url","price","model"}],
 "segment_served":true/false,        # czy solo/offline/one-time JUŻ obsłużony
 "gap":"konkretny powód luki albo 'BRAK LUKI'",
 "demand":"dowód popytu (społeczność/płatni/forum)",
 "market":"szac. rozmiar + kraje",
 "verdict":"REAL_GAP|THIN|CONTESTED|NO_GAP",
 "confidence":"H|M|L",
 "killer_risk":"co to zabija"}
