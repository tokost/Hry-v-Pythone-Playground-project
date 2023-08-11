Pokračovanie č. I

> ## Viacnásobné priradenie n-tíc
Najprv pripomeňme, ako funguje viacnásobné priradenie: ak je pred znakom priradenia = viac premenných, ktoré sú oddelené čiarkami, tak za znakom priradenia musí byť iterovateľný objekt, ktorý má presne toľko hodnôt, ako počet premenných. Iterovateľným objektom môže byť zoznam (list), n-tica (tuple), znakový reťazec (str), generovaná postupnosť čísel (range()) ale aj otvorený textový súbor (open()), ktorý má presne toľko riadkov, koľko je premenných v priradení.

Ak do jednej premennej priraďujeme viac hodnôt oddelených čiarkou, Python to chápe ako priradenie n-tice. Pozrite nasledovné priradenia.

> ### Priradíme n-ticu
~~~
a1, a2, a3, a4 = 3.14, 'joj', len, (1, 3, 5)
print(a1, a2, a3, a4)

3.14 joj <built-in function len> (1, 3, 5)

a, b, c, d, e, f = 3 * (5, 7)
print(a, b, c, d, e, f)

5 7 5 7 5 7
~~~
> ### Priradíme vygenerovanú postupnosť 4 čísel
~~~
a, b, c, d = range(2, 6)
print(a, b, c, d)

2 3 4 5
~~~
> ### Priradíme znakový reťazec
~~~
d, e, f, g, h, i = 'Python'
print(d, e, f, g, h, i)

P y t h o n
~~~
> ### Priradíme riadky textového súboru
~~~
with open('C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\\Aplikovana_Informatika\\13_hodina\\dva.txt', 'w') as f:
    f.write('first\nsecond\n')

with open('C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\\Aplikovana_Informatika\\13_hodina\\dva.txt') as subor:
    prvy, druhy = subor

print(prvy)
'first\n'

print(druhy)
'second\n'
~~~
čo vieme zapísať (v dôsledku rôznorodosťi programovania) aj takto:
~~~
prvy, druhy = open(''C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\\Aplikovana_Informatika\\13_hodina\\dva.txt')
~~~
Tento posledný príklad je veľmi umelý a v praxi sa asi priamo do premenných takto čítať nebude.

Viacnásobné priradenie používame napríklad aj na výmenu obsahu dvoch (aj viac) premenných:
~~~
x, y, z = y, z, x
~~~
Aj v tomto príklade je na pravej strane priradenia (za =) n-tica: (y, z, x).

> ### n-tica ako návratová hodnota funkcie
V Pythone sa dosť využíva to, že návratovou hodnotou funkcie môže byť n-tica, t.j. výsledkom funkcie je naraz niekoľko návratových hodnôt. Napríklad nasledovný príklad počíta celočíselné delenie a súčasne zvyšok po delení:
~~~
def zisti(a, b):
    return a // b, a % b
~~~
Funkciu môžeme použiť napríklad takto:
~~~
podiel, zvysok = zisti(153, 33)
print('podiel =', podiel, 'zvysok =', zvysok)

podiel = 4 zvysok = 21
~~~
Ak z výsledku takejto funkcie potrebujeme použiť len jednu z hodnôt, môžeme zapísať:
~~~
print('zvysok =', zisti(153, 33)[1])
~~~
Ďalšia funkcia vráti postupnosť všetkých deliteľov nejakého čísla:
~~~
def delitele(cislo):
    vysl = ()
    for i in range(1, cislo+1):
        if cislo % i == 0:
            vysl = vysl + (i,)
    return vysl
~~~
Na záver otestujeme:
~~~
deli = delitele(24)
print(deli)

(1, 2, 3, 4, 6, 8, 12, 24)

if 2 in deli:
        print('parne')
parne

print('sucet delitelov =', sum(deli))
sucet delitelov = 60

print('je prvocislo =', len(delitele(int(input('zadaj cislo: '))))==2)
zadaj cislo: 11213
je prvocislo = True

print('je prvocislo =', len(delitele(int(input('zadaj cislo: '))))==2)
zadaj cislo: 1001
je prvocislo = False
~~~
> **Poznatkom tohoto testovania je, že keď je výsledkom n-tica, tak ju môžeme ďalej rôzne spracovať alebo testovať.**

> ### Ďalšie funkcie a metódy n-tíc
S n-ticami vedia pracovať nasledovné štandardné funkcie:

* len(ntica) - vráti počet prvkov n-tice

* sum(ntica) - vypočíta súčet prvkov n-tice (všetky musia byť čísla)

* min(ntica) - zistí najmenší prvok n-tice (prvky sa musia dať navzájom porovnať, nemôžeme tu miešať rôzne typy)

* max(ntica) - zistí najväčší prvok n-tice (ako pri min() ani tu sa nemôžu typy prvkov miešať)

Na rozdiel od zoznamov a znakových reťazcov, ktoré majú veľké množstvo metód, n-tice majú len dve:

* ntica.count(hodnota) - zistí počet výskytov nejakej hodnoty v n-tici

* ntica.index(hodnota) - vráti index (poradie) v n-tici prvého (najľavejšieho) výskytu danej hodnoty, ak sa hodnota v n-tici nenachádza, metóda spôsobí spadnutie na chybe (ValueError: tuple.index(x): x not in tuple)

Ukážme tieto funkcie na malom príklade. V n-tici uložíme niekoľko nameraných teplôt a potom vypíšeme priemernú, minimálnu aj maximálnu teplotu:
~~~
teploty = (14, 22, 19.5, 17.1, 20, 20.4, 18)
print('počet nameraných teplôt: ', len(teploty))
počet nameraných teplôt:  7

print('minimálna teplota: ', min(teploty))
minimálna teplota:  14

print('maximálna teplota: ', max(teploty))
maximálna teplota:  22

print('priemerná teplota: ', round(sum(teploty) / len(teploty), 2))
priemerná teplota:  18.71
~~~
Ďalej môžeme zistiť, kedy bola nameraná konkrétna hodnota:
~~~
teploty.index(20)
4

teploty.index(20.1)
    ...
ValueError: tuple.index(x): x not in tuple
~~~
Môžeme zistiť, koľko-krát sa nejaká konkrétna teplota vyskytla v našich meraniach:
~~~
teploty.count(20)
1

teploty.count(20.1)
0
~~~