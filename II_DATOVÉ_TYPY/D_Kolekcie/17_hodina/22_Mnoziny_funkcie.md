
Pokračovanie č. I

Funkcia set() sa tiež používa na konverziu objektu typu reťazec, n-tica alebo slovník na objekt množiny, ako je znázornené nižšie.
~~~
s = set('Hello') # converts string to set
print(s)
{'l', 'H', 'o', 'e'}

s = set((1,2,3,4,5)) # converts tuple to set
print(s)
{1, 2, 3, 4, 5}

d = {1:'One', 2: 'Two'} 
s = set(d)   # converts dict to set
print(s) 
{1, 2}
~~~

>### Použitie metódy pop()
Na odstraňovanie prvkov z množiny, tak ako tomu bolo pri zoznamoch aj tu možno použiť funkciu či metódu pop().
~~~
>>> a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
>>> a_set.pop()                                ①
1
>>> a_set.pop()
3
>>> a_set.pop()
36
>>> a_set
{6, 10, 45, 15, 21, 28}
>>> a_set.clear()                              ②
>>> a_set
set()
>>> a_set.pop()                                ③
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
~~~
①	Metoda pop() odstraní jeden prvek z množiny a vrátí jeho hodnotu. Ale množiny jsou neuspořádané a neexistuje u nich nic takového jako „poslední“ hodnota. Proto také neexistuje možnost ovlivnit, která hodnota bude odstraněna. Je to zcela náhodné.\
②	Metoda clear() odstraní všechny prvky množiny a množina se stane prázdnou. Ve výsledku je to stejné jako provedení příkazu a_set = set(), který vytvoří novou prázdnou množinu a přepíše původní hodnotu proměnné a_set.\
③	Pokus o volání metody pop() pro prázdnou množinu vede k vyvolání výjimky KeyError.

# Ďalšie funkcie nad množinami (set-mi)

>## Bežné množinové funkcie (metódy)
Pythonovský datový typ set podporuje niekoľko bežných množinových funkcii (metód) či operácií.

~~~
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
30 in a_set                        ①        
True

31 in a_set
False

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.union(b_set)                 ②

{1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}

a_set.intersection(b_set)          ③
{9, 2, 12, 5, 21}

a_set.difference(b_set)            ④
{195, 4, 76, 51, 30, 127}

a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.symmetric_difference(b_set)  ⑤
{1, 3, 4, 6, 8, 76, 15, 17, 18, 195, 127, 30, 51}
~~~
①	Ak chceme otestovať, či je daná hodnota prvkom množiny, použijeme operátor **in**. Funguje rovnakým spôsobom ako u je to u zoznamov.\
②	Metóda union() (zjednotenie) vracia novú množinu, ktorá obsahuje všetky prvky ako z jednej, tak aj z druhej množiny.\
③	Metoda intersection() (prienik) vracia novú množinu, ktorá obsahuje všetky prvky ktoré sa nachádzajú se v oboch množinách súčasne.\
④	Metoda difference() (rozdíl) vrací novou množinu obsahující všechny prvky, které se nacházejí v množině a_set, ale nenacházejí se v množině b_set.\
⑤	Metoda symmetric_difference() (symetrický rozdiel) vracia novú množinu obsahujúcu všetky prvky, ktoré se nachádzajú práve v jednej z množín.\

Tri z týchto funkcii (metód) sú tzv. symetrické čo znamená súmernosť z hladiska. V náväznosti na predchádzajúci príklad sú to tieto funkcie:
~~~
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set.symmetric_difference(a_set)  ①
{3, 1, 195, 4, 6, 8, 76, 15, 17, 18, 51, 30, 127}

b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set)  ②
True


b_set.union(a_set) == a_set.union(b_set)  ③
True

b_set.intersection(a_set) == a_set.intersection(b_set)  ④
True

