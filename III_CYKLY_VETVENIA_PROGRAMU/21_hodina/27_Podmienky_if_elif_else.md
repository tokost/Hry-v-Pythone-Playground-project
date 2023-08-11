V tejto časti sa budeme zaoberať príkazmi ktoré umožňujú vykonať vetvenie programu podľa splnenia zadaných podmienok. To znamená že ak program príde pri svojom vykonávaní t.j. postupnom spracovávaní jednotlivých príkazov k takýmto príkazom v ktorých su definované určité podmienky, tak sa skúma či sú zadané podmienky splnené alebo nie. Podĺa toho porgram ďalej pokračuje vo vykonávaní príkazov ktoré sa nachádzajú vo vetve ktorá zodpovedá splnenej podmienke.

>## Podmienený príkaz if

Python podporuje obvyklé logické podmienky z matematiky:

* Rovná sa: a == b
* Nerovná sa: a != b
* Menšie ako: a < b
* Menšie alebo rovné: a <= b
* Väčšie ako: a > b
* Väčšie alebo rovné: a >= b

Tieto podmienky možno použiť niekoľkými spôsobmi, najčastejšie sa v+sak používajú v príkazoch príkazoch **if** a cykloch **for**. Príkaz "if" sa zapisuje pomocou kľúčového slova if .
~~~
a = 33
b = 200
if b > a:
  print("b is greater than a")
~~~

V tomto príklade používame dve premenné, a a b , ktoré sa používajú ako súčasť príkazu if na testovanie, či je b väčšie ako a . Keďže a je 33 a b je 200 , vieme, že 200 je väčšie ako 33, a preto vytlačíme na obrazovku, že „b je väčšie ako a“.

> **Odsadenie:**
Python sa pri definovaní rozsahu v kóde spolieha na odsadenie (medzery na začiatku riadku). Príkaz If bez odsadenia (vyvolá chybu):
~~~
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
~~~

>## Podmienený príkaz elif (if...elif)

Kľúčové slovo **elif** je spôsob, akým Python hovorí „ak predchádzajúce podmienky neboli pravdivé, skúste preskúmať novú podmienku“ nachádzajúcu sa za elif a pokiaľ bude táto podmienka splnená vykonaj príkazy v tele.
~~~
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
~~~
V tomto príklade sa a rovná b , takže prvá podmienka nie je pravdivá, ale podmienka elif je pravdivá, takže na obrazovku vytlačíme, že „a a b sú rovnaké“.

>## Podmienený príkaz else (if...else)

S týmto príkazom sme sa už stretli v prípade príkazu cyklu for a tu to kľúčové slovo plní totožnú funkciu. **else** zachytáva všetko, čo nie je zachytené predchádzajúcimi podmienkami.
~~~
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
~~~
V tomto príklade je a väčšie ako b , takže prvá podmienka nie je pravdivá, ani podmienka elif nie je pravdivá, takže prejdeme na podmienku else a vytlačíme na obrazovku, že „a je väčšie ako b“. Môžete mať aj elsebez elif:
~~~
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
~~~

Pri programovaní často riešime situácie, keď sa program má na základe nejakej podmienky rozhodnúť medzi viacerými možnosťami a podľa splnenia resp. nesplnenia podmienky vykonať **rozvetvenie**. 

Majme napr. program ktorý má vypísať, či zadaný počet bodov stačí na danú známku z predmetu. Preto si program najprv vyžiada číslo ktoré zodpovedá získanému počtu bodov. Potom toto číslo **porovná** s požadovanou hranicou, napr. 50 bodov a na základe toho vypíše, či je to dosť na príslušnú známku, alebo nie:
~~~
body = int(input('Zadaj získaný počet bodov: '))
if body >= 50:
    print(body, 'bodov je dostačujúci počet na známku')
else:
    print(body, 'bodov je málo na získanie známky')
~~~
Použili sme tu podmienený príkaz (príkaz vetvenia) **if**. Všeobecný zápis tohoto bloku vyzerá takto:
~~~
if podmienka:    # ak je podmienka splnená t.j. True, vykonaj 1. skupinu príkazov
    prikaz
    prikaz
    ...
else:            # ak podmienka neplatí t.j. False, vykonaj 2. skupinu príkazov
    prikaz
    prikaz
    ...
~~~
V našom príklade sú je v oboch skupinách príkazov len po jednom príkaze print(). Odsadenie skupiny príkazov (blok príkazov) má rovnaký význam ako v cykle for preto je potrebné ich odsadzovať min. 4 medzery alebo **tabulátorom**.

Rozšírme podmienky na získanie známok o ďalšie kritéria ktorým sú priradené príslušné známky:

známka A za 90 a viac\
známka B za 80\
známka C za 70\
známka D za 60\
známka E za 50\
známka F za menej ako 50

