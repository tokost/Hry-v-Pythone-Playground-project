1. Zistite, akú hodnotu True alebo False (alebo inú) majú tieto výrazy:
* najprv to skúste bez počítača, potom to skontrolujte v Pythone
~~~
x, y = 7, 'ab'
8 < x <= 7
x <= 3 + x // 2
y != 2 * x or 2 * y == 'abab'
x < x + 1 < 2 * x

x // 8 or x * y
x or y
x and y
not y
not x % 2
~~~
2. Napíšte program, ktorý najprv prečíta 3 desatinné čísla a, b, c a potom vypíše, koľko reálnych ale rôznych koreňov má kvadratická rovnica so zadanými koeficientami (zrejme výsledkom bude 0, alebo 1, alebo 2)

napr.
~~~
zadaj a: 1
zadaj b: 2
zadaj c: 1
kvadraticka rovnica ma jeden koren

zadaj a: 1
zadaj b: 0
zadaj c: 1
kvadraticka rovnica nema realne korene

zadaj a: 1
zadaj b: 2
zadaj c: -3
kvadraticka rovnica ma dva rozne korene
~~~
3. Máme daný tento program.

* ručne bez počítača zistite, čo vypočíta pre vstupnú hodnotu 11:
~~~
cislo1 = 0
cislo2 = int(input('? '))
while cislo2 > 0:
    if cislo2 % 2 == 0:
        cislo2 //= 2
    else:
        cislo2 -= 1
    cislo1 += 1
~~~
* Vedeli by ste matematikovi, ktorý nevie programovať ale pozná dvojkovú sústavu, vysvetliť, čo tento program vypočíta?

4. Napíšte program, ktorý najprv prečíta celé číslo a potom opakuje blok príkazov, kým je toto číslo väčšie ako 0: teda vypíše jeho poslednú cifru a potom ho ešte vydelí 10. Takto by ste mali dosiahnuť postupný výpis všetkých cifier vstupného čísla ale od konca (od poslednej cifry).

napr.
~~~
zadaj cislo: 50273
3
7
2
0
5
~~~
5. Prerobte riešenie predchádzajúceho príkladu (4) tak, že cifry sa nebudú vypisovať, ale sčitovať. Takto by ste mali dostať ciferný súčet daného čísla
napr.
~~~
zadaj cislo: 50273
ciferny sucet je 17
~~~
6. Využite ideu riešenia predchádzajúceho príkladu a vyriešte: program zistí, koľkokrát sa v zadanom čísle objaví nejaká konkrétna cifra
napr.
~~~
zadaj cislo: 123456789123456781234567
zadaj cifru: 8
cifra 8 sa vyskytla 2 krat

zadaj cislo: 123456789123456781234567
zadaj cifru: 0
cifra 0 sa vyskytla 0 krat
~~~
vyskúšajte to aj pre nejaké veľké číslo, napr. 2 ** 1000


7. Napíšte program, ktorý najprv prečíta celé číslo a vypíše jeho rozklad na prvočinitele.

snažte sa vyrobiť výpis v takomto tvare:
~~~
zadaj cislo: 24
24 = 2 * 2 * 2 * 3

zadaj cislo: 31
31 = 31

zadaj cislo: 65536
65536 = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
~~~
8. Napíšte program, ktorý nájde také najväčšie n, pre ktoré n! (faktoriál) je menší ako 1000000.

použite while-cyklus

9. Fibonacciho postupnosť sa skladá z čísel 0,1,1,2,3,5,8,13,21, …, teda každé ďalšie v postupnosti je súčtom dvoch predchádzajúcich. Napíšte program, ktorý zistí najväčšie fibonacciho číslo, ktoré nie je väčšie ako 1000000.

použite while-cyklus

10. Máme daný tento program.
* najprv bez počítača odhadnite čo urobí
~~~
for i in range(10):
    while random.randrange(4):
        print(end='x')
    print()
~~~
* uvažujte nad tým, čo nové ste sa na tomto príklade naučili

11. Grafická plocha má veľkosť vel x vel (vel je konštanta, napr. vel = 500). Generujeme do nej n náhodných bodiek (malé krúžky s polomerom 3), pričom súradnice x a y sú z intervalu <0, vel). Ak vzdialenosť vygenerovanej bodky od bodu (0, 0) je menšia ako vel, bodka bude červená, inak bude modrá. Počet bodiek n prečítajte zo vstupu. Počas generovania bodiek spočítajte, koľko z nich je červených. Na záver program vypíše pomer počtu červených bodiek ku všetkým vygenerovaným krát 4.
* Vedeli by ste zdôvodniť, prečo sa tento pomer pre veľké n blíži k číslu pi?

12. Grafická plocha má veľkosť 300x200 a generujeme do nej náhodné bodky (malé krúžky s polomerom 3), pričom súradnica x je z intervalu <0,300) a y <0, 200). Ak vzdialenosť vygenerovanej bodky od bodu (100, 100) je menšia ako 80, bodka bude červená, inak ak vzdialenosť od bodu (180, 100) je menšia ako 90, bodka bude modrá, inak bodka bude čierna. Vygenerujte n takýchto bodiek.
* n prečítajte zo vstupu

13. Nastavte grafickú plochu na veľkosť sirka, vyska = 250, 250. Nakreslite do nej šachovnicu 8x8 štvorčekov každý bude veľkosti 30x30, pričom ľavý horný štvorček má ľavý horný roh na súradniciach (5, 5). Pri kreslení striedavo zafarbujte políčka šachovnice dvomi farbami, napr. červenou a modrou (dajte pozor na rozostavenie farieb ako na šachovnici).
* riešte dvomi vnorenými for-cyklami

14. Predchádzajúci príklad (13) riešte tak, že sa nenakreslí šachovnica veľkosti 8x8, ale šachovnica, v ktorej je len toľko štvorčekov v riadku, resp. v stĺpci, aby sa každý z nich zmestil do grafickej plochy. Napr. pre sirka, vyska = 200, 150 bude mať šachovnica v každom riadku len 6 štvorčekov a riadky budú len 4.
* namiesto dvoch vnorených for-cyklov použite while-cykly