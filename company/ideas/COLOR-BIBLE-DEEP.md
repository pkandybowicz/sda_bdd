# Color Bible — głęboki opis produktu

> Robocza nazwa: **PaletteLock** (alt: „RefColors", „CharaPalette").
> Jednozdaniowo: *lokalna apka, która trzyma kolory (hex/RGB) per postać w jednym
> miejscu, z odcieniami i błyskawicznym kopiowaniem — żeby Twoje postacie nie
> „dryfowały" kolorem przez setki rysunków.*

---

## 1. Dla kogo (5 segmentów, wszystkie z tym samym bólem)

| Segment | Skala / zachowanie | Czemu płaci |
|---|---|---|
| **Rysownicy webcomiców** (Webtoon/Tapas) | setki tysięcy aktywnych; rysują tę samą obsadę latami | wpadka kolorystyczna = widoczny błąd dla czytelników |
| **Solo animatorzy 2D** | rosnący, robią serie/krótkie filmy | spójność klatka-do-klatki jest krytyczna |
| **Furry / właściciele furson** | **ogromna, bardzo wydająca ekonomia zleceń** | każda fursona ma ref-sheet z dokładnymi hexami; zamawiają dużo artu |
| **VTuberzy** | duży, zarabiający rynek | model + outfity muszą być spójne między artystami/klipami |
| **OC-artyści / character designers** (Toyhouse) | masowy hobby; setki OC per osoba | kolekcjonują postacie z paletami, zlecają art |

**Wspólny mianownik:** osoba prowadzi **wiele postaci**, każda z **ustaloną
paletą**, i musi tę paletę **wielokrotnie odtwarzać** (sama lub przekazać
zleceniobiorcy). Dziś = chaos.

## 2. Ból (konkretne scenariusze)
- Rysownik webcomicu po 3 miesiącach: „jaki dokładnie był hex bluzy Mai?" → szuka
  w starych plikach, pipetuje ze screena, kolor wychodzi *prawie* ten sam → cień
  na panelach się rozjeżdża.
- Furry zamawiający art: wysyła artyście ref, ale paleta jest „gdzieś na obrazku"
  bez kodów → artysta zgaduje → poprawki, frustracja, stracony czas obu stron.
- VTuber z 4 outfitami: każdy artist robi trochę inny odcień głównego koloru →
  brand się rozjeżdża.
- OC-artysta z 60 postaciami: pamięta palety „mniej więcej"; przy nowym rysunku
  traci 15 min na odtworzenie kolorów.

## 3. Co robią dziś (i czemu to słabe)
- **Coolors / Adobe Color** — generyczne palety; **nie wiążą koloru z POSTACIĄ ani
  z ROLĄ** (skóra/włosy/oczy), brak odcieni per slot, brak struktury per projekt.
- **Paleta w Procreate/Clip Studio** — jest w jednym programie, bez etykiet, nie
  przenosi się, nie ma odcieni nazwanych, nie da się oddać zleceniobiorcy.
- **Screeny / kartki / notatnik** — pipetowanie, błędy, zero szukania.
- **AI ref-generatory** — *tworzą* postać, ale **nie przechowują** Twoich
  istniejących, dokładnych kodów do ręcznego malowania.
→ **Nikt nie robi: „nazwana paleta per postać, z odcieniami, kopiowalna i
przenośna".** To jest luka.

## 4. Produkt — rdzeń
Hierarchia: **Projekt → Postać → Sloty koloru → Odcienie**.
- **Projekt** = komiks / fursona-set / kanał VTuber / folder OC.
- **Postać** = wpis z miniaturą/awatarem.
- **Slot koloru** = nazwana rola: „Skóra", „Włosy", „Oczy", „Bluza", „Akcent"…
- **Odcień** = light / base / shadow (+ opcjonalnie highlight, line) dla każdego slotu.
- Każdy kolor: HEX + RGB + (opcjonalnie) oklch/HSL; **tap = kopiuj** do schowka.

## 5. Funkcje — MVP (v1) vs v2

**MVP (v1) — minimum, które już sprzedaje:**
1. Tworzenie projektów i postaci (z miniaturą).
2. Sloty koloru z nazwą + 3 odcienie (light/base/shadow).
3. **Tap-to-copy** HEX/RGB.
4. **Pipeta z obrazka** (wczytaj rysunek, pobierz kolor do slotu).
5. **Szukajka** po nazwie postaci/slotu (szybkie przywołanie w trakcie pracy).
6. 100% **offline**, lokalna baza; kupno jednorazowe.

