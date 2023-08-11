

### Formátovanie reťazca pomocou funkcie str.format()
* vracia nový reťazec v zadanom tvare
* má tvar: **reťazec.format(parametre)**

kde **reťazec** je text v úvodzovkách (alebo apostrofoch) obsahujúci aj formátovacie polia uzavreté v zložených zátvorkách {}. Na miesta formátovacích polí sa do nového reťazca vložia v predpísanom formáte hodnoty **parametrov** z funkcie **format**. Názvy formátovacích polí, v najjednoduchších zápisoch, sú 0, 1, 2,...

Funkcia format sa najviac využíva v príkaze print, ale môže sa použiť kdekoľvek, kde potrebujeme upraviť formát reťazca. Napríklad zápis:
> "Súčet = {0}".format(sucet) pre hodnotu 123 premennej sucet vráti reťazec ***Súčet = 123***
~~~
>>> sucet = 123
>>> print("Súčet = {0}".format(sucet))
Súčet = 123
~~~
> "Súčet prvých {0} prirodzených čísel je {1}".format(pocet, sucet) pre pocet = 100 a sucet = 5050 vráti reťazec ***Súčet prvých 100 prirodzených čísel je 5050***
~~~
>>> pocet = 100
>>> sucet = 5050
>>> print("Súčet prvých {0} prirodzených čísel je {1}".format(pocet, sucet))
~~~
Nuž a čo sa stalo ? Stalo sa to že do textu boli vložené údaje z premenných podľa toho na ktorej pozícii sa v príkaze formát nachádzali. Namiesto {0} sa vložil obsah premennej pocet a namiesto {1} obsah premennej sucet lebo v takomto poradí boli tieto premenné uvedené v príkaze format. 

Od verzie Pythonu 3.0 pribudla reťazcom funkcia resp. v OOP sa tomu hovorí aj metoda s názvom **format()** spolu s { } a argumentami. Staršie verzie používali operátor % ale tomuto spôsobu formátovania sa venovať nebudeme.

Do zložených zátvoriek je možné napísať index argumentu, ktorým sa majú zátvorky nahradit. Nasledovné príklady nám pomôžu tento úkon pochopiť lepsie.
~~~
>>> print("{ }!".format("Hello",'world'));
Hello world!
>>> print("{1} {0} {1}!".format("baby","go"));
go baby go!
~~~