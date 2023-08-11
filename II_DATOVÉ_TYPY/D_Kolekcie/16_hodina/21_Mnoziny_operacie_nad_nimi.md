# Množiny (set)
Množiny sa používajú na uloženie viacerých položiek do jednej premennej. Set je kolekcia, ktorá je neusporiadaná , nemeniteľná t.j. neindexovaná a iterovatelná. Je to druh kolekcie ktorá opäť vychádza zo zoznamu (list) s tým rozdielom, že môže obsahovať iba unikátné (neopakujúce sa) položky t.j. **každá položka môže byť v množine zastúpená iba jeden krát**. Hlavnou výhodou použitia množiny na rozdiel od zoznamu je to, že má vysoko optimalizovanú metódu na kontrolu, **či je v množine obsiahnutý konkrétny prvok ktorý nás zaujíma**.Kedže táto vlastosť zodpovedá matematickéj definicii množiny, tak táto kolekcia aj v Pythone dostala názov množiny. V súvislosti so set-om tiež hovoríme že **položky nie sú zotriedené** - sú neusporiadané, čo znamená to, že položka bude pridaná svojvolne na ľubovolné miesto do množiny a položky nemajú definované poradie t.j. nie sú indexované a teda nie je možné na ne odkazovať podľa indexu alebo definovaného kľuča. Pojem **immutable** resp. nemenné znamená, že po ich vytvorení ich už nemôžeme meniť. Môžeme ich však zmazať alebo pridať ako nové v požadovanej podobe. Výraz **neopakujúce sa** zase znamená, že ak zadáme príkaz na pridanie hodnoty do množiny, bude táto hodnota vložená do množiny, len vtedy ak sa v nej ešte nevyskytuje. Pojem **iterovatelnosti** znamená že môžeme prechádzať prvkami kolekcie pomocou cyklu (napr. for a pod). Cyklami sa budeme zaoberať neskôr avšak na tomto mieste uvedieme kvôli názornosti iba malú ukážku:
~~~
pole = [2, 3, 5, 7, 11, 13, 17]
for i in pole:
    print(i, i*i)
~~~


Množinu môžeme vytvoriť aj manuálne a to tak že nejakej premennej ktorej dáme napr. názov a_set priradíme hodnoty ktoré sú v zložených zátvorkách oddelené čiarkami.
~~~
a_set = {1}         #   ①
print(a_set)
{1}

print(type(a_set))  #   ②
<class 'set'>

a_set = {1, 'Stevo', 10.5, True}      #   ③
print(a_set)
{1, 'Stevo', 10.5, True}

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums) 
{1, 2, 3, 4, 5}


~~~
①	Zápis množiny keď chceme vytvoriť množinu s jednou hodnotou. Vtedy uzatvoríme túto hodnotu do zložených zátvoriek { }.
②	Množiny sú v skutočnosti implementované ako triedy, ale týmto sa teraz zaoberať nebudeme.
③	Ak chceme vytvoriť množinu s viacerými hodnotami, oddelíme hodnoty čiarkami a všetko uzatvoríme do zložených zátvoriek. Pritom možno použiť aj rôzne údajové typy.

Súčasťou vytvoreného objektu môžu byť iba nemenné (a hašovateľné) prvky. Čísla (celé čísla, pohyblivé čísla, ako aj komplexné), reťazce a objekty tuple sú akceptované, ale objekty množiny, zoznamu a slovníka nie. Aj keď meniteľné prvky nemôžu byť uložené v množine, množina samotná je meniteľným objektom.
~~~
myset = {(10,10), 10, 20}
print(myset)

myset = {[10, 10], 10, 20}  #TypeError can't add a list

