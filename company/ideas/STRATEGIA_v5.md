# 🏭 Strategia v5 — soczewka komercyjna „tysiące, nie miliony"

## Zmiana paradygmatu (czemu v4 gubił złoto)
v4 pytał „czy arkusz wystarcza?" → kasował zwalidowany popyt. v5 pyta o **EV = cena × osiągalni kupujący × konwersja − koszt budowy**.
Nowe osie: demand_proof (konkurenci = DOWÓD), wedge_strength, addressability (jedna społeczność = złoto), build_cheapness, factory_fit.
Odwrócone dogmaty: (1) subskrypcyjny konkurent = dowód WTP, nie wyrok; (2) free_sub mniej ważny niż POWÓD niewystarczalności.

## 5 dróg
- A — Silnik zamiast loggera (obliczenie/decyzja/generacja, której arkusz nie zrobi). 155 nisz.
- B — Fabryka: 1 silnik + N reskinów (64 kolekcje, 77 trackerów, 216 kalkulatorów wspólnego kształtu).
- C — Pobić subskrypcję, nie pustkę (344 nisze z sub/freemium = popyt udowodniony).
- D — Krzyżowanie par (luka-bez-apki + silnik z sąsiedztwa).
- E — Produktem jest WIEDZA (załadowana baza/szablony, nie pusty logger).

## Flagowa hipoteza: „Maker Costing Studio"
Offline, one-time $8–15. Silnik: COGS + wycena (z prowizjami Etsy + marża) + receptura/batch + prosty inwentarz.
Reskin per rzemiosło: świece (fragrance load %), mydło (lye/superfat), żywica (objętość × ratio), skóra (yield), biżuteria, ceramika (szkliwo/wypał), wypieki (baker's %).
- Incumbent: Craftybase ($24–79/mc!), Vish, darmowe-ale-brzydkie pojedyncze web-calc.
- Popyt: Etsy ~9M sprzedawców; r/candlemaking ~200k; subskrypcje = dowód WTP.
- Adresowalność: subreddity rzemiosł, grupy FB Etsy-sellers, YouTube — tanio i skupione.
- Fabryka: 1 silnik → 8–10 skinów. „Tysiące": 8 × 500 szt. × $8 ≈ $32k.

## Status: weryfikacja klina (3 agenci product-analyst) w toku.

## WYNIKI 3 KLASTRÓW (zweryfikowane on-the-nose)

### Meta-odkrycie: jedna ARCHITEKTURA, trzy rynki
Wszystkie 3 klastry mają identyczny szkielet: **wspólny silnik/shell offline + pakiety (calc/treść) jako moduły**. To nie 3 pomysły — to jeden **model fabryki**, gdzie SKU #k kosztuje ~5% pierwszego. To jest właściwe „złoto".

### Klaster 1 — Maker Costing Studio (konsument/mikrobiz)
- Zwycięzca: **MYDŁO (cold process) 3/3**. SoapCalc=ług bez COGS; Craftybase $24/mc bez lye-calc; SoapMaker 3 = $99 i tylko Windows. Nikt nie łączy lye+COGS+wycena offline one-time. WTP dowiedzione ($99 konkurent się sprzedaje). r/soapmaking ~100k.
- Dalej: świece / skóra (r/leathercraft 864k) / wypieki / ceramika (remis 18/27).
- Cena $8–15. Ryzyko: spreadsheet-satisficing (hobbysta godzi się na arkusz).

### Klaster 2 — Hobby Log+Kalkulator (mashupy, Droga D)
- 3/3: **MycoLog** (uprawa grzybów, r/MushroomGrowers 200k+, ZERO narzędzi, calc C:N substratu), **KvasLog** (fermentacja, r/fermentation 440k, pustka), **SmokeLog** (peklowanie equilibrium %, r/meatcuring), **FrameChem** (foto analog reciprocity, r/analog 350k).
- Cena $5–10. Najniższa konkurencja, najbardziej zaangażowane społeczności. Ryzyko: wrażliwość cenowa hobbystów.

### Klaster 3 — Trade Inspection Logbook (B2B solo)
- 3/3: **Technik gaśnic NFPA 10** (lider Inspect Point CELOWO pomija solo!), **HVAC/F-gazy EPA 608** (federalnie OBOWIĄZKOWY logbook; RefriComply $29/mc), **Kominiarz NFPA 211**, **Backflow ASSE 5110**.
- Cena $15–25, B2B, często odliczalne od podatku, popyt OBOWIĄZKOWY (nie „nice-to-have").
- Model: „Inspection Shell" $0/$5 + pakiety norm $15 (Content-DLC). Twarda granica: zero schedulingu/faktur.

## MACIERZ DECYZYJNA (soczewka „tysiące")
| Kryterium | Trade (Fire/HVAC) | Maker (Soap) | Hobby (Myco) |
|---|---|---|---|
| Pewność popytu | ★★★ obowiązkowy | ★★ ($99 konkurent) | ★ nice-to-have |
| Cena/WTP | $15–25 B2B | $8–15 | $5–10 |
| Koszt dotarcia | ★★ asocjacje | ★★★ subreddity | ★★★ subreddity |
| Konkurencja | sub, ignoruje solo | trochę free | ZERO |
| Fosa/moat | norma+compliance | silnik calc | silnik calc |
| Fabryka (skala) | ★★★ pakiety norm | ★★★ pakiety rzemiosł | ★★ pakiety hobby |

**Rekomendacja kolejności:** #1 Trade (najpewniejszy realny przychód, popyt obowiązkowy) → #2 Maker/Soap (najczystszy klin konsumencki) → #3 Hobby (najtańsza walidacja, najmniej konkurencji). Każdy pierwszy SKU waliduje shell, reszta to reskiny.
