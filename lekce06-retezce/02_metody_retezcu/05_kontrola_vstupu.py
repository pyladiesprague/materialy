# ---------------------------------------------
#  Kontrola vstupu
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.


# Metoda isdigit() odpoví, jestli jsou v textu jenom číslice:
print("42".isdigit())       # True
print("ahoj".isdigit())     # False
print("4.2".isdigit())      # False – tečka není číslice


# Z input() chodí vždycky text. Než ho pustíš do int(), vyplatí se
# zeptat, jestli je co převádět:
def za_rok(vstup):
    if vstup.isdigit():
        print(f"Za rok ti bude {int(vstup) + 1}")
    else:
        print("To není číslo.")


za_rok("30")        # Za rok ti bude 31
za_rok("třicet")    # To není číslo.
za_rok("")          # To není číslo.


# Bez té kontroly program na stejné hodnotě spadne na ValueError:
print(int("třicet"))
