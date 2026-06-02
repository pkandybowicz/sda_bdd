# Reality-check konkurencji (REALNE dane z sieci) — Iteracja 2

> Wykonane przez managera z działającym WebSearch. To zastępuje miękkie self-score'y
> generatorów (które często nie miały sieci i twierdziły „PUSTA/luka" bezpodstawnie).
> **Wynik brutalny: 6/6 top-kandydatów = rynek ZATŁOCZONY lub pusty z przyczyny.**

## Werdykty (z nazwami konkurentów)

| Kandydat | Werdykt | Znalezieni konkurenci (z nazwy) |
|----------|---------|---------------------------------|
| **FODMAPLog** | 🔴 ZATŁOCZONA | **IBS Tracker: FODMAP Food Guide** (offline, jednorazowy, eksport PDF dla lekarza, bez konta — *1:1 nasz pomysł*), Cara Care, myIBS, Monash FODMAP, „Low FODMAP Diet: IBS Tracker", Poop Tracker (CareClinic) |
| **MigraineMap** | 🔴 ZATŁOCZONA | **Migraine Buddy** (zaprojektowany przez neurologów, eksport raportu), **HeadApp** (tryb offline + eksport PDF — *1:1 nasz pomysł*), Migraine Diary „Brain Twin" (PDF print/share), N1-Headache, Migraine Trust diary |
| **DyeRatio / HairColorRecord** | 🔴 ZATŁOCZONA | **Charm** (palety Wella/L'Oréal/Schwarzkopf/Matrix/Redken — *dokładnie nasza tabela proporcji*), **Gloss**, HairTracker, Salon Formulator, Vish, SalonScale |
| **FoodTemp (HACCP)** | 🔴 ZATŁOCZONA | **Inspectly360** (offline-first), Food Safe System, Hubl, Xenia, **Temperature Log Book** (App Store), Clever Logger |
| **HiveLog (pszczelarstwo)** | 🔴 ZATŁOCZONA | **HiveBook** (offline + prywatne), HiveLogger/Hive Trackr, Apiary Book (offline), ApiManager, Beentry, BeePlus, HiveTracks, APiLOG — *nawet wąskie hobby ma 8+ apek* |
| **HeirSplit** | 🟠 PUSTA Z PRZYCZYNY | Darmowe web-kalkulatory bez logowania: Toolsparx, CalculatorSpot — popyt obsłużony za darmo, niska gotowość płacić $5 |

Źródła: linki w wyszukiwaniach (play.google.com, apps.apple.com, monashfodmap.com,
migraine app store listings, glossapp.club, hairtracker.app, inspectly360.com,
hivebook.app, toolsparx.com — pełne URL-e w logu sesji).

## Dlaczego self-score'y kłamały
Generatorzy w Fazie A często mieli `tool_uses=0` (brak sieci) → „luka/PUSTA" było
zgadywaniem z pamięci modelu. Nasz własny dowód: każdy „differentiator" (offline +
PDF dla lekarza + jednorazowo + bez konta) **już istnieje** wielokrotnie. To są
*table stakes*, nie przewaga.

## Strategiczny wniosek (najważniejszy efekt)
„Aplikacja, której nie ma, a jest popyt" w przestrzeni konsumenckiej to **w 95% mit**.
App store'y są nasycone nawet w mikroniszach. Wniosek dla decydenta:

1. **Przestań szukać pustej niszy.** Wygrana NIE jest z nowości pomysłu.
2. **Wygrana = ostry klin w niszę, która JUŻ płaci:** przewaga na (a) cenie
   ($5 jednorazowo vs subskrypcje konkurentów), (b) bardzo wąskim pod-segmencie
   (np. konkretny kraj/język/regulacja), (c) dystrybucji (kanał, nie pomysł).
3. To domyka się z lekcją z Briefu #001 (DiffLens = arbitraż ceny vs subskrypcja),
   tyle że teraz **udowodnioną danymi**, nie zgadywaną.

## Co dalej (Iteracja 3, poprawiony cel)
Zmieniamy pytanie z „co nie istnieje?" na **„gdzie istnieje płacący rynek z drogimi
subskrypcjami i fragmentaryczną, słabą konkurencją, którą da się pobić ceną $5 +
węższym targetem?"** — i każdego kandydata od razu prześwietlamy 10 metodami PRZED
scoringiem, nie po.
