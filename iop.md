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

### PB1 Dodanie nowego rodzaju posiłku

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Dodanie nowego rodzaju posiłku".
2. Organizator wpisuje nazwę rodzaju posiłku.
3. Organizator zatwierdza.
4. System zapisuje nowy rodzaj posiłku.
5. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-3. Jak w scenariuszu głównym

4. Wprowadzone dane są niepoprawne.
5. System wyświetla komunikat o błędzie.
6. Powrót do punktu 1.

### PB2 Edycja rodzaju posiłku

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Edycja rodzaju posiłku".
2. System prezentuje listę rodzajów posiłku.
3. Organizator wybiera rodzaj posiłku z listy.
4. Organizator wpisuje nazwę rodzaju posiłku.
5. Organizator zatwierdza.
6. System zapisuje nowy rodzaj posiłku.
7. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-5. Jak w scenariuszu głównym

6. Wprowadzone dane są niepoprawne.
7. System wyświetla komunikat o błędzie.
8. Powrót do punktu 1.

### PB3 Usunięcie rodzaju posiłku

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Usunięcie rodzaju posiłku".
2. System prezentuje listę rodzajów posiłku.
3. Organizator wybiera rodzaj posiłku z listy.
4. Organizator zatwierdza.
5. System zapisuje nowy rodzaj posiłku.
6. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-4. Jak w scenariuszu głównym

5. rodzaj posiłku został wybrany przez uczestników wydarzenia.
6. System wyświetla osoby, przez które rodzaj posiłku został wybrany.
7. Powrót do punktu 1.

### PB4 Dodanie nowej możliwości noclegu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Dodanie nowej możliwości noclegu".
2. Organizator wpisuje nazwę, opis, miejsce i cenę możliwości noclegu.
3. Organizator zatwierdza.
4. System zapisuje nową możliwość noclegu.
5. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-3. Jak w scenariuszu głównym

4. Wprowadzone dane są niepoprawne.
5. System wyświetla komunikat o błędzie.
6. Powrót do punktu 1.

### PB5 Edycja możliwości noclegu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Edycja możliwości noclegu".
2. System prezentuje listę możliwości noclegu.
3. Organizator wybiera możliwość noclegu z listy.
4. Organizator wpisuje nazwę, opis, miejsce i cenę możliwości noclegu.
5. Organizator zatwierdza.
6. System zapisuje nową możliwość noclegu.
7. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-5. Jak w scenariuszu głównym

6. Wprowadzone dane są niepoprawne.
7. System wyświetla komunikat o błędzie.
8. Powrót do punktu 1.

### PB6 Usunięcie możliwości noclegu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Usunięcie możliwości noclegu".
2. System prezentuje listę możliwości noclegu.
3. Organizator wybiera możliwość noclegu z listy.
4. Organizator zatwierdza.
5. System zapisuje nową możliwość noclegu.
6. System wyświetla komunikat o sukcesie.

### PB7 Dodanie nowego warsztatu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Dodanie nowego warsztatu".
2. Organizator wpisuje nazwę, opis, miejsce i cenę warsztatu.
3. Organizator zatwierdza.
4. System zapisuje nowy warsztat.
5. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-3. Jak w scenariuszu głównym

4. Wprowadzone dane są niepoprawne.
5. System wyświetla komunikat o błędzie.
6. Powrót do punktu 1.

### PB8 Edycja warsztatu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Edycja warsztatu".
2. System prezentuje listę warsztatów.
3. Organizator wybiera warsztat z listy.
4. Organizator wpisuje nazwę, opis, miejsce i cenę warsztatu.
5. Organizator zatwierdza.
6. System zapisuje nowy warsztat.
7. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-5. Jak w scenariuszu głównym

6. Wprowadzone dane są niepoprawne.
7. System wyświetla komunikat o błędzie.
8. Powrót do punktu 1.

### PB9 Usunięcie warsztatu

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Usunięcie warsztatu".
2. System prezentuje listę warsztatów.
3. Organizator wybiera warsztat z listy.
4. Organizator zatwierdza.
5. System zapisuje nowy warsztat.
6. System wyświetla komunikat o sukcesie.

### PB10 Dodanie nowej wycieczki

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Dodanie nowej wycieczki".
2. Organizator wpisuje nazwę, opis, miejsce i cenę wycieczki.
3. Organizator zatwierdza.
4. System zapisuje nowa wycieczka.
5. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-3. Jak w scenariuszu głównym

4. Wprowadzone dane są niepoprawne.
5. System wyświetla komunikat o błędzie.
6. Powrót do punktu 1.

### PB11 Edycja wycieczki

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Edycja wycieczki".
2. System prezentuje listę wycieczek.
3. Organizator wybiera wycieczka z listy.
4. Organizator wpisuje nazwę, opis, miejsce i cenę wycieczki.
5. Organizator zatwierdza.
6. System zapisuje nowa wycieczka.
7. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-5. Jak w scenariuszu głównym

6. Wprowadzone dane są niepoprawne.
7. System wyświetla komunikat o błędzie.
8. Powrót do punktu 1.

### PB12 Usunięcie wycieczki

Aktorzy: Organizator

_Scenariusz główny:_

1. Organizator wybiera opcję "Usunięcie wycieczki".
2. System prezentuje listę wycieczek.
3. Organizator wybiera wycieczka z listy.
4. Organizator zatwierdza.
5. System zapisuje nowa wycieczka.
6. System wyświetla komunikat o sukcesie.

### PB13 Dodanie nowej konferencji

Aktorzy: Administrator

_Scenariusz główny:_

1. Administrator wybiera opcję "Dodanie nowej konferencji".
2. Administrator wpisuje nazwę i opis konferencji.
3. Administrator zatwierdza.
4. System zapisuje nową konferencja.
5. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-3. Jak w scenariuszu głównym

4. Wprowadzone dane są niepoprawne.
5. System wyświetla komunikat o błędzie.
6. Powrót do punktu 1.

### PB14 Edycja konferencji

Aktorzy: Administrator

_Scenariusz główny:_

1. Administrator wybiera opcję "Edycja konferencji".
2. System prezentuje listę konferencji.
3. Administrator wybiera konferencja z listy.
4. Administrator wpisuje nazwę i opis konferencji.
5. Administrator zatwierdza.
6. System zapisuje nową konferencja.
7. System wyświetla komunikat o sukcesie.

_Scenariusz alternatywny 1:_

1-5. Jak w scenariuszu głównym

6. Wprowadzone dane są niepoprawne.
7. System wyświetla komunikat o błędzie.
8. Powrót do punktu 1.

### PB15 Usunięcie konferencji

Aktorzy: Administrator

_Scenariusz główny:_

1. Administrator wybiera opcję "Usunięcie konferencji".
2. System prezentuje listę konferencji.
3. Administrator wybiera konferencja z listy.
4. Administrator zatwierdza.
5. System zapisuje nową konferencja.
6. System wyświetla komunikat o sukcesie.


## Przypadki Systemowe


## Diagram
<img src=przypadki.png>