b_set.difference(a_set) == a_set.difference(b_set)  ⑤
False
~~~
①	Symetrický rozdiel množín a_set od b_set vypadá inak ako symetrický rozdiel množín b_set od a_set. Ale pamätujme na to, že množiny sú neusporiadané. Akékoľvek dve množiny, ktorých všetky hodnoty sa zhodujú (žiadna nesmie byť vynechaná), sa považujú za zhodné.\
②	A presně tento prípad nastal tu. Nenechajme sa zmiať reprezentáciami týchto množín ktoré zobrazené v pythonovskom shelle. Obsahujú rovnaké hodnoty, takže sú zhodné.\
③	Zjednocenie dvoch množín je tiež symetrické.\
④	Prienik dvoch množín je taktiež symetrický.\
⑤	Rozdiel dvoch množín symetrický neni. Ono to dáva zmysel. Podobá sa to na odčítanie jedného čísla od druhého. Na poradí operandov tu ale záleží !

A nakoniec tu máme niekoľk funkcii ktoré vyhodnocujú zadané otázky vztiahnuté na množiny. 
~~~
a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
a_set.issubset(b_set)    ①
True

b_set.issuperset(a_set)  ②
True

a_set.add(5)             ③
a_set.issubset(b_set)
False

b_set.issuperset(a_set)
False
~~~
①	Množina a_set je podmnožinou množiny b_set — všechny prvky množiny a_set jsou současně prvky množiny b_set.\
②	Stejnou otázku můžeme položit obráceně. Množina b_set je nadmnožinou množiny a_set, protože všechny prvky množiny a_set jsou současně prvky množiny b_set.\
③	Jakmile do množiny a_set přidáme hodnotu, která se v množině b_set nenachází, oba testy vrátí hodnotu False.

>## Množiny v booleovském kontextu

Množiny můžeme použít v booleovském kontextu, například v příkazu if.
~~~
>>> def is_it_true(anything):
...   if anything:
...     print("yes, it's true")
...   else:
...     print("no, it's false")
...
>>> is_it_true(set())          ①
no, it's false
>>> is_it_true({'a'})          ②
yes, it's true
>>> is_it_true({False})        ③
yes, it's true
~~~
①	Prázdná množina se v booleovském kontextu vyhodnocuje jako false.
②	Ľubovolná množina s alespoň jedním prvkem se vyhodnocuje jako true.
③	Ľubovolná množina s alespoň jedním prvkem se vyhodnocuje jako true. Hodnota prvků je nepodstatná.

Nasledujúca tabuľka uvádza vstavané metódy funkcie nad množinou (set) s odkazom na príklady:

