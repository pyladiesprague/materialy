# ---------------------------------------------
#  Když klíč chybí
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

darky = {"Anna": "dort", "Petra": "víno", "Jana": "chlebíčky"}


# Zápis in znáš z lekce 8. U slovníku hledá mezi klíči, ne mezi hodnotami:
print("Petra" in darky)     # True
print("víno" in darky)      # False – víno je hodnota, ne klíč


# Čtení klíče, který ve slovníku není, skončí chybou. Uvidíš ji na konci
# souboru. Proto se před čtením hodí zeptat, jestli tam klíč je:
jmeno = "Karel"

if jmeno in darky:
    print(darky[jmeno])
else:
    print(f"{jmeno} není na seznamu.")     # Karel není na seznamu.


# Kratší cesta je metoda get. Když klíč chybí, nespadne a vrátí None,
# které znáš z lekce 5:
print(darky.get("Petra"))   # víno
print(darky.get("Karel"))   # None

# Jestli jsi dostala None, zjistíš zápisem is None:
darek = darky.get("Karel")

if darek is None:
    print("Karel nic nepřinese.")   # Karel nic nepřinese.

# Jako druhý argument můžeš metodě get dát hodnotu, kterou má vrátit
# místo None:
print(darky.get("Karel", "nic"))    # nic


# Klíče rozlišují velká a malá písmena. "petra" je jiný klíč než "Petra":
print("petra" in darky)     # False


# Když klíč chybí a čteš ho hranatými závorkami, program spadne. Je to
# obdoba IndexError ze seznamů: čteš něco, co tam není.
print(darky["Karel"])       # KeyError: 'Karel'
