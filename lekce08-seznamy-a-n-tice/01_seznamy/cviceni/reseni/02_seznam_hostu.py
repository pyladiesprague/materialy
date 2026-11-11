# Řešení cvičení 2 – Seznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na jméno. Když je na seznamu hostů, vypiš "Vítej!".
#    Když není, vypiš "Na seznamu nejsi.".
#    Vstup uprav tak, aby prošlo i " anna " nebo "ANNA".

hoste = ["Anna", "Petra", "Jana", "Eva"]

jmeno = input("Jméno: ").strip().title()

if jmeno in hoste:
    print("Vítej!")
else:
    print("Na seznamu nejsi.")
