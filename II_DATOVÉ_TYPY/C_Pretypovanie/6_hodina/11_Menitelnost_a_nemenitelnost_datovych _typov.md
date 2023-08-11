# Menitelnosť a nemenitelnosť dátových typov

Datové typy rozlišujeme aj podľa toho, či ich hodnoty môžeme měnit alebo nie. Podľa toho rozlišujeme:

* **nemenitelné (immutable)** typy ku ktorým patrí int, float, bool, str, tuple.
* **menitelné (mutable)** typy ku ktorým patrí list, set, dict ktorými sa budeme zaoberať neskôr v časti C.

    Takéto rorozlišovanie je napríklad dôležité v súvislosti s indexovaním ako je to v prípade slovníkov – dictionary. Indexovať t.j. priraďovať jednotlivým prvkom označenie poradia - index môžeme totiž  iba u tých ktoré obsahujú nemenitelné typy.

># Pretypovanie hodnôt
Jednotlivé typy hodnôt, premenných a objektov môžeme v určitých prípadoch zmeniť na iné typy. Je potrebné spomenúť že používanie pretypovania alebo konverzných funkcii spôsobí aj zmenu typu premennej. K tomu nás väčšinou vedie potreba zjednotenia dátových typov pri aplikácii jednotlivých operácii a funkcii. To ako to urobiť si ukážeme v nasledovnej časti.

Názvy typov sú súčasne názvami tzv.vstavaných funkcí, ktoré pomocou ktorých vykonáme tzv. **pretypovanie**. Typy premenných sú veľmi dôležité a je im potrebné venovať zvýšenú pozornosť nakoľko sa často stáva že nedostaneme očakávaný výsledok, alebo sa objaví chyba ktorá je práve výsledkom konfliktu odlišných dátových typov. Kontrolu datového typu vykonávame pomocou funkcie **type()**. Dátové typy nám napríklad ovlyvňujú aj význam operátorov s ktorými jednotlivé funkcie narábajú. Typickým príkladom je pretypovanie čísla na retezec:
~~~
x = 15      # x predstavuje celé číslo
print(x)    # vypíše 15
print(3*x)  # vypíše 45
x = str(x)  # pretypovanie na retazec, x teraz nepredstavuje celé číslo, ale kombináciu znakov "15"
print(x)    # vypíše 15 (tu sa ešte rozdiel typu neprejaví)
print(3*x)  # vypíše 3x 15 t.j. 151515 (pretože x je teraz retazec a operácia * pre retťazec znamená opakované zreťazenie)
~~~

* **celociselna_premenna = int(hodnota)**\
z danej hodnoty vyrobí celé číslo, napr.\
int(3.14) => 3
int('37') => 37\
a=int(2.7) ... v premennej a bude celé číslo 2\
b=int(-3.14) ... v premennej b bude celé číslo -3\
c=int(‘524’) ... v premennej c bude celé číslo 524

* **realna_premenna = float(hodnota)**\
z danej hodnoty vyrobí desatinné číslo, napr.\
float(333) => 333.0
float('3.14') => 3.14\
d=float(2) ... v premennej d bude reálne číslo 2.0\
e=float(‘-3.14’) ... v premennej e bude číslo -3.14

* **retazec = str(hodnota)**\
z danej hodnoty vyrobí znakový reťazec, napr.\
str(356) => '356'\
str(3.14) => '3.14'\
w=str(27) ... v premennej w bude reťazec ‘27’

Využijeme jednu z troch konvertovacích (pretypovacích) funkcií:

Mená typov int, float a str zároveň súžia ako mená pretypovacích funkcií, ktoré dokážu z jedného typu vyrobiť hodnotu iného typu:

>Pretypovanie reťazca na číslo bude fungovať len vtedy, keď je to správne zadaný reťazec, inak funkcia vyhlási chybu.

Aby náš program poskytol správny výsledok, potom po pretypovaní bude vyzerať takto:
~~~
cislo_str = input('zadaj cenu jedneho vyrobku: ')
cislo = float(cislo_str)       # pretypovanie
spolu = cislo * 4
print('4 vyrobky stoja', spolu, 'euro')
~~~

Na záver si ešte ukážeme ako vyzerá **pretypovanie v prípade n-tice** kedy vykonáme náhodný výber farby z n-tice mojefarby pomocou funkcie random.choice() z knižnice ranšho kódu importovat. Podobne je to aj v prípade ďalšej n-tice (tuple)
zviera.
~~~
import random

mojefarby = ('red', 'pink', 'purple', '#A0FF54')
vybrana_farba = random.choice(mojefarby)
print(f"Vybrana farba je :", vybrana_farba)
print(type(vybrana_farba))

zviera = ('slon', 2013, 'gray')
vybrane_zviera = random.choice(zviera)
print(vybrane_zviera)
print(type(vybrane_zviera))
~~~

Vyššie sme sa zoznámili so základnými prvkami programovacieho jazyka Python: typy hodnôt, premenné, pretypovanie a najmä spôsobom priradovania napr. pomocou rovnítka a pod. 

Zopakujme si niektoré veci ktoré súvisia s priradením nejakej hodnoty.
~~~
meno = input('ako sa volas? ')
print('ahoj', meno)
~~~
V tomto príklade sa využíva funkcia input(), ktorá zastaví bežiaci výpočet, čaká aby používateľ zadal nejaký text a odoslal ho stlačením klávesy Enter. Tieto údaje sa týmto uložia do premennej s názvom meno. Na koniec toto zadané meno vypíše. Program spustíme klávesou Ctrl+F5 alebo F5. Beh programu v konzolovom okne (shell pythonu) môže vyzerať napr. takto
~~~
ako sa volas? Jozef
ahoj Jozef
>>>
~~~
Týmto síce program skončil ale my môžeme ďalej pokračovať napr. v skúmaní obsahu použitých premenných. V programovom režime zistíme hodnotu premennej meno:
~~~
>>> meno
'Jozef'
~~~
V našich budúcich programoch bude bežné, že na začiatku sa vypýtajú hodnoty nejakých premenných a ďalej potom program s nimi pracuje .

Ďalší program ukazuje, ako to vyzerá, keď chceme načítať nejaké číslo:
~~~
cislo = input('zadaj cenu jedneho vyrobku: ')
spolu = cislo * 4
print('4 vyrobky stoja', spolu, 'euro')
~~~
Týmto programom sme chceli prečítať cenu jedného výrobku a z toho vypočítať, aká je cena 4 takýchto výrobkov. Po spustení programu dostávame:
~~~
zadaj cenu jedneho vyrobku: 1.2
4 vyrobky stoja 1.21.21.21.2 euro
~~~
Takýto výsledok je zrejme nesprávny: očakávali sme celkovú cenu 4.8 euro. Problémom tu bolo to, že funkcia input() zadanú hodnotu vráti nie ako číslo, ale ako znakový reťazec, teda '1.2'. Na tomto mieste potrebujeme takýto reťazec **prekonvertovať** na desatinné číslo.
