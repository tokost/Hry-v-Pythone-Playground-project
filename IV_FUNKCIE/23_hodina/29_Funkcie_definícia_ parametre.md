># Funkcie

Už aj doteraz sme sa stretli s funkciami. Boli to tzv. štandardné funkcie ako napr.

* vstup a výstup input() a print()
* aritmetické funkcie abs() a round()
* generovanie postupnosti čísel pre for-cyklus funkcia range()
* 
Všetky tieto funkcie niečo vykonali (vypísali, prečítali, vypočítali, …) a niektoré z nich vrátili nejakú hodnotu, ktorú sme mohli ďalej spracovať. Tiež sme videli, že niektoré majú rôzny počet parametrov, prípadne sú niekedy volané bez parametrov. **Parameter** funkcie je premenná zapísaná pri definovaní funkcie. Premenná s takýmto názvom je dostupná v rámci funkcie.
~~~
def function(parameter):
    print(parameter)
~~~
Okrem toho sme pracovali aj s funkciami, ktoré boli definované v iných moduloch:

* keď napíšeme na začiatku kódu import random, môžeme pracovať napr. s funkciami random.randint() a random.randrange()
* keď napíšeme import math, môžeme pracovať napr. s funkciami math.sin() a math.cos()

Všetky tieto a tisícky ďalších v Pythone naprogramovali programátori pred nejakým časom, aby nám neskôr zjednodušili samotné programovanie. Vytváranie vlastných funkcií pritom vôbec nie je komplikované a teraz sa to naučíme aj my.

Ak ale potrebujeme nejakú funkciu ktorá nepatrí k štandardným (nenajdeme ju zozname standardných funkcii) , alebo ju nenájdeme ani v knižniciach, tak si ju ako uvidíme neskôr vytvoriť sami.

>## Definícia funkcie
Funkcia je pomenovaný blok príkazov (niekedy sa tomu hovorí aj podprogram). Definujeme ju nasledovnou konštrukciou:
~~~
def meno_funkcie():   # zapamätaj si blok príkazov
    príkaz            # ako novú funkciu
    prikaz
    prikaz
    ...
~~~
> Definícia začína kľúčovým slovom ***def** za ktorým nasleduje **meno_funkcie** a potom v zátvorke parametre. Viacero argumentov sa oddeluje čiarkami a za zátvorkou musí nasledovať **dvojbodka**

>#### Funkcie v Pythone neurčujú datový typ návratovej fodnoty ! Neurčujú dokonca ani to či funkcia vračia alebo nevracia návratovú hodnotu.

V skutočnosti si ale Python sám pre seba eviduje návratovú hodnotu, ale pokial to programátor nepožaduje získať tým že definuje príslušný parameter, tak si to Python necháva iba pre seba. Napr. ak funkcia vykoná príkaz return, vráti v ňom uvedenú hodnotu. V ostatných prípadoch však vracia **None** čo je pythonovský ekvivalent hodnoty nič, žiadna hodnota, neznáma hodnota a pod. Nie je to však nula ako číslo.

Tým že zapíšeme definíciu funkcie, tak sa z bloku príkazov (hovoríme tomu **telo funkcie**) ktoré sa nachádzajú pod definíciou ešte nič nevykoná. Táto definícia sa „len“ zapamätá a jej referencia sa priradí k zadanému menu - vlastne sa do premennej meno_funkcie priradí **referencia** - odkaz na telo funkcie. Je to podobné tomu, ako sa priraďovacím príkazom do premennej priradí hodnota z pravej strany príkazu.

Ako prvý príklad zapíšme takúto definíciu funkcie:
~~~
def vypis():
    print('**********')
    print('**********')
~~~

