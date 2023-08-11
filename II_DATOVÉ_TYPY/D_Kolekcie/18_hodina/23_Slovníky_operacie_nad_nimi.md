# Slovník (Dictionary) 

V Pythone je slovník kolekcia, ktorá nám umožňuje ukladať dáta v key:value (kľúč:hodnota) pároch. Funguje tiež podobne ako zoznam, rozdieľ je však v tom, že k dictionary nepristupujeme len pomocou indexov, ale aj na základe klúčov ktoré môžu byť rôznych  dátových typov . Klúč slovníka tu predstavuje index. Na poradí jednotlivých položiek v slovníku pritom nezáleží. **Slovník je kolekcia, ktorá je neusporiadaná, meniteľná a indexovaná.**

Údaje v kolekcii sú uložené speciálnym spôsobom, tzv. [hashovaním](https://en.wikipedia.org/wiki/Hash_function) t.j. mechanizmom v informatiky, ktorý umožňuje rýchlejšie vyhľadávanie objektov v pamäti počítača. To nám umožňuje pristupovat k prvkom kolekcie pomocou klúča omnoho rýchlejšie, ako keby sme ich vyhľadávali hledali např. v obyčajnom zozname. V zozname je totiž potrebné všetky prvky prejisť a kontrolovať, či
náhodou vlastnosť daného prvku nezodpovedá tomu, co hľadáme. Dictionary resp. slovník dokáže na prvok kolekcie siahnuť omnoho rýchlejšie vďaka výpočtu tzv. hashe (otlačku). Môžeme si to predstaviť tak, že máme prvky v obyčajnomm zozname. Nie sú však bezprostredne za sebou a nejaké indexy nie sú využité vôbec. Finta spočíva v tom, že sme schopní z klúča zistiť index prvku pomocou hashovacej funkcie. Ak budeme mať napr. v slovníku uložených zamestnancov a klúčom bude ich meno, hashovacia funkcia nám z "Jan Novák" vráti např. hodnotu 114. Keď siahneme na 114. prvok, tak je tam Jan Novák. A slovník pritom vôbec nemusíme vôbec iterovat.

Slovník deklarujeme rovnako ako zoznam. Hlavný rozdiel spočíva v tom, že používame zložené zátvorky { } a musíme k položkám definovat i ich klúče. K tomu používame **operátor dvobodky :**. Slovníky sú teda používané k **uloženiu hodnôt v pároch klúč:hodnota (key:value)**. Prvkom kolekcie na rozdiel od iných typov dvojica.
~~~
oblubeneVeci= {
    'Jan Novak':'114',
    'homer': 'siska',
    'marge': 'truba',
    'bart': 'prak',
    'lisa': 'saxofon',
    'maggie': 'cumlik'
}
~~~
Zápis položiek sme úmyselne rozdelili kvôli prehľadnosti do viacerých riadkov, ale môže sa to zapísať aj v jednom. V našom slovníku máme šesť hodnôt: '114','siska',
'troba', 'prak', 'saxofon','cumlik'. Každá hodnota patrí nejakému klúču ('Jan Novak','homer', 'marge', 'bart','lisa' a 'maggie'). Hodnoty priradíme ku klúču pomocou dvojbodky (:) a oddelujeme ich čiarkou, ktorá sa vetšinou píše aj za poslednú položku.

**Poznámka:** Kľúče slovníka musia byť nemenné, ako sú napr. n-tice (tuple), reťazce, celé čísla atď. Ako kľúče nemôžeme použiť meniteľné objekty, ako sú napr. zoznamy a pod. V kľúčoch slovníka sa rozlišujú malé a veľké písmená, s rovnakým názvom, ale s rôznymi prípadmi kľúča sa bude zaobchádzať odlišne. 
Pre prácu so slovníkom platí to isté, čo sme si ukazovali pri zozname:

~~~
oblubeneVeci= {
    'Jan Novak':'114',
    'homer': 'siska',
    'marge': 'truba',
    'bart': 'prak',
    'lisa': 'saxofon',
    'maggie': 'cumlik'
}
print("Homer má rád " + oblubeneVeci['Jan Novak'])
~~~
Namiesto zápisu oblubeneVeci[0] sme použili klúč typu string. Veľkou výhodou použitia slovníku je lepšia čiteľnosť, kedy priamo vidíme, akú hodnotu ze slovníka dostávame. Zatiaľ čo u číselných indexov možno ani nevieme, o akú hodnotu ide. Každý klúč musí byť unikátný, ale hodnoty za nim také už nemusia byť t.j. môžu sa v kolekcii opakovať. Páry klúč:hodnota môžu byť akékoľvek nemenné datové typy. Ak definujeme rovnaký klúč v tom istom slovníku viac krát a s rôznymi hodnotami, bude klúču priradený posledná hodnota.

># Operácie nad slovníkom

# Vytvorenie slovníka
Na vytváranie slovníkov môžeme použiť aj funkciu Pythonu dict(). Patrí k vstavaným funkciám ktorých zoznam najdeme [tu](https://www.w3schools.com/python/python_ref_functions.asp).
~~~
# Vytvoríme slovník obsahujúci osobné informácie

x = dict(name = "Ján", age = 36, country = "Slovakia")

~~~
Zložitosti pri vytváraní slovníka:
Časová zložitosť: O(len(diktát))

Zložitosť priestoru: O(n)

![Vnorený slovník](.\Tahaky_Dokumenty_Obrazky/vnoreny_slovnik.png)
~~~
# Creating a Nested Dictionary

# as shown in the below image

Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)
~~~

# Pridávanie položiek
Do slovníku môžeme jednoducho pridať ďalšie položky priradením nových kĹúčov: 
~~~
oblubeneVeci= {
    'homer': 'sisky',
    'marge': 'truba',
    'bart': 'prak',
    'lisa': 'saxofon'
}

oblubeneVeci['maggie'] = 'dudlik'
print("Homer má rád " + oblubeneVeci['homer'])
print("Maggie má ráda "+oblubeneVeci['maggie'])
~~~
Na pridanie položiek do slovníka môžeme však použiť aj metódu update() .Rovnakým spôsobom môžeme modifikovať už uložené hodnoty.

# Zisťovanie počtu položiek
Pre zistenie počtu položiek v dictionary opäť použijem globálnu (lebo je všeobecne použitelná) funkciu len() ktorú poznáme už aj zo zoznamov a množín.
~~~
oblubeneVeci= {
    'homer': 'sisky',
    'marge': 'truba',
    'bart': 'prak',
    'lisa': 'saxofon'
}
print('Počet položek: %d' % (len(oblubeneVeci)))
~~~

# Prístup k položkám slovníka
K hodnote položky v slovníku môžeme pristupovať umiestnením kľúča do hranatých zátvoriek alebo použitím metódy get() ktorej sa venujeme v ďalšej kapitole.
~~~
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}
print(country_capitals["United States"])  # Washington D.C.

