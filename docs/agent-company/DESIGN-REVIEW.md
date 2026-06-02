# Krytyczna analiza i poprawki

Dokument zbiera **słabe strony** pierwotnego pomysłu, **przyjęte poprawki** oraz
**dziennik decyzji**. To jest „dlaczego" stojące za [`ARCHITECTURE.md`](./ARCHITECTURE.md).

## Słabe strony i poprawki

### 🔴 Architektura

**1. Statyczny portal vs. działające Start/Stop — sprzeczność.**
Statyczny HTML czyta JSON, ale **nie zapisuje** plików na serwer/repo.
`localStorage` żyje tylko w przeglądarce — manager (kontener/CLI) go nie widzi.
→ **Poprawka:** Start/Stop jako **plik-flaga** `control.json`, którą przełącza
manager. Portal tylko pokazuje tryb. (Decyzja D-1.)

**2. Portal nie ma skąd czytać stanu.**
Pliki `company/*.json` żyją w efemerycznym kontenerze; portal działa w
przeglądarce. Te światy się nie widzą.
→ **Poprawka:** stan **commitowany/pushowany**, portal czyta zacommitowane dane.
Akceptujemy latencję cyklu commit/push; status = „ostatni znany + timestamp".

**3. „Co teraz robi" — subagent nie streamuje stanu.**
Subagent: odpalany → pracuje → zwraca wynik. W trakcie nie wysyła stanu do
plików.
→ **Poprawka:** status zmienia się na **granicach zadań** (start/koniec). UI
nie udaje żywego paska postępu.

**4. Izolacja workspace i wyścigi przy zapisie.**
Izolowany worktree gubi zapis workera; równoległy zapis do `board.md`/`state.json`
→ nadpisywanie.
→ **Poprawka:** **manager = jedyny zapisujący**. Workerzy zwracają tekst,
manager utrwala. (Decyzja D-3.)

### 🟠 Jakość i koszty

**5. Grube persony palą tokeny i psują pracę.**
Duży „charakterowy" system prompt na każde wywołanie = strata tokenów i gorszy
research (agent gra postać zamiast pracować).
→ **Poprawka:** persona = **kosmetyka portalu** (`employees.json`); prompt
roboczy chudy i zadaniowy.

**6. Brak definicji „done" i bramki jakości.**
Research puchnie w nieskończoność, nazbiera się śmieci.
→ **Poprawka:** zadania **ograniczone zakresem** + krok **review** (Opus „Nova"
lub manager) przed DONE. Przy okazji filtr na prompt injection.

**7. DiceBear z CDN przy renderze.**
Zewnętrzne wywołanie przy każdym renderze → wyciek użycia, łamie się offline/CSP.
→ **Poprawka:** avatary generowane **raz** i zapisane jako SVG w repo.

### 🔵 Bezpieczeństwo / prywatność

**8. Publiczne logi in/out = publikowanie wnętrza firmy.**
Surowe prompty i odpowiedzi na publicznej stronie; research z sieci niesie
**prompt injection**, które może wpłynąć na treść pokazywaną publicznie.
→ **Poprawka:** portal **prywatny, za loginem** — pełne logi bez ryzyka wycieku.
Treść z sieci traktowana jako niezaufana; manager recenzuje przed utrwaleniem.
(Decyzja D-2.)

### Ograniczenia przyjęte świadomie (nie „bugi")

- **„24/7" = praca falami.** Silnikiem jest sesja managera; nic nie działa
  autonomicznie w tle. Zgodne z modelem „wolne tokeny / tempo ustala właściciel".
- **Limity Max20 to twardy sufit.** Opus + 2× Sonnet non-stop wyczerpią limit;
  firma pracuje cyklicznie.
- **Brak głębokiego zagnieżdżania:** worker nie odpala własnych subagentów —
  wszystko orkiestruje manager.
- **Brak peer-to-peer między subagentami:** „komunikacja" idzie przez wspólny
  stan w repo (board / reports / logi), nie bezpośrednio.

## Dziennik decyzji

| ID | Decyzja | Wybór | Uzasadnienie |
|----|---------|-------|--------------|
| D-1 | Mechanizm Start/Stop | **Plik-flaga, przełącza manager** | Portal zostaje czysto statyczny; zero backendu do utrzymania; właściciel i tak steruje tempem. |
| D-2 | Widoczność portalu i logów | **Prywatny, za loginem** | Pozwala pokazać pełne logi in/out bez ryzyka wycieku; auth daje istniejąca strona. |
| D-3 | Kto zapisuje stan | **Tylko manager** | Koniec wyścigów i problemów z izolacją; spójne, pewne logowanie. |
| D-4 | Persona vs prompt roboczy | **Rozdzielone** | Tańsze tokenowo, lepszy research; charakter tylko na portalu. |
| D-5 | Avatary | **Generowane raz, SVG w repo** | Zero wywołań CDN przy renderze; działa offline/CSP. |
| D-6 | Model „24/7" | **Praca falami, silnik = sesja managera** | Uczciwe wobec limitów i modelu „wolne tokeny". |

## Otwarte kwestie (do ustalenia później)

- **Temat pierwszego researchu** — potrzebny do zasiania `board.md`. *(„Napiszę")*
- Format i wielkość raportów (limit długości, struktura sekcji).
- Polityka rotacji/archiwizacji logów (gdy `*.jsonl` urosną).
- Czy portal ma pokazywać prosty licznik „zadania w tej fali" jako proxy kosztu.
