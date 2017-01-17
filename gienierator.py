#!/usr/bin/env python3

import io, os, re
from collections import namedtuple

print("---")
print("title: '**Zadanie 2**: obsługa konferencji naukowej'")
print("author:")
print("- Adam Kwiatkowski")
print("- Katarzyna Romasevska")
print("- Tomasz Zwornicki")
print("- Maciej Bielecki")
print("geometry: margin=2cm")
print("---")
print("Zgłaszanie referatów, recenzowanie, ")
print("organizacja eventu - program wystąpień, eventy typu przyjęcie, wycieczka ze zwiedzaniem itp.")
print()

print("### Lista aktorów")
print("""
- administrator - osoba zarządzająca systemem
- prelegent - osoba prezentująca na konferencji
- recenzent - osoba, która decyduje o akceptacji lub odrzuceniu referatu
- organizator - osoba zarządzająca terminarzem
- słuchacz - osoba słuchająca prezentacji
- dziennikarz - osoba relacjonująca wydarzenie
- czas
""")

pb_out = io.StringIO()
fu_out = io.StringIO()
pb_graph_out = io.StringIO()
fu_graph_out = io.StringIO()

current_out = pb_out
graph_out = pb_graph_out

def output(s=''):
    current_out.write(s + '\n')

class state:
    kolejny_pb = 1
    kolejny_fu = 1
    kolejny_punkt = 1
    kolejny_alt = 1
    pb_name = ''

def reset():
    state.kolejny_punkt = 1
    state.kolejny_alt = 1

def przypadek(id, nazwa, aktorzy, wyjebac_scenariusz_glowny=False):
    reset()
    state.pb_name = nazwa

    output()
    output("### %s %s" % (id, nazwa))
    output()
    output("Aktorzy: %s" % aktorzy)
    output()

    if not wyjebac_scenariusz_glowny:
        output("_Scenariusz główny:_")
        output()

    first = True
    for aktor in aktorzy.split(', '):
        right = aktor in ['Prelegent']
        graph_node(aktor, '%s %s' % (id, nazwa), right, first)
        first = False

def graph_node(src, dst, on_right, arrow):
    if on_right:
        src, dst = dst, src
        arrow_fmt = '[dir=back]'
    else:
        arrow_fmt = ''

    if not arrow:
        arrow_fmt = '[dir=none]'

    graph_out.write('"%s" -> "%s" %s\n' % (src, dst, arrow_fmt))

def PB(*args, **kwargs):
    global current_out
    current_out = pb_out
    global graph_out
    graph_out = pb_graph_out
    przypadek('PB%d' % state.kolejny_pb, *args, **kwargs)
    state.kolejny_pb += 1

def FU(*args, **kwargs):
    global current_out
    current_out = fu_out
    global graph_out
    graph_out = fu_graph_out
    przypadek('FU%d' % state.kolejny_fu, *args, **kwargs)
    state.kolejny_fu += 1

def punkt(tresc):
    punkt = state.kolejny_punkt
    output('%d. %s.' % (punkt, tresc.capitalize()))
    state.kolejny_punkt += 1
    return punkt

def alt(to_point=None):
    n = state.kolejny_alt
    output()
    output("_Scenariusz alternatywny %d:_" % n)
    output()
    state.kolejny_alt += 1

    def render_range_to(to_point):
        if to_point > 1:
            return '1-%d' % to_point
        else:
            return '1'

    if to_point:
        output("""%s. Jak w scenariuszu głównym\n""" % render_range_to(to_point))
        state.kolejny_punkt = to_point + 1
    else:
        state.kolejny_punkt = 1

def powrot(do_p):
    punkt('Powrót do punktu %d' % do_p)

def wybiera_opcje(kto):
    punkt('%s wybiera opcję "%s"' % (kto, state.pb_name))

N = namedtuple('N', ('mianownik', 'dopelniacz', 'biernik',
      'dopelniacz_lm',
      'nowy_mianownik', 'nowy_dopelniacz', 'nowy_biernik'))

