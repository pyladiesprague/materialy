# ---------------------------------------------
#  N-tice: hodnoty, které patří k sobě
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

# Každý host něco přinese. K jednomu hostu teď patří dvě různé věci: jméno
# a dárek. Na to je tu n-tice. Píše se do kulatých závorek.
#
# Odkud ten název? Dvě hodnoty jsou dvojice, tři trojice, čtyři čtveřice.
# Písmeno n se v matematice píše místo čísla, které může být jakékoli.
# N-tice je tedy skupina n hodnot, ať je jich kolik chce. Anglicky se jí
# říká tuple, podle double a triple. To slovo uvidíš v chybových hláškách.
anna = ("Anna", "dort")             # dvojice
petra = ("Petra", "víno", 2)        # trojice

print(anna)         # ('Anna', 'dort')
print(petra)        # ('Petra', 'víno', 2)


# Čtení funguje stejně jako u seznamu:
print(anna[0])      # Anna
print(len(petra))   # 3


# Seznam použij, když máš víc věcí stejného druhu a jejich počet se může
# měnit. To jsou hosté. N-tici použij, když je hodnot pevný počet a patří
# k sobě. Často má každá pozice jiný význam, třeba jméno a dárek. Jindy
# jsou hodnoty stejného druhu, třeba souřadnice (3, 5).
#
# N-tici po vytvoření změnit nejde. Tak proč n-tice vůbec používat,
# když seznam umí všechno, co ony, a ještě víc?
#   - Co se měnit nemá, nezměníš omylem. Dvojice jméno a dárek zůstane
#     pohromadě a nikdo do ní nepřidá třetí hodnotu.
#   - Kdo čte kód, hned vidí, že hodnoty patří k sobě jako celek.
#   - V lekci 9 uvidíš, že n-tice může být klíčem ve slovníku. Seznam
#     ne, právě proto, že se dá měnit.
#
# N-tice proto nemá append a položku v ní nenahradíš:
anna[1] = "koláč"   # TypeError: 'tuple' object does not support item assignment
