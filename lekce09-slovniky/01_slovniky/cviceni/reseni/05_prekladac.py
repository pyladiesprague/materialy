# Řešení cvičení 5 – Slovníky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci preloz, která má na vstupu větu a slovník s překlady.
#    Vrátí větu přeloženou slovo po slově. Slova, která ve slovníku
#    nejsou, nechá, jak jsou. Velikost písmen ve větě nehraje roli.
#
#    Pak se zeptej na větu a vypiš její překlad.
#
#      Věta: Kočka pije mléko
#      cat drinks milk
#
#      Věta: pes jí knedlík
#      dog eats knedlík

slovnik = {
    "pes": "dog",
    "kočka": "cat",
    "jí": "eats",
    "pije": "drinks",
    "mléko": "milk",
    "maso": "meat",
    "a": "and",
}


def preloz(veta, slovnik):
    prelozena = []
    for slovo in veta.lower().split():
        if slovo in slovnik:
            prelozena.append(slovnik[slovo])
        else:
            prelozena.append(slovo)
    return " ".join(prelozena)


veta = input("Věta: ")
print(preloz(veta, slovnik))

# Podmínku v cyklu jde zkrátit metodou get. Když slovo ve slovníku není,
# vrátí místo překladu slovo samotné:
#
#     prelozena.append(slovnik.get(slovo, slovo))
#
# Funkce větu nevypisuje, ale vrací. Díky tomu ji můžeš vyzkoušet i bez
# psaní do terminálu:
#
#     print(preloz("pes a kočka", slovnik))     # dog and cat