print(country_capitals["England"]) # London
~~~
> ### Prístup k prvku vnoreného slovníka
Ak chcete získať prístup k hodnote ľubovoľného kľúča vo vnorenom slovníku, použite syntax indexovania [].
~~~
# Creating a Dictionary

Dict = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'For'}}

# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
~~~

# Zmena hodnoty prvku
Keďže slovníky Pythonu sú meniteľné, hodnotu prvku slovníka môžeme zmeniť odkazom na jeho kľúč. Napríklad takto:
~~~
country_capitals = {
  "United States": "New York", 
  "Italy": "Naples", 
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)
~~~
# Odstránenie položky zo zoznamu
Na odstránenie položky zo slovníka používame príkaz del. Napríklad:
~~~
country_capitals = {
  "United States": "New York", 
  "Italy": "Naples" 
}

# delete item having "United States" key
del country_capitals["United States"]

print(country_capitals)
~~~
Na odstránenie položky zo slovníka môžeme obdobne použiť aj metódu pop(), ale ak potrebujeme odstrániť všetky položky zo slovníka naraz, môžeme použiť metódu clear().

# Zistenie existencie určitého klúča v slovníku
Pomocou operátora **in** sa spýtame či slovník obsahuje daný kľúč. Nekontroluje sa ale či existuje alebo neexistuje nejaká hodnota.
~~~
oblubeneVeci= {
    'homer': 'sisky',
    'marge': 'truba',
    'bart': 'prak',
    'lisa': 'saxofon'
}
simpson = input("Ahoj, zadaj svojeho oblúbeného Simpsona (z rodiny Simpsonov): ")
if simpson in oblubeneVeci:
    print("%s má rád %s." % (simpson.lower(), oblubeneVeci[simpson]))
else:
    print("Ale, toto nie je Simpson!")
~~~
# Iterácia cez slovník
 Slovník je usporiadaná kolekcia položiek čo znamená to, že **slovník zachováva poradie svojich položiek**.

Môžeme iterovať cez slovníkové klávesy jeden po druhom pomocou cyklu [for](https://www.programiz.com/python-programming/for-loop) .
~~~
country_capitals = {
  "United States": "New York", 
  "Italy": "Naples" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:

    capital = country_capitals[country] # zapis hodnoty do premennej

    print(capital)
~~~

Pokračovanie 1

