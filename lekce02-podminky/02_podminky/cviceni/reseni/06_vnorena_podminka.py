# Řešení cvičení 6 – Podmínky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vnořená podmínka s otázkami na uživatele.
#    Zeptej se: "Máš hlad? (ano/ne)" a ulož odpověď do proměnné hlad.
#    Když má hlad, zeptej se ještě "Máš doma jídlo? (ano/ne)":
#      - když má jídlo, vypiš "Uvař si."
#      - když nemá, vypiš "Objednej si."
#    Když nemá hlad, vypiš "Tak nic, uvidíme později.".

hlad = input("Máš hlad? (ano/ne) ")
if hlad == "ano":
    jidlo = input("Máš doma jídlo? (ano/ne) ")
    if jidlo == "ano":
        print("Uvař si.")
    else:
        print("Objednej si.")
else:
    print("Tak nic, uvidíme později.")
