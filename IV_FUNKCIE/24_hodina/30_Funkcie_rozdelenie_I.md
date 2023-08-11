>### Mechanizmus volania funkcie

si vysvetlíme na volaní vypis_hviezdiciek(30):

1. zapamätá sa návratová adresa volania
2. vytvorí sa **nová** premenná pocet (formálny parameter) a priradí sa do nej hodnota **skutočného parametra** 30
3. vykonajú sa všetky príkazy v definícii funkcie (telo funkcie)
4. zrušia sa všetky premenné, ktoré vznikli počas behu funkcie
5. riadenie sa vráti na miesto, kde bolo volanie funkcie

Už vieme, že priraďovací príkaz vytvára premennú a referenciou ju spojí s nejakou hodnotou. Premenné, ktoré vzniknú počas behu funkcie, sa stanú **lokálnymi premennými:** budú existovať len počas tohto behu a po skončení funkcie, sa automaticky zrušia. Aj parametre vznikajú pri štarte funkcie a zanikajú pri jej skončení: tieto premenné sú pre funkciu tiež lokálnymi premennými.

V nasledovnom príklade funkcie vypis_sucet() počítame a vypisujeme súčet čísel od 1 po zadané n:
~~~
def vypis_sucet(n):
    sucet = 1
    print(1, end=' ')
    for i in range(2, n + 1):
        sucet = sucet + i
        print('+', i, end=' ')
    print('=', sucet)
~~~
Pri volaní funkcie sa pre parameter n = 10 vypíše:
~~~
>>> vypis_sucet(10)
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
~~~
Počas behu vzniknú 2 lokálne premenné a jeden parameter, ktorý je pre funkciu tiež lokálnou premennou:
* **n** vznikne pri štarte funkcie aj s hodnotou 10
* **sucet** vznikne pri prvom priradení sucet = 1
* **i** vznikne pri štarte for-cyklu

Po skončení behu funkcie sa všetky tieto premenné automaticky zrušia.

Pred chvíľkou sme sa dozvedeli že existujú lokálne premenné ktoré vznikajú a sú používané pri definovaní funkcii. Okrem týchto lokálných premenných rozlišujeme a štandardné a globálne premenné ktoré vystupujú v tzv. **menných priestoroch (namespace)**

Aby sme lepšie pochopili ako naozaj fungujú spomínané lokálne premenné, musíme rozumieť, čo to je a ako funguje menný priestor. Najprv však trochu ďalšej terminológie: všetky identifikátory v Pythone sú jedným z troch typov (Python má pre identifikátory 3 rôzne tabuľky mien):

* **štandardné**, napr. int, print, …
    * hovorí sa tomu **builtins**
* **globálne** - definujeme ich na najvyššej úrovni mimo funkcií, napr. funkcia vypis_sucet
    * hovorí sa tomu **main**
* **lokálne** - ktoré vznikajú počas behu funkcie

Tabuľka štandardných mien je len jedna, jedna je tiež tabuľka globálnych mien, ale každá funkcia má svoju „súkromnú“ lokálnu tabuľku mien, ktorá vznikne pri štarte (zavolaní) funkcie a zruší sa pri konci vykonávania funkcie.

Keď na nejakom mieste použijeme identifikátor - trvalý identifikačný údaj ktorý udáva jednoznačnosť príslušného objektu (napr. rodné číslo u človeka), Python ho najprv hľadá (v tzv. **priestoroch mien**):

* v lokálnej tabuľke mien, ak tam tento identifikátor nenájde, hľadá ho
* * v globálnej tabuľke mien, ak tam tento identifikátor nenájde, hľadá ho
v štandardnej tabuľke mien

Ak nenájde v žiadnej z týchto tabuliek, hlási chybu NameError: name 'identifikátor' is not defined.

