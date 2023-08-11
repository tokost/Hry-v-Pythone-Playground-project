Pokračovanie 1.

># Funkcie resp. metódy nad slovníkom

Podobne ako tomu bolo pri zoznamoch aj pre slovníky existuje niekoľko dostupných metód. Pozrime sa na tie najdôležitejšie.

# get()

Metóda get() ponúka ďalší spôsob na získanie položky zo slovníka. Hlavnou výhodou tejto metódy je to, že nevyhodí žiadnu výhradu (požiadavku na zadefinovanie výnimky) v prípade, že sa hľadaný klúč v slovníku nenachádza. Miesto toho vráti hodnotu s názvom **None** (že neexistuje) alebo niektorú východziu hodnotu, specifikovatelnú v druhom parametri ktorý možno pridať.
~~~
oblubeneVeci= {
    'homer': 'sisky',
    'marge': 'truba',
    'bart': 'prak',
    'lisa': 'saxofon'
}
print(oblubeneVeci.get('homer'))
print(oblubeneVeci.get('krusty'))
print(oblubeneVeci.get('krusty', 'nikdo'))
~~~

# values(), keys() a items()
Pomocou týchto metód môžeme previesť slovník (dictionary) na zoznam (list). Môžeme tak vyčleniť hodnoty, klúče alebo dokonca môžeme vytvoriť zoznamy n-tic (tuple) párov klúč-hodnota.
~~~
oblubeneVeci= {
    'homer': 'sisky',
    'marge': 'truba',
    'bart': 'prak',
    'lisa': 'saxofon'
}
print(oblubeneVeci.values())
print(oblubeneVeci.keys())
print(oblubeneVeci.items())
~~~
# clear()
Ako naznačuje smamotný názov, tak táto metóda "vyčistí" všetky položky zo slovníka.

Syntax: dictionary.clear()

Parametre: metóda clear() neberie žiadne parametre

Návratová hodnota: metóda clear() nvracia žiadnu hodnotu

~~~
# dictionary
numbers = {1: "one", 2: "two"}

# removes all the items from the dictionary
numbers.clear()

print(numbers)

# Output: {} t.j. metóda nám vrátila prázdny slovník s názvom numbers
~~~

# pop()
Odstráni a vráti položku zo slovníka s daným klúčom (key-om).

Syntax: dictionary.pop(key[, predvolené])

Parametre: metóda pop() má dva parametre \
*   **key** - kľúč, ktorý sa má vyhľadať na odstránenie
*   **default** - hodnota, ktorá sa má vrátiť, keď kľúč nie je v slovníku

Návratová hodnota: metóda pop() vracia:
* Ak key sa nájde - odstránený/vyskočený prvok zo slovníka
* Ak key sa nenájde - hodnota zadaná ako druhý argument (predvolené)
* Ak key sa nenájde a nie je zadaný predvolený argument - KeyError vyvolá sa výnimka
~~~
# create a dictionary
marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }

element = marks.pop('Chemistry')

print('Popped Marks:', element)

# Output: Popped Marks: 72
print('The rest of dictionary is:', marks)
~~~
Príklad na výber prvku ktorý sa v slovníku nenachádza:
~~~
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava')
# KeyError: 'guava'
~~~
Príklad na výber prvku ktorý sa v slovníku nenachádza keď je zadaná predvolená hodnota:
~~~
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava', 'Kľúč guava neexistuje v slovníku sales')

print('The popped element is:', element)
print('The dictionary is:', sales)
~~~
Ako vidieť v príkade vyberaný ból prvok kľúčom "guava" ktorý sa v dictionary nenachádzal. Pretože pri jeho výbere bola zadaná predvolená hodnota resp. text "Kľúč guava neexistuje v slovníku sales", bude zobrazený práve tento text.

# popitem()
Metóda Python popitem() odstráni a vráti posledný pár prvkov (kľúč>:hodnota) vložený do slovníka

Syntax: dict.popitem()

Parametre: metóda dict.popitem() neberie žiadne parametre

Návratová hodnota: Táto metóda sa vráti [plytkú kópiu](https://www-programiz-com.translate.goog/python-programming/shallow-deep-copy?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) slovníka. Nezmení pôvodný slovník.
~~~
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

# inserting a new element pair
person['profession'] = 'Plumber'

# now ('profession', 'Plumber') is the latest element
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)
~~~
Poznámka : Ak je slovník prázdny metóda popitem() vyvoláva chybu KeyError .

# update()
Metóda update() aktualizuje daný slovník pridaním prvkov z iného slovníka alebo z iterovatelných párov kľúč:hodnota.

Syntax: dict.update([other])

Parametre: Metóda update() používa slovníky ako celky alebo iterovateľný objekt párov kľúč:hodnota (vo všeobecnosti [n-tice](https://www-programiz-com.translate.goog/python-programming/tuple?_x_tr_sl=sk&_x_tr_tl=en&_x_tr_hl=sk&_x_tr_pto=wapp) ).
Ak sa update() zavolá bez zadania parametrov, slovník zostane nezmenený.

Návratová hodnota: update()metóda aktualizuje slovník s prvkami z iného slovníka alebo iterovateľného objektu párov kľúč:hodnota.

Nevracia žiadnu hodnotu iba uskutoční zlúčenie a preto ju nemožno priradiť ani nejakej premennej (vracia None).
~~~
marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}

marks.update(internal_marks)

print(marks)
# Output: {'Physics': 67, 'Maths': 87, 'Practical': 48}

zlucenie = marks.update(internal_marks)
print(zlucenie)
~~~
Fungovanie funkcie update():
~~~
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)

