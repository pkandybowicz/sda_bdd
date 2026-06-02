# RAPORT KOŃCOWY — Brief #001

**5 pomysłów na aplikację „zrób raz, 5 $ jednorazowo, 1000 szt./rok"**
Wykonali: Atlas (T-001) · Pixel (T-002) · Nova (T-003) · Review: Manager.

---

## Review managera (bramka jakości)
- ✅ Dostarczono dokładnie **5 pomysłów**, każdy z analizą konkurencji (linki + ceny) i matematyką 1000×5 $.
- ✅ Nova skorygowała zawyżone oceny nisz z T-002 → wnioski są **konserwatywne**, nie marketingowe.
- ⚠️ **Liczby sprzedaży to założenia lejka, nie dane.** Żaden agent nie podał twardych wolumenów — przed budową zalecana walidacja (Google Trends, mining recenzji, ankieta na społeczności).
- ⚠️ Część stron zwracała 403 podczas T-001/T-002 — sygnały popytu częściowo oparte na logice rynkowej.

---

## 🏆 Ranking finalny

| # | Pomysł | Nisza | Werdykt |
|---|--------|-------|---------|
| **1** | **DiffLens** | słabo obsłużona | **REKOMENDACJA** — pewny popyt + dowód płacenia |
| 2 | RegexPilot | słabo obsłużona | mocny „drugi strzał" dla publiczności dev |
| 3 | BatchLens | słabo obsłużona | solidny, warunkowy |
| 4 | ColorVault | słabo obsłużona | ryzykowny (darmo wszędzie) |
| 5 | ExifScrub | słabo obsłużona | odradzany („pusty z przyczyny") |

---

## 1. ⭐ DiffLens — lokalny, prywatny diff tekstu/plików

- **Co robi:** wizualne porównanie dwóch tekstów/plików, czysty UI, w 100% offline.
- **Użytkownik:** developerzy, prawnicy, redaktorzy, biuro — każdy, kto porównuje wersje dokumentów.
- **Dowód popytu:** twardy. Diffchecker monetyzuje subskrypcją (~$15/mc), Beyond Compare ($30–60 jednorazowo) sprzedaje się od lat → ludzie **już płacą** za diff.
- **Konkurencja / luka:** Diffchecker drogi i online; Kaleidoscope → subskrypcja (backlash); Beyond Compare przeładowany; Meld/WinMerge darmowe, toporne, jednoplatformowe. **Luka = tani ($5), ładny, jednorazowy, cross-platform, offline.**
- **Dopasowanie do ograniczeń:** idealne — czysta logika lokalna, zero API, zero treści do aktualizacji.
- **Matematyka 1000×5 $:** SEO („diffchecker alternative one-time", „offline diff tool private") + argument prywatności (nie wklejasz tekstu do sieci). Jesteś 6–12× tańszy od Beyond Compare. 1000/rok realne przy szerokim TAM.
- **Nakład budowy:** średni (silnik diff + UI); biblioteki diff są gotowe.
- **Ryzyka:** VS Code/Meld/WinMerge darmowe „wystarczają" części użytkowników.

## 2. RegexPilot — offline tester regex z prywatną biblioteką wzorców

- **Co robi:** testowanie regex z live-highlight, własną biblioteką snippetów, eksportem do kodu (JS/Python/Go), offline.
- **Użytkownik:** developerzy, QA.
- **Dowód popytu:** średnio-wysoki. regex101 ma ogromny ruch; „offline regex tester" to powtarzalne zapytanie.
- **Konkurencja / luka:** regex101 wymaga netu; RegexBuddy Win-only ~$54; Expressions Mac-only; istnieją **darmowe** offline (RegexLab). Luka = UX + biblioteka + prywatność, **nie** pustka.
- **Matematyka 1000×5 $:** najlepszy czysty lejek (SEO + GitHub + HN/Reddit/SO), ale…
- **Ryzyka:** wysokie — darmowe substytuty offline istnieją, a devi najchętniej „zrobią to sami za darmo" (próg „za proste żeby płacić").

## 3. BatchLens — wizualny batch-rename z regex + tokeny EXIF

- **Co robi:** masowa zmiana nazw plików z podglądem na żywo, regexem i tokenami (data/EXIF/sekwencja).
- **Użytkownik:** fotografowie, archiwiści, content managerowie.
- **Dowód popytu:** średnio-wysoki. A Better Finder Rename (~$13, Mac) sprzedaje się latami.
- **Konkurencja / luka:** Bulk Rename Utility darmowy, ale koszmarny UI i Windows-only; ABFR Mac-only; PowerRename darmowy (Win). **Luka = nowoczesny, cross-platform UI + EXIF.**
- **Matematyka 1000×5 $:** społeczności foto/data-hoarder + SEO. Token EXIF zawęża do fotografów (chętniej płacą).
- **Ryzyka:** średnio-wysokie — darmowe potężne alternatywy; czy „ładny UI" wart $5.

## 4. ColorVault — capture + menadżer palet kolorów

- **Co robi:** pobieranie koloru z ekranu, organizacja palet, eksport CSS/Tailwind/Figma.
- **Użytkownik:** designerzy UI/UX, front-end.
- **Dowód popytu:** średni; mocno rozdrobniony i obsłużony za darmo. Sip przeszedł na subskrypcję (sygnał, że jednorazówka słabo się trzymała).
- **Konkurencja / luka:** eksport jest **darmowy wszędzie** (wtyczki Figma, uicolors.app); realna wartość = capture + biblioteka.
- **Matematyka 1000×5 $:** słaba-średnia — konkuruje z darmem na każdym kroku lejka.
- **Ryzyka:** wysokie; kolory to nie dane wrażliwe → brak argumentu prywatności.

## 5. ExifScrub — selektywne usuwanie metadanych EXIF (GUI)

- **Co robi:** podgląd i wybiórcze usuwanie metadanych zdjęć lokalnie.
- **Użytkownik:** fotografowie, prawnicy, dziennikarze, osoby dbające o prywatność.
- **Dowód popytu:** średni, ale **epizodyczny** (robi się raz na jakiś czas).
- **Konkurencja / luka:** ExifTool (CLI), ExifCleaner (kasuje wszystko), online removery, natywny „Remove Properties" w Windows. Cienka dyferencjacja.
- **Matematyka 1000×5 $:** słaba — to nisza **pusta z przyczyny**: użytkownik prywatnościowy z definicji wybiera darmowe/offline.
- **Ryzyka:** najwyższe — „za proste żeby płacić" + brak powracalności.

---

## Rekomendacja decydenta
**Buduj DiffLens.** To jedyny pomysł, gdzie „istnieje popyt" i „nisza ma okazję"
zbiegają się bez naciągania: rynek udowodnił gotowość płacenia (Beyond Compare,
Diffchecker), a Ty wchodzisz tańszy, prostszy, prywatny i cross-platform.
**RegexPilot** trzymaj jako szybki „drugi strzał" dla publiczności technicznej.

**Następny krok przed kodem:** walidacja popytu twardymi danymi (Google Trends
dla zapytań, mining recenzji Diffchecker/Beyond Compare pod kątem bólu, szybka
ankieta w społeczności dev/prawniczej). Dopiero potem budowa.
