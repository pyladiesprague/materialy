# ---------------------------------------------
#  Metoda vrací nový řetězec
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.

slovo = "pyladies"

# Zavoláme metodu a s výsledkem nic neděláme:
slovo.upper()
print(slovo)            # pyladies

# Řádek se slovo.upper() proběhl. Velká písmena nikde nejsou, protože
# metoda výsledek vrátila a nikdo si ho nevzal. Je to stejná situace jako
# v lekci 5, kde funkce s return nic nevypsala, dokud sis návratovou
# hodnotu neuložila nebo nevytiskla.

print(slovo.upper())    # PYLADIES

velke = slovo.upper()
print(velke)            # PYLADIES

# Původní řetězec zůstal, jak byl:
print(slovo)            # pyladies


# Když chceš mít v proměnné upravený text, přepíšeš ji výsledkem:
slovo = slovo.upper()
print(slovo)            # PYLADIES
