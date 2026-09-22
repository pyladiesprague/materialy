# ---------------------------------------------
#  Proč vlastní funkce
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Funkce používáš od první lekce, jenom jsme jim tak neříkali:
#
#   print("Ahoj")       vypíše text
#   input("Jméno: ")    počká na odpověď
#   len("Ahoj")         spočítá znaky
#   round(3.14159, 2)   zaokrouhlí
#   randrange(1, 7)     hodí kostkou
#
# Pokaždé je to stejné: napíšeš jméno funkce, do závorek pošleš hodnoty,
# se kterými má pracovat, a ona odvede svoji práci. Kdo ji napsal a co
# je uvnitř, řešit nemusíš.
#
# Tyhle funkce má Python připravené. Na všechno ale hotová funkce být
# nemůže – co budeš zrovna potřebovat, dopředu nikdo netuší.
# Vlastní funkci si proto napíšeš sama. Třeba takovou, která zkontroluje,
# jestli je heslo dost dlouhé.
#
# Nejdřív se podíváme, jak taková kontrola vypadá bez ní.
# Heslo bereme jako dost dlouhé, když má aspoň 8 znaků:

moje_heslo = "kolo"
if len(moje_heslo) < 8:
    print(moje_heslo, "– moc krátké")
else:
    print(moje_heslo, "– dost dlouhé")

moje_heslo = "pyladies2026"
if len(moje_heslo) < 8:
    print(moje_heslo, "– moc krátké")
else:
    print(moje_heslo, "– dost dlouhé")

moje_heslo = "abc"
if len(moje_heslo) < 8:
    print(moje_heslo, "– moc krátké")
else:
    print(moje_heslo, "– dost dlouhé")


# Stejné čtyři řádky třikrát. Až se hranice změní z 8 na 10,
# musíme to opravit na třech místech a na žádné zapomenout.


# Kontrolu si proto pojmenujeme a napíšeme jenom jednou:
def zkontroluj_heslo(heslo):
    if len(heslo) < 8:
        print(heslo, "– moc krátké")
    else:
        print(heslo, "– dost dlouhé")


# Samotné def ještě nic nevypíše. Funkce se spustí, až když ji zavoláme:
zkontroluj_heslo("kolo")
zkontroluj_heslo("pyladies2026")
zkontroluj_heslo("abc")


# Takhle se definice čte:
#   def              = klíčové slovo (definuju funkci)
#   zkontroluj_heslo = jméno, které si volíš sama
#   (heslo)          = parametr, se kterým funkce pracuje
#   :                = dvojtečka na konci řádku
#   odsazení         = odsazené řádky jsou tělo funkce
