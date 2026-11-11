# Řešení bonusu 2 – N-tice
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Funkce zip prochází dva seznamy vedle sebe a vrací dvojice:
#
#      for jmeno, vek in zip(jmena, veky):
#
#    Vypiš každou osobu na vlastní řádek a spočítej, kdo je nejstarší.
#
#      Anna: 30
#      Petra: 41
#      Jana: 27
#      Nejstarší: Petra

jmena = ["Anna", "Petra", "Jana"]
veky = [30, 41, 27]

nejstarsi = ""
nejvyssi_vek = 0

for jmeno, vek in zip(jmena, veky):
    print(f"{jmeno}: {vek}")
    if vek > nejvyssi_vek:
        nejvyssi_vek = vek
        nejstarsi = jmeno

print(f"Nejstarší: {nejstarsi}")
