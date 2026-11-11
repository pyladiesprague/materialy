# ---------------------------------------------
#  Slovník ve funkci a kopie
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Se slovníkem je to stejné jako se seznamem v lekci 8. Funkce dostane
# ten samý slovník, a když ho změní, je to vidět i venku:
def pridej_skupinu(host):
    if host["vek"] < 18:
        host["skupina"] = "dítě"
    else:
        host["skupina"] = "dospělý"


anna = {"jmeno": "Anna", "vek": 34}
pridej_skupinu(anna)
print(anna)     # {'jmeno': 'Anna', 'vek': 34, 'skupina': 'dospělý'}

# Funkce nic nevrací, a přesto se slovník změnil. Někdy je to přesně to,
# co chceš. Funkce pak upraví všechny záznamy v seznamu jedním cyklem:
hoste = [{"jmeno": "Petra", "vek": 25}, {"jmeno": "Tom", "vek": 9}]

for host in hoste:
    pridej_skupinu(host)

print(hoste)
# [{'jmeno': 'Petra', 'vek': 25, 'skupina': 'dospělý'},
#  {'jmeno': 'Tom', 'vek': 9, 'skupina': 'dítě'}]


# Pozor na to i mimo funkce. Přiřazení slovník nezkopíruje, obě proměnné
# pak ukazují na jeden slovník:
jana = {"jmeno": "Jana", "vek": 41}
druha = jana
druha["vek"] = 99
print(jana["vek"])          # 99


# Když původní slovník změnit nechceš, udělej si kopii metodou copy.
# Funguje stejně jako u seznamů v lekci 8 (soubor 07_dve_jmena.py):
def s_kontaktem(host, telefon):
    novy = host.copy()
    novy["telefon"] = telefon
    return novy


jana = {"jmeno": "Jana", "vek": 41}
jana_s_kontaktem = s_kontaktem(jana, "608 999 000")

print(jana_s_kontaktem)     # {'jmeno': 'Jana', 'vek': 41, 'telefon': '608 999 000'}
print(jana)                 # {'jmeno': 'Jana', 'vek': 41}


# Shrnutí celé lekce. Slovník se hodí na tři věci:
#
#     hledání podle klíče      ceník, telefonní seznam, překlady
#     počítání a skupiny       hlasy pro písničky, kdo přinese co
#     záznam o jedné věci      host se jménem, věkem a dárkem
#
# Seznam slovníků je pak celá tabulka. Přesně s těmihle třemi postupy
# budeš pracovat na sobotním workshopu.
