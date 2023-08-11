# Operácie nad n-ticami

> ## Indexovanie
n-tice indexujeme rovnako ako sme indexovali zoznamy:

* prvky postupnosti môžeme indexovať v [] zátvorkách, pričom index musí byť od 0 až po počet prvkov-1

* pomocou rezu (slice) vieme indexovať časť n-tice (niečo ako podreťazec) tak, že [] zátvoriek zapíšeme aj dvojbodku:

    * ntica[od:do] n-tica z prvkov s indexmi od až po do-1

    * ntica[:do] n-tica z prvkov od začiatku až po prvok s indexom do-1

    * ntica[od:] n-tica z prvkov s indexmi od až po koniec n-tice

    * ntica[od:do:krok] n-tica z prvkov s indexmi od až po do-1, pričom berieme každý krok prvok

Niekoľko príkladov:
~~~
prvo = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
prvo[2]
    5

prvo[2:5]
    (5, 7, 11)

prvo[4:5]
    (11,)

prvo[:5]
    (2, 3, 5, 7, 11)

prvo[5:]
    (13, 17, 19, 23, 29)

prvo[::2]
    (2, 5, 11, 17, 23)

prvo[::-1]
    (29, 23, 19, 17, 13, 11, 7, 5, 3, 2)
~~~
Vidíme, že **s n-ticami pracujeme** veľmi **podobne ako** sme pracovali **so znakovými reťazcami a so zoznamami**. Keď sme ale do znakového reťazca chceli pridať jeden znak (alebo aj viac), museli sme to robiť rozoberaním a potom skladaním:
~~~
prvo = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
prvo = prvo[:5] + ('fuj',) + prvo[5:]
print(prvo)

(2, 3, 5, 7, 11, 'fuj', 13, 17, 19, 23, 29)
~~~
V príklade pred 5-ty prvok vložíme nejaký znakový reťazec (fuj).

Rovnako nemôžeme zmeniť ani hodnotu nejakého znaku reťazca obyčajným priradením:
~~~
ret = 'Python'
ret[2] = 'X'
    ...
TypeError: 'str' object does not support item assignment

ret = ret[:2] + 'X' + ret[3:]
ret
'PyXhon'

ntica = (2, 3, 5, 7, 11, 13)
ntica[2] = 'haha'
    ...
TypeError: 'tuple' object does not support item assignment

ntica = ntica[:2] + ('haha',) + ntica[3:]
ntica
(2, 3, 'haha', 7, 11, 13)
~~~
Všimnite si, že Python vyhlásil rovnakú chybu pre tuple ako pre string.
**Hovoríme, že ani reťazce ani n-tice nie sú meniteľné (teda sú immutable) !!!**

> ## Porovnávanie n-tíc
Porovnávanie n-tíc je veľmi podobné ako porovnávanie reťazcov a zoznamov. Pripomeňme si, ako je to pri zoznamoch:

* postupne porovnáva i-te prvky oboch zoznamov, kým sú rovnaké; pri prvej nerovnosti je výsledkom porovnanie týchto dvoch hodnôt

* ak je pri prvej nezhode v prvom zozname menšia hodnota ako v druhom, tak prvý zoznam je menší ako druhý

* ak je prvý zoznam kratší ako druhý a zodpovedajúce prvky sa zhodujú, tak prvý zoznam je menší ako druhý

Hovoríme tomu **lexikografické** porovnávanie.

Teda aj pri porovnávaní n-tíc sa budú postupne porovnávať zodpovedajúce si prvky a pri prvej nerovnosti sa skontroluje, ktorý z týchto prvkov je menší. Treba tu ale dodržiavať jedno veľmi dôležité pravidlo: porovnávať hodnoty napríklad na menší môžeme len vtedy, keď sú zhodných typu:
~~~
5 < 'a'
    ...
    TypeError: unorderable types: int() < str()

(1, 5, 10) < (1, 'a', 10)
    ...
    TypeError: unorderable types: int() < str()

(1, 5, 10) != (1, 'a', 10)
    True
~~~
Najlepšie je porovnávať také n-tice, ktoré majú prvky rovnakého typu. Pri n-ticiach, ktoré majú zmiešané typy si musíme dávať väčší pozor:
~~~
('Janko', 'Hrasko', 'Zilina') < ('Janko', 'Jesensky', 'Martin')
True

(1, 2, 3, 4, 5, 5, 6, 7, 8) < tuple(range(1, 9))
True

('Janko', 'Hrasko', 2008) < ('Janko', 'Hrasko', 2007)
False
~~~
Pokračovanie č. I

