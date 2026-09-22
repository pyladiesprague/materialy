# ---------------------------------------------
#  return funkci ukončí
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Jakmile Python narazí na return, funkci opustí. Řádky pod ním
# se už neprovedou:

def pozdrav_a_vrat(jmeno):
    print("Zdravím,", jmeno)
    return "hotovo"
    print("Tenhle řádek se nikdy nevypíše.")


print(pozdrav_a_vrat("Anno"))


# Funkce může mít returnů víc. Použije se ten, ke kterému program dojde
# jako k prvnímu – takhle si funkce vybírá z několika odpovědí:
def ohodnot_znamku(znamka):
    if znamka == 1:
        return "Výborně"
    elif znamka == 2:
        return "Chvalitebně"
    elif znamka == 3:
        return "Dobře"
    else:
        return "Ještě zabereme"


for znamka in range(1, 6):
    print(znamka, "->", ohodnot_znamku(znamka))


# Tuhle funkci jsi psala i v minulé složce, tam ale hodnocení rovnou
# vypisovala. Teď ho vrací, takže si volající může vybrat, co s ním –
# vypsat ho, uložit, nebo poslat do další funkce.
hodnoceni = ohodnot_znamku(1)
print("Na vysvědčení bude:", hodnoceni)
