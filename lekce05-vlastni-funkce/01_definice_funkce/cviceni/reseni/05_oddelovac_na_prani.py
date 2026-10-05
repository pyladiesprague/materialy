# Řešení cvičení 5 – Definice funkce
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Předělej oddělovač z prvního úkolu tak, aby šlo při volání vybrat
#    znak a délku řádku. Když se nevybere nic, ať vypíše 30 hvězdiček
#    jako dřív.
#    Funkce musí zvládnout všechna tři volání:
#        oddelovac()
#        oddelovac("=")
#        oddelovac("-", 10)
#    Oba parametry mají výchozí hodnotu, takže se dá vynechat
#    jeden i oba.

def oddelovac(znak="*", delka=30):
    print(znak * delka)


oddelovac()
oddelovac("=")
oddelovac("-", 10)
