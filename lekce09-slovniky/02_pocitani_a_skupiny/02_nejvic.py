# ---------------------------------------------
#  Kdo vyhrál
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

pocty = {"Trezor": 3, "Jožin z bažin": 2, "Holky z naší školky": 1}


# Funkce max ti řekne nejvyšší počet hlasů, ale ne písničku:
print(max(pocty.values()))      # 3

# Vítěze najdeš stejným cyklem, jakým jsi v lekci 3 hledala největší
# číslo. Jen si k počtu pamatuješ i klíč:
vitez = ""
nejvic = 0

for pisnicka, pocet in pocty.items():
    if pocet > nejvic:
        vitez = pisnicka
        nejvic = pocet

print(f"Vyhrála písnička {vitez} ({nejvic} hlasy).")
# Vyhrála písnička Trezor (3 hlasy).


# Co když mají dvě písničky stejně hlasů? Porovnání > pustí dál jen
# větší počet, takže vyhraje ta, která byla ve slovníku dřív:
pocty = {"Trezor": 2, "Jožin z bažin": 2}

vitez = ""
nejvic = 0

for pisnicka, pocet in pocty.items():
    if pocet > nejvic:
        vitez = pisnicka
        nejvic = pocet

print(vitez)    # Trezor


# Když chceš všechny vítěze, najdi nejdřív nejvyšší počet a pak posbírej
# všechny písničky, které ho mají:
nejvic = max(pocty.values())

vitezove = []
for pisnicka, pocet in pocty.items():
    if pocet == nejvic:
        vitezove.append(pisnicka)

print(vitezove)     # ['Trezor', 'Jožin z bažin']
