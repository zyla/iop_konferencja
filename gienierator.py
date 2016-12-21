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

def reset():
    state.kolejny_punkt = 1

def przypadek(id, nazwa, aktorzy):
    reset()

    print()
    print("### %s %s" % (id, nazwa))
    print()
    print("Aktorzy: %s" % aktorzy)

def PB(nazwa):
    przypadek('PB%d' % state.kolejny_pb, nazwa)
    state.kolejny_pb += 1

def punkt(tresc):
    punkt = state.kolejny_punkt
    print('%d. %s' % (punkt, tresc))
    state.kolejny_punkt += 1
    return punkt

def alt():


PB('Zgłoszenie referatu')
punkt("""Prelegent wypełnia formularz z danymi:
 - temat prezentacji
 - abstrakt
 - dane kontaktowe
 - draft publikacji""")
punkt("System zapisuje publikację")
punkt("System wysyła e-mail z potwierdzeniem do prelegenta")
