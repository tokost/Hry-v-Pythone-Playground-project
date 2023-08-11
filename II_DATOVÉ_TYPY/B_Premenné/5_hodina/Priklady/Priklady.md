1. Zistite, čo sa vypočíta
skontrolujte

~~~
>>> 1/0
>>> 1//0
>>> 1%0
>>> 1--2
>>> 1---2
>>> 1----2
>>> 1-----2
~~~
2. Vieme, že desatinné čísla sú obmedzené nejakou konkrétnou maximálnou hodnotou. Pokusmi nájdite taký čo najväčší exponent v semilogaritmickom zápise desatinného čísla 1e+xxx, že už o 1 väčší by vzniklo niečo iné ako desatinné číslo napr.
~~~
>>> 1e+100
1e+100
>>> 1e+101
1e+101
~~~
3. Pre dané odvesny a a b vypočítajte preponu c napr.
~~~
>>> a = 10
>>> b = 14
>>> c = ...
>>> c
17.204650534085253
~~~
4. V premenných meno a priezvisko sú priradené nejaké dva znakové reťazce. Do premennej desat priraďte reťazec, ktorý obsahuje desaťkrát meno a priezvisko oddelené čiarkou napr.
~~~
>>> meno = 'Janko'
>>> priezvisko = 'Hraško'
>>> desat = ...
>>> desat
'Janko Hraško, Janko Hraško, Janko Hraško, Janko, Hraško, Janko Hraško, Janko Hraško, Janko Hraško,Janko Hraško, Janko Hraško, Janko Hraško'
~~~
5. V dvoch premenných cislo1 a cislo2 sú priradené nejaké dve celé čísla (cislo2 bude učite trojciferné). Vytvorte novú hodnotu do premennej cislo3, ktorá zlepí tieto dve čísla do jedného celého čísla. Nepoužívajte znakové reťazce napr.
~~~
>>> cislo1 = 4567
>>> cisko2 = 912
>>> cislo3 = ...
>>> cislo3
4567912
~~~
6. Zapíšte prevod českej koruny na euro a opačne (predpokladajte, že kurz je 26 korun za 1 euro) napr. ak priradíme do ck 1000 korún, vypočíta sa euro a potom sa 30 euro prepočíta na české koruny
~~~
>>> ck = 1000
>>> euro = ...
>>> euro
38.46153846153846
>>> euro = 30
>>> ck = ...
>>> ck
780
~~~
7. Vypočítajte stav účtu, na ktorom je na 4% úrok na začiatku 100 euro. V premennej pocet_rokov je priradená hodnota počtu rokov, ktoré nás zaujímajú napr.
~~~
>>> pocet_rokov = 10
>>> stav_uctu = ...
>>> stav_uctu
148.02442849183444
~~~
8. Napíšte skript, ktorý vypíše vašu vizitku: bude orámovaná znakmi '-' a '|' a obsahovať by mala aspoň vaše meno, adresu a telefón (adresu a telefón si môžete vymyslieť) napr.
~~~
+---------------------+
| Janko Hraško        |
| Pri brázde 17       |
| mobil: 0999 123456  |
+---------------------+
~~~
9. Napíšte skript, ktorý najprv do troch premenných prvy, druhy a treti priradí tri rôzne znakové reťazce a potom vypíše všetky rôzne poradia týchto reťazcov (permutácie) napr. pre prvy = 'biela', druhy = 'modrá' a treti = 'červená' vypíše
~~~
biela modrá červená
modrá červená biela
...
~~~
10. Napíšte skript, v krtorom sa najprv do premennej cislo priradí nejaké celé číslo a potom do troch premenných c1, c2, c3 priradí posledné tri cifry daného čísla. Potom tieto tri cifry vypíše napr. pre cislo = 12345678 vypíše
~~~
posledné tri cifry čísla 12345678 sú 6 7 8
~~~
11. Napíšte skript, ktorý najprv do premennej n priradí nejakú celočíselnú hodnotu, pre ktorú n >= 10. Potom na základe tejto hodnoty vypíše orámovaný text 'PYTHON'. Tento text bude v rámiku „prirazený“ k ľavému okraju, pričom medzi textom a rámikom bude práve jedna medzera napr. pre n = 12 program vypíše:
~~~
************
*          *
* PYTHON   *
*          *
************
~~~
12. Napíšte skript, ktorý najprv do premennej n priradí nejakú celočíselnú hodnotu, pre ktorú n >= 10. Potom na základe tejto hodnoty vypíše orámovaný text 'PYTHON', ktorý bude ale vycentrovaný (pozor na nepárne n) napr. pre n = 20 program vypíše:
~~~
********************
*                  *
*      PYTHON      *
*                  *
********************
~~~