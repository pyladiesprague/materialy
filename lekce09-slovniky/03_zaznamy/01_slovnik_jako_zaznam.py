# ---------------------------------------------
#  Slovník jako záznam
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

# V lekci 8 jsi o hostovi držela víc údajů v n-tici:
anna = ("Anna", 34, "dort")
print(anna[1])          # 34

# Co je 34? Musíš si pamatovat, že na indexu 1 je věk.


# Slovník může držet údaje o jedné věci. Klíče jsou názvy údajů, takže
# je hned vidět, co je co:
anna = {"jmeno": "Anna", "vek": 34, "darek": "dort"}

print(anna["vek"])      # 34
print(f"{anna['jmeno']} přinese {anna['darek']}.")     # Anna přinese dort.

# V lekci 8 jsme si řekli, že míchat v seznamu různé druhy hodnot nebývá
# dobrý nápad. V záznamu je to naopak běžné: text, číslo, cokoli. Každý
# klíč má svůj vlastní údaj, takže víš, co pod ním najdeš.


# Údaj přidáš nebo změníš jako u každého slovníku:
anna["telefon"] = "602 111 222"
anna["darek"] = "koláč"
print(anna)
# {'jmeno': 'Anna', 'vek': 34, 'darek': 'koláč', 'telefon': '602 111 222'}


# Takhle může vypadat i výsledek funkce. V lekci 8 vracela funkce
# n-tici a ty sis musela pamatovat pořadí. Ve slovníku má každá hodnota
# jméno.
#
# Dlouhý slovník se dá rozepsat na víc řádků, jako seznam s kvízem
# v lekci 8. Každá dvojice na vlastním řádku se líp čte.
def statistika(veky):
    if len(veky) == 0:
        return {"pocet": 0, "prumer": None, "nejstarsi": None}

    return {
        "pocet": len(veky),
        "prumer": sum(veky) / len(veky),
        "nejstarsi": max(veky),
    }


vysledek = statistika([34, 25, 41])
print(f"{vysledek['prumer']:.1f}")     # 33.3
print(vysledek["nejstarsi"])    # 41

print(statistika([]))   # {'pocet': 0, 'prumer': None, 'nejstarsi': None}

# Prázdný seznam se kontroluje jako první. Jinak by funkce spadla
# na dělení nulou.
