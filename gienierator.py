#!/usr/bin/env python3

import io, os
from collections import namedtuple

print("# **Zadanie 2**: obsługa konferencji naukowej")
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

# for truly interactive development
print("""<script>setTimeout(function() { location.reload(); }, 1000);</script>""")

pb_out = io.StringIO()
fu_out = io.StringIO()
graph_out = io.StringIO()

current_out = pb_out

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

def przypadek(id, nazwa, aktorzy):
    reset()
    state.pb_name = nazwa

    output()
    output("### %s %s" % (id, nazwa))
    output()
    output("Aktorzy: %s" % aktorzy)
    output()
    output("_Scenariusz główny:_")
    output()

    for aktor in aktorzy.split(', '):
        graph_node(aktor, nazwa)

def PB(*args, **kwargs):
    current_out = pb_out
    przypadek('PB%d' % state.kolejny_pb, *args, **kwargs)
    state.kolejny_pb += 1

def punkt(tresc):
    # TODO cap first
    punkt = state.kolejny_punkt
    output('%d. %s.' % (punkt, tresc))
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

N = namedtuple('N', ('mianownik', 'dopelniacz', 'biernik', 'dopelniacz_lm', 'nowy_mianownik', 'nowy_dopelniacz'))

def graph_node(src, dst):
    graph_out.write('"%s" -> "%s"\n' % (src, dst))

def CRUD(thing, fields, delete_alt=None, aktor='Organizator'):
    PB('Dodanie %s %s' % (thing.nowy_dopelniacz, thing.dopelniacz), aktor)
    wybiera_opcje(aktor)
    punkt('%s wpisuje %s %s' % (aktor, fields, thing.dopelniacz))
    p_zatw = punkt('%s zatwierdza' % aktor)
    punkt('System zapisuje %s %s' % (thing.nowy_mianownik, thing.mianownik))
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
    punkt('System zapisuje %s %s' % (thing.nowy_mianownik, thing.mianownik))
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
    punkt('System zapisuje %s %s' % (thing.nowy_mianownik, thing.mianownik))
    punkt('System wyświetla komunikat o sukcesie')

    if delete_alt:
        alt(p_zatw) 
        delete_alt()

def RejestracjaNa(thing, aktorzy, aktor_gl):
    PB('Rejestracja na %s' % thing.mianownik, aktorzy)
    wybiera_opcje(aktor_gl)
    punkt('System prezentuje listę %s' % thing.dopelniacz_lm)
    punkt('%s wybiera %s' % (aktor_gl, thing.mianownik)) # FIXME grammer
    p_zatw = punkt('%s zatwierdza' % aktor_gl)
    punkt('System generuje rachunek do zapłacenia')
    punkt('System zapisuje rezerwację')

    alt(p_zatw)
    punkt('Miejsce zostało zajęte w międzyczasie')
    punkt('System wyświetla komunikat o błędzie')
    powrot(1)

#    ###############################################################################
#    PB('Zgłoszenie referatu', 'prelegent, recenzent')
#    p_form = punkt("""Prelegent wypełnia formularz z danymi:
#     - temat prezentacji
#     - abstrakt
#     - dane kontaktowe
#     - draft publikacji""")
#    p_zapis = punkt("System zapisuje publikację")
#    punkt("System wysyła e-mail z potwierdzeniem do prelegenta")
#    
#    alt(p_form)
#    punkt("Dane są niepoprawne")
#    punkt("System wyświetla komunikat o błędzie")
#    powrot(p_form)
#    
#    alt(p_zapis)
#    punkt("Prelegent jest osobą zaproszoną")
#    punkt("Publikacja jest automatycznie akceptowana")
#    
#    
#    ###############################################################################
#    PB("Przeglądanie terminarza",
#       "prelegent, recenzent, organizator, słuchacz lub dziennikarz (\"użytkownik\")")
#    wybiera_opcje("Użytkownik")
#    punkt("System prezentuje listę wydarzeń wraz i ich terminami")

def delete_alt_wybrany(thing, wybrany):
    def _alt():
         punkt('%s %s przez uczestników wydarzenia' % (thing.mianownik, wybrany))
         punkt('System wyświetla osoby, przez które %s %s' % (thing.mianownik, wybrany))
         powrot(1)
    return _alt

###############################################################################
# rodzaj_posilku = N('rodzaj posiłku', 'rodzaju posiłku', 'rodzajów posiłku', 'nowy', 'nowego')
# CRUD(rodzaj_posilku, 'nazwę',
     # delete_alt=delete_alt_wybrany(rodzaj_posilku, 'został wybrany'))

# mozliwosc_noclegu = N('możliwość noclegu', 'możliwości noclegu', 'możliwości noclegu', 'nową', 'nowej')
# CRUD(mozliwosc_noclegu, 'nazwę, opis, miejsce i cenę')

warsztat = N(
        mianownik='warsztat',
        dopelniacz='warsztatu',
        biernik='warsztat',
        dopelniacz_lm='warsztatów',
        nowy_mianownik='nowy warsztat',
        nowy_dopelniacz='nowego warsztatu'
        )

CRUD(warsztat, 'nazwę, opis, miejsce i cenę')

# wycieczka = N('wycieczka', 'wycieczki', 'wycieczek', 'nowa', 'nowej')
# CRUD(wycieczka, 'nazwę, opis, miejsce i cenę')

# konferencja = N('konferencja', 'konferencji', 'konferencji', 'nową', 'nowej') # FIXME grammar
# CRUD(konferencja, 'nazwę i opis', aktor='Administrator')

RejestracjaNa(warsztat, aktorzy='Słuchacz, Dziennikarz, Prelegent', aktor_gl='Uczestnik')

# RejestracjaNa(wycieczka, aktorzy='Słuchacz, Dziennikarz, Prelegent', aktor_gl='Uczestnik')

print()
print("## Przypadki Biznesowe")
print(pb_out.getvalue())

print()
print("## Przypadki Systemowe")
print(fu_out.getvalue())

print()
print("## Diagram")

f = open('przypadki.dot', 'w')
f.write('digraph { rankdir=LR; ' + graph_out.getvalue() + ' }')
f.close()

os.system('dot -Tpng < przypadki.dot > przypadki.png')

print('<img src=przypadki.png>')
