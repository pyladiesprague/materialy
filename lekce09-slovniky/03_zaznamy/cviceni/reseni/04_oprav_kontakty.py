# Řešení cvičení 4 – Záznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Program má vypsat telefon každého hosta. Petra ale telefon nenechala
#    a program na ní spadne. Spusť ho, přečti si hlášku a oprav ho tak,
#    aby u Petry vypsal "neuvedeno".
#
#      Anna: 602 111 222
#      Petra: neuvedeno
#      Jana: 608 999 000

hoste = [
    {"jmeno": "Anna", "telefon": "602 111 222"},
    {"jmeno": "Petra"},
    {"jmeno": "Jana", "telefon": "608 999 000"},
]

for host in hoste:
    telefon = host.get("telefon", "neuvedeno")
    print(f"{host['jmeno']}: {telefon}")

# Hláška KeyError: 'telefon' říká, že v jednom záznamu klíč chybí.
# Metoda get vrátí místo chyby výchozí hodnotu.
