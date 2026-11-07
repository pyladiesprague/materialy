# ---------------------------------------------
#  Z textu seznam a zpátky
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# Kamarádka ti poslala jména ve zprávě. Metoda split rozdělí text na
# seznam podle oddělovače, který jí zadáš:
zprava = "Anna, Petra, Jana"
hoste = zprava.split(", ")

print(hoste)                # ['Anna', 'Petra', 'Jana']
print(len(hoste))           # 3


# Bez oddělovače dělí split podle mezer:
print("Python je fajn".split())     # ['Python', 'je', 'fajn']


# Metoda join dělá opak: z mnoha textů udělá jeden. Na první pohled
# vypadá obráceně. Tečku nepíšeš za seznam, ale za text, který bude mezi
# položkami. Seznam patří do závorek:
#
#     " a ".join(hoste)
#     ─────      ─────
#       │          └── seznam, který se má spojit
#       └── oddělovač, který přijde mezi položky
oddelovac = " a "
veta = oddelovac.join(hoste)
print(veta)                 # Anna a Petra a Jana

# Obvykle se to píše na jeden řádek, bez proměnné na oddělovač:
print(", ".join(hoste))     # Anna, Petra, Jana


# Položky musí být texty. Čísla join spojit neumí:
stoly = ["1", "2", "3"]
print("+".join(stoly))      # 1+2+3
