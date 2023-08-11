Ak programovací jazyk podporuje objekty ktoré sú spracovávané jednotne bez ohľadu na to či sú uložené v datových štruktúrach, či sú odovzdávané ako argumenty alebo sú použité v riadiacich štruktúrach hovoríme o tzv. objektoch prvej triedy. Súčasne takýto programovací jazyk tým podporuje aj tzv. funkcie prvej triedy a zaobchádza s nimi totožne ako je to s objektami prvej triedy. Python podporuje **funkcie prvej triedy** ktorých vlasnosti možno zhnúť do nasledovných bodov:
* Funkcia je [inštanciou typu Object](https://sk.strephonsays.com/object-and-vs-instance-12673) - časťou pamäte ktorá odkazuje na vlastnosti a správanie objektov
* Funkciu môžete uložiť do premennej.
* Funkciu môžete odovzdať ako parameter inej funkcii.
* Funkciu môžete vrátiť z funkcie.
* Môžete ich uložiť do dátových štruktúr, ako sú hašovacie tabuľky, zoznamy, …

### Príklady ilustrujúce funkcie prvej triedy v Pythone

1. **Funkcie sú objekty:** Funkcie Pythonu sú objekty prvej triedy. V nižšie uvedenom príklade priraďujeme funkciu premennej. Toto priradenie nevolá funkciu. Zoberie funkčný objekt, na ktorý odkazuje shout, a vytvorí druhé meno, ktoré naň ukazuje, yell.
~~~
# Python program to illustrate functions
# can be treated as objects

def shout(text):
   	return text.upper()

print (shout('Hello'))
yell = shout
print (yell('Hello'))

Vysledok:
HELLO
HELLO
~~~

2. **Funkcie môžu byť odovzdané ako argumenty iným funkciám:** Pretože funkcie sú objekty, môžeme ich odovzdať ako argumenty iným funkciám. Funkcie, ktoré môžu prijať iné funkcie ako argumenty, sa tiež nazývajú **funkcie vyššieho rádu**. V nižšie uvedenom príklade sme vytvorili funkciu greet , ktorá preberie funkciu ako argument.
~~~
# Python program to illustrate functions
# can be passed as arguments to other functions

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
# storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")

    print (greeting)

greet(shout)
greet(whisper)

Vysledok:

HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
hi, i am created by a function passed as an argument.
~~~

3. **Funkcie môžu vrátiť inú funkciu:** Pretože funkcie sú objekty, môžeme vrátiť funkciu z inej funkcie. V nižšie uvedenom príklade funkcia create_adder vracia funkciu adder.
~~~
# Python program to illustrate functions
# Functions can return another function

def create_adder(x):

    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)
print (add_15(10))

Vysledok:

25
~~~

### Funkcie operátorov pre prácu s kontajnermi 
Najjednoduchšia definícia kontajnera ho popisuje ako samostatný balík softvéru, ktorý obsahuje všetko potrebné na spustenie a chod aplikácie.

Dlhšia definícia by ho popísala ako samostatný logický balík softvéru, ktorý enkapsuluje a oddeľuje aplikáciu spolu so všetkými jej závislosťami tak, aby bola aplikácia schopná bežať nezávisle od prostredia na ktorom bola vytvorená. 
Cieľom je oddeliť aplikáciu a všetky jej závislosti od operačného systému a jeho prostredia takým spôsobom, aby sa dala následne jednoducho, rýchlo a spoľahlivo zapnúť na hocijakom inom prostredí.

Tak ako sa na lodi prepravuje tovar v osobitných kontajneroch, takisto je to aj s kontajnermi vo vývoji softvéru. Pri vytváraní kontajnera by malo platiť pravidlo, že jeden kontajner je jedna služba.

Na to, aby sme docielili tieto vlastnosti kontajnerov, musíme dodržať 3 hlavné princípy kontajnerizácie: Štandardnosť (Standard), Jednoduchosť (Lightweight) a Izolovanosť (Isolated). Tieto princípy sú popísané na oficiálnej Docker stránke a taktiež ich uznáva aj Google.

