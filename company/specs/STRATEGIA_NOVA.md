# STRATEGIA NOVA — klin regulacyjny odporny na freemium (red-team)

Autor: senior researcher (red-team). Data: 2026-06-03.
Kontekst: `PROTOKOL_ANTYWTOPA.md`, `PUSH2_PODSUMOWANIE.md`, `tools/score_v6.py`.
Cel: zastąpić fałszywe „brak konkurencji" twardą tezą o TRWAŁYM klinie =
deliverable to REKORD REGULACYJNY (compliance), oraz dać protokół, który sami
obalamy zanim zrobi to user.

---

## 0. Re-framing: „compliance" to NIE jest automatyczna odporność

Lekcja z weryfikacji (poniżej): „compliance" samo w sobie NIE chroni przed
freemium. Dowody:
- SafetyCulture i Lumiform mają DARMOWE, edytowalne szablony LOLER / fire damper /
  legionella, gotowe do druku PDF.
  ([SafetyCulture LOLER](https://safetyculture.com/library/construction/loler-inspection-sheet),
  [Lumiform LOLER](https://lumiformapp.com/templates/loler-inspection-checklist-template_33316))
- Istnieją jednorazowe „Prüfprotokoll-Software" za kilkanaście-kilkadziesiąt EUR
  na Amazon.de (DGUV Leiter/Tritte), czyli generyczny one-time już pokrywa rubrykę.
  ([Amazon.de DGUV Prüfprotokoll](https://www.amazon.de/Digitales-Pr%C3%BCfprotokoll-Pr%C3%BCfung-Leitern-Vorschrift/dp/B06XHH3YCJ))
- Część rejestrów ma OFICJALNY DARMOWY TOR rządowy — wtedy gra jest skończona.
  PL `c-KOB` (książka obiektu budowlanego) jest bezpłatna, rządowa, ma już app
  iOS/Android. To twarde NO_GAP dla „książki obiektu".
  ([c-KOB GUNB](https://www.gunb.gov.pl/strona/c-kob),
  [gov.pl](https://www.gov.pl/web/gunb/ruszyla-cyfrowa-ksiazka-obiektu-budowlanego-c-kob))

Wniosek: TRWAŁY klin to nie „jest norma", lecz przecięcie WSZYSTKICH warunków:
1. deliverable = obowiązkowy rekord, którego BRAK/BŁĄD = kara lub utrata uprawnień;
2. norma KRAJOWA, ucieleśniona w treści (preładowane pola/limity) — bariera wiedzy;
3. inspekcja RZADKA (rocznie/2-3 lata) → SaaS-abonament jest dla solo absurdem;
4. BRAK darmowego oficjalnego toru i BRAK dobrego darmowego szablonu w PL/lokalnym
   języku (szablony SafetyCulture są EN i generyczne);
5. dane WRAŻLIWE / klient chce OFFLINE (RODO, brak chmury inspektora w obiekcie).

Punkt 4 i 5 to faktyczne źródło przewagi, a nie samo „compliance". Niżej kategorie
ważymy właśnie tym przecięciem.

---

## 1. KATEGORIE odporne na freemium (z uzasadnieniem)

Cecha wspólna: deliverable to dokument dla TRZECIEJ STRONY (inspektor, ubezpieczyciel,
sąd, urząd), a nie dla samego usera. To zabija mechanikę „freemium w weekend": kalkulator
można skopiować, ale formularz zgodny z normą + retencja + ślad audytowy + odpowiedzialność
za format to praca, którą hobbysta-dev nie podejmie, bo nie zna normy i ryzyka.

Typy odporne (rdzeń):
- **Inspekcja okresowa rzadka, obowiązkowa, z osobistą odpowiedzialnością „competent person"**
  (raz/rok lub rzadziej) — abonament to dla jednoosobowego inspektora czysty koszt.
- **Rejestr „na żądanie organu"** — musi istnieć w określonym formacie i być wydany
  na kontroli; błąd = mandat. Retencja 5 lat (typowa w UK/DE H&S).
- **Certyfikat wystawiany klientowi** z numerem i podpisem (deliverable opuszcza firmę).

Typy WYKLUCZone z definicji „odporne" (mimo że brzmią jak compliance):
- cokolwiek z oficjalnym darmowym torem rządowym (c-KOB, MCS-portale, Benchmark);
- cokolwiek, gdzie generyczny one-time „Maker Pro / Prüfprotokoll-Software" już pokrywa;
- log, którego jedynym odbiorcą jest sam user (to tylko tracker → freemium-bait).

### 6–8 konkretnych podkategorii do dalszej DEEP-VERIFY

Każdą traktuj jako HIPOTEZĘ do przepuszczenia przez protokół red-team z §2.
Status to wstępna ocena z dzisiejszej weryfikacji, nie werdykt końcowy.

1. **DE — Regalprüfung (DIN EN 15635 / DGUV 208-061), protokół rzadkiej rocznej
   inspekcji regałów magazynowych przez „Regalprüfer".**
   Dlaczego odporne: kwalifikowany rzeczoznawca, roczny cykl, protokół + klasyfikacja
   uszkodzeń (zielony/żółty/czerwony), krajowa norma DE. Nisza węższa niż „Leiter".
   Ryzyko: istnieją apps (Hoppe, kevox); trzeba sprawdzić czy obsługują SOLO-rzeczoznawcę
   one-time, czy tylko duże magazyny w abonamencie.
   Źródła: [Lagertechnik Regalprüfung](https://www.lagertechnik.de/regalpruefung/),
   [DGUV 208-016 PDF](https://www.dguv.de/medien/fb-handelundlogistik/pdf-dokumente/dguv-info-208-016.pdf).
   Status: CANDIDATE (wymaga sprawdzenia solo/one-time).

2. **UK — anchor point / eyebolt re-test certificate (BS EN 795 + BS 7883, PUWER),
   roczny (lub 6-mies.) certyfikat punktów kotwiących dachowych.**
   Dlaczego odporne: prawny obowiązek 12-mies. re-testu, certyfikat per-eyebolt z
   pull-testem, deliverable dla zarządcy budynku, niszowy zawód (firmy work-at-height).
   Ryzyko: usługodawcy mają własne „digital compliance reports"; sprawdzić czy są to
   wewnętrzne narzędzia czy produkt do kupienia, oraz darmowe szablony.
   Źródła: [Velocity Safety EN795/BS7883](https://velocitysafety.co.uk/services/fall-arrest-anchor-installation-testing/),
   [ALTUS eyebolt testing](https://www.altussafety.com/eyebolt-and-anchor-point-compliance-testing/).
   Status: CANDIDATE.

3. **UK — fire & smoke damper inspection record (NFPA 80 19.4.9 / NFPA 105 / BS 9999),
   cykl 1 rok po montażu → 4 lata (6 lat szpitale).**
   Dlaczego odporne: AHJ-ready record per damper (asset ID, kwalifikacja technika,
   pass/fail, deficiency), retencja 3 cykli. Bardzo niszowi technicy life-safety.
   Ryzyko: OxMaint/eAuditor/Safenetix obsługują temat; sprawdzić segment solo/offline.
   Źródła: [Safenetix NFPA 80](https://www.safenetix.com/2024/02/29/breaking-down-nfpa80-fire-smoke-damper-inspections/),
   [LSS cert required](https://info.lifesafetyservices.com/fire-damper-inspection-certification-required).
   Status: CANDIDATE.

4. **UK — landlord legionella risk assessment + miesięczny log temperatur (ACoP L8 /
   HSG274), samodzielnie wykonywany przez małego wynajmującego.**
   Dlaczego odporne: prawny obowiązek duty-holder, retencja 5 lat, log temperatur z
   datą/lokalizacją/odczytem; deliverable bywa żądany przez agencję/ubezpieczyciela.
   Ryzyko WYSOKIE: jest już „self-service app dla prywatnych landlordów" + szablony
   SafetyCulture. Prawdopodobnie CONTESTED/NO_GAP — wpisuję jako test ostrości protokołu.
   Źródła: [AnyInspect landlord guide](https://anyinspect.ai/en-US/blog/legionella-risk-assessment-landlord-guide),
   [SafetyCulture templates](https://safetyculture.com/checklists/legionella-risk-assessments).
   Status: AT-RISK (kandydat na NO_GAP — dobry test kryteriów §3).

5. **UK — F-gas logbook dla jednoosobowego inżyniera chłodnictwa (EU/GB F-Gas Reg,
   leak-check log per instalacja >5 t CO2e, retencja 5 lat).**
   Dlaczego potencjalnie odporne: prawny rekord per-asset, ślad ilości czynnika,
   cert inżyniera. Ryzyko: REFCOM/Joglogic dają DARMOWY moduł członkom REFCOM →
   to jest „oficjalny darmowy-ish tor" zabijający WTP. Prawdopodobnie NO_GAP w UK.
   Źródła: [Joblogic REFCOM free](https://www.joblogic.com/refcom/),
   [Field Ascend (offline)](https://field-ascend.com/f-gas-compliance-software).
   Status: AT-RISK (UK NO_GAP-em; ewentualnie inne geo bez darmowego toru).

6. **DE — Pflanzenschutz Gerätekontrolle (Spritzen-TÜV), 3-letni obowiązkowy przegląd
   opryskiwaczy + rejestr stosowania ŚOR (Aufzeichnungspflicht).**
   Dlaczego odporne: 3-letni cykl (anty-abonament), rejestr stosowania ŚOR wymagany
   ustawowo per zabieg, dane gospodarstwa, krajowy reżim DE, język DE. Dwa deliverable:
   protokół kontroli urządzenia + dziennik zabiegów na żądanie kontroli.
   Ryzyko: rynek rolny ma duże FMS (365FarmNet itp.) — sprawdzić segment małego
   gospodarstwa/usługodawcy oprysków solo, offline w polu.
   Źródła: [LWK NRW Gerätekontrolle](https://www.landwirtschaftskammer.de/landwirtschaft/pflanzenschutz/technik/geraetekontrolle.htm),
   [LfL Sachkunde](https://www.lfl.bayern.de/ips/recht/054922/).
   Status: CANDIDATE (silny, jeśli small-farm/offline niezaspokojony).

7. **PL — protokół okresowej kontroli przewodów kominowych/wentylacyjnych (rzadki
   1-roczny, uprawnienia mistrza kominiarskiego) — bez oficjalnego darmowego toru.**
   Dlaczego odporne: ustawowy obowiązek, protokół z numerem dla właściciela, uprawnienia
   zawodowe, język PL i polski wzór. Uwaga: c-KOB obejmuje WPIS do książki, ale NIE
   produkuje protokołu kontroli — to nadal robi kominiarz. Klin = generator protokołu PL
   offline dla solo-kominiarza, nie konkurencja dla c-KOB.
   Ryzyko: sprawdzić desktopowe programy kominiarskie i czy są tanie/darmowe.
   Źródło kontekstowe: [c-KOB GUNB](https://www.gunb.gov.pl/strona/c-kob) (potwierdza, że
   c-KOB to rejestr, nie generator protokołu).
   Status: CANDIDATE (wymaga sprawdzenia istniejących programów kominiarskich PL).

8. **DE/UK — tachograph / wzorcowanie w warsztacie ATC: wewnętrzny protokół czynności
   kalibracyjnych (deliverable dla DVSA/organu) dla małego Approved Tachograph Centre.**
   Dlaczego odporne: tylko ATC może kalibrować, mechanik wystawia protokół wyników,
   silny reżim, mały rynek licencjonowanych warsztatów.
   Ryzyko WYSOKIE: producenci (Stoneridge) i sieci mają własne narzędzia; rynek BARDZO
   mały (liczebność ATC) → możliwe odrzucenie na progu rynku §3.
   Źródła: [Stoneridge DSRC Tester](https://stoneridge-tachographs.com/en/products/dsrc-tester),
   [GEA DVSA tacho](https://gea.co.uk/dvsa-tachograph/).
   Status: AT-RISK (próg rynku — patrz §3).

Priorytet do DEEP-VERIFY: #6 (DE Spritzen-TÜV), #1 (Regalprüfung), #2 (anchor EN795),
#7 (PL kominiarz). #4/#5/#8 trzymamy jako testy ostrości protokołu (spodziewane NO_GAP).

---

## 2. PROTOKÓŁ RED-TEAM — checklista „obal w 1 minutę"

Stosować do KAŻDEJ ocalałej niszy PRZED wpisaniem REAL_GAP. Cel: znaleźć konkurenta
lub darmowy tor szybciej, niż zrobi to user. Zapisuj URL + cenę + model dla każdego trafienia.
Podstawiamy `<x>` = nazwa niszy w EN i w języku kraju (PL/DE), bo darmowe szablony bywają tylko EN.

A. Sklepy z aplikacjami (intencja: gotowy produkt mobilny):
- `site:apps.apple.com <x> inspection` / `site:apps.apple.com <x> certificate`
- `site:play.google.com <x> inspection log`
- App Store / Google Play search bezpośrednio: `<x>`, `<x> report`, `<x> protokoll`

B. Darmowy / freemium (intencja: zabójca WTP):
- `free <x> app`
- `free <x> template` oraz `<x> template pdf` (łapie SafetyCulture/Lumiform/GoCanvas)
- `<x> safetyculture` / `<x> lumiform` / `<x> jotform` (czołowi dostawcy darmowych szablonów)

C. Generyczny one-time (intencja: „Craft Maker Pro" danego pionu):
- `<x> software one-time purchase` / `<x> software lifetime licence`
- `<x> Prüfprotokoll Software` / `<x> Software kaufen` (DE — łapie tanie one-time)
- Amazon/Gumroad/Etsy: `<x> spreadsheet etsy`, `<x> excel template`, `<x> logbook amazon`

D. Oficjalny darmowy tor (intencja: gra skończona):
- `<x> official government app` / `<x> gov.uk` / `<x> gunb gov pl` / `<x> bund.de`
- `<x> scheme portal` (UK: MCS, Benchmark, Gas Safe, REFCOM, NICEIC) —
  jeśli scheme daje darmowe narzędzie członkom → NO_GAP.

E. Popyt + głos rynku (intencja: czy ktoś tego chce i na czym dziś jeżdżą):
- `<x> app reddit` / `<x> software reddit`
- `<x> spreadsheet` (jeśli wszyscy jadą na arkuszu = popyt + brak produktu)
- forum branżowe kraju: PL (elektroda, forum kominiarskie), DE (Landwirt.com), UK (trade forums)

F. Incumbent SaaS / poziomy gigant (intencja: czy solo już obsłużony tanio):
- `<x> software pricing` (sprawdź czy jest plan dla 1 osoby i jego cena/mc)
- czy ofertę pokrywa: Jobber / Housecall / ServiceTitan / SafetyCulture / GoCanvas /
  Joblogic (lista z `score_v6.py: HORIZ_GIANT`).

Reguła czasu: jeśli w pierwszych ~5 trafieniach A–D znajdziesz dobry darmowy/one-time
produkt LUB oficjalny tor → STOP, werdykt NO_GAP. Nie szukaj uzasadnień, że „to nie to samo".

---

## 3. KRYTERIA ODRZUCENIA → NO_GAP

Wpisz NO_GAP (lub CONTESTED, jeśli częściowo), gdy zachodzi DOWOLNE:

1. **Dobra darmowa/freemium appka** obsługująca solo (darmowy plan użyteczny bez płacenia),
   np. self-service legionella app dla landlordów.
2. **Tani generyk one-time** pokrywa deliverable: „Craft Maker Pro"-typ lub DE
   „Prüfprotokoll-Software" za <~€30 jednorazowo na Amazon/Gumroad.
3. **Oficjalny darmowy tor**: rządowy (c-KOB) lub schemowy (REFCOM/Joblogic free, MCS,
   Benchmark) wystawiający/przechowujący ten sam rekord.
4. **Dobre darmowe szablony** SafetyCulture / Lumiform / GoCanvas / JotForm pokrywające
   formularz W JĘZYKU rynku (jeśli tylko EN-generic, a nisza wymaga PL/DE-specyfiki —
   to NIE dyskwalifikuje, ale obniża wedge).
5. **Poziomy gigant FSM** ma plan solo w rozsądnej cenie (`HORIZ_GIANT`) — solo obsłużone.
6. **Próg rynku**: realna liczba płacących < ~3 000 podmiotów w dostępnym geo
   (np. mała liczba ATC tachografów) → za mały, by utrzymać produkt one-time, ODRZUĆ
   chyba że cena jednostkowa wysoka (>€100) i konwersja wiarygodna.
7. **Deliverable tylko dla usera** (czysty self-log bez odbiorcy zewnętrznego) → to nie
   compliance-klin, to tracker → traktuj jak hobby-kalkulator (freemium-bait).
8. **Brak dowodu przymusu**: nie ma jasnej kary/utraty uprawnień za brak rekordu → THIN.

Werdykt REAL_GAP tylko gdy: żadne z 1–8 NIE zachodzi, A protokół §2 nie znalazł killera,
A spełnione co najmniej 4 z 5 warunków przecięcia z §0.

---

## 4. Scoring v6 → v7 — propozycje (wzory/wagi)

Cel: ukarać „łatwo-freemium-izowalne", nagrodzić „regulacyjny deliverable z odbiorcą
zewnętrznym + krajową normą + rzadkim cyklem + brakiem darmowego toru". Nie psujemy
istniejących osi; dodajemy oś REG i twarde gate'y.

### v7.1 — Nowa oś REG_MOAT (waga ~0.20, kosztem wedge 0.22→0.16, scale 0.20→0.18)

Sygnały do oznaczania nisz (pola wejściowe lub keyword-detekcja):
```
mandatory_record  : deliverable obowiązkowy prawnie (kara/utrata uprawnień)   +1.0
external_recipient: rekord trafia do inspektora/urzędu/ubezpieczyciela/sądu   +0.8
national_norm     : norma krajowa ucieleśniona w treści (PL/DE-specyfika)     +0.7
rare_cycle        : inspekcja co >=12 mies. (anty-abonament)                  +0.6
penalty_known     : udokumentowana kara/sankcja                              +0.4
REG_MOAT = clamp(suma, 0, 3)
```
Uzasadnienie: to mierzy DOKŁADNIE to, czego freemium-hobbysta nie zrobi (norma + ryzyko
+ format dla trzeciej strony), a nie „czy jest kalkulator".

### v7.2 — Twardy mnożnik FREEMIUM_KILL (gate, nie miękka kara)

```
free_official_track : istnieje rządowy/schemowy darmowy tor (c-KOB/REFCOM-free) -> KILL
good_free_app       : użyteczny darmowy plan obsługuje solo                      -> KILL
cheap_onetime_generic: generyk one-time <~€30 pokrywa deliverable               -> *0.55
free_template_local : darmowy szablon SC/Lumiform W JĘZYKU rynku                 -> *0.7
free_template_en_only: tylko EN-generic, nisza wymaga PL/DE                      -> *0.9 (lekko)
```
KILL = ustaw v7 = min(v7, 35) i flaga `verdict_hint=NO_GAP`. To formalizuje §3.1/§3.3:
darmowy oficjalny tor lub dobra darmowa appka WYRZUCA z topu niezależnie od reszty.
Rozszerz `SATURATED_FREE` o pozycje potwierdzone (np. „książka obiektu / c-kob").

### v7.3 — TRACKER_PENALTY (kara za czysty self-log bez odbiorcy)

```
if mandatory_record == 0 and external_recipient == 0
   and family in {fieldlog}:           v7 -= 12
```
Uzasadnienie: dziś `fieldlog` dostaje punkty za „compliance" keyword nawet gdy to tylko
prywatny dziennik. To karze freemium-bait („log dla siebie") i odróżnia go od
prawdziwego rejestru ustawowego (§3.7).

### v7.4 — Korekta osi demand (spójność z protokołem)

- Utrzymać `model=free -> +0.0` (już w v6, dobre).
- Dodać: `if free_official_track: demand -= 1.0` — istnienie darmowego rządowego toru to
  NIE dowód WTP, to dowód braku WTP (rząd już daje za darmo).

### Sugerowana nowa formuła łączna v7
```
raw = 0.22*demand + 0.16*wedge + 0.18*scale + 0.09*addr + 0.11*build
      + 0.10*fact + 0.14*reg_moat
v7  = 100*raw/3 + min(dur,10)*0.5
v7 *= FREEMIUM_MULT          # 0.55 / 0.7 / 0.9 wg v7.2
v7  = min(v7, 35) if FREEMIUM_KILL else v7
v7 -= 12 if TRACKER_PENALTY
v7 -= 18 if lowconf
```
Walidacja regresją: po wdrożeniu sprawdź, że c-KOB-nisze, legionella-landlord i
F-gas-UK SPADAJĄ z topu (powinny — mają darmowy tor/appkę), a Spritzen-TÜV /
Regalprüfung / anchor-EN795 ROSNĄ (mają REG_MOAT bez darmowego toru). Jeśli nie —
sygnały REG źle oznaczone.

---

## 5. Definicja DONE dla tej fazy
- Każda z 8 podkategorii przepuszczona przez checklistę §2 (A–F), z URL/ceną/modelem.
- Werdykt per nisza wg §3 (REAL_GAP / CONTESTED / THIN / NO_GAP) z killer_risk.
- v7 zaimplementowany i przeszedł walidację regresją z §4 (znane NO_GAP spadają,
  znane CANDIDATE rosną).
- Brak ani jednego „brak konkurencji" bez logu szukania (zasada z PROTOKOL_ANTYWTOPA).