Napr. podmienka pre získanie známky A t.j. 90 a viac bodov potom bude vyzerať nasledovne:
~~~
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
else:
    ...
~~~
Ak je bodov menej ako 90, už to môže byť len horšia známka a tak dopíšeme testovanie na známku B:
~~~
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
else:
    if body >= 80:
        print('za', body, 'bodov získavaš známku B')
    else:
        ...
~~~
Všetky riadky v druhej skupine príkazov (za else) musia byť odsadené o min. 4 medzery, preto napr. print(), ktorý vypisuje správu o známke B je odsunutý o 8 medzier. Podobným spôsobom zapíšeme všetky zvyšné podmienky:
~~~
body = int(input('Zadaj získaný počet bodov: '))
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
else:
    if body >= 80:
        print('za', body, 'bodov získavaš známku B')
    else:
        if body >= 70:
            print('za', body, 'bodov získavaš známku C')
        else:
            if body >= 60:
                print('za', body, 'bodov získavaš známku D')
            else:
                if body >= 50:
                    print('za', body, 'bodov získavaš známku E')
                else:
                    print('za', body, 'bodov si nevyhovel a máš známku F')
~~~
Odsadzovanie príkazov je v Pythone **veľmi dôležité** a musíme byť pri tom veľmi presní. Príkaz if, ktorý sa nachádza vo vnútri niektorej vetvy iného if, sa nazýva **vnorený príkaz if**.

>## Vnorený príkaz elif
V Pythone existuje konštrukcia, ktorá uľahčuje takúto vnorenú sériu if-ov:
~~~
if podmienka_1:      # ak podmienka_1 platí, vykonaj 1. skupinu príkazov
    prikaz
    ...
elif podmienka_2:    # ak podmienka_1 neplatí, ale platí podmienka_2, ...
    prikaz
    ...
elif podmienka_3:    # ak ani podmienka_1 ani podmienka_2 neplatia, ale platí podmienka_3, ...
    prikaz
    ...
else:                # ak žiadna z podmienok neplatí, ...
    prikaz
    ...
~~~
Ukážme ešte jedno riešenie tejto úlohy - jednotlivé podmienky zapíšeme ako intervaly:
~~~
body = int(input('Zadaj získaný počet bodov: '))
if body >= 90:
    print('za', body, 'bodov získavaš známku A')
if 80 <= body < 90:
    print('za', body, 'bodov získavaš známku B')
if 70 <= body < 80:
    print('za', body, 'bodov získavaš známku C')
if 60 <= body < 70:
    print('za', body, 'bodov získavaš známku D')
if 50 <= body < 60:
    print('za', body, 'bodov získavaš známku E')
if body < 50:
    print('za', body, 'bodov si nevyhovel a máš známku F')
~~~
>V tomto riešení využívame to, že **else-vetva v príkaze if môže chýbať** a teda pri neplatnej podmienke, sa nevykoná nič:

Ak máte vykonať iba jeden príkaz, môžete ho umiestniť na rovnaký riadok ako príkaz if.

Pri tejto konštrukcii sme použili nasledovnú tabuľku:

|Zápis             | Popis                                                 |
|------------------|-------------------------------------------------------|
|body < 90         | je menšie ako 90
|body <= 50        | je menšie alebo rovné ako 50
|body == 50        | rovná sa 50
|body != 77        | nerovná sa 77
|body > 100        | je väčšie ako 100
|body >= 90        | je väčšie alebo rovné ako 90
|40 < body <= 50   | je väčšie ako 40 a zároveň menšie alebo rovné ako 50
|a < b < c         | a je menšie ako b a zároveň je b menšie ako c

Treba si však uvedomiť že príkaz je vyhodnotený ako True ak zápis platí a False ak nie.
~~~
if a > b: print("a is greater than b")
~~~
Obdobne pre jeden príkaz if a jeden príkaz else môžeme vykonať zápis nasledovne:
~~~
a = 2
b = 330
print("A") if a > b else print("B")
~~~
Táto technika zápisu viacerých príkazov do jedného riadku je známa ako **ternárne operátory** alebo **podmienené výrazy** a v rovnakom riadku môžeme mať aj viacero iných príkazov. Jeden riadok, ak je else, s 3 podmienkami:
~~~
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
~~~

~~~
if podmienka:        # ak podmienka platí, vykonaj skupinu príkazov
    prikaz
    prikaz
    ...              # ak podmienka neplatí, nevykonaj nič
~~~
Zrejme každý príkaz if po kontrole podmienky (a prípadnom výpise správy) pokračuje na ďalšom príkaze, ktorý nasleduje za ním (a má rovnaké odsadenie ako if). Okrem toho vidíme, že teraz sú niektoré podmienky trochu zložitejšie, lebo testujeme, či sa hodnota nachádza v nejakom intervale. (podmienku 80 <= body < 90 sme mohli zapísať aj takto 90 > body >= 80)

