Napíš funkciu posun(zoznam), ktorá posunie prvky v danom zozname tak, že prvý sa presťahuje na koniec. Funkcia nič nevracia, len zmení obsah pôvodného zoznamu. Napríklad:

a = [2, 3, '5', 7, 11]
posun(a)
a
    [3, '5', 7, 11, 2]
zoz = 'kto druhemu jamu kope'.split()
for i in range(5):
        print(zoz)
        posun(zoz)
    ['kto', 'druhemu', 'jamu', 'kope']
    ['druhemu', 'jamu', 'kope', 'kto']
    ['jamu', 'kope', 'kto', 'druhemu']
    ['kope', 'kto', 'druhemu', 'jamu']
    ['kto', 'druhemu', 'jamu', 'kope']

Napíš funkciu vyhod_none(ntica), ktorá z danej n-tice vyhodí všetky výskyty None. Funkcia vráti (return) túto novú n-ticu (nič nevypisuje). Napríklad:

ntica = vyhod_none((None, 1, None, None))
ntica
    (1,)

Napíš funkciu dve_kocky(pocet), ktorá vráti 13-prvkový zoznam celých čísel. Tento sa skonštruuje takto: zadaný pocet-krát hodí dvoma kockami (dve nádodné čísla od 1 do 6), pre každý takýto hod urobí ich súčet a v 13-prvkovom zozname si eviduje počet výskytov každého súčtu, napríklad zoznam[5] bude označovať, koľko krát pri našej simulácii padol súčet 5; zrejme na začiatku budú v zozname samé 0 a potom pri každom hode sa číslo na príslušnom indexe zvýši o 1. Funkcia nič nevypisuje, len vráti vytvorený 13-prvkový zoznam celých čísel. Mohol by si dostať napríklad, takýto zoznam:

dve_kocky(1000)
    [0, 0, 29, 36, 90, 105, 137, 181, 125, 126, 93, 50, 28]

Napíš funkciu osmickova(cislo), ktorá vráti (return) zoznam cifier daného čísla v osmičkovej sústave. Využi funkcie oct a int. Napríklad:

osmickova(11213)
    [2, 5, 7, 1, 5]

Napíš funkciu dvojkova(cislo), ktorá vráti (return) zoznam cifier daného čísla v dvojkovej sústave. Využi f'{cislo:b}'. Napríklad:

dvojkova(11213)
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1]

Napíš funkciu z_dvojkovej(zoznam), ktorá dostane zoznam cifier dvojkového zápisu čísla v tvare z predchádzajúcej úlohy. Funkcia vráti celé číslo (return), ktorého cifry v dvojkovej sústave zodpovedajú zadanému zoznamu. Napríklad:

z_dvojkovej([1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1])
    11213
z = [1] + [0] * 20
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
z_dvojkovej(z)
    1048576
2 ** 20
    1048576
Využi funkciu int(reťazec, 2), pomocou ktorej sa zo znakového reťazca s dvojkovým zápisom čísla vyrobí celé číslo.


Napíš funkciu nahodne_body(pocet), ktorá vráti zadaný počet náhodných bodov v grafickej ploche (dvojíc čísel z 380x260). Funkcia vráti zoznam, ktorý bude obsahovať dvojprvkové n-tice celých čísel. Napríklad:

nahodne_body(5)
    [(118, 103), (299, 27), (247, 118), (166, 237), (269, 225)]

Ak by si celú postupnosť 100 náhodných bodov z predchádzajúcej úlohy vykreslil pomocou jediného create_line, dostal by si nejakú čmáranicu (vyskúšaj). Ďalej otestuj, ako sa vykreslí táto postupnosť, keď sa najprv usporiada pomocou funkcie sorted. Napríklad, náhodná postupnosť 100 bodov:

../_images/09_c01.png
a po usporiadaní pomocou sorted:

../_images/09_c02.png

Napíš funkciu sort_y(zoznam), kde zoznam obsahuje dvojice (typ tuple) celých čísel. Tieto reprezentujú súradnice (x, y) nejakých bodov v rovine. Tento zoznam treba usporiadať od najmenšieho po najväčší, lenže podľa druhých prvkov dvojíc (y-ových súradníc). Uvedom si, že volanie zoznam.sort() by usporiadalo zoznam podľa prvých prvkov dvojíc (x-ových súradníc). Napríklad:

