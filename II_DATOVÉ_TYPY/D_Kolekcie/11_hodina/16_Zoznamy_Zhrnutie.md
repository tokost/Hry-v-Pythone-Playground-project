> ## Zhrnutie

> **Vytvorenie zoznamu**

Na vytvorenie zoznamu v Pythone používame hranaté zátvorky ( []). Zoznam vyzerá takto:

> MenoZoznamu = [PrvokZoznamu, PrvokZoznamu1, PrvokZoznamu2, PrvokZoznamu3, ...]

Príklad:\
names = ["Jane", "John", "Jade", "Joe

Pričom zoznamy môžu obsahovať rôzne typy údajov. Môžete obsahovať alebo iba konkrétny typ údajov, alebo ich môžu mať zmiešané.

> **Zistenie či v zozname existuje položka**

Ak chcete zistiť, či sa určitá položka nachádza v zozname, použijeme kľúčové slovo **in**. Dajme tomu že chceme zistiť či sa v zozname nachádza prvok "apple":
Príklad:
~~~
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:   # tym ze je to True prejde na vypis
    print("Yes, 'apple' is in the fruits list")

print("No, 'apple' is not in the fruits list")

Yes, 'apple' is in the fruits list    
~~~
> **Prístup k položkám zoznamu**

* K položkám v zozname môžete pristupovať pomocou indexu položky.

A to alebo pozitívneho, alebo negatívneho indexovania.

Príklad pozitívneho indexovania:
~~~
names = ["Jane", "John", "Jade", "Joe"]
print(names[0])

Jane
~~~
Zobrazili sme položku s indexom 0: print(names[0]). Vytlačená položka bola „Jane“, pretože je to prvá položka v zozname.

Index 0 = Jane
Index 1 = John
Index 2 = Jade
Index 3 = Joe

Pomocou negatívneho indexovania môžeme pristupovať k položkám od konca poľa. 

Príklad negatívneho indexovania:
~~~
names = ["Jane", "John", "Jade", "Joe"]
print(names[-1])

Joe
~~~
Index -1 = Joe\
Index -2 = Jade\
Index -3 = John\
Index -4 = Jane

* Prístup k intervalu položiek od začiatku

Zadaním rozsahu indexov určíme kde sa má rozsah začať a kde sa má skončiť. Po vykonaní operácie bude návratovou hodnotou nový zoznam so zadanými položkami. Vyhľadávanie pritom začne od prvého indexu (napr.2) a skončí pred druhým indexom (t.j. 4). 

Príklad:
~~~
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

['cherry', 'orange', 'kiwi']
~~~
Vynechaním počiatočnej hodnoty sa rozsah začne od prvej položky:
~~~
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

['apple', 'banana', 'cherry', 'orange']
~~~
Vynechaním koncovej hodnoty sa rozsah presunie na koniec zoznamu:
~~~
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

['cherry', 'orange', 'kiwi', 'melon', 'mango']
~~~


* Prístup k intervalu položiek od konca
  
Ak chcete spustiť vyhľadávanie od konca zoznamu, zadajte záporné indexy:
~~~
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

['orange', 'kiwi', 'melon']
~~~
> **Zmena hodnoty položiek zoznamu**

Ak chcete zmeniť hodnotu položky v zozname, musíte sa odvolať na index položky a potom jej priradiť novú hodnotu.

Príklad:
~~~
names = ["Jane", "John", "Jade", "Joe"]
names[0] = "Doe"
print(names)

['Doe', 'John', 'Jade', 'Joe']
~~~
V kóde sme zmenili hodnotu prvej položky z „Jane“ na „Doe“ pomocou indexu položky a priradení nového reťazca: names[0] = "Doe".

> **Vkladanie do zoznamu**

Videli sme viac rôznych spôsobov, ako môžeme pridať jednu hodnotu do zoznamu. Vkladanie nejakej hodnoty pred prvok s indexom **i**:

* pomocou rezu (**mutable**):

    > zoznam[i:i] = [hodnota]

* pomocou metódy insert() (**mutable**):

    > zoznam.insert(i, hodnota)

Príklad:\
~~~
names = ["Jane", "John", "Jade", "Joe"]
names.insert(2, "Doe")
print(names)

['Jane', 'John', 'Doe', 'Jade', 'Joe']
~~~


* ak i == len(zoznam), pridávame na koniec (za posledný prvok), môžeme použiť metódu append() (**mutable**):

    > zoznam.append(hodnota)

Príklad:
~~~
names = ["Jane", "John", "Jade", "Joe"]
names.append("Doe")
print(names)

['Jane', 'John', 'Jade', 'Joe', 'Doe']
~~~

* to isté dosiahneme aj takto (**mutable**):

    > zoznam += [hodnota]

Vo vašich programoch použijete ten zápis, ktorý sa vám bude najlepšie hodiť, ale zápis s rezom zoznam[i:i] je najmenej čitateľný a používa sa veľmi zriedkavo.

* zrejme funguje aj (**immutable**):

    > zoznam = zoznam[:i] + [hodnota] + zoznam[i:]

Toto priradenie nemodifikuje pôvodný zoznam, ale vytvára nový s pridanou hodnotou.

> **Vyhadzovanie zo zoznamu**

Aj vyhadzovanie prvku zo zoznamu môžeme robiť viacerými spôsobmi. Ak vyhadzujeme prvok na indexe **i**, môžeme zapísať:

* pomocou rezu (**mutable**):

    > zoznam[i:i+1] = []

* pomocou príkazu del (**mutable**):

    > del zoznam[i]

Príklad:
~~~
names = ["Jane", "John", "Jade", "Joe"]
del names[1]    # zadanie indexu prvku zoznamu
                # AK HO NEZADAME VYMAZE CELY ZOZNAM !!!
print(names)

['Jane', 'Jade', 'Joe']
~~~


* pomocou metódy pop(), ktorá nám aj vráti vyhadzovanú hodnotu (**mutable**):

    > hodnota = zoznam.pop(i)

Príklad:
~~~
names = ["Jane", "John", "Jade", "Joe"]
names.pop()   # takto odstrani poslednu polozku zoznamu
              # alebo cez index urcit polozku napr. pop(2)
print(names)

['Jane', 'John', 'Jade']
~~~

* Pomocou metódy remove() je to veľmi neefektívne, lebo ako parameter očakáva nie index ale vyhadzovanú hodnotu (**mutable**):
  

    > zoznam.remove(zoznam[i])

Príklad:
~~~
names = ["Jane", "John", "Jade", "Joe"]
names.remove("John") # ako parameter funkcie odovzdame polozku ktora sa ma vyhodit
print(names)

['Jane', 'Jade', 'Joe']
~~~
Tento spôsob je veľmi neefektívny (zbytočne sa totiž hľadá prvok v zozname čím sa navyšuje čas vykonávania operácie a čerpanie výpočtový zdrojov napr. CPU, pamäte a pod.) Okrem toho niekedy sa môže vyhodiť nie i-ty prvok, ale prvok s rovnakou hodnotou, ktorý sa v zozname nachádza skôr, ako na indexe i.

* zrejme funguje aj (**immutable**):

    > zoznam = zoznam[:i] + zoznam[i+1:]

Toto priradenie nemodifikuje pôvodný zoznam, ale vytvára nový bez prvku s daným indexom.

> **Vyhodenie všetkých prvkov zo zoznamu**

* najjednoduchší spôsob (**immutable**):

    > zoznam = []

Môžeme ho v+sak použiť len vtedy, keď nepotrebujeme uchovať referenciu na zoznam - toto priradenie nahradí momentálnu referenciu na zoznam referenciou na úplne nový zoznam; ak to ale použijeme vo vnútri funkcie, stratí sa tým referencia na pôvodný zoznam.

***Nasledujúce ďalšie spôsoby uchovávajú referenciu na zoznam:***

* všetky prvky zoznamu postupne vyhodíme pomocou while-cyklu (**mutable**):

    > while zoznam:\
&emsp; &nbsp;zoznam.pop()

Toto je však zbytočne veľmi neefektívne riešenie.

* priradením do rezu (**mutable**):

    > zoznam[:] = []

Toto je yase ťažšie čitateľné a menej pochopiteľné riešenie.

* metódou clear() (**mutable**):

    > zoznam.clear()

Príklad:
~~~
names = ["Jane", "John", "Jade", "Joe"]
names.clear()

print(names)
[]
~~~
A toto je asi najčitateľnejší zápis !!!

> **Vytvorenie kópie zoznamu**

Ak potrebujeme vyrobiť kópiu celého zoznamu, dá sa to urobiť:

* pomocou cyklu:

    > kopia = [ ]\
for prvok in zoznam:\
&nbsp;&emsp; &nbsp;&emsp; &nbsp; kopia.append(prvok)

* môžeme využiť aj rez:

    >kopia = zoznam[:]

* keďže funguje funkcia list(), môžeme zapísať:

    > kopia = list(zoznam)

> **Spájanie zoznamov**
Ak chcete do aktuálneho zoznamu pridať prvky z iného zoznamu, použijeme metódu funkciu resp. metódu extend(). Kedy nové pr
Príklad :
~~~
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
~~~
Vzhľadom k tomu že ako zoznam tak aj n-tice, množiny a slovníky patria do skupiny .... môžeme aj ich spájať navzájom.

Príklad spojenia list a tuple:
~~~
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
thislist.extend(this_tuple)
print(this_list)

['apple', 'banana', 'cherry', 'kiwi', 'orange']
~~~

[SPAŤ](15_Dalsie_operacie_so_zoznamami04.md)