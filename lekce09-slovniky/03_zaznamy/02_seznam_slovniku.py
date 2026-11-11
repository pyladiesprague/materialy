# ---------------------------------------------
#  Seznam slovníků: tabulka
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Hostů je víc, takže záznamy dáš do seznamu. Každý slovník je jeden host
# a všechny mají stejné klíče:
hoste = [
    {"jmeno": "Anna", "vek": 34, "darek": "dort"},
    {"jmeno": "Petra", "vek": 25, "darek": "víno"},
    {"jmeno": "Jana", "vek": 41, "darek": "víno"},
]

# Je to vlastně tabulka. Položky seznamu jsou řádky, klíče sloupce:
#
#     jmeno   vek   darek
#     Anna     34   dort
#     Petra    25   víno
#     Jana     41   víno


# Jeden údaj přečteš ve dvou krocích. Nejdřív vezmeš hosta ze seznamu,
# pak údaj ze slovníku:
prvni = hoste[0]
print(prvni["jmeno"])           # Anna

# Oba kroky jde napsat za sebe. Čte se to zleva doprava:
print(hoste[0]["jmeno"])        # Anna

# Kratší ale neznamená lepší. Když se ti to líp čte ve dvou krocích,
# piš to ve dvou krocích.


# V cyklu dostaneš po jednom celé záznamy:
for host in hoste:
    print(f"{host['jmeno']:6} {host['vek']:3}   {host['darek']}")

# Anna    34   dort
# Petra   25   víno
# Jana    41   víno


# Se záznamy funguje všechno, co už znáš. Kdo přinese víno:
vino = []
for host in hoste:
    if host["darek"] == "víno":
        vino.append(host["jmeno"])

print(vino)                     # ['Petra', 'Jana']

# Průměrný věk:
soucet = 0
for host in hoste:
    soucet = soucet + host["vek"]

print(f"Průměrný věk: {soucet / len(hoste):.1f}")      # Průměrný věk: 33.3


# Přesně takhle vypadají data z tabulky v souboru CSV. Každý řádek se
# načte jako jeden slovník. Na workshopu a v lekci 13 to uvidíš naživo.
