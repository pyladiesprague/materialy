# ---------------------------------------------
#  Proč slovník
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Na konci lekce 8 jsi hledala, co přinese Petra. Seznam dvojic jsi
# musela projít cyklem, dokud jsi ji nenašla:
darky = [("Anna", "dort"), ("Petra", "víno"), ("Jana", "chlebíčky")]

for jmeno, darek in darky:
    if jmeno == "Petra":
        print(darek)        # víno


# Slovník si ke každému klíči pamatuje hodnotu. Píše se do složených
# závorek. Před dvojtečkou je klíč, za ní hodnota a dvojice oddělují čárky:
darky = {"Anna": "dort", "Petra": "víno", "Jana": "chlebíčky"}

# Hodnotu dostaneš rovnou podle klíče, bez cyklu:
print(darky["Petra"])       # víno

print(darky)        # {'Anna': 'dort', 'Petra': 'víno', 'Jana': 'chlebíčky'}
print(len(darky))   # 3 – počet dvojic

# Když v f-stringu čteš hodnotu podle textového klíče, napiš klíč do
# apostrofů. Stejné uvozovky jako kolem celého f-stringu by ho ukončily:
print(f"Petra přinese {darky['Petra']}.")   # Petra přinese víno.


# Odkud ten název? Funguje jako překladový slovník: najdeš slovo
# a vedle něj stojí překlad. Anglicky se mu říká dictionary, v Pythonu
# zkráceně dict. To slovo uvidíš v chybových hláškách.
preklady = {"pes": "dog", "kočka": "cat", "večírek": "party"}
print(preklady["večírek"])  # party


# Hledá se jen jedním směrem. V telefonním seznamu najdeš podle jména
# číslo, ale podle čísla jméno ne:
telefony = {"Anna": "602 111 222", "Petra": "731 333 444"}
print(telefony["Anna"])     # 602 111 222


# U seznamu je klíčem pořadí (index). U slovníku si klíč vybereš sama.
# Nejčastěji je to text, ale může to být i číslo:
stoly = {1: "Anna", 2: "Petra", 7: "Jana"}
print(stoly[7])             # Jana

# Tady 7 neznamená osmou položku. Je to klíč 7 a slovník má jen tři dvojice.


# Hodnotou může být cokoli, co znáš: text, číslo, True a False, seznam
# i n-tice. Klíčem bývá text nebo číslo:
oblibene = {"Anna": ["dort", "víno"], "Petra": ["džus"]}
print(oblibene["Anna"])     # ['dort', 'víno']
