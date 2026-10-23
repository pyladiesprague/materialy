# Řešení bonusu 2 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na heslo a zkontroluj tři věci:
#    je aspoň osm znaků dlouhé, je v něm aspoň jedna číslice
#    a je v něm aspoň jedno velké písmeno.
#
#    Ke každé podmínce vypiš, jestli prošla. Na konec vypiš, jestli
#    je heslo přijaté – to je, jen když prošly všechny tři.
#
#    Na číslici se zeptáš průchodem přes znaky: cyklus for z lekce 3
#    a isdigit() na každý znak.
#    Na velké písmeno stačí porovnat heslo se sebou samým po lower().

heslo = input("Zadej heslo: ")

dost_dlouhe = len(heslo) >= 8
ma_velke = heslo != heslo.lower()

ma_cislici = False
for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break

print(f"Aspoň osm znaků:  {dost_dlouhe}")
print(f"Obsahuje číslici: {ma_cislici}")
print(f"Velké písmeno:    {ma_velke}")

if dost_dlouhe and ma_cislici and ma_velke:
    print("Heslo přijato.")
else:
    print("Heslo nevyhovuje.")

# isdigit() na celém hesle by se ptalo, jestli jsou číslice všechny
# znaky. Tady potřebuješ vědět, jestli je číslice aspoň jedna – proto
# cyklus. Break ho ukončí, jakmile je jasno.
#
# heslo != heslo.lower() funguje proto, že lower() vrací nový řetězec.
# Když se od původního liší, bylo v něm velké písmeno.
