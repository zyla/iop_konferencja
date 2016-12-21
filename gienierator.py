#!/usr/bin/env python3

print("# *Zadanie 2*: obsługa konferencji naukowej")
print("- zgłaszanie referatów, recenzowanie")
print("- organizacja eventu - program wystąpień, eventy typu przyjęcie, wycieczka ze zwiedzaniem itp.")

print("## Przypadki Biznesowe")

state = object()

def reset():
    state.kolejny_punkt = 1

def przypadek(id, nazwa):
    reset()

    print("### %s %s" % (id, nazwa))
