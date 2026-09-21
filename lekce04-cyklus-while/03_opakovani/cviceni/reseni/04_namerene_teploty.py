# Řešení cvičení 4 – Opakování
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Uživatel zadává naměřené teploty. Po každé se zeptej
#    "Další? (ano/ne) ". Až odpoví "ne", vypiš nejvyšší teplotu.
#    První teplotu si rovnou zapamatujeme jako zatím nejvyšší,
#    každou další s ní porovnáme.

nejvyssi = int(input("Zadej teplotu: "))
while True:
    dalsi = input("Další? (ano/ne) ")
    if dalsi == "ne":
        break
    teplota = int(input("Zadej teplotu: "))
    if teplota > nejvyssi:
        nejvyssi = teplota

print("Nejvyšší teplota byla", nejvyssi)
