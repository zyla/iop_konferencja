#!/usr/bin/env python3

print("# **Zadanie 2**: obsługa konferencji naukowej")
print("- zgłaszanie referatów, recenzowanie")
print("- organizacja eventu - program wystąpień, eventy typu przyjęcie, wycieczka ze zwiedzaniem itp.")
print()
print("## Przypadki Biznesowe")

class state:
    kolejny_pb = 1
    kolejny_fu = 1
    kolejny_punkt = 1
    kolejny_alt = 1

def reset():
    state.kolejny_punkt = 1

def przypadek(id, nazwa, aktorzy):
    reset()

    print()
    print("### %s %s" % (id, nazwa))
    print()
    print("Aktorzy: %s" % aktorzy)
    print()
    print("__Scenariusz główny:__")
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
    print("__Scenariusz alternatywny %d:__" % n)
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

PB('Zgłoszenie referatu', 'prelegent, recenzent')
p_form = punkt("""Prelegent wypełnia formularz z danymi:
 - temat prezentacji
 - abstrakt
 - dane kontaktowe
 - draft publikacji""")
p2 = punkt("System zapisuje publikację")
punkt("System wysyła e-mail z potwierdzeniem do prelegenta")

alt(p2)
punkt("Dane są niepoprawne")
punkt("System wyświetla komunikat o błędzie")
powrot(p_form)
