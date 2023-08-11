# n-tice (tuple)
Sú to vlastne len nemeniteľné (**immutable**) zoznamy. 

Pythonovský typ tuple dokáže robiť skoro všetko to isté ako list okrem mutable operácií. Takže to najprv zhrňme a potom si ukážeme, ako to pracuje:

* operácia + na zreťazovanie (spájanie dvoch n-tíc)

* operácia * na viacnásobné zreťazovanie (viacnásobné spájanie jednej n-tice)

* operácia in na zisťovanie, či sa nejaká hodnota nachádza v n-tici

* operácia indexovania [i] na zistenie hodnoty prvku na zadanom indexe

* operácia rezu [i:j:k] na zistenie hodnoty nejakej podčasti n-tice

* relačné operácie ==, !=, <, <=, >, >= na porovnávanie obsahu dvoch n-tíc

* metódy count() a index() na zisťovanie počtu výskytov, resp. indexu prvého výskytu

* prechádzanie n-tice pomocou for-cyklu (iterovanie)

* štandardné funkcie len(), sum(), min(), max() ktoré zisťujú niečo o prvkoch n-tice

Takže n-tice, tak ako aj zoznamy sú štruktúrované typy, t.j. sú to typy, ktoré obsahujú hodnoty nejakých (možno rôznych) typov (sú to tzv. kolekcie):

* konštanty typu n-tica uzatvárame do okrúhlych zátvoriek a navzájom oddeľujeme čiarkami

* funkcia len() vráti počet prvkov n-tice, napríklad:

~~~
stred = (150, 100)
zviera = ('slon', 2013, 'gray')

print(stred)
    (150, 100)

print(zviera)
    ('slon', 2013, 'gray')

nic = ()
print(nic)
    ()

len(stred)
    2

len(zviera)
    3

len(nic)
    0

type(stred)
    <class 'tuple'>
~~~
Vidíte, že n-tica môže byť aj prázdna, označujeme ju **()** a vtedy má počet prvkov 0 (teda len(()) je 0). Ak n-tica nie je prázdna, hodnoty sú navzájom oddelené čiarkami.

> ## n-tica s jednou hodnotou
Pre jednoprvkovú n-ticu musíme do zátvoriek zapísať aj čiarku:
~~~
p = (12,)

print(p)
    (12,)

len(p)
    1

type(p)
    <class 'tuple'>
~~~
n-ticu s jednou hodnotou teda nemôžeme zapísať takto:
~~~
p = (12)

print(p)
    12

type(p)
    <class 'int'>
~~~
**Ak zapíšeme ľubovoľnú hodnotu do zátvoriek, nie je to n-tica (v našom prípade je to len jedno celé číslo).**

> ## Pre Python sú dôležitejšie čiarky ako zátvorky. V mnohých prípadoch si Python zátvorky domyslí (čiarky si nedomyslí nikdy):
~~~
stred = 150, 100
zviera = 'slon', 2013, 'gray'
p = 12,

print(stred)
(150, 100)

print(zviera)
('slon', 2013, 'gray')

print(p)
(12,)
~~~
Aj na tomto príklade vidíme význam a funkciu čiarok. Našli ste ste rozdiel medzi premennými **a** a **b** ?
~~~
a = 3.14
b = 3,14

print(a, type(a))
    3.14 <class 'float'>

print(b, type(b))
    (3, 14) <class 'tuple'>
~~~


> ## Funkcia tuple()
Vyrobí n-ticu z ľubovoľnej postupnosti (z iterovateľného objektu, t.j. takého objektu, ktorý sa dá prechádzať for-cyklom), napríklad zo znakového reťazca, zo zoznamu, vygenerovanej postupnosti celých čísel pomocou range(), ale iterovateľný je aj otvorený textový súbor. Znakový reťazec funkcia tuple() rozoberie na znaky:
~~~
tuple = tuple('Python')
print(tuple)

('P', 'y', 't', 'h', 'o', 'n')
~~~
n-tice môžeme vytvoriť aj pomocou funkcie range():
~~~
rozsah = tuple(range(1, 16))
print(rozsah)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

a = tuple(range(1000000))
print(len(a))
1000000
~~~
Podobne môžeme skonštruovať n-ticu z textového súboru. Predpokladajme, že súbor styri_riadky.txt obsahuje tieto 4 riadky:
~~~
prvy
druhy
treti
stvrty

potom
with open('C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\Aplikovana_Informatika\\11_hodina\\styri_riadky.txt', encoding="utf-8") as t:
    obsah = tuple(t)
print(obsah)

('prvy\n', 'druhy\n', 'treti\n', 'stvrty\n')
~~~
Kedy riadky súboru styri_riadky.txt sa postupne stanú prvkami n-tice.
Pokračovanie č. I

