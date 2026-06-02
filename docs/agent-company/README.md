# Agent Company — wizja i przegląd

> Symulacja małej firmy złożonej z agentów Claude Code: jeden **manager** (Opus,
> sterowany przez człowieka) oraz trzech **pracowników-subagentów** (1× Opus,
> 2× Sonnet), którzy dostają zadania, realizują je, raportują i są pokazani na
> prywatnym portalu jako „pracownicy" z wyglądem, charakterem i statusem.

## Cel

Zbudować coś, co **imituje firmę**: agenci dostają zadania (na start — research),
wykonują je, raportują i komunikują się przez wspólny stan w repo. Całość ma
działać w ramach subskrypcji (Max20) i **wolnych tokenów** — tempo określa
właściciel, nie automat.

## Skład „firmy"

| Rola | Model | Imię | Charakter (kosmetyka portalu) |
|------|-------|------|-------------------------------|
| Manager / Director | Opus | *(Ty + sesja)* | Rozdaje zadania, recenzuje, zapisuje stan |
| Senior Researcher | Opus | Nova | dociekliwa, sceptyczna, lubi przypisy |
| Researcher | Sonnet | Atlas | szybki, syntetyczny, lubi tabele |
| Researcher (Junior) | Sonnet | Pixel | kreatywny, dużo pyta, energiczny |

> Imiona/charaktery są **wyłącznie warstwą prezentacji** na portalu. Prompt
> roboczy pracownika jest chudy i zadaniowy (patrz `ARCHITECTURE.md`,
> sekcja „Persona vs prompt roboczy").

## Jak to działa (model mentalny)

1. **Silnikiem firmy jest sesja managera** prowadzona przez właściciela. Nic nie
   pracuje autonomicznie w tle — praca dzieje się „falami", gdy odpalasz manager.
2. Manager czyta tablicę zadań, rozdaje taski subagentom, **zbiera ich raporty
   (tekst)**, recenzuje, zapisuje wyniki i aktualizuje stan firmy w repo.
3. Stan jest **commitowany/pushowany** do repo. Prywatny **portal** (statyczna
   podstrona za loginem Twojej strony) czyta ten stan i pokazuje pracowników,
   ich status oraz logi in/out.
4. **Start/Stop** to plik-flaga `control.json`. Stop = bieżące zadania się
   kończą, nowych manager nie rozdaje (łagodne zatrzymanie, nic nie urywa się
   w połowie).

## Świadome ograniczenia (uczciwie)

- **„24/7" = praca falami**, nie ciągła. Przy modelu „wolne tokeny" to celowe.
- **Status to „ostatni znany + timestamp"**, nie żywy pasek postępu — subagent
  nie streamuje stanu w trakcie pracy.
- **Portal jest opóźniony o cykl commit/push** względem rzeczywistej pracy.
- **Limity Max20 to twardy sufit** — Opus + 2× Sonnet non-stop wyczerpią limit.

## Dokumenty

- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — komponenty, model danych, schematy JSON, wdrożenie.
- [`DESIGN-REVIEW.md`](./DESIGN-REVIEW.md) — krytyczna analiza, słabe strony i przyjęte poprawki + dziennik decyzji.

## Status

📄 **Faza dokumentacji.** Kod (struktura `company/`, definicje agentów, portal)
nie jest jeszcze budowany — czeka na zielone światło i temat pierwszego researchu.
