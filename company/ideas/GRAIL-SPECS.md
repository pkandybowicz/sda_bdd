# Specyfikacje graali — Color bible & Voice bible

> Dwa najmocniejsze znaleziska sesji (PUSTA Z OKAZJI). Wspólny rdzeń: „per-projekt
> referencja tożsamości: nazwana encja → atrybuty + PRÓBKA (kolor / audio) →
> błyskawiczne przywołanie podczas pracy". **Jeden silnik, dwa skiny, dwa rynki.**

---

## 🎨 COLOR BIBLE (robocza nazwa: „PaletteLock")

**Problem.** Rysownik webcomiców / solo animator rysuje te same postacie przez
**setki paneli/klatek**. Kolory „dryfują" — skóra, włosy, oczy, ubrania zmieniają
odcień między rozdziałami. Wpadka jest widoczna i wstydliwa, a poprawki kosztują godziny.

**Kto (rynek).** Twórcy na Webtoon/Tapas, rysownicy komiksów, ilustratorzy serii,
solo animatorzy 2D. Rynek duży (Webtoon = miliony twórców), płacący za narzędzia.

**Co robią dziś (konkurencja = goły generyk).** Adobe Color, zrzuty ekranu palet,
notatnik, paleta w Procreate/Clip Studio — **żadne nie trzyma kolorów OZNACZONYCH
per postać z odcieniami**. Brak dedykowanej apki (potwierdzone wieloetapowo).

**Co robi apka.**
- Projekt → **roster postaci**; każda postać = nazwane sloty koloru (skóra, włosy,
  oczy, ubranie główne, akcent…), każdy z odcieniami **light / mid / dark**.
- **Tap = kopiuj** HEX/RGB/oklch do schowka (wklejasz w dowolny program graficzny).
- **Szybkie wyszukanie** postaci podczas rysowania; pobranie koloru z obrazka (picker).
- Eksport palety (.ase/.aco/Procreate). Wszystko **lokalnie, offline**.

**Dlaczego $5 jednorazowo / offline.** To czysta lokalna baza + UI; zero serwera,
zero API, logika nigdy się nie starzeje → idealne „zrób raz".

**MVP (rdzeń).** projekt → postacie → nazwane sloty z odcieniami → kopiuj + szukaj.
Faza 2: eksport palet, color-pick z obrazu.

**Matematyka 1000×$5.** SEO („keep comic colors consistent", „character color reference"),
społeczności r/webcomics, r/ComicBookCollabs, Webtoon/Tapas Discordy, TikTok/YT „art process".
Przy milionach twórców 1000 kupujących/rok jest realne.

**Ryzyka.** Palety w Procreate/Clip Studio „wystarczają" części. Klin = **struktura
per-postać z etykietami + odcienie + kopiowanie cross-app + szukanie**. Sąsiednich
dedykowanych konkurentów: brak. **Najmocniejszy graal sesji (73).**

---

## 🎙️ VOICE BIBLE (robocza nazwa: „VoiceKeeper")

**Problem.** Narrator audiobooków (i aktor głosowy w grach) gra **wiele postaci**
przez 10h+ nagrania. Musi utrzymać spójny głos każdej postaci (wysokość, tempo,
akcent, „placement", emocja, tiki) przez całą książkę. Dryf = kosztowne re-recordy.

**Kto (rynek).** Narratorzy ACX/Audible, indie narratorzy, aktorzy głosowi w grach,
dubbing. Nisza węższa niż komiks, ale **realnie płacąca** (zarabiają na nagraniach).

**Co robią dziś.** **Arkusz** (metoda VOHeroes), Airtable, oraz luźne **voice-memo**
nazwane per postać. Niespójne, wolne w przywołaniu podczas sesji.

**Co robi apka.**
- Projekt (książka) → roster postaci; każda postać = atrybuty głosu (pitch, tempo,
  akcent, placement, baseline emocji, tiki) + **nagrana PRÓBKA audio**.
- **Jeden tap = odtworzenie próbki**, żeby „przypomnieć sobie" głos przed sceną.
- Szybkie wyszukanie po nazwie; odnośnik do strony pierwszego pojawienia. Offline/lokalnie.

**Kluczowy klin vs arkusz.** Zintegrowana **próbka audio per postać + błyskawiczne
przywołanie** w trakcie nagrania — czego arkusz/Memos nie dają płynnie.

**Uczciwa uwaga o konkurencji.** Istnieje **Game Master Journal** (wgrywa pliki
głosów NPC) — ale jest pod kampanie TTRPG, nie pod książki/sesję nagraniową narratora.
Dlatego dla narratorów to wciąż luka, choć sąsiad istnieje (stąd score 68, nie 73).

**Dlaczego $5 / offline.** Lokalna baza + nagrania na urządzeniu; prywatność,
zero serwera, zero utrzymania.

**MVP.** projekt(książka) → postacie → atrybuty + nagraj/odtwórz próbkę + szukaj.

**Matematyka 1000×$5.** Fora ACX, r/audiobooks, grupy FB narratorów (VO-BB),
trenerzy VO, Findaway. Mniejszy rynek, ale wysoka gotowość płacenia.

**Ryzyka.** Game Master Journal jako substytut; arkusz jest „za darmo"; narratorzy
przywiązani do nawyków. Klin = **UX pod sesję nagraniową**.

---

## 🔧 Wspólny silnik (czemu to się spina biznesowo)
Oba produkty to **ta sama mechanika**: *encja (postać) → atrybuty + jedna PRÓBKA
(swatch / audio) → natychmiastowe przywołanie podczas pracy*. Budujesz **jeden rdzeń**,
robisz dwa interfejsy (Color / Voice) → **podwójny rynek przy jednym developmencie**,
co domyka matematykę 1000×$5 i obniża ryzyko (dwa strzały, jeden koszt).

**Rekomendacja:** zacznij od **Color bible** (większy rynek, brak sąsiada, score 73),
a Voice bible wypuść jako drugi skin tego samego silnika.
