# Řešení bonusu 2 – And, or a not
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Vstup do klubu. Dovnitř smí ten, komu je aspoň 18 let A ZÁROVEŇ
#     je buď členem, NEBO má pozvánku.
#     Kdo má zákaz vstupu, dovnitř nesmí nikdy – ani člen, ani s pozvánkou.
#     Zamysli se, kam patří závorky, aby podmínka fungovala správně.
#     Vypiš "Vítej v klubu." / "Dnes se nedostaneš.".

vek = 20
je_clen = False
ma_pozvanku = True
ma_zakaz = True

if not ma_zakaz and vek >= 18 and (je_clen or ma_pozvanku):
    print("Vítej v klubu.")
else:
    print("Dnes se nedostaneš.")