def CRUD(thing, fields, fields_fu, delete_alt=None, aktor='Organizator'):
    PB('Dodanie %s %s' % (thing.nowy_dopelniacz, thing.dopelniacz), aktor)
    wybiera_opcje(aktor)
    punkt('%s wpisuje %s %s' % (aktor, fields, thing.dopelniacz))
    p_zatw = punkt('%s zatwierdza' % aktor)
    punkt('System zapisuje %s %s' % (thing.nowy_biernik, thing.biernik))
    punkt('System wyświetla komunikat o sukcesie')

    alt(p_zatw)
    punkt('Wprowadzone dane są niepoprawne')
    punkt('System wyświetla komunikat o błędzie')
    powrot(1)

    PB('Edycja %s' % thing.dopelniacz, aktor)
    wybiera_opcje(aktor)
    punkt('System prezentuje listę %s' % (thing.dopelniacz_lm))
    punkt('%s wybiera %s z listy' % (aktor, thing.mianownik))
    punkt('%s wpisuje %s %s' % (aktor, fields, thing.dopelniacz))
    p_zatw = punkt('%s zatwierdza' % aktor)
    punkt('System zapisuje %s' % thing.biernik)
    punkt('System wyświetla komunikat o sukcesie')

    alt(p_zatw)
    punkt('Wprowadzone dane są niepoprawne')
    punkt('System wyświetla komunikat o błędzie')
    powrot(1)

    PB('Usunięcie %s' % thing.dopelniacz, aktor)
    wybiera_opcje(aktor)
    punkt('System prezentuje listę %s' % (thing.dopelniacz_lm))
    punkt('%s wybiera %s z listy' % (aktor, thing.mianownik))
    p_zatw = punkt('%s zatwierdza' % aktor)
    punkt('System usuwa %s' % thing.biernik)
    punkt('System wyświetla komunikat o sukcesie')

    if delete_alt:
        alt(p_zatw) 
        delete_alt()

    # FU Dodanie
    FU('Dodanie %s %s' % (thing.nowy_dopelniacz, thing.dopelniacz), aktor)
    wybiera_opcje(aktor)
    punkt('System prezentuje %s' % fields_fu)
    punkt('%s wpisuje wartości w pola formularza' % aktor)
    p_zatw = punkt('%s klika przycisk "Zapisz"' % aktor)
    punkt('System zapisuje %s %s' % (thing.nowy_biernik, thing.biernik))
    punkt('System wyświetla komunikat o sukcesie')

    alt(p_zatw)
    punkt('Wprowadzone dane są niepoprawne')
    punkt('System wyświetla komunikat o błędzie')
    powrot(1)

    # FU Edycja
    FU('Edycja %s' % thing.dopelniacz, aktor)
    wybiera_opcje(aktor)
    punkt('System prezentuje listę %s' % (thing.dopelniacz_lm))
    punkt('%s wybiera %s z listy' % (aktor, thing.mianownik))
    punkt('%s klika przycisk "Edytuj"' % aktor)
    punkt('System prezentuje %s, wypełniony danymi %s' % (fields_fu, thing.dopelniacz))
    punkt('%s edytuje dane w formularzu' % aktor)
    p_zatw = punkt('%s klika przycisk "Zapisz"' % aktor)
    punkt('System zapisuje %s' % thing.biernik)
    punkt('System wyświetla komunikat o sukcesie')

    alt(p_zatw)
    punkt('Wprowadzone dane są niepoprawne')
    punkt('System wyświetla komunikat o błędzie')
    powrot(1)

    # FU Usunięcie
    FU('Usunięcie %s' % thing.dopelniacz, aktor)
    wybiera_opcje(aktor)
    punkt('System prezentuje listę %s' % (thing.dopelniacz_lm))
    punkt('%s wybiera %s z listy' % (aktor, thing.mianownik))
    p_zatw = punkt('%s klika przycisk "Usuń"' % aktor)
    punkt('System usuwa %s' % thing.biernik)
    punkt('System wyświetla komunikat o sukcesie')

    if delete_alt:
        alt(p_zatw) 
        delete_alt()

###############################################################################
PB('Zgłoszenie referatu', 'Prelegent, Recenzent')
p_form = punkt("""Prelegent wypełnia formularz z danymi:
 - temat prezentacji
 - abstrakt
 - dane kontaktowe
 - draft publikacji""")
p_zapis = punkt("System zapisuje publikację")
punkt("System wysyła e-mail z potwierdzeniem do prelegenta")

