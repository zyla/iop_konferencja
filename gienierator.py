#!/usr/bin/env python3

print("# **Zadanie 2**: obsługa konferencji naukowej")
print("- zgłaszanie referatów, recenzowanie")
print("- organizacja eventu - program wystąpień, eventy typu przyjęcie, wycieczka ze zwiedzaniem itp.")
print()

print("### Lista aktorów")
print("""
- prelegent - osoba prezentująca na konferencji
- recenzent - osoba, która decyduje o akceptacji lub odrzuceniu referatu
- organizator - osoba zarządzająca terminarzem
- słuchacz - osoba słuchająca prezentacji
- dziennikarz - osoba relacjonująca wydarzenie
""")

print()
print("## Przypadki Biznesowe")

# for truly interactive development
print("""<script>setTimeout(function() { location.reload(); }, 1000);</script>""")

class state:
    kolejny_pb = 1
    kolejny_fu = 1
    kolejny_punkt = 1
    kolejny_alt = 1

def reset():
    state.kolejny_punkt = 1
    state.kolejny_alt = 1

def przypadek(id, nazwa, aktorzy):
    reset()

    print()
    print("### %s %s" % (id, nazwa))
    print()
    print("Aktorzy: %s" % aktorzy)
    print()
    print("_Scenariusz główny:_")
    print()

def PB(*args, **kwargs):
    przypadek('PB%d' % state.kolejny_pb, *args, **kwargs)
    state.kolejny_pb += 1

def punkt(tresc):
    punkt = state.kolejny_punkt
    print('%d. %s' % (punkt, tresc))
    state.kolejny_punkt += 1
    return punkt

def alt(to_point=None):
    n = state.kolejny_alt
    print()
    print("_Scenariusz alternatywny %d:_" % n)
    print()
    state.kolejny_alt += 1

    def render_range_to(to_point):
        if to_point > 1:
            return '1-%d' % to_point
        else:
            return '1'

    if to_point:
        print("""%s. Jak w scenariuszu głównym\n""" % render_range_to(to_point))
        state.kolejny_punkt = to_point + 1
    else:
        state.kolejny_punkt = 1

def powrot(do_p):
    punkt('Powrót do punktu %d' % do_p)

class N:
    def __init__(self, mianownik, dopelniacz, dop_lm, new):
        self.mianownik = mianownik
        self.dopelniacz = dopelniacz
        self.dop_lm = dop_lm
        self.new = new

rodzaj_posilku = N('rodzaj posiłku', 'rodzaju posiłku', 'rodzajów posiłku', 'nowy')

def CRUD(thing, fields):
    PB('Dodanie nowego %s' % thing.dopelniacz, 'organizator')
    punkt('Organizator wpisuje %s', fields)
    punkt('Organizator zatwierdza')
    punkt('System zapisuje %s %s' % (thing.new, thing.mianownik))

###############################################################################
PB('Zgłoszenie referatu', 'prelegent, recenzent')
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


###############################################################################
PB("Przeglądanie terminarza",
   "prelegent, recenzent, organizator, słuchacz lub dziennikarz (\"użytkownik\")")
punkt("System prezentuje listę wydarzeń wraz i ich terminami")
