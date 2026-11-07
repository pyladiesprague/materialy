# ---------------------------------------------
#  Řazení a past s None
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

hoste = ["Petra", "Anna", "Jana"]


# Metoda sort seřadí přímo tenhle seznam:
hoste.sort()
print(hoste)        # ['Anna', 'Jana', 'Petra']

# Metoda sort má parametr reverse s výchozí hodnotou False. Výchozí
# hodnoty parametrů znáš z lekce 5. Když chceš řadit obráceně, nastavíš
# ho na True. Napíšeš přitom i jeho jméno, ať je jasné, co to True znamená:
hoste.sort(reverse=True)
print(hoste)        # ['Petra', 'Jana', 'Anna']


# Česká písmena s háčky skončí až za písmenem z:
jmena = ["Zuzana", "Čeněk", "Anna"]
jmena.sort()
print(jmena)        # ['Anna', 'Zuzana', 'Čeněk']


# Metody append a sort mění seznam a nevracejí nic. Jejich výsledek je
# None, které znáš z lekce 5. Tohle je častá past:
veky = [34, 25, 41]
serazene = veky.sort()
print(serazene)     # None
print(veky)         # [25, 34, 41]

hoste = ["Anna"]
hoste = hoste.append("Eva")
print(hoste)        # None


# Metod seznamu je víc, než si teď zapamatuješ. Pamatovat si je nemusíš –
# všechny z téhle lekce najdeš v taháku.