xy = [(100, 30), (200, 10), (300, 20)]
sort_y(xy)
xy
    [(200, 10), (300, 20), (100, 30)]
Triediť môžeš takto: najprv v zozname v každej dvojici vymeníš x a y, potom normálne utriediš (napríklad pomocou metódy sort) a nakoniec v takto utriedenom zozname vrátiš všetky dvojice do pôvodného stavu (vymeníš x a y).

Podobne ako v predchádzajúcej úlohe vykresli takto usporiadanú postupnosť vrcholov pomocou create_line:

../_images/09_c03.png

Napíš funkciu prerob(cislo), ktorá z daného celého čísla vyrobí reťazec, ale tak, že cifry zoskupí do trojíc (sprava) a oddelí podčiarkovníkom. Využi funkciu join, preto z čísla najprv vyrob zoznam trojznakových reťazcov. Funkcia nič nevypisuje, ale vráti (return) výsledný reťazec. Napríklad:

prerob(12345678)
    '12_345_678'
Je zaujímavé, že Python aj takto zadané celé čísla považuje za korektné, napríklad:

12_345_678
    12345678
Výsledok svojej funkcie prerob môžeš skontrolovať pomocou f'{cislo:_}'.


Napíš funkciu sipka(xy1, xy2), ktorá do grafickej plochy nakreslí šípku z bodu xy1 do bodu xy2. Oba tieto parametre sú dvojice čísel (tuple), t.j. súradnice bodov. Šípku kresli pomocou create_line, v ktorej využiješ ďalší pomenovaný parameter arrow='last' (podobné šípky sme kreslili v 15. úlohe z 5.cvičenia). Teraz nakresli štyri šípky, ktoré nakreslia obrys takéhoto štvorca:

import tkinter

def sipka(xy1, xy2):
    ...

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(150, 50, 250, 150, fill='gold')
sipka(...)
sipka(...)
sipka(...)
sipka(...)

tkinter.mainloop()
Mal by si dostať takýto obrázok:

../_images/09_c04.png

Napíš funkciu vektor(xy, dlzka, uhol), ktorá nakreslí vektor (teda šípku) z bodu xy (dvojprvkový tuple celých čísel) s danou dĺžkou a s daným uhlom (v stupňoch). Uvedom si, že koncové body takéhoto vektora ležia na kružnici s polomerom dlzka a stredom xy. Na kreslenie šípky využi volanie funkcie sipka z predchádzajúcej úlohy. Funkcia vektor vráti (return) súradnicu koncového bodu vektora ako dvojicu (tuple) celých čísel. Napríklad:

import tkinter
from math import sin, cos, radians

def sipka(xy1, xy2):
    ...

def vektor(xy, dlzka, uhol):
    ...
    return ...

canvas = tkinter.Canvas()
canvas.pack()

poz = (200, 120)
for uhol in range(0, 720, 144):
    poz = vektor(poz, 100, uhol)

tkinter.mainloop()
nakreslí:

../_images/09_c05.png

Napíš funkciu ntica_cisel(retazec), ktorá z daného reťazca vyrobí n-ticu celých čísel - použi metódu split. Napríklad:

a = ntica_cisel('12 345 6 -78 9000')
a
    (12, 345, 6, -78, 9000)

Napíš funkciu retazec(ntica), ktorá z ntice čísel vyrobí reťazec - použi metódu join. Napríklad:

retazec((12, 3.45, 6, -78, 9000))
    '12 3.45 6 -78 9000'

Napíš funkciu zadaj(pocet), ktorá vráti prečítanú n-ticu čísel zo vstupu (input). Funkcia si vypýta od používateľa, aby zadal príslušný počet čísel (napríklad input(f'zadaj {pocet} čísla: ')) a ak ich používateľ nezadá požadovaný počet, bude si tento input pýtať znovu a znovu. Funkcia vráti (return) n-ticu celých čísel a nie n-ticu reťazcov. Napríklad:

tri = zadaj(3)
    zadaj 3 čísla: 12 3
    zadaj 3 čísla: 12 3 456
tri
    (12, 3, 456)

Napíš funkciu zisti(slovo1, slovo2), ktorá zistí (vráti True alebo False), či sú dve zadané slová zložené presne z tých istých písmen - možno v inom poradí. Napríklad:

zisti('Skola', 'Lasko')
    True
