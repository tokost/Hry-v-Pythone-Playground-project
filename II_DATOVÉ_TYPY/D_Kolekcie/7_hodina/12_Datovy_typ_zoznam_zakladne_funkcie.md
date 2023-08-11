># Dátové kolekcie


# Dátový typ zoznam (list) 

predstavuje súpis položiek ktorým hovoríme **prvky** a ktoré sú zostavené podľa určitého hľadiska (napr. tematického). Zoznam sa môže skladať z prvkov ktoré rôzneho dátového typu a tieto môžu byt usporiadané abecedne alebo systematicky napr. od najväčšieho po najmenšieho a pod. 
~~~
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
~~~
> ## Zoznamy sú používané pre uloženie viacerých prvkov do jednej premennej

Zoznamy patria jedným zo 4-och zabudovaných dátových typov v Pythone ktoré sa používajú na uloženie kolekcie (angl. collection) údajov. Ďalšie tri sú **Tuple**, **Set** a **Dictionary** ktoré majú odlišné použitie a kvalitu a ktorými sa budeme zaoberať neskôr. 

Prvky sú nositelmi významnej informácie ktorá ich navzájom spája a vytvára tak medzi nimi vzájomnú súvislosť. Môže to byť napr. zoznam mien žiakov v triede - list(("Matej", "Gabriel", "Zuzana")) Okrem názvu **zoznam**, môžeme používať aj názov **tabuľka** alebo **pole** (kedy pojem **pole** sa väčšinou používa pre zoznamy hodnôt rovnakého typu) 
~~~
zoznam = ["Matej", "Gabriel", "Zuzana"]
print(type(zoznam))

zoznam = list(("Matej", "Gabriel", "Zuzana")) # pouzitie zabudovanej funkcie list ktora vytvara objekt list
print(type(zoznam)) # <class 'list'>
~~~
Pripomeňme si že objekt je definovaný svojimi vlastnosťami a činnostami (funkciami) ktoré sa nad ním dajú výkonávať. Objekty rovnakých vlastností vytvárajú triedy. Napr. auto má vlastnosti kolesá, dvere, farbu atď a môžu sa nad nim vykonavať cinnosť pohyb resp. zastavenie a pod. V prípade objektu persona sú to vlastnosti ako meno, priezvisko, vek a môže sa nad ním vykonávať napr. zobrazenie týchto vlastností. Samotné zoznamy vytvárame vymenovaním prvkov v hranatých zátvorkách, a v nasledovnom príklade ich hneď aj priradíme do rôznych premenných:
~~~
>>> teploty = [10, 13, 15, 18, 17, 12, 12]
>>> nakup = ['chlieb', 'mlieko', 'rozky', 'jablka']
>>> studenti = ['Juraj Janosik', 'Emma Drobna', 'Ludovit Stur', 'Pavol Habera', 'Margita Figuli']
>>> zviera = ['pes', 'Dunco', 2011, 35.7, 'hneda']
>>> prazdny = []    # prázdny zoznam
>>> print(teploty)
    [10, 13, 15, 18, 17, 12, 12]
>>> type(zviera)
    <class 'list'>
~~~

* Položky zoznamu sú usporiadané (Ordered), meniteľné a umožňujú duplicitné hodnoty. Keď hovoríme, že zoznamy sú usporiadané, znamená to, že **položky majú definované poradie a toto poradie sa nezmení**.