Zadefinovali sme funkciu s menom vypis, pričom telo funkcie obsahuje dva príkazy na výpis riadkov s hviezdičkami. Celý **blok príkazov musí byť odsunutý o 4 medzery** rovnako ako sme odsúvali príkazy v cykloch a aj v podmienených príkazoch. Definícia tela funkcie končí vtedy, keď sa objaví riadok, ktorý už nie je odsunutý. Touto definíciou sa ešte žiadne príkazy z tela funkcie nevykonávajú. Na to potrebujeme túto funkciu **zavolať**.


>## Volanie funkcie

Volanie funkcie je taký zápis, ktorým sa začnú vykonávať príkazy z definície funkcie. Stačí zapísať meno funkcie so zátvorkami a funkcie sa spustí:

**meno_funkcie()**

Samozrejme, že funkciu môžeme zavolať až vtedy, keď už Python pozná jej definíciu ! Keď zavoláme teda funkciu vypis v príkazovom režime, tak dostaneme takýto výpis:
~~~
>>> vypis()
**********
**********
>>>
~~~
Vidíme, že sa vykonali oba príkazy z tela funkcie a potom Python ďalej čaká na ďalšie príkazy. Teraz ale zapíšme volanie funkcie aj s jej definíciou priamo do skriptu (teda v programovom režime):
~~~
def vypis():
    print('**********')
    print('**********')

print('hello')
vypis()
print('* Python *')
vypis()
~~~

Skôr, ako to spustíme, si uvedomme, čo sa udeje pri spustení:
* zapamätá sa definícia funkcie v premennej vypis
* vypíše sa slovo 'hello'
* zavolá sa funkcia vypis()
* vypíše riadok s textom '* Python *'
* znovu sa zavolá funkcia vypis()
Keď tento skript spustíme výsledok bude vyzerať takto:
~~~
hello
**********
**********
* Python *
**********
**********
~~~
Zapíšme teraz presné kroky, ktoré sa vykonajú pri volaní funkcie:

1. preruší sa vykonávanie práve bežiaceho programu (Python si presne zapamätá miesto, kde sa to stalo)
2. skočí sa na začiatok volanej funkcie
3. postupne sa vykonajú všetky príkazy
4. keď sa príde na koniec funkcie, zrealizuje sa **návrat** na zapamätané miesto, kde sa prerušilo vykonávanie programu a pokračuje sa vo vykonávaní ďalších príkazov za volaním funkcie
Pre volanie funkcie sú veľmi dôležité okrúhle zátvorky. Bez nich to už nie je volanie, ale len zisťovanie referencie na hodnotu, ktorá je priradená pre toto meno. Napr.
~~~
>>> vypis()
**********
**********
>>> vypis
<function vypis at 0x0205CB28>
~~~

Ak by sme namiesto volania funkcie takto zapísali len meno funkcie bez zátvoriek, ale v skripte (teda nie v interaktívnom režime), táto hodnota referencie by sa nevypísala, ale odignorovala. 
>**Toto býva dosť častá chyba začiatočníkov, ktorá sa ale ťažšie odhaľuje.**

Ak zavoláme funkciu, ktorú sme ešte nedefinovali, Python vyhlási chybu, napr.
~~~
>>> vipis()
...
NameError: name 'vipis' is not defined
~~~

Samozrejme, že môžeme volať len definované funkcie.
~~~
>>> vypis()
**********
**********
>>> vypis = 'ahoj'
>>> vypis
'ahoj'
>>> vypis()
...
TypeError: 'str' object is not callable
~~~

Hodnotou premennej vypis je už teraz znakový reťazec, a ten sa „nedá zavolať“, t.j. nie je „callable“ (tento objekt nie je zavolateľný ako funkcia).

Hotové funkcie, s ktorými sme doteraz pracovali, napr. print() alebo random.randint(), mali aj parametre, vďaka čomu riešili rôzne úlohy. Parametre slúžia na to, aby sme mohli funkcii lepšie oznámiť, čo špecifické má urobiť: čo sa má vypísať, z akého intervalu má vygenerovať náhodné číslo, akú úsečku má nakresliť, prípadne akej farby, …
**Argumentom** je premenná alebo akýkoľvek vstup pri volaní funkcie.?

