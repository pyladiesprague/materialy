# Řešení cvičení 1 – Záznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vytvoř slovník o sobě s klíči jmeno, mesto a oblibene_jidlo. Pak:
#    - vypiš z něj dvě věty, třeba:
#        Jmenuju se Anna a bydlím ve městě Brno.
#        Nejradši jím knedlíky.
#    - přidej klíč konicky a jako hodnotu mu dej seznam tří koníčků,
#    - vypiš každý koníček na vlastní řádek s pomlčkou na začátku.

ja = {"jmeno": "Anna", "mesto": "Brno", "oblibene_jidlo": "knedlíky"}

print(f"Jmenuju se {ja['jmeno']} a bydlím ve městě {ja['mesto']}.")
print(f"Nejradši jím {ja['oblibene_jidlo']}.")

ja["konicky"] = ["lezení", "šachy", "Python"]

for konicek in ja["konicky"]:
    print(f"- {konicek}")
