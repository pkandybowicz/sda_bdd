# Architektura

Dokument opisuje komponenty, przepływ pracy, model danych i wdrożenie
„firmy agentów". Założenia i decyzje, z których to wynika — patrz
[`DESIGN-REVIEW.md`](./DESIGN-REVIEW.md).

## Komponenty

```
┌─────────────────────────────────────────────────────────────┐
│  Właściciel (człowiek)                                       │
│      │  prowadzi sesję                                       │
│      ▼                                                       │
│  MANAGER (Opus, sesja Claude Code)  ← jedyny, który ZAPISUJE │
│      │  rozdaje zadania        ▲  zwracają tekst raportu     │
│      ▼                         │                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                   │
│  │  Nova    │  │  Atlas   │  │  Pixel   │   (subagenci)      │
│  │  Opus    │  │  Sonnet  │  │  Sonnet  │                   │
│  └──────────┘  └──────────┘  └──────────┘                   │
│      │                                                      │
│      ▼  commit / push                                       │
│  Repo: company/*.json + logi                                │
│      │                                                      │
│      ▼  odczyt (poll)                                       │
│  PORTAL (statyczny, prywatny — za loginem Twojej strony)    │
└─────────────────────────────────────────────────────────────┘
```

### Zasada nadrzędna: manager = jedyny zapisujący stan

Workerzy są **bezstanowi**: dostają zadanie → **zwracają tekst raportu**. To
manager pisze pliki raportów, aktualizuje `state.json`, `board.md`, logi i
`control.json`. Eliminuje to:
- wyścigi przy równoległym zapisie do tych samych plików,
- problem izolacji worktree (zapis workera nie ginie),
- niepewne logowanie (manager loguje in/out na granicach zadań).

### Persona vs prompt roboczy

Dwie **rozdzielone** warstwy:
- **Persona (kosmetyka portalu)** — imię, avatar, bio, cechy. Żyje w
  `employees.json`. Nie wpływa na jakość pracy.
- **Prompt roboczy** — chudy, zadaniowy, bez „grania postaci". Oszczędza tokeny
  i daje lepszy research.

## Cykl pracy (jedna „fala")

1. Manager czyta `control.json`. Jeśli `stopping` → nie rozdaje nowych zadań.
2. Manager bierze zadania z `board.md` (TODO), ustawia status pracowników na
   `working` w `state.json`, loguje wejście (`in`).
3. Subagenci wykonują zadania i **zwracają tekst** (raport / draft).
4. Manager **recenzuje** (bramka jakości; Opus „Nova" lub sam manager):
   - filtr na prompt injection z treści z sieci,
   - zgodność z definicją „done".
5. Manager zapisuje raport do `company/reports/`, loguje wyjście (`out`),
   aktualizuje `board.md` (DONE) i `state.json` (`idle`).
6. `git commit && git push` → portal zobaczy zmiany w następnym pollu.

## Struktura katalogów (docelowa)

```
company/
  control.json            # tryb pracy firmy: running | stopping
  board.md                # tablica zadań: TODO / IN PROGRESS / DONE
  employees.json          # profile pracowników (persona + avatar)
  state.json              # bieżący stan każdego pracownika
  reports/                # zatwierdzone raporty (1 plik = 1 zadanie)
  logs/
    nova.jsonl            # logi in/out (pełne — portal prywatny)
    atlas.jsonl
    pixel.jsonl
  avatars/
    nova.svg             # avatary wygenerowane RAZ, zapisane (zero CDN)
    atlas.svg
    pixel.svg
.claude/agents/
  worker-nova.md          # definicje subagentów (model + chudy prompt)
  worker-atlas.md
  worker-pixel.md
portal/
  index.html             # statyczny portal (vanilla JS, zero buildu)
```

## Model danych (schematy)

### `control.json`
```json
{
  "mode": "running",
  "updatedAt": "2026-06-02T10:00:00Z",
  "updatedBy": "manager"
}
```
- `mode`: `"running"` (rozdaje nowe zadania) | `"stopping"` (kończy bieżące,
  nowych nie bierze).
- Źródło prawdy dla Start/Stop. Portal tylko **czyta**; przełącza manager.

### `employees.json`
```json
[
  {
    "id": "nova",
    "name": "Nova",
    "role": "Senior Researcher",
    "model": "opus",
    "personality": ["dociekliwa", "sceptyczna", "lubi przypisy"],
    "bio": "Nie ufa źródłu bez trzech potwierdzeń.",
    "avatar": "avatars/nova.svg"
  }
]
```

### `state.json`
```json
{
  "nova": {
    "status": "working",
    "currentTask": "T-001: Mapowanie konkurencji",
    "since": "2026-06-02T10:05:00Z",
    "lastReport": "reports/T-001-nova.md"
  }
}
```
- `status`: `"working"` | `"idle"` | `"review"`.
- `since`: kiedy zaczął bieżący stan (portal pokazuje „od kiedy").

### `logs/<id>.jsonl` (jedna linia = jeden wpis)
```json
{"ts":"2026-06-02T10:05:00Z","dir":"in","task":"T-001","text":"Zbadaj X..."}
{"ts":"2026-06-02T10:18:00Z","dir":"out","task":"T-001","text":"Raport: ..."}
```
- `dir`: `"in"` (zadanie do agenta) | `"out"` (wynik od agenta).
- Portal prywatny → można trzymać i pokazywać pełną treść.

### `board.md` (format)
```markdown
## TODO
- [ ] T-002 (atlas) — Zebrać cenniki narzędzi X, Y, Z

## IN PROGRESS
- [ ] T-001 (nova) — Mapowanie konkurencji  ⏳ od 10:05

## DONE
- [x] T-000 (pixel) — Rozgrzewka: lista źródeł  ✓ reports/T-000-pixel.md
```

## Wdrożenie i „live"

- Stan żyje w **efemerycznym kontenerze** → musi być **commitowany/pushowany**,
  by portal (w przeglądarce) cokolwiek zobaczył.
- Portal hostowany jako **podstrona Twojej strony, za loginem**. Auth zapewnia
  Twoja istniejąca strona — portal pozostaje statyczny.
- „Na żywo" = **poll co kilka sekund** zacommitowanego stanu. Realna latencja:
  cykl commit/push (+ ew. cache hostingu). To **nie jest** sub-sekundowy live i
  tak jest to opisane w UI (status = „ostatni znany + timestamp").

## Sterowanie tempem (Start/Stop)

- **Mechanizm: plik-flaga.** `control.json.mode` przełącza **manager** na Twoją
  komendę („stop"/„start").
- Portal pokazuje aktualny tryb i przyciski jako **wskazanie intencji** (np.
  kopiowalna komenda / sygnał), ale autorytatywnie przełącza manager.
- **Stop jest łagodny**: bieżące zadania dokańczają się, nowe nie są rozdawane.
