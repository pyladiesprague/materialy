# Cvičení 2 – Záznamy
# Doplň kód pod zadání a soubor spusť (Run).

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
