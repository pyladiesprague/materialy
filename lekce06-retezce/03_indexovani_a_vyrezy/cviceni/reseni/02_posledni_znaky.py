# Řešení cvičení 2 – Indexování a výřezy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na slovo a vypiš jeho poslední tři znaky. Když je slovo
#    kratší než tři znaky, vypiš místo toho, že je moc krátké.
#
#    Délku změříš len() z lekce 3, rozhodneš se podmínkou z lekce 2.

slovo = input("Napiš slovo: ")

if len(slovo) < 3:
    print("To je moc krátké.")
else:
    print(slovo[-3:])

# Se záporným indexem nepotřebuješ vědět, jak je slovo dlouhé.
# Výřez by u krátkého slova nespadl, jen by vrátil míň znaků –
# podmínka je tu proto, že chceme říct něco jiného.
