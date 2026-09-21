# Řešení bonusu 1 – And, or a not
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Druh trojúhelníku. Máš tři strany. Urči a vypiš, jaký to je
#     trojúhelník:
#       - "rovnostranný", když jsou všechny tři strany stejné,
#       - "rovnoramenný", když jsou aspoň dvě strany stejné,
#       - "různostranný", když jsou všechny strany různé.

a = 5
b = 5
c = 8
if a == b and b == c:
    print("rovnostranný")
elif a == b or b == c or a == c:
    print("rovnoramenný")
else:
    print("různostranný")