alt(p_form)
punkt("Dane są niepoprawne")
punkt("System wyświetla komunikat o błędzie")
powrot(p_form)

alt(p_zapis)
punkt("Prelegent jest osobą zaproszoną")
punkt("Publikacja jest automatycznie akceptowana")


PB('Zgłoszenie innej formy', 'Prelegent, Recenzent')
output("""
1. Prelegent wypełnia formularz z następującymi danymi:
 - temat prezentacji
 - krótki opis wraz z informacja o formie prezentacji
 - dane kontaktowe
2. System zapisuje informacje. Wysyła e-mail do recenzentów i e-mail z potwierdzeniem do prelegenta.

_Scenariusz alternatywny 1:_

1. Jak w scenariuszu głównym

2. Dane są niepoprawne.
3. System wyświetla komunikat o błędzie.
4. Powrót do punktu 1.

_Scenariusz alternatywny 2:_

1-2. Jak w scenariuszu głównym

3. Prelegent jest osobą zaproszoną.
4. Publikacja jest automatycznie akceptowana.
""")

###############################################################################
#   PB("Przeglądanie terminarza",
#      "prelegent, recenzent, organizator, słuchacz lub dziennikarz (\"użytkownik\")")
#   wybiera_opcje("Użytkownik")
#   punkt("System prezentuje listę wydarzeń wraz i ich terminami")

def delete_alt_wybrany(thing, wybrany):
    def _alt():
         punkt('%s %s przez uczestników wydarzenia' % (thing.mianownik, wybrany))
         punkt('System wyświetla osoby, przez które %s %s' % (thing.mianownik, wybrany))
         powrot(1)
    return _alt

def RejestracjaNa(thing, aktorzy, aktor_gl):
    # Rejestracja
    PB('Rejestracja na %s' % thing.biernik, aktorzy)
    wybiera_opcje(aktor_gl)
    punkt('System prezentuje listę %s' % thing.dopelniacz_lm)
    punkt('%s wybiera %s' % (aktor_gl, thing.biernik))
    p_zatw = punkt('%s zatwierdza' % aktor_gl)
    punkt('System generuje rachunek do zapłacenia')
    punkt('System zapisuje rezerwację')

    alt(p_zatw)
    punkt('Miejsce zostało zajęte w międzyczasie')
    punkt('System wyświetla komunikat o błędzie')
    powrot(1)

    FU('Rejestracja na %s' % thing.biernik, aktorzy)
    wybiera_opcje(aktor_gl)
    punkt('System prezentuje listę %s' % thing.dopelniacz_lm)
    punkt('%s lokalizuje %s na liście' % (aktor_gl, thing.biernik))
    p_zatw = punkt('%s zatwierdza' % aktor_gl)
    punkt('System generuje rachunek do zapłacenia')
    punkt('System zapisuje rezerwację')

    alt(p_zatw)
    punkt('Miejsce zostało zajęte w międzyczasie')
    punkt('System wyświetla komunikat o błędzie')
    powrot(1)

    # Rezygnacja
    PB('Rezygnacja z %s' % thing.dopelniacz, aktorzy)
    wybiera_opcje(aktor_gl)
    punkt('System prezentuje listę %s' % thing.dopelniacz_lm)
    punkt('%s wybiera %s' % (aktor_gl, thing.biernik))
    punkt('%s zatwierdza' % aktor_gl)
    p_anuluje_rez = punkt('System anuluje rezerwację %s' % thing.dopelniacz)
    punkt('System anuluje rachunek')

    alt(p_anuluje_rez)
    punkt('Rachunek został już zapłacony')
    punkt('Pieniądze nie są zwracane')

    FU('Rezygnacja z %s' % thing.dopelniacz, aktorzy)
    wybiera_opcje(aktor_gl)
    punkt('System prezentuje listę %s' % thing.dopelniacz_lm)
    punkt('%s lokalizuje %s na liście' % (aktor_gl, thing.biernik))
    p_zatw = punkt('%s zatwierdza' % aktor_gl)
    p_anuluje_rez = punkt('System anuluje rezerwację %s' % thing.dopelniacz)
    punkt('System anuluje rachunek')

    alt(p_anuluje_rez)
    punkt('Rachunek został już zapłacony')
    punkt('Pieniądze nie są zwracane')


###############################################################################
# actual definitions

