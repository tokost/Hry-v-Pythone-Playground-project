Pokračovanie č. II

> ## Prechádzanie prvkov zoznamu

## Iterovanie zoznamu
**Iterovanie - opakovanie** sa najčastejšie vykonáva pomocou for-cyklu t.j opakovanému vykonávaniu rovnakých operácii (v našom prípade zobrazovania formátovaných údajov) pri ktorých sa menia parametre premennej i vystupujúcej najprv ako hodnota poradového čísla typu integer a neskôr ako index zoznamu. Napríklad:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i in range(7):
        print(f'{i}. deň', teploty[i])

 Zobrazenie výsledku :      
    0. deň 10
    1. deň 13
    2. deň 15
    3. deň 18
    4. deň 17
    5. deň 12
    6. deň 12
~~~

Využili sme indexovanie prvkov zoznamu indexmi od 0 do 6 a použili sme funkciu range() ktorá obmedzuje parameter i na 7 iterácii. Ak nepotrebujeme pracovať s indexmi, ale stačia nám samotné hodnoty, zapíšeme:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for prvok in teploty:
        print(prvok, end=', ')

Zobrazenie výsledku : 
    10, 13, 15, 18, 17, 12, 12,
~~~
## Enumerate zoznamu
Ďalšou vstavanou funkciou je **enumerate - odpočítavanie** ktorá nám umožňuje sledovať **počet iterácii (opakovaní)** v slučke:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i, prvok in enumerate(teploty):
        print(f'{i+1}. deň', prvok)

Zobrazenie výsledku :
    1. deň 10
    2. deň 13
    3. deň 15
    4. deň 18
    5. deň 17
    6. deň 12
    7. deň 12
~~~

## Výpočet priemernej hodnoty zoznamu
Takto môžeme napr. zapísať **výpočet priemernej hodnoty** - teploty:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = 0
for prvok in teploty:   # premenna prvok je parameter ako i ktory iteruje od 1 az po zastavenie ktore musime zabezpecit my aby sa to nezacyklilo
    sucet += prvok
priemer = sucet / 7
print(f'priemerná teplota je {priemer:.1f}')    # formátovanie desatinného čísla na jedno miesto

Zobrazenie výsledku :
priemerná teplota je 13.9
~~~
## Výpočet maximálnej hodnoty zoznamu
Podobne vieme zistiť, napríklad **maximálnu hodnotu v zozname**:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
mx = teploty[0]
for prvok in teploty:
    if mx < prvok:
        mx = prvok
print('najteplejšie bolo', mx, 'stupňov')

Zobrazenie výsledku :
najteplejšie bolo 18 stupňov
~~~
## Výpočet odchylok napr. nadpriemerne teplých dní zoznamu
Alebo zistenie počtu nadpriemerne teplých dní. Prečítaj kód s porozumením resp. pozri si to v online pythone https://pythontutor.com/ :
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = 0
for prvok in teploty:   # Pozor on iteruje cez poziciu zoznamu t.j. index ale do premennej prvok vklada hodnotu prvku !!!
    sucet += prvok
priemer = sucet / 7
pocet = 0
for prvok in teploty:
    if prvok > priemer:
        pocet += 1
print('počet nadpriemerne teplých dní', pocet)

Zobrazenie výsledku :
počet nadpriemerne teplých dní 3    # pricom priemerna hodnota je 13.8571
~~~

## Zhrnutie operácii prechodu zoznamom
Z týchto jednoduchých príkladov môžeme vytvoriť šablóny, ktoré niečo zisťujú o prvkoch zoznamu.
> ### Šablóna na zisťovanie hodnôt v zozname
Táto šablóna spočíta hodnoty prvkov (prvky by sme mohli, napríklad aj násobiť, alebo zreťazovať):
~~~
sucet = 0
for prvok in zoznam:
    sucet = sucet + prvok
print(sucet)
~~~

> ### Šablóna na zisťovanie zisťovanie nejakých informácii o zozname
Šablóna budeme zisťovať nejakú informáciu o prvkoch zoznamu, napríklad minimálny prvok. Pri+com podmienka aj priradenie budú závisieť od konkrétnej úlohy.:
~~~
mn = zoznam[0]
for prvok in zoznam:
    if prvok < mn:
        mn = prvok
print(mn)
~~~
### Šablóna na vypísanie prvkov zoznamu do jedného riadku
~~~
zoznam = [47, 'ab', -13, 22, 9, 25]
print('prvky zoznamu:', end=' ')
for prvok in zoznam:
    print(prvok, end=' ')
print()

Zobrazenie výsledku :
prvky zoznamu: 47 ab -13 22 9 25
~~~

### Šablóna keď pristupujeme k niektorým prvkom viackrát
~~~
for i in range(10):
    index = i % 4
    farba = ['red', 'blue', 'yellow', 'green'][index]
    print(farba)

Zobrazenie výsledku :
red
blue
yellow
green
red
blue
yellow
green
red
blue
~~~

Pokračovanie č. III

