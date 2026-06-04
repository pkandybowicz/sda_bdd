# Krytyka #1 (sterylizacja) + retrospektywa całości

## Krytyka #1 — Log sterylizacji (dental/tattoo/vet): DEMOTE z #1
Weryfikacja na żywo obaliła kluczowe założenie "tatuaż/wet pominięte":
- Dental ZATŁOCZONE: Reprolog (integ. z Open Dental/Dentrix/Eaglesoft/Curve), Sowingo, Dental SteriTrack, SterilWize, W&H.
- Wet pokryte przez suites: ezyVet, Cornerstone (IDEXX), IntraVet.
- Tattoo "bez apki" ale pełno substytutów: darmowe PDF (PopProbe, consteril.com, template.net), Tattoo Studio Pro (suite), paper logbook Amazon ~$8.
- KILLER: mail-in spore testing (Mesa Labs, HealthFirst) daje WŁASNY compliance dashboard, przechowuje wyniki 3+ lata, w cenie pasków które MUSISZ kupować co tydzień → WTP za osobną apkę bliskie zera (jak eyewash Z358.1).
- "238k TAM" = trzy różne produkty/regulacje/kupujący, nie jeden rynek.
- Offline = WADA dla prawnego rekordu (brak backupu = utrata dowodu na kontroli).
- Liability/support wyżej niż modelowano.
Werdykt: Tier C (RT2 miał rację; dossier b2 przeważył rozmiarem rynku).

## Lekcja dla całej piątki
- Self-kept log (sterylizacja, pompa pożarowa §8.3) → zabija darmowy PDF/paper/dashboard dostawcy. SŁABSZE.
- Billable cert/report do trzeciej strony (anchor-point EN795/BS7883, NFPA 96 jako deliverable technika) → darmowy szablon nie wystarcza. MOCNIEJSZE.
Realne #1 = prawdopodobnie anchor-point EN795/BS7883 (mniejszy przychód ~$9k/rok netto, ale najtrwalszy klin).

## RETROSPEKTYWA — czemu wynik rozczarowuje (uczciwie)
1. Z 4071 przebadanych nisz po rygorystycznym red-teamie przeżyły TYLKO 4 — i wszystkie są MAŁE (rynki 2-5k podmiotów) lub niskopłacące. Brak jednego wyraźnego zwycięzcy.
2. Pierwotne podejście (hunt "pustych nisz") generowało dużo fałszywych trafień; dopiero weryfikacja App Store/Play + red-team je obalała. To kosztowało dużo iteracji.
3. Model "offline + jednorazowo + bez backendu" jest atrakcyjny dla biernego dochodu, ale w praktyce: w niszach z wysokim WTP (compliance) klient chce chmury/backupu; w niszach offline-friendly (hobby/maker) WTP jest niskie i freemium je zjada.
4. Realny wniosek: ten konkretny model (offline, one-time, solo) daje co najwyżej $9-25k/rok per apka przy 30-42% szansy — "dochód bierny", ale skala wymaga zbudowania wielu apek, a każda ma realnych konkurentów.

## Co jest w repo (stan końcowy)
- company/ideas/verified.json — 4071 nisz (surowa baza)
- company/tools/ — ingest.py, score_v4/v5/v6.py (silniki rankingu)
- company/ideas/verify/ — 9 plików głębokiej weryfikacji + rt_1/rt_2 (red-team) + _REALGAP_pool.json
- company/ideas/biz/ — b1_uk, b2_us, b3_pl_maker (dossiers biznesowe z liczbami+źródłami)
- company/specs/ — STRATEGIA_v5, STRATEGIA_NOVA, PROTOKOL_ANTYWTOPA, PUSH2_PODSUMOWANIE,
  oraz PDF: TOP10_v5, TOP10_v6, TOP20_zweryfikowany, TOP5_biznes + ten plik.

## Jeśli wracać do tematu — rekomendacja
NIE budować od razu. Najpierw walidacja popytu (10 rozmów + landing z preorderem) dla anchor-point EN795/BS7883 LUB NFPA 96 (billable-deliverable, nie self-log). Próg go/kill PRZED jakimkolwiek kodem.