rodzaj_posilku = N(
        mianownik='rodzaj posiłku',
        dopelniacz='rodzaju posiłku',
        biernik='rodzaj posiłku',
        dopelniacz_lm='rodzajów posiłku',
        nowy_mianownik='nowy',
        nowy_dopelniacz='nowego',
        nowy_biernik='nowy')
CRUD(rodzaj_posilku,
    fields='nazwę',
    fields_fu='formularz z polem "nazwa"',
    delete_alt=delete_alt_wybrany(rodzaj_posilku, 'został wybrany'))

mozliwosc_noclegu = N(
        mianownik='możliwość noclegu',
        dopelniacz='możliwości noclegu',
        biernik='możliwość noclegu',
        dopelniacz_lm='możliwości noclegu',
        nowy_mianownik='nową',
        nowy_dopelniacz='nowej',
        nowy_biernik='nową')
CRUD(mozliwosc_noclegu,
        fields='nazwę, opis, miejsce i cenę',
        fields_fu='formularz z polami: nazwa, opis, miejsce, cena za dobę')

warsztat = N(
        mianownik='warsztat',
        dopelniacz='warsztatu',
        biernik='warsztat',
        dopelniacz_lm='warsztatów',
        nowy_mianownik='nowy',
        nowy_dopelniacz='nowego',
        nowy_biernik='nowy'
        )

CRUD(warsztat,
        fields='nazwę, opis, miejsce i cenę',
        fields_fu='formularz z polami: nazwa, opis, miejsce, cena')

wycieczka = N(
        mianownik='wycieczka',
        dopelniacz='wycieczki',
        biernik='wycieczkę',
        dopelniacz_lm='wycieczek',
        nowy_mianownik='nowa',
        nowy_dopelniacz='nowej',
        nowy_biernik='nową')
CRUD(wycieczka,
        fields='nazwę, opis, miejsce i cenę',
        fields_fu='formularz z polami: nazwa, opis, miejsce, cena')

konferencja = N(
        mianownik='konferencja',
        dopelniacz='konferencji',
        biernik='konferencję',
        dopelniacz_lm='konferencji',
        nowy_mianownik='nową',
        nowy_dopelniacz='nowej',
        nowy_biernik='nową')
CRUD(konferencja,
        fields='nazwę i opis',
        fields_fu='formularz z polami: nazwa, opis',
        aktor='Administrator')

SDP = 'Słuchacz/Dziennikarz/Prelegent'

RejestracjaNa(warsztat, aktorzy=SDP, aktor_gl='Uczestnik')

RejestracjaNa(wycieczka, aktorzy=SDP, aktor_gl='Uczestnik')

posilek = N(
        mianownik='posiłek',
        dopelniacz='posiłku',
        biernik='posiłek',
        dopelniacz_lm='posiłków',
        nowy_mianownik='nowy',
        nowy_dopelniacz='nowego',
        nowy_biernik='nowy')

RejestracjaNa(posilek, aktorzy=SDP, aktor_gl='Uczestnik')

nocleg = N(
        mianownik='nocleg',
        dopelniacz='noclegu',
        biernik='nocleg',
        dopelniacz_lm='noclegów',
        nowy_mianownik='nowy',
        nowy_dopelniacz='nowego',
        nowy_biernik='nowy')

RejestracjaNa(nocleg, aktorzy=SDP, aktor_gl='Uczestnik')

########################################################################################
# custom shit

PB('Recenzja referatu', 'Recenzent, Prelegent')
output("""
1. Recenzent czyta opis i draft publikacji
2. Recenzent wpisuje swoje uwagi
3. Recenzent zatwierdza publikację
4. System zmienia status publikacji na przyjętą przez kolejnego recenzenta.
5. System wysyła do Prelegenta e-mail z informacją i uwagami  po zaakceptowaniu przez określoną liczbę recenzentów.

_Scenariusz alternatywny 1:_

1-2. Jak w scenariuszu głównym

3. Recenzent odrzuca publikację.
4. System zmienia status publikacji na odrzuconą przez kolejnego recenzenta.
5. System wysyła do Prelegenta e-mail z informacją o odrzuceniu i uwagami po odrzuceniu przez określoną liczbę recenzentów.
""")

