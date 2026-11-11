# ---------------------------------------------
#  Funkce, která vrací víc hodnot
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Funkce vrací jednu hodnotu. Tou hodnotou ale může být n-tice. Tady
# rozsazujeme hosty ke stolům:
def rozsad(hoste, mist_u_stolu):
    return hoste // mist_u_stolu, hoste % mist_u_stolu


print(rozsad(17, 4))    # (4, 1)


# Za return nejsou závorky potřeba, čárky stačí. Výsledek hned rozbalíš:
stoly, zbyva = rozsad(17, 4)

print(f"Plných stolů: {stoly}")     # Plných stolů: 4
print(f"Zbývá hostů: {zbyva}")      # Zbývá hostů: 1


# Tak může funkce vrátit i dvě hodnoty ze seznamu:
def nejmladsi_a_nejstarsi(veky):
    return min(veky), max(veky)


mladsi, starsi = nejmladsi_a_nejstarsi([34, 25, 41])
print(f"Věk od {mladsi} do {starsi}")   # Věk od 25 do 41