myset = { {10, 10}, 10, 20} #TypeError can't add a set
~~~
Vo vyššie uvedenom príklade (10,10)je to n-tica, a preto sa stáva súčasťou sady. Ide však [10,10]o zoznam, preto sa zobrazí chybové hlásenie, že zoznam je nehašovateľný. ( [Hashovanie](https://en.wikipedia.org/wiki/Hash_function) je mechanizmus v informatike, ktorý umožňuje rýchlejšie vyhľadávanie objektov v pamäti počítača.)

Pre množiny **neexistuje žiadná zvláštna syntax** ako to bolo v prípade zoznamov či n-tic, vytvárame ich jednoducho použitím globálnej funkcie set(), ku ktorej môžeme napr. použitím funkcie add() priložiť novú hodnotu, ktorá sa nachádza v jej parametri. To je príklad jednej z viacerých funkcii resp. metód ktoré môžeme použiť nad danou množinou:
~~~
planety = set(("Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun"))
print(planety)

planety.add("Pluto")
print(planety)

planety.add("Neptun")
print(planety)

Výsledok:
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země'}
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země', 'Pluto'}
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země', 'Pluto'}
~~~
V príklade výššie sme vytvorili množinu šiestich mien planet. Dvojité zátvorky na riadku s funkciou set() znamenajú, že sme odovzdali názvy planet formou n-tice ako parameter tejto
funkcie. Poradie položiek není zoradené podľa abecedy, a nezmení sa ani po pridaní novej položky. To ale nie je žiadná chyba, lebo položky sú evidované v danom poradí, čo nám pomáha na množine určiť pozíciu každej položky.

>**Množinu môžeme vytvoriť aj zo zoznamu (list).**
~~~
a_list = ['a', 'b', 'mpilgrim', True, False, 42]    # toto je zoznam, viete preco

a_set = set(a_list)                           #      ①
print(a_set)                                   
{'a', False, 'b', True, 'mpilgrim', 42}       #      ②

print(a_list)                                  
['a', 'b', 'mpilgrim', True, False, 42]       #      ③
~~~
①	K vytvoreniu množiny zo zoznamu sme použili funkciu set(). (Odborníci na Python vedia ako sú množiny implementované. Vedia teda že aj to že v skutočnosti nejde o volanie funkcie, ale o vytváranie tzv. inštancie triedy. Táto problematika spadá do vlastného OOP ktorou sa budeme zaoberať v ďalšom ročníku lebo teraz našu pozornosť sústreďujeme hlavne na základy Pythonu. Preto nám yzatiaľ bude stačit vedieť, že set() sa chová ako funkcia a že vracia množinu.)\
②	Ako sme sa už zmienili skôr, jedna množina môže obsahovať hodnoty ľubovolného datového typu. A tiež sme už spoznali, že množiny sú neusporiadané. Táto množina si nepamätuje pôvodné poradie prvkov v zozname, ktorý ból použitý k jej vytvoreniu. Ak by sme do množiny pridávali ďalšie prvky, nebude si množina pamätovať poradie, v akom ste ich vkladali.\
③	Pôvodný zoznam zostáva nezmenený.

**Poznámka:** Hodnoty Truea 1sa v súboroch považujú za rovnakú hodnotu a zaobchádza sa s nimi ako s duplikátmi.

>**Vytvorenie prázdnej množiny**

Ak nemáme k dispozícii žiadne hodnoty (s tým že budú vytvorené resp. načítané podľa nejakého kritéria neskôr) nie je to žiadny problém. Môžeme totiž vytvoriť tzv. prázdnu množinu čím si vyčleníme (alokujeme) priestor a názov množiny pre neskoršiu aktualizáciu.
~~~
a_set = set()          #  ①
a_set                  #  ②
print(set())
# set()

>>> type(a_set)        #  ③
<class 'set'>

print(len(a_set))      #  ④
# 0

>>> not_sure = {}      #  ⑤
>>> type(not_sure)
<class 'dict'>
~~~
①	K vytvoreniu prázdnej množiny zavoláme set() bez argumentov.\
②	Zobrazená reprezentácia prázdnej množiny vypadá trochu divne. Asi sme očakávali niečo ako { } . Týmto spôsobom sa ale vyjadruje prázdny slovník (dictionary) a nie množina. O slovníkoch se dozvieme v nasledujúcej časti.\
③	Navzdory podivnosti zobrazenej reprezentácie to skutočne je množina...\
④	...a táto množina neobsahuje žiadné prvky.\
⑤	Prázdnu množinu nie je možné vytvoriť zápisom dvoch zložených zátvoriek kvôli histórii vývoja verzii (z Pythonu ver. 2). Týmto spôsobom sa vyjadruje prázdny slovník a nie množina.
>## Pridávanie hodnôt do množiny

# Operácie nad množinami (set-mi)
>## Zistenie počtu položiek množiny
Ak chcete zistiť, koľko položiek má sada, použite len()funkciu.
~~~
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
~~~

Do existující množiny můžeme přidávat hodnoty dvěma různými způsoby: metodou add() a metodou update().
~~~
>>> a_set = {1, 2}
>>> a_set.add(4)  ①
>>> a_set
{1, 2, 4}
>>> len(a_set)    ②
3
>>> a_set.add(1)  ③
>>> a_set
{1, 2, 4}
>>> len(a_set)    ④
3
~~~
①	Metoda add() přebírá jeden argument, který může být libovolného datového typu, a přidává zadanou hodnotu do množiny.
②	Množina teď má tři členy.
③	Množiny jsou kolekcemi jedinečných hodnot. Pokud do množiny zkusíme přidat hodnotu, která se v ní již nachází, neudělá to nic. Nevznikne chyba. Jde zkrátka o prázdnou operaci.
④	Množina má pořád jen tři členy.
~~~
>>> a_set = {1, 2, 3}
>>> a_set
{1, 2, 3}
>>> a_set.update({2, 4, 6})                       ①
>>> a_set                                         ②
{1, 2, 3, 4, 6}
>>> a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})  ③
>>> a_set
{1, 2, 3, 4, 5, 6, 8, 9, 13}
>>> a_set.update([10, 20, 30])                    ④
>>> a_set
{1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 20, 30}
~~~
①	Metoda update() přebírá jeden argument, rovněž množinu, a přidá všechny její členy do původní množiny. Je to, jako kdybychom volali metodu add() pro všechny členy množiny předané argumentem.
②	Protože cílová množina nemůže obsahovat jednu hodnotu dvakrát, duplicitní hodnoty se ignorují.
③	Ve skutečnosti můžete metodu update() volat s libovolným počtem argumentů. Pokud ji zavoláte s dvěma množinami, metoda update() přidá všechny členy z každé z předaných množin do původní množiny (duplicitní hodnoty se přeskočí).
④	Metoda update() umí zpracovat objekty různých datových typů, včetně seznamů. Pokud jí předáte seznam, pak metoda update() přidá do původní množiny všechny členy seznamu.

