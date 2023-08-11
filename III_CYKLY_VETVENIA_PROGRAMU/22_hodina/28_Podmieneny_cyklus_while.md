># Podmienený cyklus - while

V Pythone existuje konštrukcia cyklu, ktorá opakuje vykonávanie postupnosti príkazov v závislosti od splnenia nejakej podmienky. V podstate tu spojíme príkazy for a if o ktorých sme si už povedali vyššie:
~~~
while podmienka:              # opakuj príkazy, kým platí podmienka
    prikaz
    prikaz
    ...
~~~
Vidíme podobnosť s podmieneným príkazom if - vetvením. 

Tento nový príkaz postupne:

* zistí hodnotu podmienky, ktorá je zapísaná za slovom while
* ak má táto podmienka hodnotu False, blok príkazov, ktorý je telom cyklu, sa preskočí a pokračuje sa na nasledovnom príkaze za celým while-cyklom (podobne ako v príkaze if), hovoríme, že sa ukončilo vykonávanie cyklu
* ak má podmienka hodnotu True, vykonajú sa všetky príkazy v tele cyklu (odsunutom bloku príkazov)
* a znovu sa testuje podmienka za slovom while, t.j. celé sa to opakuje

Najprv zapíšeme príklad pomocou, for-cyklu:
~~~
for i in range(1, 21):
    print(i, i * i)
~~~
Vypíše tabuľku druhých mocnín čísel od 1 do 20. Prepis na cyklus while znamená, že zostavíme podmienku, ktorá bude testovať, napr. premennú i: tá nesmie byť väčšia ako 20. Samozrejme, že už pred prvou kontrolou premennej i v podmienke cyklu while, musí mať nejakú hodnotu:
~~~
i = 1
while i < 21:
    print(i, i * i)
    i += 1
~~~
V cykle sa vykoná print() a zvýši sa hodnota premennej i o jedna.

>**while-cykly** sa ale častejšie používajú vtedy, keď zápis pomocou for-cyklu je príliš komplikovaný, alebo sa ani urobiť nedá.

Cyklus while je možné tak ako v prípade if použiť v spokjení s príkazom else. Jeho syntax je nasledujúci:
~~~
while podmienka:
    blok_príkazov
else:
    blok_príkazov
~~~
Blok while pokračuje vo vykonávaní príkazov tak dlho, kým platí podmienka. Ak podmienka neplatí, vykoná sa **nepovinný blok else**. Blok else sa ale nevykoná v prípade, že sa z cyklu vyskočí napr. pomocou príkazov break alebo return ktoré sú spomenuté nižšie.

>### Uvedomme si, že podmienka nehovorí, kedy má cyklus skončiť, ale naopak - kým podmienka platí, vykonávajú sa všetky príkazy v tele cyklu.

Vyššie sme zostavili program, ktorý zisťoval, či je zadané číslo prvočíslo. Použili sme for-cyklus, v ktorom sme zadané číslo postupne delili všetkými číslami, ktoré sú menšie ako samotné číslo. Ak si uvedomíme, že na zisťovanie prvočísla nepotrebujeme skutočný počet deliteľov, ale malo by nám stačiť zistenie, či existuje aspoň jeden deliteľ. Keď sa vyskytne prvý deliteľ (t.j. platí cislo % delitel != 0), cyklus môžeme ukončiť a vyhlásiť, že číslo nie je prvočíslo. Ak ani jedno číslo nie je deliteľom nášho čísla, hodnota premennej delitel dosiahne cislo a to je situácia, keď cyklus tiež skončí (t.j. keď delitel == cislo, našli sme prvočíslo). Zapíšeme to while-cyklom:
~~~
cislo = int(input('Zadaj číslo: '))
delitel = 2
while delitel < cislo and cislo % delitel != 0:
    delitel = delitel + 1

if delitel == cislo:
    print(cislo, 'je prvočíslo')
else:
    print(cislo, 'nie je prvočíslo')
~~~
Do podmienky while-cyklu sme pridali novú časť. Operátor and tu označuje to, že aby sa cyklus opakoval, musia byť splnené obe časti. Uvedomte si, že **cyklus skončí vtedy**, keď prestane platiť zadaná podmienka, t.j. (a ďalej to matematicky upravíme):

* not (delitel < cislo and cislo % delitel != 0)
* not delitel < cislo or not cislo % delitel != 0
* delitel >= cislo or cislo % delitel == 0

**while-cyklus teda skončí vtedy, keď delitel >= cislo, alebo cislo % delitel == 0**

>## Nekonečný cyklus
Cyklus s podmienkou, ktorá má stále hodnotu True, bude nekonečný. Napr.
~~~
i = 0
while i < 10:
    i -= 1
~~~
Nikdy neskončí, lebo premenná i bude stále menšia ako 10. Takéto výpočty môžeme prerušiť stlačením klávesov **Ctrl/C**.

Aj nasledovný cyklus je úmyselne nekonečný:
~~~
while 1:
    pass
~~~
V Pythone existuje príkaz **break**, ktorý môžeme použiť v tele cyklu a vtedy sa zvyšok cyklu nevykoná. V tomto prípade sa bude pokračovať až na príkazoch za cyklom (funguje to aj pre cyklus for nielen pre while). Najčastejšie sa break vyskytuje v príkaze if, napr.
~~~
sucet = 0
while True:
    retazec = input('zadaj cislo: ')
    if retazec == '':
        break
    sucet += int(retazec)
print('sucet precitanych cisel =', sucet)
~~~
V tomto príklade sa čítajú čísla zo vstupu, kým nezadáme prázdny reťazec: vtedy cyklus končí a program vypíše súčet prečítaných čísel.
~~~
for i in range(1000):
...     if i % 3 == 0:
...         print('hups')
...         continue
...     if i > 10:
...         print('konec')
...         break;
...     print(i)
~~~

Ak chceme po prechode do vetvy s else napr. iba výpísať nejakú správu môžeme k tomu použiť kľúčové slovo **pass** ktoré sa používa kedykoľvek ak chceme aby daná časť kódu nič nerobila.
~~~
print("Dotieravá aplikácia")
pokracovat = True
while pokracovat:
    slovo = input("\nNapíšte Python pre ukončenie: ")
    if (slovo == "Python" or slovo == "python"):
        print("\nSlovo zadané!")
        pokracovat = False
    else:
        pass # nič sa nestane
input("\nAplikáciu ukončíte stlačením ľubovoľného klávesu...")
~~~
~~~
all = [1, 2, 3 ,4, 5]
>>> for i in all:
...     if i == 100:
...         print('Hurra, je tu 100')
...         break
...     else:                 # Kdyby byl potreba blok else pro if, tak je tu.
...         pass              # Neni potreba :-)
... else:                     # else cyklu for - je odsazene stejne jako for
...     print('Sto nenalezeno')
~~~