print(d)
# Výstup: {1: 'jeden', 2: 'dva'}

d1 = {3: "three"}

# adds element with key 3
d.update(d1)

print(d)
# Výstup:{1: 'jeden', 2: 'dva', 3: 'tri'}
~~~
**Poznámka :** Metóda update() pridá prvok(y) do slovníka, ak kľúč nie je v slovníku. Ak je kľúč v slovníku, aktualizuje kľúč novou hodnotou.
Príklad keď vytvoríme slovník na báze párov kľúč:hodnota t.j. pomocou tuple (n-tice) bude vyzerať nasledovne:
~~~
dictionary = {'x': 2}

dictionary.update([('y', 3), ('z', 0)])

print(dictionary)
# Výstup: {'x': 2, 'y': 3, 'z': 0}
~~~
V tomto príklade sme funkcii update() odovzdali zoznam n-tic (tuple) [('y', 3), ('z', 0)]. V tomto prípade sa prvý prvok n-tice použije ako kľúč a druhý prvok sa použije ako hodnota.

# copy()
Metóda copy()vracia kópiu (plytkú kópiu) slovníka.

Syntax: dict.copy()

Parametre: metóda dict.copy() neberie žiadne parametre

Návratová hodnota: m

~~~
original_marks = {'Physics':67, 'Maths':87}

copied_marks = original_marks.copy()


print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)

# Output: Original Marks: {'Physics': 67, 'Maths': 87}
#         Copied Marks: {'Physics': 67, 'Maths': 87}
~~~

~~~
original = {1:'one', 2:'two'}

new = original.copy()

print('Orignal: ', original)
print('New: ', new)

# Output: Pôvodné: {1: 'jeden', 2: 'dva'}
# Output: Nové: {1: 'jeden', 2: 'dva'}
~~~
Keď  použije metóda copy(), vytvorí sa nový slovník, ktorý sa naplní kópiou odkazov na pôvodný slovník. Pri použití operátora =  vytvorí sa nový odkaz na pôvodný slovník čím sa tiež vytvára kopírovanie slovníkov.
~~~
original = {1:'one', 2:'two'}

new = original

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

# Output: new: {}
#         originál: {}
~~~
Keď je vypísaný nový slovník new, tak je tiež vypísaný aj originálny slovník original.

# fromkeys() 
https://www.w3schools.com/python/ref_dictionary_fromkeys.asp

# setdefault()
https://www.w3schools.com/python/ref_dictionary_setdefault.asp

**Pravidlá pre výber** jednej z týchto dátových štruktúr sú v skutočnosti celkom jednoduché:

Ak potrebujete ***iba postupnosť prvkov***, ku ktorým máte prístup cez indexovanie, vyberte ***zoznam-list***.

Ak potrebujete ***rýchlo vyhľadať konrétny prvok*** namapovaný na konkrétny jedinečný kľúč, vyberte si ***slovník-dictionary***.

![](./Tahaky_dokumenty_obrazky/zoznamy_alebo_slovniky.png)

[Video a zhrnutie základných úkonov](https://www.programiz.com/python-programming/dictionary)

## Základné metódy
| Metóda    | Popis                                                                    |
|-----------|---------------------------------------------------------------------------|
|[dic.clear()](https://www.programiz.com/python-programming/methods/dictionary/clear)| Odstráňte všetky prvky zo slovníka
|[dict.copy()](https://www.programiz.com/python-programming/methods/dictionary/copy)| Vráti kópiu slovníka
|[dict.items()](https://www.programiz.com/python-programming/methods/dictionary/items)|  Vráti zoznam obsahujúci n-ticu pre každý pár kľúč-hodnota
| [dic.keys](https://www.programiz.com/python-programming/methods/dictionary/clear) | Vráti zoznam obsahujúci kľúče slovníka
|[dict.update(dikt2)](https://www.programiz.com/python-programming/methods/dictionary/update)| Aktualizuje slovník zadanými pármi kľúč – hodnota
| [dict.values()](https://www.programiz.com/python-programming/methods/dictionary/values) | 	 Vráti zoznam všetkých hodnôt slovníka
|[pop()](https://www.programiz.com/python-programming/methods/dictionary/pop)| Odstráňte prvok špecifikovaným kľúčom
|[popItem()](https://www.programiz.com/python-programming/methods/dictionary/popitem)|Odstráni posledný vložený pár kľúč – hodnota
|[dict.setdefault(key,default= “Žiadne”)](https://www.w3schools.com/python/ref_dictionary_setdefault.asp) | 	 nastavte kľúč na predvolenú hodnotu, ak kľúč nie je špecifikovaný v slovníku
|[dict.has_key(kľúč)](https://www.geeksforgeeks.org/python-dictionary-has_key/)| vráti hodnotu true, ak slovník obsahuje zadaný kľúč. Lepšie je však použiť [konštrukciu s in](https://stackoverflow.com/questions/1323410/should-i-use-has-key-or-in-on-python-dicts)
|[dict.get(kľúč, predvolené = “Žiadne”)](https://www.programiz.com/python-programming/methods/dictionary/get)|Vráti hodnotu zadaného kľúča.

Príklady
~~~
# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict2 = dict1.copy()
print(dict2)
                     
# clear() method
dict1.clear()
print(dict1)
                    
# get() method
print(dict2.get(1))

# items() method
print(dict2.items())
                     
# keys() method
print(dict2.keys())
                     
# pop() method
dict2.pop(4)
print(dict2)
                     
# popitem() method
dict2.popitem()
print(dict2)
                     
# update() method
dict2.update({3: "Scala"})
print(dict2)
                     
# values() method
print(dict2.values())
~~~
