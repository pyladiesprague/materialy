# Řešení cvičení 3 – Cyklus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".

odpoved = input("Jaké je hlavní město Česka? ")
while odpoved != "Praha":
    odpoved = input("Jaké je hlavní město Česka? ")
print("Správně!")
