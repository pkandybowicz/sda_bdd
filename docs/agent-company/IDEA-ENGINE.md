# IDEA ENGINE — silnik firmy do generowania pomysłów

> Cała firma skupiona na jednym: znaleźć pomysł na aplikację „zrób raz / 5 $ /
> 1000 szt./rok". Nie pojedynczy strzał — **maszyna**: wiele metod × wiele źródeł
> × 10-krotna weryfikacja konkurencji × pętla, która doskonali się z każdą iteracją.
> „10000 pomysłów" traktujemy jako kierunek skali, nie dosłownie — operujemy na
> maksymalnej praktycznej skali przy zachowaniu jakości.

---

## 20 METOD GENERACJI (lensy)

Każdy generator stosuje przydzielone metody i produkuje hurtowo kandydatów.

1. **Wish-mining** — explicite „I wish there was an app that…".
2. **Hate-mining** — recenzje 1★/2★: czego ludzie nienawidzą → luka.
3. **Spreadsheet/paper replacement** — ręczne arkusze/kartki do powtarzalnego zadania.
4. **Niche tribe pains** — bóle hobby/rzemiosła poza IT.
5. **Subscription-rage** — drogie subskrypcje → tani odpowiednik jednorazowy.
6. **CLI/pro-tool → consumer GUI** — potężne narzędzie eksperckie bez ludzkiego UI.
7. **Life-event one-offs** — ślub, przeprowadzka, spadek, opieka nad seniorem.
8. **Compliance/forced tasks** — obowiązkowe zadania małych firm/zawodów.
9. **Calculation permanence** — czysta matematyka/konwersja (logika nigdy nie gnije).
10. **Reference-table apps** — deterministyczny lookup (tabele, normy, dawkowanie).
11. **Boring-but-mandatory** — nudne, ale konieczne czynności zawodowe.
12. **Analog ritual digitization** — kolekcjonerzy, dzienniki, liczniki.
13. **Cross-domain transplant** — narzędzie z domeny A przeniesione do B.
14. **Accessibility/seniors** — grupy niedoobsługiwane przez software.
15. **Hyperlocal/cultural** — potrzeby specyficzne kulturowo/regionalnie.
16. **Anti-AI / privacy** — to, co ludzie chcą BEZ chmury i bez AI.
17. **Kids/education single-purpose** — jedno konkretne narzędzie do nauki.
18. **Niche health/fitness trackers** — offline, wąska grupa.
19. **Gift/occasion generators** — deterministyczne generatory na okazje.
20. **Recurring-decision simplifiers** — upraszczacze powtarzalnych decyzji.

## 30 ŹRÓDEŁ (gdzie kopać)

