# Řešení cvičení 2 – Záznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Na filmový večer hosté obodovali filmy od 1 do 10. Napiš tři funkce,
#    které mají na vstupu seznam filmů:
#    - filmy_od_roku má na vstupu ještě rok a vrátí seznam názvů filmů
#      natočených v tom roce nebo později,
#    - prumer_bodu vrátí průměrný počet bodů,
#    - nejlepsi_film vrátí celý záznam filmu s nejvíc body.
#
#    Když je seznam prázdný, vrátí prumer_bodu a nejlepsi_film None.
#    Pak pomocí funkcí vypiš:
#
#      Od roku 2000: Kytice, Tmavomodrý svět, Samotáři
#      Průměr: 7.5
#      Nejlepší: Pelíšky (9 bodů)

filmy = [
    {"nazev": "Vesničko má středisková", "rok": 1985, "body": 8},
    {"nazev": "Kytice", "rok": 2000, "body": 6},
    {"nazev": "Tmavomodrý svět", "rok": 2001, "body": 7},
    {"nazev": "Pelíšky", "rok": 1999, "body": 9},
    {"nazev": "Samotáři", "rok": 2000, "body": 8},
    {"nazev": "Obecná škola", "rok": 1991, "body": 7},
]


def filmy_od_roku(filmy, rok):
    nazvy = []
    for film in filmy:
        if film["rok"] >= rok:
            nazvy.append(film["nazev"])
    return nazvy


def prumer_bodu(filmy):
    if len(filmy) == 0:
        return None

    soucet = 0
    for film in filmy:
        soucet = soucet + film["body"]
    return soucet / len(filmy)


def nejlepsi_film(filmy):
    if len(filmy) == 0:
        return None

    nejlepsi = filmy[0]
    for film in filmy:
        if film["body"] > nejlepsi["body"]:
            nejlepsi = film
    return nejlepsi


print(f"Od roku 2000: {', '.join(filmy_od_roku(filmy, 2000))}")
print(f"Průměr: {prumer_bodu(filmy):.1f}")

nejlepsi = nejlepsi_film(filmy)
print(f"Nejlepší: {nejlepsi['nazev']} ({nejlepsi['body']} bodů)")

# U nejlepšího filmu si stačí pamatovat celý záznam. Název i body
# z něj pak přečteš.
#
# Kontrola prázdného seznamu je ve funkcích první. Bez ní by průměr
# spadl na dělení nulou a filmy[0] na IndexError.
