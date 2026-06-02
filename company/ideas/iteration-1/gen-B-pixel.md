# Iteracja 1 — Generacja B (Pixel, metody 6–10)

> ~40 kandydatów. Pixel miał częściowy dostęp do sieci (tool_uses=28) → część
> sygnałów [F] zweryfikowana. Sam odrzucił kilka pomysłów jako zajęty rynek.

## TOP 8 Pixel (self-score)
1. **HeirSplit** (45) — kalkulator podziału spadku (aktywa niepieniężne + wyrównania gotówkowe), offline. Matematyka wieczna, segment offline pusty.
2. **DivorceAssets** (44) — podział majątku małżeńskiego, tryb multi-scenario. „$5 za prywatność" w mediacji.
3. **DyeRatio** (44) — tabela proporcji farb do włosów (~200 marek) + kalkulator ml. 1M+ salonów EU, fryzjerka bez WiFi.
4. **DosePaw** (42) — tabela dawkowania leków OTC dla psów/kotów wg wagi + alerty toksyczności. Krytyczny ból „o 2 w nocy".
5. **FoodTemp** (42) — ewidencja temperatur HACCP (wymóg sanepidu) z eksportem raportu. Najsilniejsza obronność (lokalny compliance).
6. **MileageLog** (41) — ewidencja przejazdów do podatków, offline. ~10M freelancerów EU.
7. **SmokeWood** (40) — tabela drewna do wędzenia (gatunek→smak/temp/mięso). Hobby BBQ, bez WiFi przy wędzarni.
8. **HairColorRecord** (40) — karta koloryzacji klientki salonu (formuła/data/zdjęcie).

## Pełna lista (skrót)
- **CLI→GUI:** SmokeScheduler(39), LUFSdrop(normalizacja głośności audio,39), ChronoTiler(31), PDFstamp(36), WireframePrint(22✗), CropForPrint(38), AudioSplit(34), MetaStrip(34).
- **Life-events:** HeirSplit(45), BoxLabel(32), WeddingCount(30), CarePlan(37), FuneralPace(39), NewbornLog(32✗zajęty: ParentLove $5), DivorceAssets(44), RelocationKit(24✗starzeją się dane).
- **Compliance:** MileageLog(41), HoursSheet(39), FoodTemp(42), VATPulse(26✗starzeje się), ChemLabel(etykiety GHS/CLP,40), TireLog(36), CashRegAudit(30), HairColorRecord(40).
- **Calc permanence:** AmortizeIt(37), TileCalc(39), RoofArea(39), FabricCut(metraż tkaniny do szycia,40), BrewCalc(39), GardenBed(35), PetFood(30✗darmowe), SleepCycles(31).
- **Reference-table:** DyeRatio(44), SmokeWood(40), DosePaw(42), BuildNorm(23✗normy się zmieniają), WineMatch(32), NailCure(czasy utwardzania żeli UV,40), ConcreteClass(38), KnotStrength(36).

## Meta-obserwacja Pixel
Życiowe one-offy (HeirSplit/DivorceAssets) + branżowe tabele referencyjne (DyeRatio/DosePaw/NailCure) i compliance (FoodTemp) biją najwyżej. Bundle'e: HeirSplit+DivorceAssets jako jeden produkt z trybami; DyeRatio+HairColorRecord dla salonów. Odrzucił: NewbornLog, PetFood, WeddingCount (rynek zajęty), VATPulse/BuildNorm/RelocationKit (dane się starzeją → łamią durability).