Príkaz dir() ktorý je štandardnou funkciou  vypíše tabuľku globálnych mien. Hoci pri štarte Pythonu by táto tabuľka mala byť prázdna, obsahuje niekoľko špeciálnych mien, ktoré začínajú aj končia znakmi '__':
~~~
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
~~~
Keď teraz vytvoríme nejaké nové globálne mená, objavia sa aj v tejto globálnej tabuľke:
~~~
>>> premenna = 2015
>>> def funkcia():
      pass

>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
 'funkcia', 'premenna']
~~~
Podobne sa vieme dostať aj k tabuľke štandardných mien (builtins):
~~~
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', ...
~~~
S týmito tabuľkami súvisí aj príkaz del na zrušenie premennej.

>### Príkaz del

Príkazom del zrušíme identifikátor z tabuľky mien. 

Formát príkazu:

**del** premenná

Príkaz najprv zistí, v ktorej tabuľke sa identifikátor nachádza (najprv pozrie do lokálnej a keď tam nenájde, tak do globálnej tabuľky) a potom ho z tejto tabuľky vyhodí. Príkaz nefunguje pre štandardné mená.

Ukážme to na príklade: identifikátora **print** ktorý je menom štandardnej funkcie (v štandardnej tabuľke mien). Ak v priamom režime (čo je globálna úroveň mien) do premennej print priradíme nejakú hodnotu, toto meno vznikne v globálnej tabuľke:
~~~
>>> print('ahoj')
ahoj
>>> print=('ahoj')          # do print sme priradili nejakú hodnotu
>>> print
'ahoj'
>>> print('ahoj')
...
TypeError: 'str' object is not callable
~~~
Teraz už print nefunguje ako funkcia na výpis hodnôt, ale len ako obyčajná globálna premenná. Ale v štandardnej tabuľke mien print stále existuje, len je **prekrytá** globálnym menom. Python predsa najprv prehľadáva globálnu tabuľku a až keď sa tam nenájde, hľadá sa v štandardnej tabuľke. A ako môžeme vrátiť funkčnosť štandardnej funkcie print? Stačí v+sak vymazať identifikátor z globálnej tabuľky a zase dostaneme funkciu:
~~~
>>> del print
>>> print('ahoj')
ahoj
~~~
Vymazaním globálneho mena print ostane definovaný len identifikátor v tabuľke štandardných mien, teda opäť začne fungovať funkcia na výpis hodnôt.

Pozrime sa teraz na prípad, keď sa v tele funkcie bude nachádzať volanie inej funkcie (tzv. **vnorené volanie**), napr.
~~~
def vypis_hviezdiciek(pocet):
    print('*' * pocet)

def trojuholnik(n):
    for i in range(1, n + 1):
        vypis_hviezdiciek(i)
~~~
Pri ich definovaní v globálnom priestore mien vznikli dva identifikátory: **vypis_hviezdiciek a trojuholnik**. Zavoláme funkciu trojuholnik:
~~~
>>> trojuholnik(5)
~~~
Najprv sa pre túto funkciu vytvorí jej menný priestor (lokálna tabuľka mien) s dvomi lokálnymi premennými: n a i. Teraz **pri každom** (vnorenom) volaní vypis_hviezdiciek(i) sa pre túto funkciu:

* vytvorí nový menný priestor s jedinou premennou pocet
* vykoná sa príkaz print()
* nakoniec sa zruší jej menný priestor, t.j. zanikne premenná pocet

