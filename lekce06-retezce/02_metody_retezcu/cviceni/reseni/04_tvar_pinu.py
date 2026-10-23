# Řešení cvičení 4 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na PIN a zkontroluj, jestli má správný tvar: přesně čtyři
#    znaky a všechny číslice. Vypiš, jestli je v pořádku.
#    Mezery navíc ať nevadí.
#
#    V lekci 5 jsi PINu dávala tři pokusy na uhodnutí. Tady jde o to,
#    jestli vůbec vypadá jako PIN.

pin = input("Zadej PIN: ").strip()

if pin.isdigit() and len(pin) == 4:
    print("PIN má správný tvar.")
else:
    print("PIN musí být přesně čtyři číslice.")

# Samotné isdigit() by pustilo i "12" nebo "123456", samotné len()
# zase "ab12". Teprve obě podmínky dohromady dávají tvar PINu.