PB('Edycja terminarza wydarzenia', 'Organizator')
output("""
1. Organizator edytuje lub dodaje daty i godziny wydarzeń wcześniej wprowadzonych do systemu
2. System zapisuje zmiany.

_Scenariusz alternatywny 1:_

1. Jak w scenariuszu głównym.
2. System informuje o kolizjach.
""")

PB('Przeglądanie terminarza', 'Prelegent/Recenzent/Organizator/Słuchacz/Dziennikarz')
output("""
1. Aktor wybiera opcję przeglądania terminarza.
2. System wyświetla terminarz wydarzenia.

_Scenariusz alternatywny 1:_

1. Jak w scenariuszu głównym.
2. System powiadamia, że terminarz nie został jeszcze utworzony.
""")

PB('Kontakt z organizatorem', 'Prelegent/Recenzent/Słuchacz/Dziennikarz, Organizator')
output("""
1. Aktor wybiera opcję "Kontakt z organizatorem".
2. System wyświetla formularz do wypełnienia danymi:

- Imię
- Nazwisko
- Temat
- Treść

3. Aktor zatwierdza wypełnione dane.
4. System wysyła formularz w formia e-maila do organizatora, wraz z adresem e-mail pytającego.

_Scenariusz alternatywny 1:_

1-3 Jak w scenariuszu głównym.

4. System wyświetla informację o nie wypełnieniu części formularza
5. Powrót do punktu 2 scenariusza głównego.
""")

PB('Generowanie identyfikatorów dla uczestników', 'Organizator')
output("""
1. Organizator wybiera opcję “Generuj identyfikatory dla uczestników”
2. System generuje identyfikatory i zapisuje je.
3. System potwierdza wykonanie polecenia.

_Scenariusz alternatywny 1:_

1. Zapisy nie są jeszcze zamknięte. Opcja “Generuj identyfikatory dla uczestników” nie jest dostępna.
""")

PB('Wnoszenie opłaty za publikację artykułu', 'Prelegent')
output("""
1. Prelegent wybiera opcję “Opłata za publikację artykułu”.
2. Prelegent dokonuje płatności za pomocą systemu bankowego.
3. System zapisuje fakt dokonania płatności.
4. System wysyła prelegentowi e-mail z potwierdzeniem wykonania operacji.

_Scenariusz alternatywny 1 - płatność anulowana:_

1. Jak w scenariuszu głównym.
2. Prelegent nie zatwierdził płatności w systemie bankowym.
3. System wyświetla informację o niepowodzeniu.

_Scenariusz alternatywny 2:_

1. Artykuł jest już opłacony. Opcja “Opłata za publikację artykułu” nie jest dostępna.
""")


PB('Zgłaszanie poprawek do artykułów', 'Prelegent')
output("""
1. Prelegent wybiera opcję “Zgłoś poprawki do artykułu”.
2. System prezentuje tytuł i abstract artykułu z możliwością edycji.
3. Prelegent edytuje dane.
4. Prelegent przesyła na serwer plik z nowym draftem artukułu.
5. Prelegent zatwierdza zmiany.
6. System zapisuje zmiany.
7. System wysyła e-mail do recenzentów z informacją o poprawkach.

_Scenariusz alternatywny 1:_

Prelegent nie zgłosił jeszcze pierwszej wersji artykułu. Opcja “Zgłoś poprawki” nie jest dostępna.

_Scenariusz alternatywny 2:_

1-5. Jak w scenariuszu głównym.

6. Plik z draftem jest w niepoprawnym formacie.
7. System informuje o błędzie.
8. Powrót do punktu 2.
""")

PB('Zgłaszanie ostatecznych wersji artykułów', 'Prelegent, Recenzent')
output("""
1. Prelegent wybiera opcję “Zgłoś wersję artykułu jako ostateczną”.
2. System zapisuje ostateczną wersję.
3. System wysyła e-mail do recenzentów i e-mail z potwierdzeniem do prelegenta.

_Scenariusz alternatywny 1:_

1. Prelegent nie zgłosił jeszcze pierwszej wersji artykułu. Opcja “Zgłoś wersję jako ostateczną” nie jest dostępna.
""")

