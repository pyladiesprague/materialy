# ---------------------------------------------
#  Data v datech
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Seznam jako hodnotu ve slovníku znáš ze skupin v minulé sekci. Hodnotou
# může být i další slovník. Nové je tu čtení o dvě úrovně hluboko. Celý
# večírek v jedné proměnné:
vecirek = {
    "datum": "21. 11.",
    "hoste": ["Anna", "Petra", "Jana"],
    "rozpocet": {"jidlo": 1500, "piti": 800},
}


# Čte se to po krocích, stejně jako seznam slovníků. Pod klíčem "hoste"
# je seznam:
hoste = vecirek["hoste"]
print(hoste)                    # ['Anna', 'Petra', 'Jana']
print(hoste[0])                 # Anna

# Za sebou:
print(vecirek["hoste"][0])      # Anna


# Pod klíčem "rozpocet" je další slovník:
rozpocet = vecirek["rozpocet"]
print(rozpocet["piti"])         # 800

# Za sebou:
print(vecirek["rozpocet"]["piti"])      # 800

# Zápis za sebou je kratší, s mezikrokem přehlednější. Vyber si, co se
# ti líp čte.
#
# Když si nejsi jistá, co je pod klíčem schované, vypiš to. Hranaté
# závorky ve výpisu znamenají seznam, složené slovník.


# Měnit se to dá stejně. Přišla Eva a na pití se přidává 200 Kč:
vecirek["hoste"].append("Eva")
vecirek["rozpocet"]["piti"] = vecirek["rozpocet"]["piti"] + 200

print(vecirek["hoste"])         # ['Anna', 'Petra', 'Jana', 'Eva']
print(vecirek["rozpocet"])      # {'jidlo': 1500, 'piti': 1000}


# Celkový rozpočet sečteš přes hodnoty vnitřního slovníku:
print(sum(vecirek["rozpocet"].values()))       # 2500


# Data z webových služeb a ze souborů JSON vypadají přesně takhle:
# slovníky a seznamy v sobě. Potkáš je na workshopu.