meno_volanej_funkcie(argument)
~~~
def hello(name): # definovanie funkcie s parametrom name
...     print("Hello "+str(name)) # využitie parametru – premenná name
... 
>>> hello("Adam") # volanie funkcie s argumentom "Adam"
Hello Adam
~~~



>## Parametre funkcie

### Dočasná hodnota parametra
Parametrom funkcie je **dočasná premenná**, ktorá vzniká pri volaní funkcie a prostredníctvom ktorej, môžeme do funkcie poslať nejakú hodnotu. Parametre funkcií definujeme počas definovania funkcie v **hlavičke funkcie** a ak ich je viac, oddeľujeme ich čiarkami:
~~~
**def** meno_funkcie(parameter):
    prikaz
    prikaz
    ...
~~~
~~~
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)

# Output: Sum: 5
~~~
Vo vyššie uvedenom príklade má funkcia add_numbers()dva parametre: a a b. Tu add_numbers(2, 3)špecifikuje tieto parametre aa bzíska hodnoty 2 a 3 .

Iný príklad:
~~~
**def** vypis_hviezdiciek(pocet):
    print('*' * pocet)
~~~
V prvom riadku definície funkcie (hlavička funkcie) pribudla jedna premenná pocet - parameter. Táto premenná vznikne automaticky pri volaní funkcie, preto musíme pri volaní oznámiť hodnotu tohto parametra. Volanie zapíšeme:
~~~
>>> vypis_hviezdiciek(30)
******************************
>>> for i in range(1, 10):
        vypis_hviezdiciek(i)

*
**
***
****
*****
******
*******
********
*********
~~~
Pri volaní sa „skutočná hodnota“ **priradí** do parametra funkcie (premenná pocet).

Už predtým sme popísali mechanizmus volania funkcie, ale to sme ešte nepoznali parametre. Teraz doplníme tento postup o spracovanie parametrov. Najprv trochu terminológie:
* pri definovaní funkcie v hlavičke funkcie uvádzame tzv. formálne parametre: sú to nové premenné, ktoré vzniknú až pri volaní funkcie
* pri volaní funkcie musíme do zátvoriek zapísať hodnoty, ktoré sa stanú tzv. skutočnými parametrami: tieto hodnoty sa pri volaní priradia do formálnych parametrov

### Predvolená alebo defaultná hodnota parametra

Python umožňuje nastaviť argumentom funkcie implicitnú - priamo určenú hodnotu. Argumentom funkcie takto poskytujeme predvolené hodnoty. Tieto hodnoty z definície sú použité vtedy ak nie sú argumenty zadané pri volaní takejto funkcie.

Na poskytnutie predvolených hodnôt používame operátor =. napr.
~~~
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()
~~~
Vo vyššie uvedenom príklade si všimnite definíciu funkcie def add_numbers(a = 7, b = 8):

Tu sme zvolili predvolené hodnoty 7 a 8 pre parametre a a b. Tento program funguje potom funguje takto:

1. add_number(2, 3)
Obe hodnoty sa odovzdávajú počas volania funkcie. Preto sa tieto hodnoty používajú namiesto predvolených hodnôt.

2. add_number(2)
Počas volania funkcie sa odovzdá iba jedna hodnota. Takže podľa pozičného argumentu je 2 priradené k argumentu a a predvolená hodnota je použitá pre parameter b.

3. add_number()
Počas volania funkcie sa neodovzdáva žiadna hodnota. Preto sa pre parametre a aj pre b použijú pôvodné hodnoty.

### Parametre volané menom
Argumenty alebo parametre funkcie svojimí názvami zodpovedajú názvom kľučových slov použitých v tele funkcie napr.
~~~
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')
~~~
Tu si všimnite volanie funkcie,
~~~
display_info(last_name = 'Cartman', first_name = 'Eric')
~~~
Tu sme priradili názvy argumentom počas volania funkcie.