Podmienky v Pythone môžu obsahovať logické operácie - majú obvyklý význam ako sa používajú v matematike:

* podmienka1 **and** podmienka2 … (a súčasne) znamená, že musia platiť obe podmienky
* podmienka1 **or** podmienka2 … (alebo) znamená, že musí platiť aspoň jedna z podmienok
*  podmienka **not**… (neplatí) znamená, že daná podmienka neplatí

Otestovať rôzne kombinácie podmienok môžeme napr. takto:
~~~
>>> a = 10
>>> b = 7
>>> a < b
False
>>> a >= b + 3
True
>>> b < a < 2 * b
True
>>> a != 7 and b == a - 3
True
>>> a == 7 or b == 10
False
>>> not a == b
True
>>> 1 == '1'
False
>>> 1 < '2'
...
TypeError: unorderable types: int() < str()
~~~

Všimnite si, že podmienky ktoré platia, majú hodnotu True a ktoré neplatia, majú False - sú to dve špeciálne hodnoty, ktoré Python používa ako výsledky porovnávania - tzv. logických výrazov. Sú logického typu, tzv. bool. Môžeme to skontrolovať:

~~~
>>> type(1 + 2)
<class 'int'>
>>> type(1 / 2)
<class 'float'>
>>> type('12')
<class 'str'>
>>> type(1 < 2)
<class 'bool'>
~~~

V prípadoch, keď Python očakáva logickú hodnotu (napr. v príkaze if, alebo v operáciách and, or, not) môžeme uvádzať aj hodnoty iných typov. Napr.
~~~
pocet = int(input('zadaj:'))
if pocet:
    print('pocet je rôzny od 0')
else:
    print('pocet je 0')
meno = input('zadaj:')
if meno:
    print('meno nie je prázdny reťazec')
else:
    print('meno je prázdny reťazec')
~~~

Logické operácie majú v skutočnosti trochu rozšírenú interpretáciu:

>**operácia: prvý and druhý**

* ak **prvý** nie je False, tak
    * výsledkom je **druhý**
* inak (teda **prvý** je False)
    * výsledkom je **prvý**

>**operácia: prvý or druhý**

* ak **prvý** nie je False, tak
    * výsledkom je **prvý**
* inak (teda **prvý** je False)
    * výsledkom je **druhý**

>**operácia: not prvý**

* ak **prvý** nie je False, tak
    * výsledkom je False
* inak
    *výsledkom je True

Napr.
~~~
>>> 1 + 2 and 3 + 4       # keďže 1+2 nie je False, výsledkom je 3+4
7
>>> 'ahoj' or 'Python'    # keďže 'ahoj' nie je False, výsledkom je 'ahoj'
'ahoj'
>>> '' or 'Python'        # keďže '' je False, výsledkom je 'Python'
'Python'
>>> 3 < 4 and 'kuk'       # keďže 3<4 nie je False, výsledkom je 'kuk'
'kuk'
~~~
>## Použitie podmieneného príkazu pri náhodnom rozhodovaní.

Ďalší príklad zisťuje, akých deliteľov má zadané číslo:
~~~
cislo = int(input('Zadaj číslo: '))
pocet = 0
print('delitele:', end=' ')
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:
        pocet += 1
        print(delitel, end=' ')
print()
print('počet deliteľov:', pocet)
~~~

Výstup môže byť napríklad takýto:
~~~
Zadaj číslo: 100
delitele: 1 2 4 5 10 20 25 50 100
počet deliteľov: 9
~~~

Malou modifikáciou tejto úlohy vieme urobiť ďalšie dva programy. 

Prvý zisťuje, či je číslo prvočíslo:
~~~
cislo = int(input('Zadaj číslo: '))
pocet = 0
for delitel in range(1, cislo+1):
    if cislo % delitel == 0:
        pocet += 1
if pocet == 2:
    print(cislo, 'je prvočíslo')
else:
    print(cislo, 'nie je prvočíslo')
~~~

Po spustení napr.:
~~~
Zadaj číslo: 101
101 je prvočíslo
~~~

Druhý program zisťuje, či je nejaké číslo dokonalé, t.j. súčet všetkých deliteľov menších ako samotné číslo sa rovná samotnému číslu. Na základe tohto nájde (postupne preverí) všetky dokonalé čísla do 10000:
~~~
print('dokonalé čísla do 10000 sú', end=' ')
for cislo in range(1,10001):
    sucet = 0
    for delitel in range(1, cislo):
        if cislo % delitel == 0:
            sucet += delitel
    if sucet == cislo:
        print(cislo, end=' ')
print()
print('=== viac ich už nie je ===')
~~~
Program vypíše:
~~~
dokonalé čísla do 10000 sú 6 28 496 8128
=== viac ich už nie je ===
~~~