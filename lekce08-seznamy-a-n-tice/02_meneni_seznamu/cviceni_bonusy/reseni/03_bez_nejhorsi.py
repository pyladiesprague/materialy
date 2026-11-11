# Řešení bonusu 3 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Napiš funkci bez_nejhorsi, která má na vstupu seznam známek a vrátí
#    nový seznam bez jedné nejhorší známky. Původní seznam se nesmí
#    změnit.
#
#    znamky = [1, 3, 2, 3]
#    print(bez_nejhorsi(znamky))     # [1, 2, 3]
#    print(znamky)                   # [1, 3, 2, 3]

def bez_nejhorsi(znamky):
    kopie = znamky.copy()
    kopie.remove(max(kopie))
    return kopie


znamky = [1, 3, 2, 3]
print(bez_nejhorsi(znamky))     # [1, 2, 3]
print(znamky)                   # [1, 3, 2, 3]