Preto first_name je volanie funkcie priradené first_name v definícii funkcie. Podobne last_name vo funkcii je volanie priradené last_name v definícii funkcie. Pritom nezáleží na pozíciách argumentov.
[Video k tomu](https://youtu.be/Gf-Ws2cXEuA?list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn)

Ak chceme použiť aj väčší počet parametrov, môžeme využiť pole:
~~~
def sucin(pole):
    vysl = 1
    for prvok in pole:
        vysl *= prvok
    return vysl

print(sucin([3, 7]))
~~~
~~~
Teraz to funguje pre ľubovoľný počet čísel, ale musíme ich uzavrieť do hranatých (alebo okrúhlych) zátvoriek:

>>> sucin([3, 7])
21
>>> sucin([2, 3, 4, 5, 6])
720
>>> sucin([2, 3, 4, 5, 6, 7])
5040
>>> sucin(range(2, 8))
5040
>>> sucin(range(2, 41))
815915283247897734345611269596115894272000000000
~~~

### Funkcia s ľubovoľnými argumentmi - zbaleným parametrom
Niekedy vopred nepoznáme počet argumentov, ktoré budú odovzdané funkcii. Na zvládnutie tejto situácie môžeme použiť ľubovoľné argumenty v Pythone.

Ľubovoľné argumenty nám umožňujú odovzdať rôzny počet hodnôt počas volania funkcie.

Na označenie tohto druhu argumentu používame pred názvom parametra hviezdičku (*). 

**Zbalený parameter** (po anglicky packing):
* pred menom parametra v hlavičke funkcie píšeme znak * (zvyčajne je to posledný parameter)
* pri volaní funkcie sa všetky zvyšné parametre zbalia do jednej n-tice (typ tuple)

Otestujme:
~~~
def test(prvy, *zvysne):
    print('prvy =', prvy)
    print('zvysne =', zvysne)
~~~
po spustení:
~~~
>>> test('jeden', 'dva', 'tri')
prvy = jeden
zvysne = ('dva', 'tri')
>>> test('jeden')
prvy = jeden
zvysne = ()
~~~
Funkcia sa môže volať s jedným alebo aj viac parametrami. Prepíšme funkciu sucin() s použitím jedného zbaleného parametra:
~~~
def sucin(*pole):            # zbalený parameter
    vysl = 1
    for prvok in pole:
        vysl *= prvok
    return vysl
~~~
Uvedomte si, že teraz jeden parameter pole zastupuje ľubovoľný počet parametrov a Python nám do tohto parametra automaticky zbalí všetky skutočné parametre ako jednu n-ticu (tuple). Otestujeme:
~~~
>>> sucin()
1
>>> sucin(3, 7)
21
>>> sucin(2, 3, 4, 5, 6, 7)
5040
>>> sucin(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
479001600
>>> sucin(range(2, 13))
...
TypeError: unsupported operand type(s) for *=: 'int' and 'range'
~~~

V poslednom príklade vidíte, že range(...) tu nefunguje: Python tento jeden parameter zbalí do jednoprvkovej n-tice a potom sa s týmto range() bude chcieť násobiť, čo samozrejme nefunguje.

Iný príklad:
~~~
# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)
Spustiť kód

Výsledok:
Súčet = 6
Súčet = 13
~~~
Vo vyššie uvedenom príklade sme vytvorili funkciu find_sum(), ktorá prijíma ľubovoľné argumenty. 
~~~
find_sum(1, 2, 3)

find_sum(4, 9)
~~~
Tu sme schopní volať rovnakú funkciu s rôznymi argumentmi.

Poznámka : Po získaní viacerých hodnôt numbers sa správajte ako pole, aby sme mohli použiť for cyklus na prístup ku každej hodnote.

Ešte ukážme druhý podobný prípad, ktorý sa môže vyskytnúť pri práci s parametrami funkcií. Napíšme funkciu, ktorá dostáva dva alebo tri parametre a nejako ich vypíše:
~~~
def pis(meno, priezvisko, rok=2015):
    print('volam sa {} {} a narodil som sa v {}'.format(meno, priezvisko, rok))
~~~
Napr.
~~~
>>> pis('Janko', 'Hrasko', 2014)
volam sa Janko Hrasko a narodil som sa v 2014
>>> pis('Juraj', 'Janosik')
volam sa Juraj Janosik a narodil som sa v 2015
~~~

Malá nepríjemnosť nastáva vtedy, keď máme takéto hodnoty pripravené v nejakej štruktúre:
~~~
>>> p1 = ['Janko', 'Hrasko', 2014]
>>> p2 = ['Juraj', 'Janosik']
>>> p3 = ['Monty', 'Python', 1968]
>>> pis(p1)
...
TypeError: pis() missing 1 required positional argument: 'priezvisko'
~~~

Nefunguje volanie tejto funkcie s trojprvkovým poľom, ale musíme prvky tohto poľa rozbaliť, aby sa priradili do príslušných parametrov, napr.
~~~
>>> pis(p1[0], p1[1], p1[2])
volam sa Janko Hrasko a narodil som sa v 2014
>>> pis(p2[0], p2[1])
volam sa Juraj Janosik a narodil som sa v 2015
~~~

>Takáto situácia sa pri programovaní stáva dosť často: 

V nejakej štruktúre (napr. v poli) máme pripravené parametre pre danú funkciu a my potrebujeme túto funkciu zavolať s rozbalenými prvkami štruktúry. Na toto slúži rozbaľovací operátor, pomocou ktorého môžeme ľubovoľnú štruktúru poslať ako skupinu parametrov, pričom sa automaticky rozbalia (a teda prvky sa priradia do formálnych parametrov). **Rozbaľovací operátor** pre parametre je opäť znak * a používa sa takto:
~~~
>>> pis(*p1)              # je to isté ako pis(p1[0], p1[1], p1[2])
volam sa Janko Hrasko a narodil som sa v 2014
>>> pis(*p2)              # je to isté ako pis(p2[0], p2[1])
volam sa Juraj Janosik a narodil som sa v 2015
~~~
Takže, všade tam, kde sa očakáva nie jedna štruktúra ako parameter, ale veľa parametrov, ktoré sú prvkami tejto štruktúry, môžeme použiť tento rozbaľovací operátor (po anglicky unpacking argument lists).

Tento operátor môžeme využiť napr. aj v takýchto situáciách:
~~~
>>> print(range(10))
range(0, 10)
>>> print(*range(10))
0 1 2 3 4 5 6 7 8 9
>>> print(*range(10), sep='...')
0...1...2...3...4...5...6...7...8...9
>>> param = (3, 20, 4)
>>> print(*range(*param))
3 7 11 15 19
>>> dvenasto = 2**100
>>> print(dvenasto)
1267650600228229401496703205376
>>> print(*str(dvenasto))
1 2 6 7 6 5 0 6 0 0 2 2 8 2 2 9 4 0 1 4 9 6 7 0 3 2 0 5 3 7 6
>>> print(*str(dvenasto), sep='-')
1-2-6-7-6-5-0-6-0-0-2-2-8-2-2-9-4-0-1-4-9-6-7-0-3-2-0-5-3-7-6
>>> p = [17, 18, 19, 20, 21]
>>> [*p[3:], *range(5), *p]
[20, 21, 0, 1, 2, 3, 4, 17, 18, 19, 20, 21]
~~~
Pripomeňme si funkciu sucin(), ktorá počítala súčin ľubovoľného počtu čísel - tieto sa spracovali jedným zbaleným parametrom. Teda funkcia očakáva veľa parametrov a niečo z nich vypočíta. Ak ale máme jednu štruktúru, ktorá obsahuje tieto čísla, musíme použiť rozbaľovací operátor:
~~~
>>> cisla = [7, 11, 13]
>>> sucin(cisla)              # pole [7, 11, 13] sa násobí 1
[7, 11, 13]
>>> sucin(*cisla)
1001
>>> sucin(*range(2, 11))
3628800
~~~
>### Zbalené pomenované parametre
Pozrime sa na túto funkciu:
~~~
def vypis(meno, vek, vyska, vaha, bydlisko):
    print('volam sa', meno)
    print('    vek =', vek)
    print('    vyska =', vyska)
    print('    vaha =', vaha)
    print('    bydlisko =', bydlisko)
~~~
otestujeme:
~~~
>>> vypis('Janko Hrasko', vek=5, vyska=7, vaha=0.3, bydlisko='Pri poli')
volam sa Janko Hrasko
    vek = 5
    vyska = 7
    vaha = 0.3
    bydlisko = Pri poli
~~~
Radi by sme aj tu dosiahli podobnú vlastnosť parametrov, ako to bolo pri zbalenom parametri, ktorý do jedného parametra dostal ľubovoľný počet skutočných parametrov. V tomto prípade by sme ale chceli, aby sa takto zbalili všetky vlastnosti vypisovanej osoby ale aj s príslušnými menami týchto vlastností. V tomto prípade nám pomôžu **zbalené pomenované parametre**: namiesto viacerých pozičných parametrov, uvedieme jeden s dvomi hviezdičkami **:
~~~
def vypis(meno, **vlastnosti):
    print('volam sa', meno)
    for k, h in vlastnosti.items():
        print('    ', k, '=', h)
~~~
Tento zápis označuje, že ľubovoľný počet pomenovaných parametrov sa zbalí do jedného parametra a ten vo vnútri funkcie bude typu **asociatívne pole** - indexy nie sú čísla, ale textové reťazce (**kľúče**). Uvedomte si ale, že v asociatívnom poli sa nezachováva poradie dvojíc:

>>> vypis('Janko Hrasko', vek=5, vyska=7, vaha=0.3, bydlisko='Pri poli')
volam sa Janko Hrasko
     vyska = 7
     vaha = 0.3
     bydlisko = Pri poli
     vek = 5


>### Parameter s meniteľnou hodnotou
Teraz trochu odbočíme od zbalených a rozbalených parametrov. Ukážme veľký problém, ktorý nás môže zaskočiť v situácii, **keď náhradnou hodnotou parametra je meniteľný typ (mutable)**. 

Pozrime na túto nevinne vyzerajúcu funkciu:
~~~
def pokus(a=1, b=[]):
    b.append(a)
    return b
~~~

Očakávame, že ak neuvedieme druhý parameter, výsledkom funkcie bude jednoprvkové pole s prvkom prvého parametra. Skôr, ako to otestujeme, vypíšme, ako túto našu funkciu vidí help():
~~~
>>> help(pokus)
Help on function pokus in module __main__:

pokus(a=1, b=[])
~~~
a teraz test:
~~~
>>> pokus(2)
[2]
~~~

Zatiaľ je všetko v poriadku. Ale po druhom spustení:
~~~
>>> pokus(7)
[2, 7]
~~~
Vidíme, že Python si tu nejako pamätá aj naše prvé spustenie tejto funkcie. Znovu pozrime help():
~~~
>>> help(pokus)
Help on function pokus in module __main__:

pokus(a=1, b=[2, 7])
~~~

A vidíme, že sa dokonca zmenila hlavička našej funkcie pokus(). Mali by sme teda rozumieť, čo sa tu vlastne deje:

* Python si pre každú funkciu pamätá zoznam všetkých náhradných hodnôt pre formálne parametre funkcie, tak ako sme ich zadefinovali v hlavičke (môžete si pozrieť premennú pokus.__defaults__)
* ak sú v tomto zozname len nemeniteľné hodnoty (immutable), nevzniká žiaden problém
* problémom sú meniteľné hodnoty (mutable) v tomto zozname: pri volaní funkcie, keď treba použiť náhradnú hodnotu, Python použije hodnotu z tohto zoznamu (použije referenciu na túto štruktúru) - keď tomuto parametru ale v tele funkcie zmeníme obsah, zmení sa tým aj hodnota v zozname náhradných hodnôt (pokus.__defaults__)

Z tohto pre nás vyplýva, že radšej **nikdy nebudeme definovať náhradnú hodnotu parametra ako meniteľný objekt**. Funkciu pokus by sme mali preto radšej zapísať takto:
~~~
def pokus(a=1, b=None):
    if b is None:
        b = []
    b.append(a)
    return b
~~~
A všetko by fungovalo tak, ako sme očakávali.

Skúsení programátori vedia túto vlastnosť využiť veľmi zaujímavo- Napr. do funkcie posielame nejaké hodnoty a funkcia nám oznamuje, či už sa taká vyskytla, alebo ešte nie:
~~~
def kontrola(hodnota, bola=set()):
    if hodnota in bola:
        print(hodnota, 'uz bolo')
    else:
        bola.add(hodnota)
        print(hodnota, 'OK')
~~~
a test:
~~~
>>> kontrola(7)
7 OK
>>> kontrola(17)
17 OK
>>> kontrola(-7)
-7 OK
>>> kontrola(17)
17 uz bolo
>>> kontrola(7)
7 uz bolo
~~~
Veľmi pekným využitím tejto nečakanej vlastnosti parametra s meniteľnou náhradnou hodnotou je zrýchlenie výpočtu fibonacciho postupnosti. Už sme sa stretli s rekurzívnou verziou, ktorá je pre väčšie hodnoty nepoužiteľne pomalá:
~~~
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
~~~

Vyskúšajte napr. fib(40).

Tu by mohol pomôcť jeden parameter navyše, vďaka ktorému by si funkcia mohla pamätať všetky doteraz vypočítané hodnoty. Zapíšme:
~~~
def fib(n, pamat={}):
    if n in pamat:
        return pamat[n]
    if n < 2:
        vysl = n
    else:
        vysl = fib(n-2) + fib(n-1)
    pamat[n] = vysl
    return vysl
~~~
Aj táto funkcia je **rekurzívna** - vie zavolať samú seba. Len si vie zapamätať niečo navyše. Takému spôsobu riešenia úlohy, pri ktorom vieme využiť až predtým vypočítané a zapamätané medzivýsledky, hovoríme **memoizácia**.
Ďalším príkladom funkcie ktorá volá samu seba je výpočet faktorialu:
~~~
def faktorial(cislo):
    if cislo > 0:
        return faktorial(cislo - 1) * cislo
    else:
        return 1
~~~
>Pri rekurzii si musíte dať pozor, aby sa niekedy ukončila. Inak program
upadne na pretečenie zásobníka.

>### Typy parametrov a typ výsledku

Python síce nekontroluje typy parametrov, ale kontroluje, čo sa s nimi robí vo funkcii.
~~~
def pocitaj(x):
    return 2 * x + 1
~~~
Táto funkcia bude fungovať pre čísla, ale pre reťazec nám program spadne:
~~~
>>> pocitaj(5)
11
>>> pocitaj('a')
...
TypeError: Can't convert 'int' object to str implicitly
~~~
V tele funkcie ale môžeme kontrolovať typ parametra, napr. takto
~~~
def pocitaj(x):
    if type(x) == str:
        return 2 * x + '1'
    else:
        return 2 * x + 1
~~~
a potom volanie
~~~
>>> pocitaj(5)
11
>>> pocitaj('a')
'aa1'
~~~

Napriek tomuto niektoré funkcie môžu fungovať rôzne pre rôzne typy, napr.
~~~
def urob(a, b):
    return 2 * a + 3 * b
~~~
niekedy funguje pre čísla aj pre reťazce. Otestujte.

Pokračovanie


