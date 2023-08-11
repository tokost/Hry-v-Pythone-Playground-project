| Metóda    | Popis                                                                    |
|-----------|---------------------------------------------------------------------------|
|dic.clear()| Odstráňte všetky prvky zo slovníka
|dict.copy()| Vráti kópiu slovníka
| dict.get(kľúč, predvolené = “Žiadne”) |  Vráti hodnotu zadaného kľúča
|dict.items()|  Vráti zoznam obsahujúci n-ticu pre každý pár kľúč-hodnota
| dic.keys | Vráti zoznam obsahujúci kľúče slovníka
|dict.update(dikt2)| Aktualizuje slovník zadanými pármi kľúč – hodnota
| dict.values() | 	 Vráti zoznam všetkých hodnôt slovníka
|pop()| Odstráňte prvok špecifikovaným kľúčom
|popItem()|Odstráni posledný vložený pár kľúč – hodnota
|  dict.setdefault(key,default= “Žiadne”) | 	 nastavte kľúč na predvolenú hodnotu, ak kľúč nie je špecifikovaný v slovníku
|dict.has_key(kľúč)| vráti hodnotu true, ak slovník obsahuje zadaný kľúč.
|dict.get(kľúč, predvolené = “Žiadne”)|používa sa na získanie hodnoty zadanej pre odovzdaný kľúč.

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