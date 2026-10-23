# ---------------------------------------------
#  Zaokrouhlení ve f-stringu
# ---------------------------------------------
# Spusť soubor a podívej se na první řádek výpisu.
#
# Ten ocas číslic na konci minulého souboru nebyl překlep. S desetinnými
# čísly počítá Python s drobnou nepřesností a na ceně je to vidět taky:

cena = 249
s_dph = cena * 1.21

print(f"Cena s DPH: {s_dph}")           # Cena s DPH: 301.28999999999996


# Dvojtečka a .2f za výrazem říkají: zaokrouhli na dvě desetinná místa.
print(f"Cena s DPH: {s_dph:.2f}")       # Cena s DPH: 301.29


# Zaokrouhlovat umí i funkce round(), kterou znáš z vestavěných funkcí.
# U částek, kterým druhé desetinné místo chybí, se obě cesty rozejdou:
zaloha = 200 * 1.21
print(round(zaloha, 2))                 # 242.0
print(f"{zaloha:.2f}")                  # 242.00