* Položky zoznamu sú indexované, prvá položka má index [0], druhá položka má index [1]atď. Ak do zoznamu pridáte nové položky, **nové položky sa umiestnia na koniec zoznamu**. 
* Existuje niekoľko [metód zoznamu](https://www.w3schools.com/python/python_lists_methods.asp) , ktoré zmenia poradie, ale vo všeobecnosti platí: poradie položiek sa nezmení.
* Zoznam je meniteľný (Changeable), čo znamená, že môžeme meniť, pridávať a odstraňovať položky v zozname po jeho vytvorení.
* Keďže zoznamy sú indexované, zoznamy môžu mať položky s rovnakou hodnotou (Allow Duplicates):
~~~
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
~~~
# Funkcie nad zoznamami

Funkcie nad zoznamami vykonávajú s nimi základné operácie a fungujú skoro presne rovnako, ako ich vieme používať so znakovými reťazcami.

## Standardné funkcie so zoznamami
Nasledovné funkcie fungujú nielen so zoznamami, ale s ľubovoľnou postupnosťou hodnôt. V niektorých prípadoch však nemajú zmysel a vyhlásia chybu (napríklad číselný súčet prvkov znakového reťazca).
> ## Zistenie dĺžky zoznamu

Ak chcete zistiť, koľko položiek má zoznam, použite funkciu **len()**:
~~~
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
~~~
> ## Zistenie typu údajov
Z pohľadu Pythonu sú zoznamy definované ako objekty s dátovým typom 'list' t.j. <class 'list'>. Na zistenie tohoto tzpu používame funkciu **typ()**:
~~~
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
~~~
> ## Konštruktor zoznamu
Konstruktor je speciálná metoda (funkcia), ktorá je automaticky volaná pri vytváraní objektu. V iných prípadoch ju volať nemôžeme ! Pri vytváraní nového zoznamu je teda tiež možné použiť **konštruktor** ktorý sa označuje ako **list()**. Pomocou takéhoto konštruktora vytvorýme zoznam nasledovne:
~~~
thislist = list(("apple", "banana", "cherry")) # všimnite si dvojité okrúhle zátvorky miesto zatvoriek hranatych ktore tento postup charakterizuju
print(thislist)
~~~
> ## Vypočítanie súčet prvkov
**funkcia sum(postupnosť)**

> ## Vráti hodnotu maximálneho prvku
**funkcia max(postupnosť)**

> ## Vráti hodnotu minimálneho prvku
**funkcia min(postupnosť)**

Pre uvedené operácie môžeme takto uviesť nasledovné príklady:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = sum(teploty)
maximum = max(teploty)
minimum = min(teploty)
priemer = sucet / len(teploty)
print('priemerná teplota je', f'{priemer:.1f}')
print('minimálna teplota je', minimum)
print('maximálna teplota je', maximum)

priemerná teplota je 13.9
minimálna teplota je 10
maximálna teplota je 18
~~~
Čo sa dá zapísať úspornejšie, ale menej čitateľne aj takto:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]

print('priemerná teplota je', f'{sum(teploty)/len(teploty):.1f}')
print('minimálna teplota je', min(teploty))
print('maximálna teplota je', max(teploty))
~~~

> ## Funkcia list
Už máme nejaké skúsenosti s tým, že v Pythone každý základný typ má definovanú svoju konverznú funkciu, pomocou ktorej sa dajú niektoré hodnoty rôznych typov prekonvertovať na daný typ. Napríklad

int(3.14) -> vráti celé číslo 3

int('37') -> vráti celé číslo 37

str(22 / 7) -> vráti reťazec '3.142857142857143'

str(2 < 3) -> vráti reťazec 'True'

Podobne funguje aj funkcia list(hodnota):

* parametrom musí byť iterovateľná hodnota, t.j. nejaká postupnosť, ktorá sa dá prechádzať (iterovať), napríklad for-cyklom

* funkcia list() túto postupnosť rozoberie na prvky a z týchto prvkov poskladá nový zoznam
* parameter môže chýbať, vtedy vygeneruje prázdny zoznam
Napríklad:
~~~
>>> zviera = ['pes', 'Dunco', 2011, 35.7, 'hneda']
>>> list(zviera)                            # kópia existujúceho zoznamu
    ['pes', 'Dunco', 8, 35.7, 'hneda']

>>> list(range(5, 16))
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

>>> list('Python')
    ['P', 'y', 't', 'h', 'o', 'n']
>>> list()                                  # prázdny zoznam
    []
>>> list(3.14)
    ...
    TypeError: 'float' object is not iterable
~~~
Ak nejaký textový súbor s názvom subor.txt obsahuje takéto riadky:
~~~
Aká
práca,

taká
pláca.
~~~
Tak aj toto Python vidí ako postupnosť (otvorený súbor sa dá prechádzať for-cyklom ako postupnosť riadkov) a preto:
~~~
>>> myfile=list(open('C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\\Aplikovana_Informatika\\6_hodina\\subor.txt', encoding='utf-8'))
>>> print(myfile)
    ['Aká\n', 'práca,\n', '\n', 'taká\n', 'pláca.\n']
~~~

Pokračovanie č. I

