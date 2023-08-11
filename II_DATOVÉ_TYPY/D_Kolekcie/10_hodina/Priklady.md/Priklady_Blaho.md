https://python.input.sk/z/08.html#zoznamy dole

1. Napíš funkciu vypis_typy(zoznam), ktorá vypíše všetky prvky zoznamu a ku každému vypíše informáciu o jeho type: ak je to int alebo float, tak vypíše 'číslo'; ak je to str, tak vypíše 'reťazec'; inak všetky ostatné typy vypíše ako 'iný typ'. Napríklad:
~~~
vypis_typy([12, 'x', None, 3.14, [], range(5), '123'])
    12 - číslo
    x - reťazec
    None - iný typ
    3.14 - číslo
    [] - iný typ
    range(0, 5) - iný typ
    123 - reťazec
~~~
Môžeš využiť takýto test: if type(prvok) == str: ....


2. Napíš funkciu nakup(zoznam), ktorá spracuje nákupný zoznam a vráti jeho celkovú cenu. Vstupný zoznam obsahuje dvojice čísel v tvare [koľko, cena, koľko, cena, ...], ktorý pre každý nakúpený tovar označuje jeho množstvo (koľko) a jednotkovú cenu (cena). Napríklad:
~~~
cena = nakup([3, 2.5, 0.5, 10, 1.2, 1.2])
cena
    13.94
~~~
3. Napíš funkciu sucin(zoznam), ktorá vráti (return) súčin prvkov zoznamu (zoznam obsahuje len čísla). Ak je zoznam prázdny, funkcia vráti 1. Napríklad:
~~~
c = [2, 3, 5, 7, 11]
sucin(c)                     # čo je 2*3*5*7*11
2310

sucin(list(range(1, 11)))    # čo je 10 faktorial
3628800

sucin([2] * 20)              # čo je 2 ** 20
1048576
~~~
4. Napíš funkciu vypis(zoznam, pocet=1), ktorá prvky daného zoznamu vypíše tak, že v každom riadku (možno okrem posledného) vypíše presne zadaný pocet prvkov zoznamu. Funkcia nemodifikuje vstupný zoznam. Napríklad:
~~~
zoz = list(range(1, 19))
vypis(zoz, 4)
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    17 18
zoz
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
vypis(list('Python'), 2)
    P y
    t h
    o n
vypis(['prvy', 'druhy', 'treti'])
    prvy
    druhy
    treti
~~~

5. Napíš funkciu spoj(zoznam, retazec=''), ktorá z daného zoznamu hodnôt (čísel alebo reťazcov) vyrobí jeden reťazec, ktorý obsahuje všetky prvky zoznamu, pričom medzi tieto hodnoty vloží zadaný retazec. Napríklad:
~~~
spoj(['12', 3, '456', '7'], '+')
    '12+3+456+7'
spoj(['12', 3, '456', 7], ' <=> ')
    '12 <=> 3 <=> 456 <=> 7'
spoj([], '*')
    ''
spoj(list('python'), '*')
    'p*y*t*h*o*n'
spoj(list(range(11, 20)))
    '111213141516171819'
~~~
6. Napíš funkciu zacina(zoznam, zacina_retazcom), ktorá vráti zoznam tých prvkov, ktoré začínajú zadaným podreťazcom. Vstupný zoznam obsahuje len znakové reťazce. Napríklad:

m = ['hela', 'adam', 'boris', 'adela', 'bobo', 'miso', 'hektor', 'borka', 'mino']
zacina(m, 'mi')
    ['miso', 'mino']
print(zacina(m, 'bor'))
    ['boris', 'borka']
print(zacina(m, 'b'))
    ['boris', 'bobo', 'borka']

Napíš funkciu zostupne(zoznam), ktorá zistí, či sú prvky vstupného zoznamu usporiadané zostupne (každý prvok v zozname nie je väčší ako jeho predchádzajúci). Funkcia vráti (return) True alebo False, nemodifikuje vstupný zoznam a nič nevypisuje. Nepoužívaj sort ani sorted. Napríklad:

zostupne([5, 5, 4, 4, 4, 2, 1])
    True
zostupne([5, 5, 4, 4, 1, 2, 1])
    False
zostupne(['zu', 'ta', 'si', 'mu', 'el'])
    True

Napíš funkciu postupnost(start, koniec, krok=1), ktorá vytvorí (vráti) takýto zoznam čísel: jeho prvky sú hodnoty od start do koniec krokom krok (podobne ako range(start, koniec, krok), ale funkcia postupnost by mohla fungovať aj pre desatinné čísla). Nepouži pritom štandardnú funkciu range(). Napríklad:

postupnost(3, 100, 7)
    [3, 10, 17, 24, 31, 38, 45, 52, 59, 66, 73, 80, 87, 94]
