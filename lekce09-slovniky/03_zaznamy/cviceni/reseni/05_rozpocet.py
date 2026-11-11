# Řešení cvičení 5 – Záznamy
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Plánovala jsi, kolik utratíš za večírek, a teď víš, kolik jsi
#    opravdu utratila. U každé položky vypiš, o kolik jsi plán překročila
#    nebo kolik ušetřila. Na konci vypiš, kolik jsi utratila celkem
#    a kolik jsi plánovala.
#
#      jídlo: přes plán o 220 Kč
#      pití: ušetřeno 150 Kč
#      výzdoba: přesně podle plánu
#      Celkem utraceno 2670 Kč z plánovaných 2600 Kč.

rozpocet = {
    "jídlo": {"plan": 1500, "utraceno": 1720},
    "pití": {"plan": 800, "utraceno": 650},
    "výzdoba": {"plan": 300, "utraceno": 300},
}

celkem_plan = 0
celkem_utraceno = 0

for polozka, castky in rozpocet.items():
    plan = castky["plan"]
    utraceno = castky["utraceno"]
    celkem_plan = celkem_plan + plan
    celkem_utraceno = celkem_utraceno + utraceno

    if utraceno > plan:
        print(f"{polozka}: přes plán o {utraceno - plan} Kč")
    elif utraceno < plan:
        print(f"{polozka}: ušetřeno {plan - utraceno} Kč")
    else:
        print(f"{polozka}: přesně podle plánu")

print(f"Celkem utraceno {celkem_utraceno} Kč z plánovaných {celkem_plan} Kč.")
