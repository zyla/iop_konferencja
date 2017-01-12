# **Zadanie 2**: obsługa konferencji naukowej
Zgłaszanie referatów, recenzowanie, 
organizacja eventu - program wystąpień, eventy typu przyjęcie, wycieczka ze zwiedzaniem itp.

### Lista aktorów

- administrator - osoba zarządzająca systemem
- prelegent - osoba prezentująca na konferencji
- recenzent - osoba, która decyduje o akceptacji lub odrzuceniu referatu
- organizator - osoba zarządzająca terminarzem
- słuchacz - osoba słuchająca prezentacji
- dziennikarz - osoba relacjonująca wydarzenie
- czas

<script>setTimeout(function() { location.reload(); }, 1000);</script>

## Przypadki Biznesowe

### PB1 Dodanie nowego warsztatu warsztatu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Dodanie nowego warsztatu warsztatu".
2. Organizator wpisuje nazwę, opis, miejsce i cenę warsztatu.
3. Organizator zatwierdza.
4. System zapisuje nowy warsztat warsztat.
5. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-3. Jak w scenariuszu głównym

4. Wprowadzone dane są niepoprawne.
5. System wyświetla komunikat o błędzie.
6. Powrót do punktu 1.

### PB2 Edycja warsztatu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Edycja warsztatu".
2. System prezentuje listę warsztatów.
3. Organizator wybiera warsztat z listy.
4. Organizator wpisuje nazwę, opis, miejsce i cenę warsztatu.
5. Organizator zatwierdza.
6. System zapisuje nowy warsztat warsztat.
7. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-5. Jak w scenariuszu głównym

6. Wprowadzone dane są niepoprawne.
7. System wyświetla komunikat o błędzie.
8. Powrót do punktu 1.

### PB3 Usunięcie warsztatu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Usunięcie warsztatu".
2. System prezentuje listę warsztatów.
3. Organizator wybiera warsztat z listy.
4. Organizator zatwierdza.
5. System zapisuje nowy warsztat warsztat.
6. System wyświetla komunikat o sukcesie.

### PB4 Rejestracja na warsztat

Aktorzy: Słuchacz, Dziennikarz, Prelegent

_Scenariusz główny:_

1. Uczestnik wybiera opcję "Rejestracja na warsztat".
2. System prezentuje listę warsztatów.
3. Uczestnik wybiera warsztat.
4. Uczestnik zatwierdza.
5. System generuje rachunek do zapłacenia.
6. System zapisuje rezerwację.

_Scenariusz alternatywny 1:_

1-4. Jak w scenariuszu głównym

5. Miejsce zostało zajęte w międzyczasie.
6. System wyświetla komunikat o błędzie.
7. Powrót do punktu 1.


## Przypadki Systemowe


## Diagram
<img src=przypadki.png>
