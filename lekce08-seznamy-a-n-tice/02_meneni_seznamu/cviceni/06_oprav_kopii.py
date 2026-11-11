# Cvičení 6 – Měnění seznamů
# Oprav kód a soubor spusť (Run).

# Program má vypsat výsledky soutěže v pořadí, jak přišly, a vedle
#    nich žebříček od nejlepšího. Jenže oba seznamy vyjdou seřazené.
#    Najdi chybu a oprav ji. Vyjít má:
#
#      Jak přišly: [12, 18, 9, 15]
#      Žebříček: [18, 15, 12, 9]

vysledky = [12, 18, 9, 15]
zebricek = vysledky
zebricek.sort(reverse=True)

print(f"Jak přišly: {vysledky}")
print(f"Žebříček: {zebricek}")
