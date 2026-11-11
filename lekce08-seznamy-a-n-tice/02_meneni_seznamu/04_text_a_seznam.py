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


# Oddělovač může být jakýkoli text. Třeba recept na koktejl:
suroviny = ["rum", "limeta", "máta", "cukr"]
print(" + ".join(suroviny))     # rum + limeta + máta + cukr

# Nebo prázdný text. Pak se položky slepí bez mezery:
slabiky = ["po", "hád", "ka"]
print("".join(slabiky))         # pohádka

# Položky ale musí být texty. Seznam čísel join nespojí a program spadne
# s chybou TypeError.
