# Řešení cvičení 8 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# V lekci 4 sis z naměřených teplot pamatovala jen nejvyšší. Teď si
#    ulož všechny. Ptej se "Teplota: ", dokud uživatel nenapíše "konec".
#    Pak vypiš nejvyšší teplotu, průměr a kolik teplot bylo nad průměrem.
#
#      Teplota: 10
#      Teplota: 20
#      Teplota: 30
#      Teplota: konec
#      Nejvyšší: 30
#      Průměr: 20.0
#      Nad průměrem: 1

teploty = []

while True:
    odpoved = input("Teplota: ")
    if odpoved == "konec":
        break
    teploty.append(int(odpoved))

prumer = sum(teploty) / len(teploty)
nad_prumerem = 0

for teplota in teploty:
    if teplota > prumer:
        nad_prumerem = nad_prumerem + 1

print(f"Nejvyšší: {max(teploty)}")
print(f"Průměr: {prumer:.1f}")
print(f"Nad průměrem: {nad_prumerem}")