# MAYBE: Tutaj powinna byc strzalka tez od Organizatora?
PB('Przypomnienie o terminie zgłoszenia ostatecznej wersji artykułu', 'Czas, Organizator, Prelegent')
output("""
1. Mija czas do 5 dni przed wydarzeniem.
2. System wysyła powiadomienie o zatwierdzenie referatu do Prelegenta.

_Scenariusz alternatywny 1:_

1. Organizator wyszukuje prelegenta w katalogu.
2. Organizator wybiera polecenie “Wyślij przypomnienie”
3. System wysyła powiadomienie o zatwierdzenie referatu do Prelegenta.
""")

PB('Uszeregowanie i wysyłanie gotowych artykułów do wydawnictwa', 'Organizator')
output("""
1. System prezentuje listę zatwierdzonych artykułów.
2. Organizator zmienia kolejność na liście.
3. Organizator zatwierdza kolejność.
4. System zapisuje kolejność artykułów.
5. System generuje plik ze wszystkimi artykułami i ze spisem treści wymieniającym je w odpowiedniej kolejności.
""")

PB('Zmiana hasła', 'Prelegent/Recenzent/Organizator/Słuchacz/Dziennikarz') 
output("""
1. Aktor wybiera opcję "Zmiana hasła".
2. System wyświetla formularz do wypełnienia danymi

- stare hasło
- nowe hasło
- powtórzenie nowego hasła

3. Aktory zatwierdza wypełnione dane.
4. System zapisuje nowe hasło.

_Scenariusz alternatywny 1:_

1-3. Jak w scenariuszu głównym.

4. System wyświetla informację o różnym wpisaniu nowego hasła.

_Scenariusz alternatywny 2:_

1-3. Jak w scenariuszu głównym.

4. System wyświetla informację o za słabym haśle.
""")


PB('Rezygnacja z konferencji', 'Słuchacz')
output("""
1. Słuchacz wybiera opcję “rezygnacja z konferencji”. 
2. System wyświetla formularz.
3. Słuchacz wpisuje imię, nazwisko oraz kod biletu.
4. System potwierdza rezygnację. Zwraca pieniądze użytkownikowi. Zaznacza że to miejsce jest wolne.

_Scenariusz alternatywny 1 - błędne dane_:
1-3. Jak w scenariuszu głównym.

4. Błędne dane. System odrzuca prośbę rezygnacji i prosi o ponowne wpisanie danych.

_Scenariusz alternatywny 2 - upłynął termin rezygnacji_:

1. Jak w scenariuszu głównym.
2. System wyświetla komunikat, że upłynął termin rezygnacji.
""")

PB('Opłata rachunku', aktorzy=SDP)
wybiera_opcje('Użytkownik')
punkt('System wyświetla listę niezapłaconych rachunków użytkownika')
p_wybiera = punkt('Użytkownik wybiera rachunek')
punkt('Użytkownik płaci za pomocą systemu bankowości on-line')
punkt('System zapisuje rachunek jako zapłacony')
punkt('System wyświetla komunikat o sukcesie')

alt(p_wybiera)
punkt('Płatność nie powiodła się')
punkt('System wyświetla komunikat o błędzie')

PB('Przeglądanie rachunków', aktorzy=SDP)
wybiera_opcje('Użytkownik')
punkt('System wyświetla listę rachunków')
punkt('Użytkownik przegląda rachunki')

########################################################################################
# Custom FU shit

FU('Logowanie', 'Prelegent/Recenzent/Organizator/Słuchacz/Dziennikarz')
output("""
1. System wyświetla formularz z polami "login" i "hasło".
2. Aktor wprowadza swoje dane.
3. System sprawdza dane.
4. System udziela aktorowi dostępu do części systemu odpowiedniej dla aktora.

_Scenariusz alternatywny 1:_

1-2. Jak w scenariuszu głównym.

3. Wprowadzony login lub hasło są niepoprawne.
4. System wyświetla komunikat o błędzie.
5. Powrót do punktu 1.
""")

FU('Rejestracja referatu', 'Prelegent, Recenzent')
output("""
1. System wyświetla formularz z polami: imię, nazwisko, e-mail, temat, opis, draft.
2. Prelegent wpisuje dane tekstowe.
3. Prelegent ładuje plik z draftem.
4. Prelegent zatwierdza dane.
5. System zapisuje referat ze stanem "Do recenzji".
6. System wyświetla komunikat o sukcesie.
7. System wysyła e-mail z powiadomieniem do recenzentów.
8. System wysyła e-mail z potwierdzeniem do prelegenta.

_Scenariusz alternatywny 1:_

1-4. Jak w scenariuszu głównym.

5. Prelegent jest osobą zaproszoną.
6. System zapisuje referat ze stanem "Zaakceptowany".
7. System wysyła e-mail z potwierdzeniem do prelegenta.
""")

