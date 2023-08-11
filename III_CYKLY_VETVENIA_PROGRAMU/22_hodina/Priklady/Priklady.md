## Zisťovanie druhej odmocniny

Ukážeme, ako zistíme druhú odmocninu čísla aj bez volania funkcie math.sqrt(x), resp. umocňovaním na jednu polovicu x**0.5. Súčasne je to názorný príkad do úvodu vytvárania vlastných  lokálnych funkcii použitých vo vytváranom kóde našej aplikácie, alebo moduloch či funkcii zlúčených v knižniciach určených pre univerzálne a opakované používanie.
~~~
cislo = float(input('zadaj cislo:'))

x = 1
while x ** 2 < cislo:
    x = x + 1

print('odmocnina', cislo, 'je', x)
~~~
Takto nájdené riešenie je veľmi nepresné, lebo x zvyšujeme o 1, takže, napr. odmocninu z 26 vypočíta ako 6. Skúsme zjemniť krok, o ktorý sa mení hľadané x:
~~~
cislo = float(input('zadaj cislo:'))

x = 1
while x ** 2 < cislo:
    x = x + 0.001

print('odmocnina', cislo, 'je', x)
~~~
Teraz dáva program lepšie výsledky, ale pre väčšiu zadanú hodnotu mu to citeľne dlhšie trvá - skúste zadať napr. 10000000. Keďže mu vyšiel výsledok približne 3162.278 a dopracoval sa k nemu postupným pripočítavaním čísla 0.001 k štartovému 1, musel urobiť vyše 3 miliónov pripočítaní a tiež toľkokrát testov vo while-cykle (podmienky x ** 2 < cislo). Kvôli tomuto je takýto algoritmus nepoužiteľne pomalý.

Využijeme inú my+slienku:

* zvolíme si interval, v ktorom sa určite bude nachádzať hľadaný výsledok (hľadaná odmocnina), napr. nech je to interval <1, cislo> (pre čísla väčšie ako 1 je aj odmocnina väčšia ako 1 a určite je menšia ako samotne cislo)
* ako x (prvý odhad nášej hľadanej odmocniny) zvolíme stred tohto intervalu
* zistíme, či je druhá mocnina tohto x väčšia ako zadané cislo alebo menšia
* ak je väčšia, tak upravíme predpokladaný interval, tak že jeho hornú hranicu zmeníme na x
* ak je ale menšia, upravíme dolnú hranicu intervalu na x
* tým sa nám interval zmenšil na polovicu
* toto celé opakujeme, kým už nie je nájdené x dostatočne blízko k hľadanému výsledku, t.j. či sa nelíši od výsledku menej ako zvolený rozdiel (epsilón)

~~~
cislo = float(input('zadaj cislo:'))

od = 1
do = cislo

x = (od + do)/2

pocet = 0
while abs(x ** 2 - cislo) > 0.001:
    if x ** 2 > cislo:
        do = x
    else:
        od = x
    x = (od + do) / 2
    pocet += 1

print('druhá odmocnina', cislo, 'je', x)
print('počet prechodov while-cyklom bol', pocet)
~~~
Ak spustíme program pre 10000000 dostávame:
~~~
zadaj cislo:10000000
druhá odmocnina 10000000.0 je 3162.2776600480274
počet prechodov while-cyklom bol 44
~~~
čo je výrazné zlepšenie oproti predchádzajúcemu riešeniu, keď prechodov while-cyklom (hoci jednoduchších) bolo vyše 3 miliónov.

## Kalkulačka 

Teraz si skúsime vylepšiť našej kalkulačku. Program nám funguje, ale kalkulačka je len na "jedno" použitie. Ak chceme zadať ďalší príklad, musíme program spustiť znova. Preto si teraz kalkulačku mierne vylepšíme
jedným cyklom a podmienkou Hlavná časť kódu kalkulačky bude uzavretá v cykle, ktorý sa bude opakovať kým používateľ kalkulačku neukončí.

Tu je kód kalkulačky:
~~~
print("Kalkulačka\n")
pokracovat = True
while pokracovat:
    prvni_cislo = int(input("Zadajte prvé číslo: "))
    druhe_cislo = int(input("Zadajte druhé číslo: "))
    print("1 - sčítanie")
    print("2 - odčítanie")
    print("3 - násobenie")
    print("4 - delenie")
    print("5 - umocňovanie")
    cislo_operace = int(input("Zadajte číslo operácie: "))
    if cislo_operace == 1:
        print("Ich súčet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Ich rozdiel je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Ich súčin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        print("Ich podiel je:", prvni_cislo / druhe_cislo)
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná voľba!")
    nezadano = True
    while nezadano:
        odpoved = input("\nPrajete si zadať ďalší príklad? y / n: ")
        if (odpoved == "y" or odpoved == "Y"):
            nezadano = False
        elif (odpoved == "n" or odpoved == "N"):
            nezadano = False
            pokracovat = False
        else:
            pass
input("\nStlačte ľubovoľný kláves...")
~~~

A toto je pre tento diel všetko. V budúcej lekcii, Riešené úlohy k 4. lekcii Pythone , si ukážeme
prácu s n-ticami, zoznamy a funkcie zip() a
len(). https://www.itnetwork.sk/python/zaklady/python-riesenu-priklady-cykly-for 
V nasledujúcom cvičení, Riešené úlohy k 4. lekcii Pythone, si precvičíme nadobudnuté skúsenosti z predchádzajúcich lekcií.  Riešené úlohy k 4. lekcii Pythone , https://www.itnetwork.sk/python/zaklady/python-riesenu-priklady-cykly-for

