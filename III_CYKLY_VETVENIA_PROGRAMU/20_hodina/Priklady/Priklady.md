Príklad: Slučka cez reťazec
for x in 'Python':
    print(x)
Spustiť kód
Výkon

P
r
t
h
o
n
Python pre slučku s rozsahom Pythonu ()
Rozsah je séria hodnôt medzi dvoma číselnými intervalmi.

range()Na definovanie hodnôt používame vstavanú funkciu rozsahu Pythonu . napr.

values = range(4)
Tu 4 vo vnútri range()obsahuje rozsah hodnôt 0, 1, 2, 3.

V Pythone môžeme použiť for slučku na iteráciu v rozsahu. napr.

# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)
Spustiť kód
Výkon

0
1
2
3
Vo vyššie uvedenom príklade sme použili forcyklus na iteráciu od 0 do 3 .

Hodnota ije nastavená na 0 a pri každej iterácii sa aktualizuje na ďalšie číslo rozsahu. Tento proces pokračuje, kým sa nedosiahne 3 .

Iterácia	Podmienka	Akcia
1	True	0je vytlačený. isa zvyšuje na 1 .
2	True	1je vytlačený. isa zvyšuje na 2 .
3	True	2je vytlačený. isa zvyšuje na 3 .
4	True	3je vytlačený. isa zvyšuje na 4 .
5	False	Slučka je ukončená
Poznámka : Ak sa chcete dozvedieť viac o použití forcyklu s rozsahom, navštívte stránku Python range() .

Použitie slučky pre bez prístupu k položkám
Nie je povinné používať sekvenciu v rámci forcyklu. napr.

languages = ['Swift', 'Python', 'Go']

for language in languages:
    print('Hello')
    print('Hi')
Spustiť kód
Výkon

Ahoj
Ahoj
Ahoj
Ahoj
Ahoj
Ahoj
Tu sa cyklus spustí trikrát, pretože náš zoznam má tri položky. V každej iterácii telo slučky vytlačí 'Hello'a 'Hi'. Položky zoznamu sa v rámci cyklu nepoužívajú.

Ak nemáme v úmysle použiť sekvenciu v rámci cyklu, môžeme cyklus napísať takto:

languages = ['Swift', 'Python', 'Go']

for _ in languages:
    print('Hello')
    print('Hi')
Spustiť kód
Symbol _sa používa na označenie prvkov, ktoré nebudú použité v tele slučky.