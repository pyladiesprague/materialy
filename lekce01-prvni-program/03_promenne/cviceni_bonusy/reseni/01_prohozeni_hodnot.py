# Řešení bonusu 1 – Proměnné
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Máš dvě proměnné: a = 5 a b = 3.
#     Prohoď jejich hodnoty tak, aby v a bylo 3 a v b bylo 5.
#     Nakonec obě vypiš.

a = 5
b = 3
pomocna = a   # dočasně si schováme hodnotu a
a = b
b = pomocna
print(a, b)