zisti('poobede', 'bopeodo')
    False
Pomôcka: použi funkciu sorted


Napíš funkciu vsetky_rozne(zoznam), ktorá zistí (vráti True alebo False), či sú všetky prvky zoznamu rôzne. Najprv si vyrob utriedený pomocný zoznam (nepokaz pôvodný) a v ňom zisťuj, či sa nenachádzajú dve rovnaké hodnoty za sebou. Napríklad:

vsetky_rozne([3, 8, 7, 9, 4, 1, 6, 10, 5, 2])
    True
zoz = [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]
vsetky_rozne(zoz)
    False
zoz
    [3, 8, 7, 9, 4, 1, 6, 3, 10, 5, 2]

Napíš funkciu enum(postupnost), ktorá vráti (return) n-ticu dvojíc. V tejto n-tici je prvý prvok poradové číslo (od 0 do počet prvkov postupnosti minus 1) a druhým je prvok z danej postupnosti. Malo by to dať rovnaký výsledok ako tuple(enumerate(postupnost)) ale bez použitia enumerate. Napríklad:

enum([12, 'dva', 3.14])
    ((0, 12), (1, 'dva'), (2, 3.14))

Python ponúka ešte jednu štandardnú funkciu zip. Táto funkcia, keď dostane nejaké dve postupnosti (napríklad zoznam, n-ticu, reťazec, range, …), vytvorí z nich jednu novú postupnosť dvojíc (tuple): v každej takejto dvojici je jeden prvok z prvej a jeden z druhej postupnosti. Môžeš vyskúšať, napríklad:

list(zip('python', [2, 3, 5, 7]))
    [('p', 2), ('y', 3), ('t', 5), ('h', 7)]
Zrejme, ak je jedna z týchto postupností kratšia, výsledok sa nastaví podľa nej. Napíš funkciu moj_zip(post1, post2), ktorá z dvoch postupností (iterovateľných objektov možno rôznej dĺžky) vytvorí jeden zoznam dvojíc. Nepouži štandardnú funkciu zip().


Prepíš funkciu enum z (18) úlohy tak, aby neobsahovala cyklus a využila tvoju funkciu moj_zip. Teda:

def enum(postupnost):
    return ... moj_zip ...

Napíš funkciu od_zip(zoznam), ktorá bude fungovať ako opak funkcie moj_zip. Funkcia dostáva zoznam dvojíc a vráti dva zoznamy prvých a druhých prvkov dvojíc. Napríklad:

z1, z2 = od_zip([(2, 'a'), ('h', 3), (5, 'o'), ('j', 7)])
z1
    [2, 'h', 5, 'j']
z2
    ['a', 3, 'o', 7]

Napíš funkciu do_dvojic(zoznam), ktorá daný zoznam (alebo n-ticu) párnej dĺžky „rozseká“ na zoznam dvojíc (list s prvkami tuple), dvojice postupne budú (prvý, druhý), (tretí, štvrtý), … Napríklad:

x = do_dvojic(('11', 22, '3', 4))
    [('11', 22), ('3', 4)]
Rieš najprv bez použitia funkcie moj_zip() z predchádzajúcich úloh (teda pomocou for-cyklu) a potom pomocou tejto funkcie (bez cyklu).


Napíš funkciu pomiesaj(zoznam), ktorá náhodne pomieša poradie prvkov v pôvodnom zozname. Funkcia nič nevypisuje ani nevracia, len zmení obsah zoznamu. Funkcia by pre n-prvkový zoznam mala pracovať takto:

najprv zvolí náhodné číslo x od 0 do n-1

v zozname vymení x-tý a posledný prvok

potom zvolí náhodné číslo x od 0 do n-2

v zozname vymení x-tý a predposledný prvok (t.j. zoznam[-2])

potom zvolí náhodné číslo x od 0 do n-3

v zozname vymení x-tý a a tretí od konca

takto to opakuje, kým sa dá

Napríklad:

for i in range(4):
    p = list(range(1, 11))
    pomiesaj(p)
    print(p)
[2, 9, 6, 1, 7, 8, 10, 3, 5, 4]
[7, 2, 10, 9, 6, 8, 4, 1, 3, 5]
[3, 8, 7, 9, 4, 1, 6, 10, 5, 2]
[2, 9, 4, 1, 8, 3, 5, 7, 6, 10]