postupnost(20, 0, -2)
    [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
postupnost(1, 5, 0)
    []
postupnost(0, 3, 0.5)
    [0, 0.5, 1.0, 1.5, 2.0, 2.5]

Napíš funkciu sucet(zoznam1, zoznam2), ktorá sčíta/zlepí dva zoznamy čísel/reťazcov po prvkoch. Tieto zoznamy môžu byť rôzne dlhé. Napríklad:

sucet([1, 20, 3, 40], [10, 2, 30, 4])
    [11, 22, 33, 44]
sucet([2, 3, 4, 5, 6, 7], [10, 20, 30])
    [12, 23, 34, 5, 6, 7]
sucet([], [2, 3, 5, 7])
    [2, 3, 5, 7]
sucet(['1.', '2.', '3.', '4.'], list('python'))
    ['1.p', '2.y', '3.t', '4.h', 'o', 'n']

Napíš funkciu kresli_kruhy(zoznam, r), ktorá z daného zoznamu farieb nakreslí rad farebných kruhov, Každý kruh má polomer r. Funkcia nemodifikuje vstupný zoznam. Napríklad:

import tkinter

def kresli_kruhy(zoznam, r):
    ...

canvas = tkinter.Canvas()
canvas.pack()

kresli_kruhy(['red', 'red', 'blue', 'orange', 'green', 'yellow'], 20)

tkinter.mainloop()
nakreslí:

../_images/08_c01.png

Napíš funkciu kresli_stvorce(zoznam), ktorá z daného zoznamu čísel (veľkostí) a farieb nakreslí rad farebných štvorcov, Funkcia nemodifikuje vstupný zoznam. Napríklad:

import tkinter

def kresli_stvorce(zoznam):
    ...

canvas = tkinter.Canvas()
canvas.pack()

kresli_stvorce([50, 'red', 100, 'blue', 70, 'yellow', 120, 'pink'])

tkinter.mainloop()
nakreslí:

../_images/08_c02.png

Napíš najprv funkciu nahodny_zoznam(n, od, do), ktorá vygeneruje n-prvkový zoznam náhodných čísel z ontervalu <od, do>. Potom napíš ďalšiu funkciu histogram(zoznam), ktorá z daného zoznamu čísel (môže byť vygenerovaný pomocou nahodny_zoznam(...)) nakreslí stĺpcový diagram (obdĺžniky rovnakej šírky a výšky podľa číselnej hodnoty zo zoznamu). Obdĺžniky budú mať takú šírku, aby čo najlepšie vyplnili šírku plochy 360 a budú mať náhodne zafarbenú výplň. Funkcia nemodifikuje vstupný zoznam. Môžeš počítať s tým, že všetky hodnoty v zozname nie sú väčšie ako 240. Napríklad:

import tkinter
import random

def nahodny_zoznam(n, od, do):
    ...

def histogram(zoznam):
    ...

canvas = tkinter.Canvas()
canvas.pack()

zoz = nahodny_zoznam(20, 10, 240)
print(zoz)
histogram(zoz)

tkinter.mainloop()
môže vypísať:

[113, 107, 103, 192, 203, 141, 77, 72, 84, 126, 106, 220, 47, 28, 170, 237, 100, 105, 218, 12]
a nakresliť:

../_images/08_c03.png

Napíš funkciu kresli_polygon(zoznam_x, zoznam_y), ktorá dostáva dva rovnakodlhé zoznamy čísel - tieto obsahujú postupnosti x-ových a y-ových súradníc bodov v grafickej ploche. Aby sme z týchto bodov mohli nakresliť polygon, treba z týchto dvoch zoznamov vytvoriť jeden, v korom sa budú striedať príslušné x-ové a y-ové súradnice. Funkcia potom nakreslí polygón s náhodne zafarbenou výplňou. Napríklad:

import tkinter
import random

def kresli_polygon(zoznam_x, zoznam_y):
    ...

canvas = tkinter.Canvas()
canvas.pack()

kresli_polygon([50, 150, 120, 60, 220], [10, 50, 200, 120, 150])

tkinter.mainloop()
nakreslí:

../_images/08_c04.png
Ak využijeme funkciu nahodny_zoznam(...) z predchádzajúcej úlohy, môže to vyzerať napríklad takto:

kresli_polygon(nahodny_zoznam(20, 10, 360), nahodny_zoznam(20, 10, 250))
../_images/08_c05.png

Napíš funkciu replace_novy(zoznam, co, zaco), ktorá vráti nový zoznam: v tomto novom zozname budú všetky prvky s hodnotou co nahradené hodnotou zaco. Ostatné prvy sa prekopírujú. Napríklad:

zoz = [12, 13, 14, 13, 11, 14, 15, 13]
novy = replace_novy(zoz, 13, 'x')
novy
    [12, 'x', 14, 'x', 11, 14, 15, 'x']
zoz
    [12, 13, 14, 13, 11, 14, 15, 13]
replace_novy([1, 2] * 10, 1, 9)
    [9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2]

Napíš funkciu replace(zoznam, co, zaco), ktorá v danom zozname všetky výskyty hodnoty co nahradí hodnotou zaco. Funkcia nič nevracia ani nevypisuje, len modifikuje obsah zoznamu. Napríklad:

zoz = [12, 13, 14, 13, 11, 14, 15, 13]
replace(zoz, 13, 'x')
zoz
    [12, 'x', 14, 'x', 11, 14, 15, 'x']
zoz = [1, 2] * 10
replace(zoz, 1, 9)
zoz
    [9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2]

Napíš funkciu dvojice(zoznam), ktorá v danom zozname spočíta (alebo zreťazí) dvojice prvkov. Teda spočíta/zreťazí (operácia +) prvý a druhý prvok a oba nahradí týmto súčtom, potom to isté s tretím a štvrtým, potom piatym a šiestym, atď. Funkcia nič nevracia ani nevypisuje, len modifikuje obsah zoznamu. Napríklad:

z = list('programovanie')
dvojice(z)
z
    ['pr', 'og', 'ra', 'mo', 'va', 'ni', 'e']
z = list(range(1, 11))
z
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dvojice(z)
z
    [3, 7, 11, 15, 19]
dvojice(z)
z
    [10, 26, 19]

Napíš funkciu fibonacci(zoznam, n), ktorá dostáva nejaký aspoň dvojprvkový zoznam čísel. Do tohto zoznamu pridá ďalších n čísel tak, že každé je súčtom dvoch predchádzajúcich. VFunkcia nič nevracia, len modifikuje vstupný zoznam. Napríklad:

zoz = [0, 1]
fibonacci(zoz, 10)
zoz
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibonacci(zoz, 5)
zoz
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
zoz = [0, -2]
fibonacci(zoz, 10)
zoz
    [0, -2, -2, -4, -6, -10, -16, -26, -42, -68, -110, -178]

Napíš funkciu rozklad(cislo), ktorá rozloží dané celé číslo cislo na prvočinitele (súčin prvočísel). Výsledkom funkcie bude zoznam týchto prvočísel (prvočiniteľov). Funkcia nič nevypisuje. Napríklad:

r = rozklad(478632)
r
    [2, 2, 2, 3, 7, 7, 11, 37]
rozklad(43)
    [43]
Zrejme, ak by sme použili funkciu sucin(...) z 3. úlohy, mohli by sme skontrolovať správnosť funkcie rozklad:

sucin(rozklad(478632))
    478632

Napíš funkciu zoznam_cifier(cislo), ktorá z daného nezáporného celého čísla vytvorí zoznam jeho cifier. Funkcia nič nevypisuje, len vráti (return) nejaký zoznam čísel. Napríklad:

zoznam_cifier(478632)
    [4, 7, 8, 6, 3, 2]
zoznam_cifier(111111111 ** 2)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Napíš funkciu cislo_zo_zoznamu(zoznam), ktorá z daného zoznamu cifier (jednociferné celé čísla) poskladá pôvodné celé číslo (obrátená funkcia k zoznam_cifier()). Funkcia nič nevypisuje, len vráti (return) nejaké číslo. Napríklad:

cislo_zo_zoznamu(list(range(1, 10)))
    123456789
cislo_zo_zoznamu(zoznam_cifier(2 ** 20))
    1048576

Napíš funkciu citaj_cisla(meno_suboru), ktorá prečíta daný textový súbor. V tomto súbore sa v každom riadku nachádza jedno celé číslo, prípadne nejaké medzery na začiatku a na konci. Funkcia vráti zoznam týchto celých čísel. Funkcia nič nevypisuje, len vráti (return) nejaký zoznam čísel. Napríklad:

print('123\n 45\n  678  \n-9 ', file=open('cisla.txt', 'w'))
citaj_cisla('cisla.txt')
    [123, 45, 678, -9]

Napíš funkciu prevrat(meno_suboru), ktorá prevráti poradie riadkov v danom textovom súbore. Funkcia nič nevypisuje ani nevracia, len zmení obsah zadaného textového súboru. Napríklad:

print('prvy\n druhy\n  treti\nstvrty', file=open('text.txt', 'w'))
prevrat('text.txt')
print(open('text.txt').read(), end='')
    stvrty
      treti
     druhy
    prvy


Napíš funkciu stvorec(x, y, r, uhol), ktorá vytvorí (vráti) 8-prvkový zoznam čísel v tvare [x, y, x, y, x, y, x, y]. Tieto čísla sú súradnicami štyroch vrcholov štvorca v grafickej ploche a tieto vrcholy ležia na kružnici so stredom (x, y) s polomerom r. Vrcholy štvorca budú na kružnici natočené o daný uhol. Ak by si tento zoznam poslal ako parameter do grafického príkazu canvas.create_polygon, dostaneš vyfarbený natočený štvorec. Napríklad:

import tkinter
from math import sin, cos, radians

def stvorec(x, y, r, uhol):
    ...

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_polygon(stvorec(180, 130, 110, 20), fill='red')
canvas.create_polygon(stvorec(180, 130, 90, 45), fill='green')
canvas.create_polygon(stvorec(180, 130, 70, 70), fill='gold')
canvas.create_polygon(stvorec(180, 130, 50, 95), fill='blue')

tkinter.mainloop()
nakreslí:

../_images/08_c06.png
