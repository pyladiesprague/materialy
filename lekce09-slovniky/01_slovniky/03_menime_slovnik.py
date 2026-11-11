# ---------------------------------------------
#  Slovník se dá měnit
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

darky = {"Anna": "dort", "Petra": "víno"}


# Slovník nemá append. Novou dvojici přidáš přiřazením:
darky["Jana"] = "chlebíčky"
print(darky)    # {'Anna': 'dort', 'Petra': 'víno', 'Jana': 'chlebíčky'}

# Dvojice zůstávají v pořadí, v jakém jsi je přidala.


# Stejný zápis hodnotu přepíše, když klíč už ve slovníku je. Petra si
# to rozmyslela:
darky["Petra"] = "džus"
print(darky)    # {'Anna': 'dort', 'Petra': 'džus', 'Jana': 'chlebíčky'}

# Každý klíč je ve slovníku jen jednou, takže druhá Petra nevznikne.
# Hodnoty se opakovat můžou:
darky["Eva"] = "dort"
print(darky)    # {'Anna': 'dort', 'Petra': 'džus', 'Jana': 'chlebíčky', 'Eva': 'dort'}


# Jana se omluvila. Metodu pop znáš ze seznamů. U slovníku odebere
# dvojici podle klíče a vrátí její hodnotu:
darek = darky.pop("Jana")
print(darek)    # chlebíčky
print(darky)    # {'Anna': 'dort', 'Petra': 'džus', 'Eva': 'dort'}


# Hodnotu můžeš změnit i výpočtem. Kolik kdo vypil sklenek:
sklenky = {"Anna": 1, "Petra": 2}

sklenky["Anna"] = sklenky["Anna"] + 1
print(sklenky)  # {'Anna': 2, 'Petra': 2}

# Je to stejné jako pocet = pocet + 1 z lekce 3. Nejdřív se vyhodnotí
# pravá strana: přečte se 1, přičte se 1 a výsledek 2 se uloží zpátky
# pod klíč "Anna".