FU('Przeglądanie terminarza', 'Prelegent/Sluchacz')
output("""
System wyświetla okno zawierające listę wydarzeń na konferencji (prelekcje i
wydarzenia dodatkowe) wraz z ich miejscami, datami i godzinami rozpoczęcia i
zakończenia. 
Aktor czyta informacje.

_Scenariusz alternatywny 1:_

Terminarz nie jest jeszcze gotowy. System zamiast informacji o
wydarzeniach wyświetla komunikat "Terminarz nie jest jeszcze gotowy".
""")

FU('Rejestracja przemówienia wstępnego, konwersatorium', 'Prelegent', wyjebac_scenariusz_glowny=True)

FU('Przeglądanie nadesłanego referatu', 'Recenzent', True)

FU('Ocenianie i skomentowanie nadesłanego referatu/innej formy', 'Recenzent', True)

FU('Rezygnacja z konferencji', 'Słuchacz')
output("""
1. System wyświetla formularz z polami: imię, nazwisko, kod biletu.
2. Słuchacz wpisuje dane.
3. System wyświetla komunikat o sukcesie.
4. System zaznacza że to miejsce jest wolne.
5. System wysyła e-mail z potwierdzeniem.
6. System zwraca pieniądze: wysyła na konto słuchacza.

_Scenariusz alternatywny 1_:

1-3. Jak w scenariuszu głównym.

4. System wyświetla komunikat że zostały wpisane błędne dane.

_Scenariusz alternatywny 2_:

1. System wyświetla komunikat że upłynął termin rezygnacji z konferencji.
""")




FU('Potwierdzenie rezerwacji miejsca', 'Słuchacz/Dziennikarz/Prelegent', True)

FU('Edycja terminarza wydarzenia', 'Organizator', True)
FU('Zgłaszanie poprawek referatów/innej formy (Przemówienie wstępne, konwersatorium)', 'Prelegent', True)
FU('Przypomnienie o zgłoszeniu ostatecznej wersji artykułu', 'Czas, Prelegent', True)
FU('Szeregowanie artykułów do wydawnictwa', 'Organizator', True)
FU('Utworzenie odpowiedniej formy zbioru artykułów do wysłania do wydawnictwa', 'Organizator', True)

FU('Opłata rachunku', aktorzy=SDP)
wybiera_opcje('Użytkownik')
punkt('System wyświetla listę niezapłaconych rachunków użytkownika')
p_wybiera = punkt('Użytkownik wybiera rachunek i klika przycisk "Zapłać"')
punkt('Użytkownik płaci za pomocą systemu bankowości on-line')
punkt('System zapisuje rachunek jako zapłacony')
punkt('System wyświetla komunikat o sukcesie')

alt(p_wybiera)
punkt('Płatność nie powiodła się')
punkt('System wyświetla komunikat o błędzie')

FU('Przeglądanie rachunków', aktorzy=SDP)
wybiera_opcje('Użytkownik')
punkt('System wyświetla listę rachunków')
punkt('Użytkownik przegląda rachunki')

########################################################################################
# output this shit

print()
print("## Przypadki Biznesowe")
print(pb_out.getvalue())

print()
print("## Przypadki Systemowe")
print(fu_out.getvalue())

def make_diagram(ident, code):

    f = open('%s.dot' % ident, 'w')
    f.write('digraph { rankdir=LR; ' + code + ' }')
    f.close()

    os.system('dot -Tpng < %s.dot > %s.png' % (ident, ident))

print()
print("## Diagram przypadków biznesowych")
make_diagram('pb', pb_graph_out.getvalue())
print('![](pb.png)\\ ')

print()
print("## Diagram przypadków systemowych")
make_diagram('ps', fu_graph_out.getvalue())
print('![](ps.png)\\ ')

print()
print("## Diagram klas")
print('![](diagram_klas.png)\\ ')
