# Cvičení 10 – Měnění seznamů
# Jsou tu tři chyby a každá je jiného druhu. Jednu ti ukáže chybová
# hláška, další dvě najdeš debuggerem. Oprav je po jedné a po každé
# opravě program spusť.

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
        if casti[1] != "ano":
            omluveni.append(casti[0])
    return omluveni


hoste = vsechna_jmena(zprava)
omluveni = kdo_se_omluvil(zprava)

prijdou = hoste
for host in omluveni:
    prijdou.remove(host)

prijdou = prijdou.sort()

print(f"Pozvaných: {len(hoste)}")
print(f"Přijde: {len(prijdou)}")
print(f"Přijdou: {prijdou}")
print(f"Omluvení: {omluveni}")