>## Odstraňovanie položiek z množiny
ednotlivé hodnoty lze z množiny odstranit třemi způsoby. První dva, discard() a remove(), se liší v jedné malé drobnosti.
~~~
>>> a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
>>> a_set
{1, 3, 36, 6, 10, 45, 15, 21, 28}
>>> a_set.discard(10)                        ①
>>> a_set
{1, 3, 36, 6, 45, 15, 21, 28}
>>> a_set.discard(10)                        ②
>>> a_set
{1, 3, 36, 6, 45, 15, 21, 28}
>>> a_set.remove(21)                         ③
>>> a_set
{1, 3, 36, 6, 45, 15, 28}
>>> a_set.remove(21)                         ④
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 21
~~~
①	Metoda discard() přebírá jeden argument a zadanou hodnotu odebere z množiny.\
②	Pokud metodu discard() voláme s hodnotou, která v množině neexistuje, neprovede se nic. Nevznikne chyba. Jde o prázdnou operaci.\
③	Metoda remove() také přebírá hodnotu jediného argumentu a také odstraňuje hodnotu z množiny.\
④	Odlišnost se projeví v případě, kdy se zadaná hodnota v množině nenachází. V takovém případě metoda remove() vyvolá výjimku KeyError.



Pokračovanie č. I