Môžeme si to pre názornosť odkrokovať pomocou [interaktívneho Pythonu]( http://www.pythontutor.com/visualize.html#mode=edit ) (zapneme voľbu Python 3.3):

* najprv do editovacieho okna zapíšeme nejaký program, napr.
![](./29_Funkcia_definicia_rozdelenie/Tahaky_dokumenty_obrazky/funkcie_del01.png)

* spustíme vizualizáciu pomocou tlačidla Visualize Execution a potom niekoľkokrát tlačíme tlačidlo Forward 
![](./29_Funkcia_definicia_rozdelenie/Tahaky_dokumenty_obrazky/funkcie_del02.png)

Všimnite si, že v pravej časti tejto stránky sa postupne zobrazujú menné priestory (tu sa nazývajú frame):
* najprv len globálny priestor s premennými vypis_hviezdiciek a trojuholnik
* potom sa postupne objavujú a aj miznú lokálne priestory týchto dvoch funkcií - na obrázku vidíme oba tieto menné priestory tesne pred ukončením vykonávania funkcie trojuholnik s parametrom 2


>## Rozdelenie funkcii

>### Funkcie s návratovou hodnotou

Väčšina štandardných funkcií v Pythone na základe parametrov vráti nejakú hodnotu, napr.
~~~
>>> abs(-5.5)
5.5
>>> round(2.36, 1)
2.4
~~~
Funkcie, ktoré sme zatiaľ vytvárali my, takú možnosť nemali: niečo počítali, niečo vypisovali, ale žiadnu návratovú hodnotu nevytvárali. Aby funkcia mohla vrátiť nejakú hodnotu ako výsledok volania funkcie, musí sa v jej tele objaviť príkaz **return**, napr.
~~~
def meno(parametre):
    prikaz
    prikaz
    ...
    return hodnota                  # takáto funkcia bude vracať výslednú hodnotu
~~~
Príkazom return sa ukončí výpočet funkcie (zruší sa jej menný priestor) a uvedená hodnota sa stáva výsledkom funkcie, napr.
~~~
def eura_na_koruny(eura):
    koruny = round(eura * 30.126, 2)
    return koruny
~~~
môžeme otestovať:
~~~
>>> print('dostal si', 123, 'euro, čo je', eura_na_koruny(123), 'korún')
dostal si 123 euro, čo je 3705.5 korún
~~~
Niekedy potrebujeme návratovú hodnotu počítať nejakým cyklom, napr. nasledovná funkcia počíta súčet čísel od 1 do n:
~~~
def suma(n):
    vysledok = 0
    while n > 0:
        vysledok += n
        n -= 1
    return vysledok
~~~
Zároveň vidíme, že formálny parameter (je to predsa lokálna premenná) môžeme v tele funkcie modifikovať.

Už sme videli, že rozlišujeme dva typy funkcií:

* také, ktoré niečo robia (napr. vypisujú, kreslia, …), ale nevracajú návratovú hodnotu (neobsahujú return s nejakou hodnotou)
* také, ktoré niečo vypočítajú a vrátia nejakú výslednú hodnotu - musia obsahovať return s návratovou hodnotou

Ďalej ukážeme, že rôzne funkcie môžu vracať hodnoty rôznych typov. Najprv číselné funkcie.

>### Číselné funkcie 
Výsledkom takejto funkcie je číslo. Nasledovná funkcia počíta n-tú mocninu nejakého čísla a tento výsledok ešte zníži o 1:
~~~
def pocitaj(n):
    return 2 ** n - 1
~~~
Zrejme výsledkom tejto funkcie je vždy len číslo.

V pythone je možné ľahko alebo množstvo matematických operácií riešiť importovaním modulu s názvom **math**, ktorý definuje rôzne funkcie na uľahčenie výpočtov v našich úlohách. Použitie niektorých z nich najdeme [tu](https://www-geeksforgeeks-org.translate.goog/mathematical-functions-python-set-1-numeric-functions/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp). **Trigonometrické funkcie** zase nájdeme [tu](https://www-geeksforgeeks-org.translate.goog/mathematical-functions-in-python-set-3-trigonometric-and-angular-functions/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) a s používaním **logaritmických funkcii** sa môžeme zoznámiť [tu](https://www-geeksforgeeks-org.translate.goog/mathematical-functions-python-set-2-logarithmic-power-functions/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp). Poslednou skupinu ktorá patrí do skupiny numerických funkcii a ktorú na tomto mieste spomenieme sú **špecialne funkcie a konštatnty**. Ich popis s príkladmi nájdeme [tu](https://www-geeksforgeeks-org.translate.goog/mathematical-functions-in-python-set-4-special-functions-and-constants/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp).

>### Logická funkcia
Funkcie môžu vracať aj hodnoty iných typov, napr.
~~~
def parne(n):
    return n % 2 == 0
~~~
Táto funkcia vráti True alebo False podľa toho či je n párne (zvyšok po delení 2 bol 0), vtedy vráti True, alebo nepárne (zvyšok po delení 2 nebol 0) a vráti False. Túto istú funkciu môžeme zapísať aj tak, aby bolo lepšie vidieť tieto dve rôzne návratové hodnoty:
~~~
def parne(n):
    if n % 2 == 0:
        return True
    else:
        return False
~~~
Hoci táto verzia robí presne to isté ako predchádzajúca, skúsení programátori radšej používajú kratšiu prvú verziu. Keď chceme túto funkciu otestovať, môžeme zapísať:
~~~
>>> parne(10)
True
>>> parne(11)
False
>>> for i in range(20, 30):
        print(i, parne(i))

Vysledok:
20 True
21 False
22 True
23 False
24 True
25 False
26 True
27 False
28 True
29 False
~~~

>### Reťazcové funkcie

Napíšme funkciu, ktorá vráti nejaký reťazec v závislosti od hodnoty parametra:
~~~
def farba(ix):
    if ix == 0:
        return 'red'
    elif ix == 1:
        return 'blue'
    else:
        return 'yellow'
~~~
Funkcia vráti buď červenú, alebo modrú, alebo žltú farbu v závislosti od hodnoty parametra.

Opäť by ju bolo dobre najprv otestovať, napr.
~~~
>>> for i in range(6):
        print(i, farba(i))

Vysledok:
0 red
1 blue
2 yellow
3 yellow
4 yellow
5 yellow
~~~
Uvedomte si, prečo ju môžeme zapísať aj takto bez else vetiev:
~~~
def farba(ix):
    if ix == 0:
        return 'red'
    if ix == 1:
        return 'blue'
    return 'yellow'
~~~

V takýchto prípadoch je na vás, ktorý zápis použijete, ktorý z nich sa vám zdá čitateľnejší.

>### Grafické funkcie

Poslednou skupinou základného rozdelenia funkcii ktorým budeme venovať samostatnú kapitolu sú grafické funkcie. Ide o funkcie pre ktoré je charakteristický grafický výstup t.j. nejaký obrázok resp. graf.

>### Funkcia ako hodnota
v Pythone sú aj funkcie objektami a môžeme ich priradiť do premennej, napr.
~~~
>>> def fun1(x):
         return x*x
>>> fun1(7)
49
>>> cojaviem = fun1
>>> cojaviem(8)
64
~~~

Funkcie môžu byť prvkami polí, napr.
~~~
>>> def fun2(x): return 2*x+1
>>> def fun3(x): return x//2
>>> pole = [fun1, fun2, fun3]
>>> for f in pole:
        print(f(10))
100
21
5
~~~

Funkciu môžeme poslať ako parameter do inej funkcie, napr.
~~~
>>> def urob(fun, x):
        return fun(x)
>>> urob(fun2, 3.14)
7.28
~~~

Funkcia (teda referencia na funkciu) môže byť aj prvkom asociatívneho poľa. Pekne to ilustruje príklad s korytnačkou:
~~~
def vykonaj():
    t = turtle.Turtle()
    p = {'fd': t.fd, 'rt': t.rt, 'lt': t.lt}
    while True:
        prikaz, parameter = input('> ').split()
        p[prikaz](int(parameter))
~~~
a funguje napr.:
~~~
>>> vykonaj()
> fd 100
> lt 90
> fd 50
> rt 60
> fd 100
~~~

>### Anonymné funkcie

Často sa namiesto jednoriadkovej funkcie, ktorá počíta jednoduchý výraz a tento vráti ako výsledok (return) používa špeciálna konštrukcia lambda. Tá vygeneruje tzv. anonymnú funkciu, ktorú môžeme priradiť do premennej alebo poslať ako parameter do funkcie, napr.
~~~
>>> urob(lambda x: 2*x+1, 3.14)
7.28
~~~

Tvar konštrukcie lambda je nasledovný:

**lambda** parametre: výraz

Tento zápis nahrádza definovanie funkcie:
~~~
def anonymne_meno(parametre):
    return vyraz
~~~

Môžeme zapísať napr.
~~~
lambda x: x%2==0              # funkcia vráti True pre párne číslo
lambda x,y: x**y              # vypočíta príslušnú mocnimu čísla
lambda x: isinstance(x, int)  # vráti True pre celé číslo
~~~

>### Mapovacie funkcie

Ideu funkcie ako parametra najlepšie ilustruje funkcia mapuj():
~~~
def mapuj(fun, pole):
    vysl = []
    for prvok in pole:
        vysl.append(fun(prvok))
    return vysl
~~~

Funkcia aplikuje danú funkciu (prvý parameter) na všetky prvky poľa a z výsledkov poskladá nové pole, napr.
~~~
>>> mapuj(fun1, (2,3,7))
[4, 9, 49]
>>> mapuj(list,'Python'))
[['P'], ['y'], ['t'], ['h'], ['o'], ['n']]
>>> mapuj(lambda x: [x]*x, range(1,6))
[[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]
~~~

V Pythone existuje štandardná funkcia **map()**, ktorá robí skoro to isté ako naša funkcia mapuj() ale s tým rozdielom, že map() nevracia pole, ale niečo ako generátorový objekt, ktorý môžeme použiť ako prechádzanú postupnosť vo for-cykle, alebo napr. pomocou list() ho previesť na pole, napr.
~~~
>>> list(map(int,str(2**30)))
[1, 0, 7, 3, 7, 4, 1, 8, 2, 4]
~~~
Vráti pole cifier čísla 2**30.

Podobná funkcii mapuj() je aj funkcia filtruj(), ktorá z daného poľa vyrobí nový nové pole, ale nechá len tie prvky, ktoré spĺňanú nejakú podmienku. Podmienka je definovaná funkciou, ktorá je prvým parametrom:
~~~
def filtruj(fun, pole):
    vysl = []
    for prvok in pole:
        if fun(prvok):
            vysl.append(prvok)
    return vysl
~~~
Napr.
~~~
>>> def podm(x): return x%2==0      # zistí, či je číslo párne
>>> list(range(1, 20, 3))
[1, 4, 7, 10, 13, 16, 19]
>>> mapuj(podm, range(1, 20, 3))
[False, True, False, True, False, True, False]
>>> filtruj(podm, range(1, 20, 3))
[4, 10, 16]
~~~

Podobne ako pre mapuj() existuje štandardná funkcia **map()**, aj pre filtruj() existuje štandardná funkcia filter() - tieto dve funkcie ale nevracajú pole (list) ale postupnosť, ktorá sa dá prechádzať for-cyklom alebo poslať ako parameter do funkcie, kde sa očakáva postupnosť.

Ukážkovým využitím funkcie map() je funkcia, ktorá počíta ciferný súčet nejakého čísla:
~~~
def cs(cislo):
    return sum(map(int,str(cislo)))

>>> cs(1234)
10
~~~

>### Čiastkové funkcie

Čiastkové funkcie nám umožňujú opraviť určitý počet argumentov funkcie a vygenerovať novú funkciu. Čiastočné funkcie možno použiť na odvodenie špecializovaných funkcií zo všeobecných funkcií, a preto nám pomáhajú znova použiť náš kód.
~~~

                    from functools import partial
                   

                    
                   

                    # A normal function
                   

                    def f(a, b, c, x):
                   

                    	return 1000*a + 100*b + 10*c + x
                   

                    
                   

                    # A partial function that calls f with
                   

                    # a as 3, b as 1 and c as 4.
                   

                    g = partial(f, 3, 1, 4)
                   

                    
                   

                    # Calling g()
                   

                    print(g(5))
                   
Vysledok:

3145
~~~
V príklade sme našu funkciu vopred vyplnili niektorým konštantnými hodnotami a, ba c. A g() má iba jeden argument, tj premennú x.

Ďalší príklad:
~~~

                    from functools import *
                   

                    
                   

                    # A normal function
                   

                    def add(a, b, c):
                   

                    	return 100 * a + 10 * b + c
                   

                    
                   

                    # A partial function with b = 1 and c = 2
                   

                    add_part = partial(add, c = 2, b = 1)
                   

                    
                   

                    # Calling partial function
                   

                    print(add_part(3))
                   
Vysledok:

312
~~~

>### Generátorová notácia

Veľmi podobná funkcii map() je generátorová notácia (po anglicky list comprehension):
* je to spôsob, ako môžeme elegantne vygenerovať nejaké pole pomocou for-cyklu a nejakého výrazu
  
* do [...] nezapíšeme prvky poľa, ale predpis, akým sa majú vytvoriť, základný tvar je tohto zápisu:

#### [vyraz **for** i **in** postupnosť]

* kde výraz najčastejšie obsahuje premennú cyklu a postupnosť je ľubovoľná štruktúra, ktorá sa dá prechádzať for-cyklom (napr. list, set, str, range(), riadky otvoreného súboru, ale aj výsledok map() a filter() a pod.
  
* táto notácia môže používať aj vnorené cykly ale aj podmienku if, vtedy je to v takomto tvare:

#### [vyraz **for** i **in** postupnosť **if** podmienka]
* generátorová notácia s podmienkou nechá vo výsledku len tie prvky, ktoré spĺňajú danú podmienku

Niekoľko príkladov:
~~~
>>> [i**2 for i in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> [[i*j for i in range(1, 6)] for j in range(1, 6)]
[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
>>> [i for i in range(100) if cs(i)==5]      # cs() vypočíta ciferný súčet
[5, 14, 23, 32, 41, 50]
~~~
Pomocou tejto konštrukcie by sme vedeli zapísať aj mapovacie funkcie:
~~~
def mapuj(fun, pole):
    return [fun(prvok) for prvok in pole]

def filtruj(fun, pole):
    return [prvok for prvok in pole if fun(prvok)]
~~~
Všimnite si, že funkcia filtruj() využíva if, ktorý je vo vnútri generátorovej notácie.

Tabuľka všetkých zabudovaných funkcii je tu :
https://docs.python.org/3/library/functions.html

>### Testovanie funkcie
Ak chceme funkciu otestovať, buď ju spustíme s konkrétnym parametrom, alebo napíšeme cyklus, ktorý našu funkciu spustí s konkrétnymi hodnotami (niekedy na testovanie píšeme ďalšiu testovaciu funkciu, ktorá nerobí nič iné, „len“ testuje funkciu pre rôzne hodnoty a porovnáva ich s očakávanými výsledkami), napr.
~~~
>>> pocitaj(5)
31
>>> for i in 1, 2, 3, 8, 10, 16, 20, 32:
        print('pocitaj( {} ) = {}'.format(i, pocitaj(i)))

pocitaj( 1 ) = 1
pocitaj( 2 ) = 3
pocitaj( 3 ) = 7
pocitaj( 8 ) = 255
pocitaj( 10 ) = 1023
pocitaj( 16 ) = 65535
pocitaj( 20 ) = 1048575
pocitaj( 32 ) = 4294967295
~~~
Ďalšia funkcia zisťuje dĺžku (počet znakov) zadaného reťazca. Využíva to, že for-cyklus vie prejsť všetky znaky reťazca a s každým môže niečo urobiť, napr. zvýšiť počítadlo o 1:
~~~
def dlzka(retazec):
    pocet = 0
    for znak in retazec:
        pocet += 1
    return pocet
~~~
Otestujeme:
~~~
>>> dlzka('Python')
6
>>> dlzka(10000 * 'ab')
20000
~~~

>



Funkcie rozdelenie pokračovanie