# ---------------------------------------------
#  Zarovnání do sloupců
# ---------------------------------------------
# Spusť soubor a sleduj, kde ve výpisu začínají čísla.

mesto = "Praha"
teplota = 23.4


# Takhle teplota začíná hned za názvem, takže u každého města jinde:
print(f"{mesto} {teplota:.1f}")     # Praha 23.4


# Za dvojtečku se vedle .1f dá napsat i číslo. To říká, kolik místa
# si hodnota zabere. Text se v tom místě zarovná doleva:
print(f"[{mesto:12}]")              # [Praha       ]

# a číslo doprava:
print(f"[{teplota:8.1f}]")          # [    23.4]


# Dvanáct míst na město a osm na teplotu udělá z výpisu tabulku:
def radek(nazev, stupne):
    print(f"{nazev:12}{stupne:8.1f}")


radek("Praha", 23.4)
radek("Brno", 8.1)
radek("Ostrava", -3.5)

# Na zarovnaných číslech je minus hned vidět.


# Směr se dá určit i ručně: > doprava, < doleva.
print(f"[{mesto:>12}]")             # [       Praha]
print(f"[{mesto:<12}]")             # [Praha       ]
