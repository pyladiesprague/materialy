# Řešení cvičení 5 – And, or a not
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Sleva na vstupné. Slevu mají děti (do 18 let) a senioři (65 a víc).
#    Navíc mají v pondělí slevu úplně všichni.
#    Zeptej se na věk a na den a vypiš "Máš slevu." / "Plné vstupné.".

vek = int(input("Věk: "))
den = input("Den: ")
if vek < 18 or vek >= 65 or den == "pondělí":
    print("Máš slevu.")
else:
    print("Plné vstupné.")