Reddit (wiele subów) · Hacker News · Quora · sieć Stack Exchange · recenzje 1★
App Store · 1★ Google Play · Trustpilot · G2 · Capterra · Product Hunt (komentarze)
· IndieHackers · Etsy (popyt na szablony cyfrowe) · Gumroad (co się sprzedaje) ·
udostępniane Google Sheets · YouTube („how I track X") · TikTok · grupy Facebook ·
Discordy społeczności · fora hobbystyczne (per nisza) · recenzje Amazon · serwisy
skarg · gripes na X/Twitter · Google autocomplete + „people also ask" · Google
Trends · narzędzia słów kluczowych · Pinterest · branżowe magazyny · wiki subredditów
· blogi „there should be an app" · marketplace'y hobbystyczne.

## GENERACJA v2 — generator kombinatoryczny (skala 15k+)

LLM proszony o „15000 pomysłów" produkuje powtórki i śmieci. Zamiast tego skala
powstaje **systematycznie**: `company/tools/generate_corpus.py` mnoży
**~160 nisz × ~100 typów narzędzi = ~16 300 kombinacji**, odfiltrowuje te bez sensu
(typ narzędzia musi pasować do niszy) → **~10 000 sensownych**, i scoruje każdą
heurystyką (spend+recurring+techAverse+size niszy + durability×2+simplicity+pain
narzędzia). To **wyczerpujące pokrycie przestrzeni**, nie zgadywanka.

Pipeline: generator (tani, deterministyczny) → `seed-corpus.csv` (pełne 16 300) →
`AUTO-SHORTLIST.md` (top 60) → **dopiero top-slice** idzie do drogiej, ludzkiej
oceny agentów i **10-metodowej weryfikacji konkurencji**. Warstwę ręczną (~155
pomysłów generatorów z 20 metod) traktujemy jako wysokojakościowy dosiew do top-slice.

## 10-METODOWA WERYFIKACJA KONKURENCJI (v2)

Cel: **żadnego fałszywego „blue ocean".** Nie 10 ogólnych pytań, tylko **10 różnych
miejsc/sposobów szukania**, każdy z INNYM zapytaniem — bo ta sama apka kryje się pod
inną nazwą. Każda metoda MUSI zwrócić **listę realnych apek z nazwy** (albo „0 wyników").

**Google Play — 3 sposoby:**
1. **Nazwa-funkcja wprost** — np. „period tracker", „mileage log".
2. **Synonimy/use-case** — inne sformułowania tego samego: „menstrual diary", „cycle calendar offline", „no account period app".
3. **`site:play.google.com` w Google + sekcja „Similar apps"** i top kategorii — wyłapuje to, czego wyszukiwarka Play nie pokazuje.

**Apple App Store — 3 sposoby:**
4. **Nazwa-funkcja wprost** w App Store.
5. **Synonimy/use-case** (jak wyżej, inne frazy).
6. **`site:apps.apple.com` w Google + „You might also like"** / ranking kategorii.

**4 inne metody:**
7. **Desktop/OSS** — AlternativeTo.net, GitHub, F-Droid, SourceForge, Product Hunt.
8. **Google ogólnie + Reddit** — „best [X]", „[X] alternative", „is there an app for [X] reddit".
9. **Marketplace szablonów** — Etsy / Gumroad / Notion templates (czy printable/arkusz już zaspokaja potrzebę i za ile).
10. **Pricing & WTP recon** — dla 3–5 najbliżej znalezionych: cena, model (sub/jednorazowo), liczba ocen (proxy skali).

**Reguła twarda:** wynik każdej metody = wypisane nazwy znalezionych apek (lub „brak").
Jeśli łącznie wyjdzie ≥ ~8–10 apek robiących to samo → nisza **ZATŁOCZONA**, ginie,
choćby self-score był wysoki. Werdykt: PUSTA Z OKAZJI / SŁABO OBSŁUŻONA / PUSTA Z PRZYCZYNY / ZATŁOCZONA.

## RUBRYKA SCORINGU (0–5 każde; matematyka 1000 i durability ważone ×2)

| Kryterium | Co oceniamy |
|-----------|-------------|
| Ból | Jak silny/realny jest problem |
| Twardość popytu | [F] dane vs [H] hipoteza |
| Pustka z okazji | Czy luka jest produktowa, nie popytowa |
| Gotowość płacić 5 $ | Czy nie „za proste żeby płacić" |
| Build-once | Da się zbudować raz i zamknąć |
| **Durability ×2** | Czy NIE wymaga utrzymania (bez API/treści) |
| **Matematyka 1000 ×2** | Realny organiczny kanał na 1000 szt./rok |
| Obronność | Czy łatwo skopiować / czy darmowe zabije |

## PĘTLA ITERACJI (doskonali się za każdym razem)

```
Iteracja N:
  1. GENERACJA  — 4 generatory × 5 metod → duży korpus surowych pomysłów
  2. FUNNEL     — manager dedupe + scoring rubryką → shortlist
  3. KONKURENCJA— 10-krotna weryfikacja (równolegle, podział listy)
  4. RED TEAM   — Brutus próbuje zabić każdego ocalałego
  5. SYNTEZA    — Nova: ranking + rekomendacja
  6. REFINE     — co zadziałało? które metody/źródła dały zwycięzców?
                  → strojenie listy metod i banów na iterację N+1
Korpus i ranking są wersjonowane: company/ideas/ — rośnie i zaostrza się.
```

**Reguła doskonalenia:** po każdej iteracji notujemy, które *metody* i *źródła*
rodziły najmocniejszych finalistów, i w następnej rundzie dokładamy im wagi, a
metody-puste wygaszamy. Bany kategorii rosną (to, co odpadło jako „puste z
przyczyny", trafia na czarną listę, żeby nie wracało).

## ŻELAZNE BANY (rosną z każdą iteracją)
Iter. 1+: diff, regex, clipboard, color picker, rename plików, JSON/YAML, markdown,
git, terminal-GUI, oraz wszystko z Briefu #001 (DiffLens, RegexPilot, BatchLens,
ColorVault, ExifScrub, ImageBatch, FontDrop, WindowSnap Pro).

## ŻYWY TOP 10 + ALGORYTM OCENY (v1)

Firma utrzymuje **stały TOP 10** (`company/ideas/TOP10.md` + `top10.json` dla portalu).
Każdy kandydat trafia tam **dopiero po realnej weryfikacji konkurencji** (zapis w
`verified.json`). Scoring liczy `company/tools/score_top10.py`:

- base 40 (rynek istnieje = popyt udowodniony) / 20 (rynek pusty = popyt niepewny)
- +15 gdy ktoś już płaci (model onetime/sub/mixed/enterprise)
- −4 za każdego konkurenta (cap −32) — gęstość rynku
- −22 gdy istnieje silny darmowy/OSS substytut (zabójca fałszywego blue ocean)
- +18 arbitraż ceny: konkurenci na subskrypcji, brak dobrego darmowego → $5 jednorazowo wygrywa
- +durability(0-10) +reach(0-8)

**Reguła re-walidacji:** każda zmiana algorytmu = bump wersji + `score_top10.py`
przelicza CAŁĄ bazę `verified.json` od nowa → TOP 10 zawsze spójny z aktualnym algorytmem.

**Pętla 24/7:** co cykl bierze następne pozycje z `queue.json`, weryfikuje konkurencję
10 metodami, dopisuje do `verified.json`, przelicza TOP 10, commituje i wypisuje tabelę.
