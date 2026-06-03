# 00 — SHELL (rdzeń fabryki) — wspólny dla wszystkich SKU

## Teza
Budujemy RAZ rdzeń, każdy kolejny produkt to reskin + pakiet. SKU #k ≈ 5% kosztu #1.

## Zasady niezmienne
- **Offline-first**, lokalna baza (SQLite). Zero konta, zero chmury obowiązkowej.
- **Jednorazowa opłata** (one-time). To główny klin vs subskrypcyjni incumbenci.
- **User-editable stałe** (prowizje Etsy, stawki kWh, ceny surowca) — neutralizuje ryzyko „dane się zdezaktualizują”.
- **Twarda granica zakresu**: NIE robimy schedulingu/faktur/CRM. To logbook/kalkulator. (chroni cenę one-time)

## Model danych (generyczny)
- `Record` (job/batch/inspekcja): id, pack_id, created_at, fields(JSON), photos[], computed(JSON), status.
- `Pack`: schema(pola+checklist), calc_module, report_template(PDF), reference_content(preload).
- `Inventory` (opcjonalne per pakiet): material, jednostka, koszt/jedn., stan.
- `Export`: PDF (raport/etykieta/cennik) + CSV backup.

## Co dostarcza shell (raz)
1. CRUD rekordów + zdjęcia (aparat/galeria) z adnotacją.
2. Silnik PDF (raport ze zdjęciami / etykieta / cennik).
3. System „pakietów” (schema+calc+template+treść) ładowanych jak wtyczki.
4. Edytowalne stałe + ustawienia waluty/jednostek.
5. Backup/restore lokalny (plik), import/eksport CSV.

## Stack (rekomendacja dla solo-dev)
- **Flutter** (jeden kod: iOS+Android+desktop), SQLite (drift/sqflite), pdf+printing package. Tanio, offline, szybko.
- Alternatywa: natywny SwiftUI tylko jeśli celujemy najpierw iOS-only.

## Monetyzacja
- **Per klaster = osobna płatna apka** (czyste pozycjonowanie w storze, inny kupujący).
- **Wewnątrz klastra = pakiety jako IAP** (np. apka „Inspection Log” + pakiety norm $15).
- Uwaga Apple/Google 30%: dla B2B trade rozważyć też sprzedaż licencji przez własny landing (Gumroad/Stripe) + kod aktywacji.

## Kolejność (oba kształty biznesu naraz)
Flagowiec #1 = pierwszy instancja shell (dowozimy do realnej sprzedaży). Gdy konwersja potwierdzona → reskiny/pakiety = tryb fabryki.