**v2 (po walidacji):**
- **Eksport ref-sheet** (PDF/PNG z paletą + kodami) — *killer dla zleceń*: wysyłasz
  artyście jeden plik z opisanymi hexami.
- Eksport palet do **.ase/.aco/Procreate swatches**.
- Sprawdzanie **kontrastu/spójności** (czy dwa slot-kolory za blisko).
- Warianty postaci (outfity/formy) jako pod-palety.
- Backup/eksport JSON (przeniesienie między urządzeniami — bez chmury).

## 6. Przepływ na ekranach
1. **Lista projektów** → 2. **Lista postaci w projekcie** (kafelki z twarzą) →
3. **Karta postaci**: rzędy slotów, w każdym 3 swatche z kodami, przycisk „kopiuj",
   przycisk „pipeta". Góra: szukajka. → 4. **Eksport** (v2): jeden tap = ref-sheet.

## 7. Model danych (lokalny)
```
Project { id, name }
Character { id, projectId, name, thumb }
Slot { id, characterId, label, order }
Swatch { id, slotId, role: light|base|shadow|..., hex }
```
Czysty, mały, deterministyczny → idealny offline, zero serwera.

## 8. Czemu pasuje do ograniczeń ($5 / zrób raz / offline)
- To **lokalna baza + UI**: zero backendu, zero zewnętrznych API, **logika nigdy
  się nie starzeje** (kolor to kolor). Klasyczne „zbuduj raz i zapomnij".
- **Prywatność/własność**: artyści nie chcą oddawać swoich postaci do chmury.
- **$5 jednorazowo** bije subskrypcyjny niesmak (Coolors Pro to subskrypcja).

## 9. Przewaga (vs każdy typ konkurenta)
- vs **Coolors/Adobe Color**: my wiążemy kolor z **postacią i rolą**, z odcieniami,
  per projekt — oni dają luźną paletę.
- vs **Procreate palette**: my jesteśmy **przenośni + opisani + z eksportem dla
  zleceniobiorcy**, działamy ponad programami.
- vs **AI ref-generatory**: my **przechowujemy Twoje istniejące kody**, nie generujemy
  losowych postaci.

## 10. Go-to-market (kanały per społeczność — organicznie, bez budżetu)
- **Reddit:** r/webcomics, r/comics, r/furry, r/furryartschool, r/VirtualYoutubers,
  r/OriginalCharacter, r/learnart, r/Tapas, r/animation.
- **Discord:** serwery webtoon-creatorów, furry-art, VTuber-art, OC-trade.
- **Toyhouse** (dom OC-artystów) — posty/integracja-mindshare.
- **TikTok/YouTube:** „art process", „how I keep my OC colors consistent".
- **SEO:** „character color reference app", „keep comic colors consistent",
  „fursona palette manager", „save character hex codes".
- **Furry/VTuber konwenty i hashtagi** (#fursona, #refsheet, #VTuberRef).

## 11. Matematyka 1000×$5 (≈ $5000/rok)
- Sama społeczność furry: setki tysięcy aktywnych, kultura **płacenia za narzędzia
  i art**. VTuber + OC-artyści + webcomic — łącznie miliony.
- Potrzebujemy **1000 kupujących / rok = ~83/mies. = ~3/dzień.** Przy organicznym
  dotarciu do choćby kilku z powyższych nisz — realne i bezpieczne.
- Każda nisza to osobny „strzał" dystrybucyjny tym samym produktem.

## 12. Ryzyka + mitygacje
- **„Procreate paleta wystarcza"** → mitygacja: eksport ref-sheet dla zleceń + odcienie
  + przenośność (to, czego paleta nie da).
- **Mały ARPU ($5)** → mitygacja: wiele nisz = wolumen; ewentualny v2-pakiet „pro" $9.
- **Ktoś skopiuje** → mitygacja: szybkość wejścia + community-fit (bądź pierwszy w furry/VTuber).
- **Discovery** → mitygacja: produkt jest „udostępnialny" (ref-sheet eksport niesie markę).

## 13. Ekspansja
Ten sam **silnik** napędza **Voice Bible** (audio: próbka głosu per postać) →
drugi rynek, jeden development. Color najpierw (większy, brak sąsiada), Voice jako drugi skin.

---

**Rekomendacja:** zbuduj **MVP v1** (projekt→postać→sloty→odcienie→tap-copy→pipeta→
szukajka, offline, $5) i waliduj na **r/furry + r/webcomics + Toyhouse** zanim dodasz v2.