| Metóda    | Popis                                                                     |
|-----------|---------------------------------------------------------------------------|
| [set.add()](https://www.tutorialsteacher.com/python/set-add) | Pridá prvok do set-u. Ak prvok už v množine existuje, nepridá tento prvok.
|[set.clear()](https://www.tutorialsteacher.com/python/set-clear)| Odstráni všetky prvky zo set-u.
|[set.copy()](https://www.tutorialsteacher.com/python/set-copy)|Vráti plytkú kópiu set-u t.j. skopírujú sa iba atribúty objektov. [Hlboká kópia predstavuje úplnú kópiu objektu.](https://sk.wiki-base.com/7779662-python-shallow-copy-and-deep-copy)
|[set.difference()](https://www.tutorialsteacher.com/python/set-difference)|Vráti novú množinu s jedinečnými prvkami, ktoré nie sú v inej množine odovzdanej ako parameter.
|[set.difference_update()](https://www.tutorialsteacher.com/python/set-difference-update)|Aktualizuje množinu, v ktorej sa metóda volá, prvkami, ktoré sú spoločné v inej množine odovzdané ako argument.
|[set.discard()](https://www.tutorialsteacher.com/python/set-discard)| Odstráni konkrétny prvok zo sady.
|[set.intersection()](https://www.tutorialsteacher.com/python/set-intersection)|Vráti novú množinu s prvkami, ktoré sú v daných množinách spoločné.
|[set.intersection_update()](https://www.tutorialsteacher.com/python/set-intersection-update) | Aktualizuje množinu, na ktorej sa volá metóda instersection_update(), o spoločné prvky medzi špecifikovanými množinami.
|[set.isdisjoint()](https://www.tutorialsteacher.com/python/set-isdisjoint)|Vráti hodnotu true, ak dané množiny nemajú žiadne spoločné prvky. Množiny sú disjunktné vtedy a len vtedy, ak je ich priesečník prázdna množina.
|[set.issubset()](https://www.tutorialsteacher.com/python/set-issubset)|Vráti hodnotu true, ak množina (na ktorej sa volá issubset()) obsahuje každý prvok druhej množiny odovzdaný ako argument.
|[set.pop()](https://www.tutorialsteacher.com/python/set-pop)|Odstráni a vráti náhodný prvok zo sady.
|[set.remove()](https://www.tutorialsteacher.com/python/set-remove) | Odstráni zadaný prvok zo sady. Ak sa zadaný prvok nenašiel, vyhláste chybu.
|[set.symmetric_difference()](https://www.tutorialsteacher.com/python/set-symmetric-difference)| Vráti novú množinu s odlišnými prvkami nachádzajúcimi sa v oboch množinách. 
|[set.symmetric_difference_update()](https://www.tutorialsteacher.com/python/set-symmetric-difference-update) |Aktualizuje množinu, na ktorú sa volala metóda instersection_update(), o prvky, ktoré sú spoločné medzi špecifikovanými sadami.
|[set.union()](https://www.tutorialsteacher.com/python/set-union)| Vráti novú množinu s odlišnými prvkami zo všetkých daných množín.
|[set.update()](https://www.tutorialsteacher.com/python/set-update)|Aktualizuje množinu pridaním odlišných prvkov z odovzdanej jednej alebo viacerých iterovateľných položiek.

>### Operácie vs. vstavané funkcie
Ako už bolo spomenuté, dátový typ množiny v Pythone sa implementuje ako množina definovaná v matematike. Preto je aj tu možné vykonávať rôzne známe operácie. Operátory |, &, - a ^ vykonávajú operácie zjednotenia, prieniku, rozdielu a symetrického rozdielu. Každý z týchto operátorov má zodpovedajúcu metódu spojenú so vstavanou triedou množín.
	
| Operácie nad set-mi                                                                                                                                                | Príklady                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Zjednotenie** : Vráti novú množinu s prvkami z oboch množín.<br><br>**Operátor** :<br>**Metóda** : [set.union()](https://www-tutorialsteacher-com.translate.goog/python/set-union?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                                     | s1={1,2,3,4,5}<br>s2={4,5,6,7,8}<br>s1 s2 #{1, 2, 3, 4, 5, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}<br>s2={4,5,6,7,8}<br>s1.union(s2) #{1, 2, 3, 4, 5, 6, 7, 8}<br>s2.union(s1) #{1, 2, 3, 4, 5, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                                                                              |
| **Prienik** : Vráti novú množinu obsahujúcu prvky spoločné pre obe množiny.<br><br>**Operátor**: &<br>**Metóda**: [set.intersection()](https://www-tutorialsteacher-com.translate.goog/python/set-intersection?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                       | s1={1,2,3,4,5} <br>s2={4,5,6,7,8} <br>s1&s2 #{4, 5}                       <br>s2&s1 #{4, 5}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}           <br>s2={4,5,6,7,8}           <br>s1.intersection(s2) #{4, 5}                                <br>s2.intersection(s1) #{4, 5}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                      |
| **Rozdiel**: Vráti množinu obsahujúcu prvky iba v prvej množine, ale nie v druhej množine.<br><br>**Operátor** : -<br>**Metóda**: [set.difference()](https://www-tutorialsteacher-com.translate.goog/python/set-difference?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                             | s1={1,2,3,4,5} <br>s2={4,5,6,7,8} <br>s1-s2 #{1, 2, 3}                    <br>s2-s1 #{8, 6, 7}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}      <br>s2={4,5,6,7,8}      <br>s1.rozdiel(s2) #{1, 2, 3}                        <br>s2.rozdiel(s1) #{8, 6, 7}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                                         |
| **Symetrický rozdiel**: Vráti množinu pozostávajúcu z prvkov v oboch množinách, s výnimkou spoločných prvkov.<br><br>**Operátor**: ^<br>Metóda: [set.symmetric_difference()](https://www-tutorialsteacher-com.translate.goog/python/set-symmetric-difference?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) | s1={1,2,3,4,5} <br>s2={4,5,6,7,8} <br>s1^s2 #{1, 2, 3, 6, 7, 8}           <br>s2^s1 #{1, 2, 3, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}               <br>s2={4,5,6,7,8}               <br>s1.symmetric_difference(s2) #{1, 2, 3, 6, 7, 8}                        <br>s2.symmetric_difference( s1) #{1, 2, 3, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) |
	
	