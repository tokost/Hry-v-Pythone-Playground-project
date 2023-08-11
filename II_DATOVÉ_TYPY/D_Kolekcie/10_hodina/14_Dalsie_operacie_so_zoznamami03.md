Pokračovanie č. III

> ## Zmena hodnoty prvku zoznamu

Dátová štruktúra zoznam je **meniteľný typ (tzv. mutable)** - môžeme meniť hodnoty prvkov zoznamu, napríklad takto:
~~~
studenti = ['Juraj Janosik', 'Emma Drobna', 'Ludovit Stur', 'Pavol Habera', 'Margita Figuli']
studenti[3]

Zobrazenie výsledku :
    'Pavol Habera'

studenti[3] = 'Janko Hrasko'
studenti[2] = 'Guido van Rossum'

Zobrazenie výsledku :
studenti
    ['Juraj Janosik', 'Emma Drobna', 'Guido van Rossum', 'Janko Hrasko', 'Margita Figuli', 'Karel Capek']
~~~
Hodnoty prvkov zoznamu môžeme zmeniť aj v cykle, ale k prvkom musíme pristupovať pomocou indexov, napríklad sme zistili, že náš teplomer ukazuje o 2 stupne menej ako je reálna teplota, preto opravíme t.j. zmen=ime všetky prvky zoznamu nasledovne:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i in range(7):
    teploty[i] = teploty[i] + 2
print(teploty)

Zobrazenie výsledku :
[12, 15, 17, 20, 19, 14, 14]
~~~
Dá sa to tiež zapísať využitím štandardnej funkcie len(), ktorá vráti počet prvkov zoznamu:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i in range(len(teploty)):
    teploty[i] += 2
print(teploty)
~~~
Pri tejto príležitosti si treba uvedomiť, že ak by sme prvky zoznamu neindexovali, ale prechádzali by sme ich priamo cez premennú cyklu prvok, tak náš zámer nedosiahneme:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for prvok in teploty:
    prvok += 2
print(teploty)

Zobrazenie výsledku :
[10, 13, 15, 18, 17, 12, 12]
~~~
Je to preto, lebo samotný zoznam sa tým nemení: **menili sme iba obsah premennej cyklu prvok** a obsah zoznamu zostal nezmenený. Preto je dobré si predstaviť, čo sa vlastne deje v pamäti pri zmene hodnoty prvku zoznamu. Zoberme si pôvodný päť prvkový zoznam prvočísel:
~~~
ab = [2, 3, 5, 7, 11]
~~~
Zmenou obsahu jedného prvku zoznamu sa zmení jediná referencia, všetko ostatné zostáva bez zmeny:
~~~
ab[2] = 55
~~~

![](./Tahaky_dokumenty_obrazky/Priradenie_do%20_jedneho_prvku.png)


Priraďovaním do jedného prvku zoznamu sa tento zoznam modifikuje, hovoríme, že priradenie do prvku je **mutable** operácia. Ukážme šablónu, pomocou ktorej vieme v cykle priradiť do rôznych prvkov rôzne hodnoty.

> ### Šablóna na vytváranie zoznamu
Táto šablóna umožňuje v cykle priradiť do prvkov zoznamu rôzne hodnoty bez toho aby vzniklo opakované prepísanie iba jednej hodnoty. **Príslušné indexy zoznamu však už musia existovať**. Najlepšie takýto zoznam pripravíme jedným priradením a viacnásobným zreťazením, napríklad pre n prvkov:
~~~
zoznam = [None] * n
for i in range(n):
    zoznam[i] = ... výpočet hodnoty
print(zoznam)
~~~
Ako príklad použitia tejto šablóny vytvoríme zoznamu prvých n druhých mocnín čísel od 0 do n-1 : kedy hodnotu premennej n načítame z klávesnice pomocou vstavanej funkcie input():
~~~
n = int(input('zadaj n: '))
mocniny = [None] * n
for i in range(n):
    mocniny[i] = i * i
print(mocniny)
~~~
Kedy hodnotu premennej n načítame z klávesnice pomocou novej vstavanej vstupnej funkcie **input()** ktorá po zadaní hodnoty čaká na stlačenie klávesy Enter:
~~~
zadaj n: 14
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
~~~
Pokračovanie č. IV


