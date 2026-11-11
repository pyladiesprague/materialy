# Řešení cvičení 6 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Program má vypsat výsledky soutěže v pořadí, jak přišly, a vedle
#    nich žebříček od nejlepšího. Jenže oba seznamy vyjdou seřazené.
#    Najdi chybu a oprav ji. Vyjít má:
#
#      Jak přišly: [12, 18, 9, 15]
#      Žebříček: [18, 15, 12, 9]

vysledky = [12, 18, 9, 15]
zebricek = vysledky.copy()
zebricek.sort(reverse=True)

print(f"Jak přišly: {vysledky}")
print(f"Žebříček: {zebricek}")

# zebricek = vysledky nedělá kopii. Obě proměnné ukazují na stejný seznam,
# takže sort seřadil i výsledky.