[Priklady funkcii operátorov nad kontajnermi](https://www-geeksforgeeks-org.translate.goog/operator-functions-python-set-2/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)

>### Hlavná funkcia main()

Niektoré programovacie jazyky vyžadujú na vykonanie programu **hlavnú funkciu** a bez nej sa program nedá spustiť. V programovacom jazyku Python to však nie je povinné alebo potrebné. Tu je to skôr iba doporučené a to najmä pri vytváraní rozsiahlejšieho kódu ktorý je vhodné rozdeliť na viacero menší tematických častí. Program pythonu teda môžeme spustiť s použitím alebo bez použitia hlavnej funkcie main().

Jedným z najdôležitejších nástrojov ktorý s používaním tejto funkcie súvisí a ktorý je používaný v takmer každom programovacom jazyku sú **moduly**. Modul je program, ktorý je možné využiť alebo importovať do iných programov. Moduly si vytvárame za účelom aby ich bolo možné použiť aj v budúcnosti bez toho, aby ste ten istý kód ktorý sa nachádza v module znova napísali.

V Pythone vystupuje hlavná funkcia main() ako špecialny druh funkcie, ktorá je po spustení programu automaticky inicializovaná aby ju bolo možné podľa potreby použiť. O tom či tak urobíme a čo všetko zaradíme do tela tejto funkcie, ktorá plní úlohu akéhosi koordinátora, už je v našej kompetencii. Treba si však uvedomiť že pokiaľ použijeme funkciu main(), tak **vykonávanie našej aplikácie začína v súbore (menu_suboru.py) v ktorom sa táto funkcia nachádza**.

>#### Aj keď použitie tejto funkcie v Pythone nie je povinné, je dobrým zvykom túto funkciu používať, pretože zlepšuje logickú štruktúru kódu.

Pozrime sa na príklad bez hlavnej funkcie.
~~~
print("Good Morning") 

def main(): 
    print("Hello Python") 

print("Good Evening")

Vysledok:
Good Morning
Good Evening
~~~
Ak sledujeme vyššie uvedený program, vytlačil iba „Dobré ráno“ a „Dobrý večer“ a nevytlačil výraz „Hello Python“, pretože sme ho nenapísali manuálne príkazom print ako ostatné dva, alebo sme ho nezavolali ako hlavnú funkciu.

Teraz sa pozrime na program s volaním funkcie, ak __name__ == „__main__“ kde __name__ je jednou zo špecialných systémových premenných ktorá sa vyhodnocuje podľa názvu aktuálneho modulu. Ak je zdrojový súbor spustený ako hlavný program, interpret nastaví premennú __name__ na hodnotu „__main__“. Ak sa tento súbor importuje z iného modulu, __name__ sa nastaví na názov modulu.
~~~
print("Good Morning") 

def main(): 
    print("Hello Python") 

print("Good Evening") 

if __name__ == "__main__": 
    main()

Vysledok:
Good Morning
Good Evening
Hello Python
~~~
Ak napíšeme vyššie uvedený program, môže vzniknúť otázka - prečo sa vôbec tlačí “Hello Python” ? Je to preto, že tu už voláme hlavnú funkciu na konci kódu. Preto sa najskôr vytlačí “Good Morning”, ďalej “Good Evening” a na konci “Hello Python”.

Čo je to vlastne  __name__ == „__main__“?
Ako už bolo spomenuté, Python je interpretačný programovací jazyk a interpreter (program ktorý vykonáva spracovanie príkazov) začne vykonávať kód hneď po ich zadaní resp. keď sa k nim dostane v programe.

Počas tejto doby interpreter implicitne nastaví viacero svojich pracovných premenných na logické hodnoty a k týmto premenným patria aj __name__ a __main__. 

Keďže aj pre hlavnú funkciu musíme vykonať jej definíciu, že musíme definovať funkciu pre hlavnú funkciu pythonu a pomocou if if__name__ == “__main__” môžeme túto funkciu vykonať.

Keď tlmočník prečíta riadok if __name__ == „__main__“, potom sa stretne s príkazom if, akoby išlo o podmienený príkaz, a skontroloval podmienku, či sa implicitná premenná __name__ rovná hodnote __main__.

Python je veľmi flexibilný a umožňuje ponechať akýkoľvek názov hlavnej funkcie, je však dobrým zvykom ponechať si názov ako main() funkciu.
~~~
print("Apple") 

def my_main(): 
    print("Mango")

if __name__ == "__main__": my_main() 
print("Orange")
~~~

Keď do programu zahrniete túto kontrolu na rovnosť if __name__ == „__main__“, povie tým interpreteru, že funkcia main() by sa mala vždy vykonať iba ako samostatný program. Ak sa telo takejto funkcie importuje do iného programu nie je to dovolené nakoľko main() môže byť vytvorený iba raz.
~~~
print("Good Morning") 
print("Value of implicit variable __name__ is: ", __name__) 

def main(): 
    print("Hello Python") 
    
print("Good Evening") 

if __name__ == "__main__": 
    main()

Vysledok
Good Morning
Value of implicit variable __name__ is: __main__
Good Evening
Hello Python
~~~

### Volanie funkcie z iného programu

Predtým, ako sa dostaneme k vysvetleniu **importu hlavnej funkcie ako modulu**,  musíme pochopť ako používať funkcie ktoré sú prítomné vo vnútri jedného programu v programe inom.
Majme súbor kódu označený ako **test.py**
~~~
# test.py

def my_fun(a, b): 
    c = a+b 
    print("Sum of a and b is: ", c)
~~~

A majme súbor kódu označený ako **test1.py**
~~~
# test1.py

import test

test.my_fun(2, 3) 
print("Done")

Vysledok:
Sum of a and b is: 5
Done
~~~

Ako modul do iného programu môžeme tiež importovať hlavnú funkciu prítomnú v jednom inom programe .

Ak si všimnete vo vyššie uvedenom kóde tento vytlačí hodnotu __name__ ako „__main__“, ale ak importujeme modul z iného programu, nebude to __main__. 

Pozrime sa na to v nasledujúcom prípade kedy sa použije program test.py 
~~~
# test.py

print("Good Morning") 
print("Value of implicit variable __name__ is: ", __name__) 

def main(): 
    print("Hello Python") 
    
print("Good Evening") 

if __name__ == "__main__": 
    main()
~~~

a program nazvaný **python_module.py**
~~~
# python_module.py

import test 
print("Hello World")

Vysledok:

Good Morning
Value of implicit variable __name__ is: test
Good Evening
Hello World
~~~

Ak sledujeme výstup vyššie uvedeného programu, prvé 3 riadky pochádzajú z testovacieho modulu. Ak si všimnete, nevykonal hlavnú metódu test.py, pretože hodnota __name__ je iná.

Vytvorme dva súbory test1.py a test2.py
~~~
# Toto je program s nazvom test1.py

def my_fun(): 
    print("Apple") # pri standalone to nie je tlacene

print("I am in test1 file") 
if __name__ == "__main__": 
    print("test1.py will run as standalone") 
else: 
    print("test1.py will run only when imported")

~~~
Po spustení dostaneme nasledovný výsledok
~~~
I am in test1 file
test1.py will run as standalone
~~~
~~~
# Toto je program s nazvom test2.py

import test1 

print('I am in test2 file') 
test1.my_fun() 
if __name__ == '__main__': 
    print('test2.py will run as standalone') 
else: print('test2.py will run only when imported')
~~~
Po spustení dostaneme nasledovný výsledok
~~~
I am in test1 file
test1.py will run only when imported
I am in test1 file
Apple
test1.py will run as standalone
~~~
>#### Ak váš program obsahuje vyhlásenie __name__ == „__main__“, program sa vykoná ako samostatný program !

## Vytvorenie vlastnej knižnice
Keď už si vieme vytvoriť vlastné funkcie a vieme ich volať v iných programoch, vieme si tieto funkie zoskúpovať do vlasných knižníc odkiaľ ich vieme tiež volať. Robíme to postupne po nasledovných krokoch:
**Krok 1: Vytvorte adresár, do ktorého chcete umiestniť svoju knižnicu**
V našom prípade si vytvoríme priečinok s názvom **mypythonlibrary**.

**Krok 2: Vytvorte virtuálne prostredie pre svoj priečinok**
Roobíme to preto lebo nakoniec urobíme zapúzdrenie nášho projektu v ktorom sa okrem požitej verzie Pythonu a niektorých knižníc nachádzajú všetky potrebné súbory ako celok. Virtuálne prostredie pomáha zabezpečiť kompatibilitu jednak čo sa týka verzii tak aj iných prostredí na iných PC.
Po to co prejdeme do nášho adresára, vyrtuálne prostredie vytvoríme príkazom
~~~
$ python -m venv venv
~~~
Pomocou Ctrl+Shift+P vo VS-Code vyhľadáme v našom adresári python a zvolíme ho pre venv.
Po vytvorení musíte prostredie aktivovať pomocou:
~~~
$ cd venv/scripts
$ source activate
~~~
Aktivácia virtuálneho prostredia upraví premenné PATH a shell tak, aby ukazovali na špecifické izolované nastavenie Pythonu, ktoré ste vytvorili vo venv. Po tomto sa príkazový riadok zmení a ukáže sa v ktorom virtuálnom prostredí sa práve nachádzate (venv). V našom prostredí budeme potrebovať na zostavenie našej knižnice pip, wheel, setuptools a twine ktoré nainštalujeme:
~~~
$ pip install wheel
$ pip install setuptools
$ pip install twine
~~~
**Krok 3: Vytvorte štruktúru priečinkov**
Vo VS-Code otvorte priečinok mypythonlibrary (alebo akýkoľvek názov, ktorý ste dali priečinku). Teraz môžete začať pridávať priečinky a súbory do svojho projektu. Môžete to urobiť buď prostredníctvom príkazového riadka alebo v samotnom kóde Visual Studio.
1. Vytvorte prázdny súbor s názvom setup.py. Toto je jeden z najdôležitejších súborov pri vytváraní knižnice Python!
2. Vytvorte prázdny súbor s názvom README.md. Toto je miesto, kde môžete napísať značku, ktorá opíše obsah vašej knižnice pre ostatných používateľov.
3. Vytvorte priečinok s názvom mypythonlib, alebo ako chcete, aby sa vaša knižnica Pythonu volala, keď ju nainštalujete pip. (Názov by mal byť jedinečný, ak ho chcete neskôr zverejniť.)
4. Vytvorte vo vnútri prázdny súbor mypythonlibs názvom __init__.py. V podstate každý priečinok, ktorý obsahuje __init__.py súbor, bude zahrnutý do knižnice, keď ju vytvoríme. Väčšinu času môžete nechať __init__.py súbory prázdne. Pri importe sa kód v rámci __init__.py spustí, takže by mal obsahovať iba minimálne množstvo kódu, ktoré je potrebné na spustenie vášho projektu. Zatiaľ ich necháme tak, ako sú.
5. V rovnakom priečinku tiež vytvorte súbor s názvom myfunctions.py.
6. A nakoniec vytvorte priečinok tests v koreňovom priečinku. Vnútri vytvorte prázdny __init__.py súbor a prázdny súbor test_myfunctions.py.

Vaše nastavenie by teraz malo vyzerať asi takto:
![](../mypythonlibrary.png)

**Krok 4: Vytvorte obsah pre svoju knižnicu**
Ak chcete funkcie vložiť do knižnice, môžete ich umiestniť do myfunctions.py súboru. Napríklad skopírujte funkciu haversine do svojho súboru:
~~~
# myfunctions.py

from math import radians, cos, sin, asin, sqrt
def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance between two points on the 
    earth (specified in decimal degrees), returns the distance in
    meters.
    All arguments must be of equal length.
    :param lon1: longitude of first place
    :param lat1: latitude of first place
    :param lon2: longitude of second place
    :param lat2: latitude of second place
    :return: distance in meters between the two sets of coordinates
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r
~~~
Táto funkcia nám poskytne vzdialenosť v metroch medzi dvoma bodmi zemepisnej šírky a dĺžky.

Vždy, keď napíšete akýkoľvek kód, **dôrazne sa odporúča**, aby ste pre tento kód napísali aj **testy**. Na testovanie s Pythonom môžete použiť knižnice pytest a pytest-runner. Nainštalujte knižnice do svojho virtuálneho prostredia:
~~~
$ pip install pytest==4.4.1
$ pip install pytest-runner==4.4
~~~
Vytvorme si malý test pre funkciu haversine. Skopírujte nasledovné a vložte ho do test_myfunctions.py súboru:
~~~
# test_myfunctions.py

from mypythonlib import myfunctions

def test_haversine():
    assert myfunctions.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 945793.4375088713
~~~

Nakoniec si vytvorme setup.py súbor, ktorý nám pomôže vybudovať knižnicu a **vložíme súbory ktoré chceme zabudovať**. Obmedzená verzia setup.pybude vyzerať asi takto:
~~~
from setuptools import find_packages, setup
setup(
    name='mypythonlib', # toto je nazov nasej kniznice
    # packages=find_packages(), nahradili sme prikazom ktory
    packages=find_packages(include=['mypythonlib']), # vlozi do kniznice 
                                # iba subory z nasho adresara
    version='0.1.0',
    description='Moja prvá knižnica Python',
    author='Tomáš Tokoš',
    license='SŠŠ Trenčín',
)
~~~
V ďalšom kroku **nastavíme požiadavky ktoré potrebuje naša knižnica splniť**. Inštalačný program Pythonu pip nepoužíva requirements.yml/ requirements.txt (stanovenie závislosťí). Preto to budete musieť špecifikovať v argumentoch install_require a tests_require vo vašom setup.py súbore. Install_requires by sa mal obmedziť na zoznam balíkov, ktoré sú nevyhnutne potrebné a nie sú súčasťou standardnej knižnice Pythonu. Naša funkcia haversine používa iba matematickú knižnicu (ktorá je v Pythone) preto môžeme tento argument nechať prázdny. V prípade pytest chceme aby bol nainštalovaný automaticky pri spustení testov.
~~~
from setuptools import find_packages, setup
setup(
    name='mypythonlib', # toto je nazov nasej kniznice
    # packages=find_packages(), nahradili sme prikazom ktory
    packages=find_packages(include=['mypythonlib']), # vlozi do kniznice 
                                # iba subory z nasho adresara
    version='0.1.0',
    description='Moja prvá knižnica Python',
    author='Tomáš Tokoš',
    license='SŠŠ Trenčín', 
    install_requires=[], 
    setup_requires=['pytest-runner'], 
    tests_require=['pytest==4.4.1'], 
    test_suite='tests', 
)
~~~
Testy uložené v priečinku 'tests'sa vykonajú príkazom .
~~~
$ python setup.py pytest
~~~
** Krok 5: Vytvorte si knižnicu**
Teraz už môžeme vybudovať našu knižnicu. Uistite sa pred tým ale, že váš aktuálny pracovný adresár je /path/to/mypythonlibrary (teda koreňový priečinok vášho projektu). V príkazovom riadku spustite:
~~~
$ python setup.py bdist_wheel
~~~

Súbor vášho wheel je uložený v novo vytvorenom priečinku „dist“. Knižnicu si môžete nainštalovať pomocou:
~~~
$ pip install c:\\..\\mypythonlibrary\\dist\\wheelfile.whl
~~~
Svoju knižnicu môžeme publikovať aj do interného súborového systému na intranete vášho pracovisku alebo do oficiálneho úložiska [PyPI](https://pypi.org/) a nainštalovať ju odtiaľ.
Po nainštalovaní knižnice Python ju môžete importovať pomocou:
~~~
import mypythonlib
from mypythonlib import myfunctions
~~~

Podrobnejší návod na vytvorenie knižnice ktorá má byť aj verejne dostupná napr. cez GitHub nájdete [tu](https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14) resp. [tu](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

Rozdiely medzi pouźívaním príkazov **import** a **from import** najdeme [tu](https://www.codingem.com/python-difference-between-import-and-from-import/)

https://www.w3schools.com/python/python_modules.asp 

Príklad zdrojového kódu knižnice [datatime](https://github.com/zopefoundation/DateTime/tree/master) resp. [celý zoznam](https://docs.python.org/3/library/index.html). 

[alebo](https://github.com/topics/python-datetime)