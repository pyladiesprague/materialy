# Řešení cvičení 4 – Slovníky
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Telefonní seznam. Ptej se "Jméno: ", dokud uživatel nenapíše "konec".
#    - Jméno uprav, ať projde i " anna" nebo "ANNA".
#    - Prázdné jméno přeskoč a zeptej se znovu.
#    - Když jméno v seznamu je, vypiš číslo.
#    - Když není, zeptej se "Číslo: " a ulož si ho.
#    Na konci vypiš celý seznam, každé jméno na vlastní řádek.
#
#      Jméno: anna
#      602 111 222
#      Jméno: Eva
#      Číslo: 777 555 666
#      Jméno: EVA
#      777 555 666
#      Jméno: konec
#      Anna: 602 111 222
#      Petra: 731 333 444
#      Eva: 777 555 666

telefony = {"Anna": "602 111 222", "Petra": "731 333 444"}

while True:
    jmeno = input("Jméno: ").strip().lower()
    if jmeno == "konec":
        break
    if jmeno == "":
        continue

    jmeno = jmeno.title()
    if jmeno in telefony:
        print(telefony[jmeno])
    else:
        telefony[jmeno] = input("Číslo: ").strip()

for jmeno, cislo in telefony.items():
    print(f"{jmeno}: {cislo}")

# Vstup se nejdřív zbaví mezer a převede na malá písmena. Díky tomu
# projde i "KONEC". Teprve potom dostane jméno velké první písmeno,
# aby sedělo s klíči ve slovníku.
