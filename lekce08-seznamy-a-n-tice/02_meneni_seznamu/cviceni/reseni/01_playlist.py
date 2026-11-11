# Řešení cvičení 1 – Měnění seznamů
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Spravuješ playlist na večírek. Postupně:
#    - první skladbu přesuň na konec,
#    - na druhé místo vlož přání "Jožin z bažin",
#    - odeber skladbu "Holky z naší školky",
#    - vypiš playlist.
#
#    Vyjít má:  ['Severní vítr', 'Jožin z bažin', 'Trezor']

playlist = ["Trezor", "Severní vítr", "Holky z naší školky"]

prvni = playlist.pop(0)
playlist.append(prvni)
playlist.insert(1, "Jožin z bažin")
playlist.remove("Holky z naší školky")
print(playlist)
