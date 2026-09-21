# Řešení cvičení 1 – Procházení textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Analýza věty. Uživatel zadá větu. Projdi ji znak po znaku a vypiš
#    počet znaků, počet samohlásek, počet mezer a počet slov ve větě.
#    (Počet slov = počet mezer + 1.)

veta = input("Napiš větu: ")
samohlasky = 0
mezery = 0
for znak in veta:
    if znak in "aeiou":
        samohlasky = samohlasky + 1
    if znak == " ":
        mezery = mezery + 1
print("Počet znaků:", len(veta))
print("Samohlásek:", samohlasky)
print("Mezer:", mezery)
print("Slov:", mezery + 1)              # slov je o jedno víc než mezer
