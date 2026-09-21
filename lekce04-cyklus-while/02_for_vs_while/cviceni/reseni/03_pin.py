# Řešení cvičení 3 – For versus while
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Ptej se na PIN tak dlouho, dokud uživatel nezadá "1234".
#    Kolikrát se splete dopředu nevíme -> while.
pin = input("Zadej PIN: ")
while pin != "1234":
    print("Špatný PIN.")
    pin = input("Zadej PIN: ")
print("Odemčeno!")
