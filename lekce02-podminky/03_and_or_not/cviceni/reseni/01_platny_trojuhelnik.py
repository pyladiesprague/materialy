# Řešení cvičení 1 – And, or a not
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Platný trojúhelník. Ze tří stran jde sestavit trojúhelník jen tehdy,
#    když je součet každých dvou stran větší než ta třetí.
#    Vypiš "Platný trojúhelník." / "Takový trojúhelník nejde.".

a = 3
b = 4
c = 5
if a + b > c and a + c > b and b + c > a:
    print("Platný trojúhelník.")
else:
    print("Takový trojúhelník nejde.")
