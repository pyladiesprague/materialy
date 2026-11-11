# Řešení cvičení 10 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Hosté poslali odpovědi na pozvánku v jedné zprávě. Píšou, jak je
# napadne, takže ano může být i " ano" nebo "Ano". Program má vypsat:
#
#   Pozvaných: 5
#   Přijde: 3
#   Přijdou: ['Anna', 'Eva', 'Jana']
#   Omluvení: ['Petra', 'Marie']

zprava = "Anna:ano, Petra:ne, Jana: ano, Eva:Ano, Marie:ne"


def vsechna_jmena(zprava):
    jmena = []
    for odpoved in zprava.split(", "):
        casti = odpoved.split(":")
        jmena.append(casti[0])
    return jmena


def kdo_se_omluvil(zprava):
    omluveni = []
    for odpoved in zprava.split(", "):
        casti = odpoved.split(":")
        if casti[1].strip().lower() != "ano":
            omluveni.append(casti[0])
    return omluveni


hoste = vsechna_jmena(zprava)
omluveni = kdo_se_omluvil(zprava)

prijdou = hoste.copy()
for host in omluveni:
    prijdou.remove(host)

prijdou.sort()

print(f"Pozvaných: {len(hoste)}")
print(f"Přijde: {len(prijdou)}")
print(f"Přijdou: {prijdou}")
print(f"Omluvení: {omluveni}")


# 1. TypeError: object of type 'NoneType' has no len().
#    Metoda sort vrací None, takže prijdou = prijdou.sort() seznam ztratí.
#    Stačí zavolat prijdou.sort() bez přiřazení.
#
#    Program doběhne, ale vypíše Pozvaných: 1 a Přijde: 1.
#
# 2. Breakpoint do kdo_se_omluvil ukáže v panelu Variables casti.
#    U Jany je casti[1] " ano", u Evy "Ano". Ani jedno se nerovná "ano",
#    takže se počítají jako omluvené. Pomůže strip() a lower().
#
#    Přijde už je správně 3, ale Pozvaných je pořád 3 místo 5.
#
# 3. Funkce jsou teď v pořádku. Breakpoint na cyklus for ukáže, že hoste
#    se zmenšují spolu s prijdou. Řádek prijdou = hoste nedělá kopii, obě
#    proměnné ukazují na stejný seznam. Pomůže hoste.copy().
