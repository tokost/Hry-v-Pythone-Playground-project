Cvičenie
20.4.1. Zbalené a rozbalené parametre
Napíšte funkciu ntica, ktorá bude mať ľubovoľný počet parametrov a vráti n-ticu z týchto parametrov

napr.
>>> ntica(5, 'x', 7)
(5, 'x', 7)
>>> p = ntica(123, ntica(37))
>>> p
(123, (37,))
Napíšte funkciu min s ľubovoľným počtom parametrov, ktorá vráti najmenšiu hodnotu medzi parametrami.

napr.
>>> min(5, 3.14, 7)
3.14
Napíšte funkciu zisti s ľubovoľným počtom parametrov, ktorá zistí (vráti True), či aspoň jeden z parametrov je n-tica (typ tuple).

napr.
>>> zisti(1, 2, 3)
False
>>> t = zisti(())
>>> t
True
Napíšte funkciu zlep s ľubovoľným počtom parametrov, pričom všetky sú typu list. Výsledkom funkcie je zreťazenie všetkých týchto parametrov.

napr.
>>> zlep(['a', 1], [], [('b', 2)])
['a', 1, ('b', 2)]
>>> zlep()
[]
Napíšte funkciu vypis(pole), ktorá pomocou print vypíše všetky prvky poľa do jedného riadka. Nepoužite for-cyklus.

napr.
>>>vypis([123, 'ahoj', (50, 120), 3.14])
123 ahoj (50, 120) 3.14
20.4.2. Funkcie ako parametre
Napíšte funkciu retazec(pole). Funkcia vráti znakový reťazec, ktorý reprezentuje prvky poľa. Prvky poľa budú v reťazci oddelené znakom bodkočiarka. Nepoužite žiadne cykly, ale namiesto toho štandardnú funkciu map a metódu join.

napr.
>>> r = retazec([123, 'ahoj', (50, 120), 3.14])
>>> r
"123; 'ahoj'; (50, 120); 3.14"
Napíšte funkciu aplikuj, ktorej parametrami sú nejaké funkcie, okrem posledného parametra, ktorým je nejaká hodnota. Funkcia postupne zavolá tieto funkcie s danou hodnotou, pričom každú ďalšiu funkciu aplikuje na predchádzajúci výsledok. Napr. aplikuj(f1, f2, f3, x) vypočíta f3(f2(f1(x))).

napr.
>>> def rev(x): return x[::-1]
>>> aplikuj(str, rev, int, 1074)
4701
Napíšte funkciu urob(k). Funkcia ako svoj výsledok vráti funkciu s jedným parametrom, ktorá bude počítať k-tu mocninu parametra.

napr.
>>> g = urob(3)   # g je funkcia, ktora pocita 3 mocninu
>>> g(4)
64
>>> urob(3)(4)    # tu sa pocita to iste
64
>>> f = urob(7)
>>> print(f(2), f(3), f(4))
127 2187 16384
20.4.3. Generátorová notácia
Napíšte funkciu mocniny(n), ktorá vráti pole druhých mocnín čísel od 1 do n.

napr.
>>> mocniny(4)
[1, 4, 9, 16]
Napíšte funkciu zistí(veta), ktorá zistí dĺžku najdlhšieho slova vo vete.

napr.
>>> zisti('isiel macek do malacek')
7
Napíšte funkciu prevrat_slova(veta), ktorá vráti zadanú vetu tak, že každé slovo v nej bude otočené.
napr.
>>> prevrat_slova('isiel macek do malacek')
'leisi kecam od kecalam'
pokúste sa celú funkciu zapísať len do jedného riadka
Napíšte funkciu najdlhsie_slovo(veta), ktorá vráti najdlhšie slovo vo vete. Riešte to takto:
funkcia najprv z danej vety vytvorí postupnosť dvojíc (dĺžka slova, slovo)
pomocou sorted() túto postupnosť dvojíc utriedi
funkcia vráti slovo z poslednej dvojice (je to najdlhšie slovo) utriedenej postupnosti
napr.
>>> najdlhsie_slovo('isiel macek do malacek')
'malacek'
pokúste sa celú funkciu zapísať do jedného riadka (return ...)
Napíšte funkciu pole2(m, n, hodnota=None), ktorá vygeneruje dvojrozmerné pole veľkosti m x n pričom všetky prvky majú zadanú hodnotu
napr.
>>> pole2(3, 2, 1)
[[1, 1], [1, 1], [1, 1]]
Predpokladáme, že textový súbor v každom riadku obsahuje niekoľko celých čísel. Napíšte funkciu citaj_pole(meno_suboru), ktorá z neho vytvorí dvojrozmerné pole čísel.
napr. pre súbor
1 2
3 4 5 6

7 8 9
vytvorí
>>> citaj_pole('subor.txt')
[[1, 2], [3, 4, 5, 6], [], [7, 8, 9]]
Napíšte funkciu rozdel(pole, x), ktorá ako výsledok vráti dve polia: prvé obsahuje všetky menšie prvky ako x a druhé všetky zvyšné.
napr.
>>> p1, p2 = rozdel([6, 8, 4, 7, 11, 9], 7)
>>> p1
[6, 4]
>>> p2
[8, 7, 11, 9]
Napíšte funkciu enumerate(postupnost), ktorá vytvorí takúto postupnosť dvojíc (typu list): prvým prvkom bude poradové číslo dvojice a druhým prvkom prvok zo vstupnej postupnosti.
napr.
>>> enumerate('python')
[(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
v Pythone existuje štandardná funkcia enumerate(), ktorá funguje skoro presne ako táto funkcia, len jej výsledkom nie je pole, ale opäť postupnosť
Napíšte funkciu zip(p1, p2), ktorá z dvoch postupností rovnakých dĺžok vytvorí pole zodpovedajúcich dvojíc, t.j. pole v ktorom prvým prvkom bude dvojica prvých prvkov postupností, druhým prvkom dvojica druhých prvkov, …
napr.
>>> zip('python', [2, 3, 5, 7, 11, 13])]
[('p', 2), ('y', 3), ('t', 5), ('h', 7), ('o', 11), ('n', 13)]
pokúste sa to zapísať tak, aby to fungovala aj pre postupnosti rôznych dĺžok: vtedy vytvorí len toľko dvojíc, koľko je prvkov v kratšej postupnosti, napr.
>>> zip('python', [2, 3, 5, 7, 11])]
[('p', 2), ('y', 3), ('t', 5), ('h', 7), ('o', 11)]
pokúste sa to zapísať tak, aby funkcia fungovala pre ľubovoľný počet ľubovoľne dlhých postupností, napr.
>>> zip('python', [2, 3, 5, 7, 11], 'abcd')]
[('p', 2, 'a'), ('y', 3, 'b'), ('t', 5, 'c'), ('h', 7, 'd')]
v Pythone existuje štandardná funkcia zip(), ktorá funguje skoro presne ako táto posledná verzia funkcie, len jej výsledkom nie je pole, ale opäť postupnosť
Logo

[Príklad č.1](https://www-geeksforgeeks-org.translate.goog/time-difference-between-expected-time-and-given-time/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) použitia časových funkcii. úlohou je vypočítať rozdiel medzi očakávaným časom a daným časom.

[Príklad č.2](https://www-geeksforgeeks-org.translate.goog/date-after-adding-given-number-of-days-to-the-given-date/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) úlohou je zistiť dátum po pripočítaní daného počtu dní k danému dátumu

[Príklad č.3](https://www-geeksforgeeks-org.translate.goog/python-time-monotonic-method/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) príklad monotónných hodín t.j. hodín ktoré nemôžu ísť dozadu