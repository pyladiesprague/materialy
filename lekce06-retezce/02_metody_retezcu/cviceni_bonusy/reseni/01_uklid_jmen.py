# Řešení bonusu 1 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Tři jména přišla z formuláře rozbitá – mezery na krajích a náhodná
#    velikost písmen. U každého vypiš jeden řádek: uklizené jméno
#    a k němu přihlašovací jméno, které z něj vyrobíš. To je celé
#    malými písmeny a místo mezery má tečku.
#
#    Pro "  anna NOVÁKOVÁ  " má vyjít:
#    Anna Nováková -> anna.nováková

jmeno1 = "  anna NOVÁKOVÁ  "
jmeno2 = "PETRA svobodová"
jmeno3 = " tereza Dvořáková   "


def uklid(jmeno):
    cele = jmeno.strip().title()
    prihlasovaci = cele.lower().replace(" ", ".")
    print(f"{cele} -> {prihlasovaci}")


uklid(jmeno1)
uklid(jmeno2)
uklid(jmeno3)

# title() udělá velké první písmeno každého slova a zbytek malý,
# takže srovná i NOVÁKOVÁ na Nováková.
#
# replace(" ", ".") vymění každou mezeru za tečku. Protože jméno
# prošlo přes strip(), žádná mezera navíc na kraji nezůstala –
# jinak by z ní vznikla tečka.
