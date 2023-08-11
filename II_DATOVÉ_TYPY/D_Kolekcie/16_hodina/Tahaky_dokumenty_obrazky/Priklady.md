Množiny (set) - vytváranie vlastných funkcii

Napíš funkciu mnozina1(n), ktorá vráti množinu všetkých čísel z intervalu <0, n>, ktoré sú deliteľné 3 a súčasne ich zvyšok po delení 5 je 1 alebo 2. Vo funkcii nepouži žiaden cyklus, len množinové operácie a funkciu range. Napríklad:

m = mnozina1(21)
type(m)
    <class 'set'>
m
    {6, 12, 21}
Teraz napíš funkciu mnozina2(n1, n2), ktorá robí to isté ako funkcia mnozina1 ale pri interval <n1, n2>. Funkciu zapíš tak, aby sa využilo volanie mnozina1. Napríklad:

mnozina2(20, 100)
    {21, 27, 36, ... }

Napíš funkciu len_v_jednom(retazec1, retazec2), ktorá vráti množinu znakov, ktoré sa vyskytujú iba v jednom z oboch reťazcov. Funkciu zapíš len jedným množinovým výrazom:

def len_v_jednom(retazec1, retazec2):
    return ...
Napríklad:

mn = len_v_jednom('isiel macek do malaciek', 'sosovicku mlacit')
mn
    {'d', 'e', 't', 'u', 'v'}

Napíš funkciu vsetky_rozne(postupnost), ktorá zistí, či sú všetky prvky danej postupnosti navzájom rôzne. Funkcia vráti True alebo False. Funkciu zapíš len jedným výrazom, v ktorom využiješ množinu:

def vsetky_rozne(postupnosť):
    return ...
Napríklad:

vsetky_rozne((2, 5, 7, 'x', 11, 13, 17, 19, 23, 'x', 29))
    False

Napíš funkciu rozdel(mnozina), ktorá vráti dve množiny: množinu čísel a množinu reťazcov. Napríklad:

m1, m2 = rozdel({7, 7.5, '12', 3, 'python'})
m1
    {7, 7.5, 3}
m2
    {'12', 'python'}

Napíš funkciu bez_parnych(mnozina), ktorá z danej množiny vyhodí všetky párne celé čísla. Funkcia nič nevypisuje ani nevracia. Funkcia len modifikuje vstupnú množinu. Napríklad:

a = {7, 6.0, '12', 4, 'python', 124}
bez_parnych(a)
a
    {7, 6.0, '12', 'python'}
b = set(range(4, 100, 2))
bez_parnych(b)
b
    set()

Napíš funkciu len_raz(retazec), ktorá vráti množinu znakov z daného reťazca, ktoré sa v ňom vyskytujú iba raz. Rieš tak, že najprv zostrojíš dve množiny: množinu všetkých znakov a množinu tých, ktoré boli viac ako raz. Potom z nich vytvoríš výsledok. Napríklad:

znaky = len_raz('anicka dusicka kde si bola')
znaky
    {'b', 'e', 'l', 'n', 'o', 'u'}
len_raz('mama ma emu a ema ma mamu')
    set()

Napíš funkciu opakuje_sa(meno_suboru), ktorá vráti množinu slov z daného súboru, ktoré sa v ňom objavujú viac ako raz (slová sú v ňom navzájom oddelené medzerami). Napríklad pre súbor text1.txt:

Ján Botto
Žltá ľalija

Stojí stojí mohyla
Na mohyle zlá chvíľa
na mohyle tŕnie chrastie
a v tom tŕní chrastí rastie
rastie kvety rozvíja
jedna žltá ľalija
Tá ľalija smutno vzdychá
Hlávku moju tŕnie pichá
a nožičky oheň páli
pomôžte mi v mojom žiali
viac = opakuje_sa('text1.txt')
viac
    {'a', 'mohyle', 'rastie', 'tŕnie', 'v', 'ľalija'}

Napíš funkciu vsetky(a, b, c, d), ktorá vráti zoznam všetkých dvojprvkových množín z prvkov a, b, c, d. Môžeš predpokladať, že všetky hodnoty parametrov sú navzájom rôzne. Napríklad:

zoz = vsetky(1, 2, 3, 4)
zoz
    [{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}]

Vylepši funkciu z predchádzajúceho príkladu vsetky(mnozina), tak aby generovala všetky dvojprvkové množiny z prvkov zadanej množiny. Napríklad:

z = vsetky(set('java'))
z
    [{'j', 'v'}, {'a', 'v'}, {'j', 'a'}]
vsetky(set(range(5)))
    [{0, 1}, {0, 2}, {0, 3}, {0, 4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}]
vsetky({3, 1, 'x', 4, 1, 2, 'x'})
    [{1, 2}, {1, 'x'}, {1, 3}, {1, 4}, {2, 'x'}, {2, 3}, {2, 4}, {3, 'x'}, {'x', 4}, {3, 4}]
vsetky({'python'})
    []

Napíš funkciu kartez_sucin(m1, m2), ktorá vráti karteziánsky súčin množín, t.j. množinu všetkých usporiadaných dvojíc (tuple), ktorých prvá zložka je z množiny m1 a druhá zložka z množiny m2. Napríklad:

k = kartez_sucin({1, 2, 3, 4}, {'a', 'b', 'c'})
type(k)
    <class 'set'>
k
    {(3, 'c'), (3, 'b'), (2, 'a'), (4, 'a'), (4, 'c'), (4, 'b'), (1, 'b'),
     (1, 'c'), (1, 'a'), (3, 'a'), (2, 'c'), (2, 'b')}
Uvedom si, že výsledná množina môže obsahovať tieto dvojice v ľubovoľnom inom poradí.

[Príklady z w3](https://www-w3schools-com.translate.goog/python/python_sets.asp?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) 


Príklad
Truea 1považuje sa za rovnakú hodnotu:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

[Riešenie](https://www-w3schools-com.translate.goog/python/trypython.asp?filename=demo_sets_duplicate_true&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)

[Príklady z Geeksforgeeks](https://www-geeksforgeeks-org.translate.goog/python-sets/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)

[Ďalšie príklady s funkciami](https://www.programiz.com/python-programming/set)