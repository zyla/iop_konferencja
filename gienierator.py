#!/usr/bin/env python3

print("# **Zadanie 2**: obsługa konferencji naukowej")
print("- zgłaszanie referatów, recenzowanie")
print("- organizacja eventu - program wystąpień, eventy typu przyjęcie, wycieczka ze zwiedzaniem itp.")

print("## Przypadki Biznesowe")

state = object()
state.kolejny_pb = 1
state.kolejny_fu = 1

def reset():
    state.kolejny_punkt = 1

def przypadek(id, nazwa):
    reset()

    print("### %s %s" % (id, nazwa))

def PB(nazwa):
    przypadek('PB' + state.kolejny_pb, nazwa)
    state.kolejny_pb += 1

def punkt(tresc):
    print('%d. %s' % (state.kolejny_punkt, tresc))
    state.kolejny_punkt += 1

PB('Zgłoszenie referatu')
punkt("""Prelegent wypełnia formularz z danymi:
 - temat prezentacji
 - abstrakt
 - dane kontaktowe
 - draft publikacji""")
punkt("System zapisuje publikację")
punkt("System wysyła e-mail z potwierdzeniem do prelegenta")
