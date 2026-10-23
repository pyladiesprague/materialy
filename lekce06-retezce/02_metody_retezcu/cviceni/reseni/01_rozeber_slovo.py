# Řešení cvičení 1 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na slovo a vypiš o něm čtyři řádky:
#    velkými písmeny, malými písmeny, kolik má znaků
#    a kolikrát je v něm písmeno "a".
#
#    Délku umí len() z lekce 3, zbytek jsou metody z výkladu.

slovo = input("Napiš slovo: ")
pocet_a = slovo.count("a")

print(f"Velkými:  {slovo.upper()}")
print(f"Malými:   {slovo.lower()}")
print(f"Znaků:    {len(slovo)}")
print(f"Písmen a: {pocet_a}")

# count("a") nepočítá velké "A". Kdybys chtěla obojí, převeď slovo
# nejdřív na malá písmena:  slovo.lower().count("a")
