# Iteracja 1 — FUNNEL (manager): ~155 → shortlist 12

> Krytyczny lens managera: self-scores są zawyżone, a generatory miały
> ograniczony dostęp do sieci. Funnel premiuje: (a) twardy dowód gotowości
> płacenia, (b) realną durability (bez API/treści, które gniją), (c) obronność,
> (d) **konwergencję** (pomysł wykopany niezależnie przez kilka metod = silniejszy sygnał).

## Klastry konwergencji (meta-sygnał)
- **🩺 Dziennik objawów → wydruk dla specjalisty** (NAJSILNIEJSZY, 5+ trafień): FODMAPLog, MigraineMap, PostureLog, GlucoLog, AllergyDiary. Wzorzec: lekarz prosi o dziennik, pacjent płaci, logika stabilna, offline = prywatność danych zdrowotnych.
- **👵 Offline narzędzia dla seniorów/opiekunów:** GlucoLog, CaretakerHandover, BigButtonPhoneBook, MedicationBlistersLog.
- **🧒 Single-purpose drille edukacyjne (+ raport dla nauczyciela):** SpellDrill, PhonicsFirst, MultiDrill, FractionFighter.
- **⚖️ Kalkulatory wydarzeń życiowych:** HeirSplit, DivorceAssets.
- **💇 Narzędzia salonowe (tabele referencyjne):** DyeRatio, HairColorRecord, NailCure.
- **📋 Compliance małych firm:** FoodTemp (HACCP), MileageLog, ContinuingEdTracker, ChemLabel.

## Dedup (te same pomysły z różnych generatorów)
- MileageLog (Pixel M8-01) = MileageLogPro (Echo #011) → 1 pozycja.
- BrewCalc/BrewLogOffline/FermentLog → klaster fermentacji, 1 reprezentant.
- Medication logi (Echo MedicationBlistersLog ≈ Vera GlucoLog) → rozdzielone (różne schorzenia), ale ten sam wzorzec.

## SHORTLIST 12 → do 10-krotnej weryfikacji konkurencji

| # | Kandydat | Co robi | Klaster | self | Czemu w shortliście |
|---|----------|---------|---------|:----:|---------------------|
| 1 | **FODMAPLog** | Dziennik FODMAP + objawy IBS, offline | 🩺 | 50 | Monash $7.99+sub = twarda WTP; protokół medyczny rekomendowany |
| 2 | **MigraineMap** | Dziennik migreny → PDF dla neurologa | 🩺 | 48 | 3. choroba świata; neurolog prosi o dziennik |
| 3 | **PostureLog** | Dziennik bólu kręgosłupa → PDF dla fizjo | 🩺 | 50 | 540M LBP; brak dedykowanego offline gracza |
| 4 | **GlucoLog Desktop** | Log cukru krwi dla seniorów → PDF lekarz | 🩺👵 | 50 | Seniorzy wolą desktop; zamożna, pomijana grupa |
| 5 | **HeirSplit** | Kalkulator podziału spadku, offline | ⚖️ | 45 | Matematyka wieczna; segment offline pusty; ból max |
| 6 | **DivorceAssets** | Podział majątku, multi-scenario, offline | ⚖️ | 44 | „$5 za prywatność" w mediacji; bundle z HeirSplit |
| 7 | **DyeRatio** | Tabela proporcji farb do włosów + kalkulator | 💇 | 44 | 1M+ salonów EU; tabela statyczna = zero utrzymania |
| 8 | **DosePaw** | Tabela dawkowania leków OTC dla psów/kotów | 🐾 | 42 | Krytyczny ból „o 2 w nocy"; emocja = płaci |
| 9 | **PhonicsFirst** | Ćwiczenia fonetyczne dla dzieci z dysleksją | 🧒 | 50 | 15-20% dzieci; rodzice płacą; alternatywy = sub |
| 10 | **SpellDrill** | Dyktando z własnej listy + TTS + raport | 🧒 | 50 | Konkretny ból rodzica; TTS systemowy = build-once |
| 11 | **PrivatePeriod** | Tracker cyklu offline na desktop | 🔒 | 50 | Mobile zasycony, desktop pusty; kontekst prywatności |
| 12 | **FoodTemp** | Ewidencja temperatur HACCP → raport | 📋 | 42 | Najsilniejsza obronność (lokalny compliance = bariera) |

## ⚠️ Ryzyka do sprawdzenia w weryfikacji (manager flaguje)
- **Klaster 🩺**: istnieją DARMOWE offline apki (np. Migraine Log na F-Droid) + ryzyko odpowiedzialności medycznej. 10× weryfikacja musi to brutalnie sprawdzić.
- **HeirSplit/DivorceAssets**: prawo spadkowe/majątkowe różni się per kraj — czy „czysty kalkulator" wystarczy bez aktualizacji prawa? (durability!)
- **DyeRatio**: bazy proporcji per marka mogą się zmieniać → ryzyko durability.
- **PrivatePeriod**: algorytm predykcji to statystyka, OK — ale rynek mobilny brutalny; czy desktop ma realny popyt?
