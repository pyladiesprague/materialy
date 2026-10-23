# Řešení cvičení 3 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ptej se na velikost trička, dokud uživatelka nenapíše S, M nebo L.
#    Na nic jiného se nespokoj a zeptej se znovu. Velikost písmen
#    ani mezery navíc ať nevadí – "s" i "  M  " mají projít.
#    Nakonec vypiš objednanou velikost velkým písmenem.
#
#    Cyklus while True a break znáš z lekce 4.

while True:
    velikost = input("Jakou velikost? (S/M/L) ").strip().upper()
    if velikost == "S" or velikost == "M" or velikost == "L":
        break
    print("Vyber S, M nebo L.")

print(f"Objednáno: tričko velikosti {velikost}.")

# Tady se hodí upper(), protože výsledek chceme velkým písmenem.
# Bez strip() a upper() by cyklus u "  m  " nikdy neskončil.
