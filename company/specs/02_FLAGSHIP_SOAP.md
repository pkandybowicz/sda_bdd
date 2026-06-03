# 02 — FLAGOWIEC MAKER: „Soap Studio” (costing + lye calc, offline one-time)

## Dlaczego mydło
Jedyny 3/3 w klastrze maker. Nikt nie łączy lye-calc + COGS + wycena offline one-time:
- **SoapCalc** = ług, ZERO kosztów/wyceny, web. **Craftybase** = $24/mc, BRAK lye-calc. **SoapMaker 3** = $99, tylko Windows.
- WTP udowodnione (SoapMaker 3 za $99 się sprzedaje). r/soapmaking ~100k, lubi narzędzia.

## Silnik #1 — saponifikacja (to czego arkusz nie robi wygodnie)
Dla receptury olejów {olej_i: masa_i}:
- NaOH_i = masa_i × SAP_NaOH(olej_i)   (baza SAP ~60 olejów; KOH dla mydła miękkiego)
- NaOH_total = Σ NaOH_i
- **Superfat/lye discount**: NaOH_aktualny = NaOH_total × (1 − superfat%)   (typ. 5–8%)
- Woda = NaOH_aktualny × (water:lye ratio)  LUB % wagi olejów (przełącznik)
- Walidacje/ostrzeżenia: lye safety, max % oleju (np. olej kokosowy), twardość/INS (v2).
- **Batch scaler**: skala do docelowej masy / liczby kostek / rozmiaru formy.

## Silnik #2 — COGS + wycena + prowizje
- koszt surowca/g (oleje, ług, FO/EO, barwniki) → koszt batcha → **koszt/kostkę** (batch yield).
- + packaging + etykieta.
- Wycena: koszt × narzut LUB cena docelowa → marża; **prowizje user-editable** (Etsy 6.5% + $0.20 + ~3% payment) → zysk netto/kostkę.

## Silnik #3 — inwentarz + cure log
- Inwentarz surowców (odejmowanie per batch; loty v2).
- Cure log: data wylania → gotowość (np. 4–6 tyg.), przypomnienie.

## Ekrany (MVP)
Recepturka (oleje+%) → Wynik ług/woda + safety → Skalowanie batcha → Costing → Wycena+prowizje → (Cure log, Inwentarz v1).

## Cena i pozycjonowanie
$8–12 one-time. Hasło: „SoapCalc + costing + wycena Etsy, offline, raz zapłać”.
Fast-follow pakiety (ten sam silnik COGS): świece (fragrance load %), świece+wosk, potem skóra/ceramika.

## Ryzyka
- Spreadsheet-satisficing → przewaga = lye-calc + prowizje + offline w JEDNYM; demo „policz zysk/kostkę w 30s”.
- Heterogeniczność (CP vs HP vs MP) → MVP = cold process; reszta presety v2.
