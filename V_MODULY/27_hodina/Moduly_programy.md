>>## Moduly

Tým že funkcia main() umožňuje volanie funkcii ktoré sú definované v iných súboroch ponúka vhodný nástroj pre štrukurovanie kódu našej aplikácie. Robí to pomocou príkazu **import** prostredníctvom ktorého sa do main() prenášajú ako moduly funkcie z iných pythonovských súborov. Tým je aj daná súvislosť medzi hlavnou funkciou main() a jej modulmi.

Všeobecne povedané **modul** v Pythone je však něco, z čeho můžeš importovat nejakú funkciu. Třeba z modulu math můžeš importovat funkci sqrt:
~~~
from math import sqrt

print(sqrt(2))
~~~

Kromě importování jednotlivých proměnných z modulu můžeš importovat i celý modul najednou. K tomu, co modul nabízí, se pak dostaneš pomocí tečky – podobně jako se pomocí 'Ahoj'.upper dostaneš k metodě, kterou nabízí řetězec.

Například:
~~~
import turtle

turtle.left(90)
turtle.color('red')
turtle.forward(100)
turtle.exitonclick()
~~~
~~~
import math

print(math.cos(math.pi))
~~~

**Hvězdičky nechceme**
Možná jsi v dokumentaci nebo na jiném kurzu viděl/a příkaz import s hvězdičkou (*). Pokud ano, v rámci tohoto kurzu na hvězdičku prosím zapomeň a importuj místo toho radši celý modul. Až začneš psát větší programy, zjednoduší ti to prácu.

>### Vlastní moduly
A teď to hlavní! Můžeš vytvořit vlastní importovatelný modul a to jen tak, že uděláš pythonní soubor. Funkce, které v něm nadefinuješ, a globální proměnné, které v něm nastavíš, pak budou k dispozici tam, kde modul naimportuješ.

Zkus si to! Vytvoř soubor louka.py a do něj napiš:
~~~
barva_travy = 'zelená'
pocet_kotatek = 28

def popis_stav():
    return f'Tráva je {barva_travy}. Prohání se po ní {pocet_kotatek} koťátek'
~~~
A pak do dalšího souboru, třeba vypis.py, napiš:
~~~
import louka

print(louka.popis_stav())
~~~
A pak spusť vypis.py cez git shell:

$ python vypis.py

Příkaz import hledá soubory (mimo jiné) v adresáři, ve kterém je „hlavní modul” programu – tedy soubor který spouštíš (tady vypis.py). Oba soubory by proto měly být ve stejném adresáři.

>#### Vedlejší efekty 
Co přesně dělá příkaz import louka?

Python najde příslušný soubor (louka.py) a provede v něm všechny příkazy, odshora dolů, jako v normálním Pythonním programu. Všechny globální proměnné (včetně nadefinovaných funkcí) pak dá k dispozici kódu, který importoval.

Když pak stejný modul importuješ podruhé, už se neprovádí všechno znovu. Druhý import jen zpřístupní stejnou sadu proměnných/funkcí jako ten první.

Zkus si to – na konci louka.py dopiš:

print('Louka je zelená!')
Spusť python (máš-li ho už spuštěný, ukonči a spusť znovu) a zadej v něm:
~~~
print('První import:')
import louka
print('Druhý import:')
import louka
~~~

Výpis se objeví jen poprvé. Co víc, když teď soubor louka.py změníš, změny se do naimportovaného modulu nepromítnou. Aby se promítly, musíš Python zavřít a spustit znovu. (I proto je dobré pouštět programy ze souborů – při každém spuštění se znovu načte aktuální verze modulů.)

Ale zpátky k volání print. Přijde ti trochu divné, že příkaz import louka něco vypíše na obrazovku?

Když takhle modul při importu „dělá“ něco víc než jen nastavení proměnných a funkcí, říká se, že má vedlejší efekt (angl. side effect). Vedlejší efekt může být vypsání něčeho na obrazovku nebo do souboru, vykreslení okýnka na obrazovku, otázka na uživatele pomocí input, atp.

V modulech připravených na importování se vedlejším efektům vyhýbej: úloha takového modulu je dát k dispozici funkce, které něco dělají, ne to udělat přímo. Všimni si například, že import turtle neukáže okýnko – to se objeví až po zavolání turtle.forward(). 
>### Importem si programátor připravuje nástroje; teprve zavoláním funkce je používá.

Příkaz print proto radši z modulu zase smaž.

>## Adresář pro každý projekt 
Od teď budeš občas psát větší projekty, které budou obsahovat více souvisejících souborů. Pro každý takový projekt si udělej zvláštní adresář. Lépe se pak vyznáš v tom, ke kterému projektu který soubor patří.

>### Používáme moduly
Moduly mohou obsahovat libovolný kód, jejich použití se tedy neomezuje na pouhé definování řady funkcí. Před prvním zavedením modulu interpretr nalezne soubor obsahující modul, načte ho a spustí všechny příkazy, které obsahuje. Tento proces se nazývá inicializace modulu. Při inicializaci vznikají objekty reprezentující funkce uvnitř modulu a je možné při ní nastavit i globální proměnné modulu do určitého stavu. Pokud chce program importovat modul, který je již zinicializován, nedojde k opětovnému spuštění kódu, nýbrž se použije objekt modulu vytvořený při inicializaci.

Zavedením modulu vznikne nový prostor jmen určený pro globální proměnné tohoto modulu. Díky tomuto mechanismu může autor modulu používat libovolné názvy proměnných a přesto nedojde ke kolizi s proměnnými jiného modulu. Proměnné v tomto jmenném prostoru jsou přístupná za použití objektu modulu (klasicky jako jméno_modulu.proměnná). Nedoporučuje se ovšem libovolným způsobem modifikovat soukromé proměnné modulu, mohli byste totiž narušit konzistenci dat modulu a ten by mohl začít chybně pracovat.

Je samozřejmé, že moduly mohou importovat jiné moduly. V Pythonu je zvykem umístit veškeré příkazy import na začátek modulu či skriptu. Definice jazyka to ovšem nevyžaduje, uznáte-li za vhodné, můžete příkaz import použít například ve větvi příkazu if nebo uvnitř funkce.

Jak jsme si řekli výše, příkaz import zavede do lokálního prostoru jmen objekt modulu. Existuje ale i varianta příkazu import, která rovnou zavede některé (popř. všechny) objekty z určitého modulu. Nemusíme tedy používat přiřazení pro vytvoření lokálního jména:

>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
Toto použití příkazu import nevytvoří jméno, odkazující na objekt modulu, v příkladě výše je tedy proměnná fibo (reprezentující modul fibo) nedefinována.

Pro zavedení všech jmen z modulu je zde další varianta příkazu import:6.3

>>> from fibo import *
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
Tento příkaz zavede z modulu všechna jména s výjimkou těch, která začínají znakem podtržítko. Je třeba podotknout, že tento způsob použití modulů je velmi zrádný. Jednak není známo, na kterém místě je která proměnná definována a jednak již může dojít ke kolizi jmen a proto u některých modulů je výslovně zakázáno použití from ... import *. Snažte se proto používání tohoto příkazu omezit pouze na interaktivní sezení a ve skriptech ho raději vůbec nepoužívejte.

>### Vyhledávání modulů
 Co se stane, pokud importujeme modul fibo poprvé? Kde všude interpretr hledá soubory obsahující definici tohoto modulu? Především nejprve se interpretr podívá do pracovního adresáře, jestliže zde najde soubor fibo.py, veškerá jeho práce končí a pokusí se zavést tento modul.

Pokud však tento soubor v tomto adresáři nenalezne, začne ho vyhledávat podle přesných pravidel specifikovaných definicí jazyka. Tedy: nejprve se podívá na proměnnou prostředí PYTHONPATH, která by měla mít stejnou syntaxi jako proměnná prostředí PATH. Není-li proměnná PYTHONPATH nastavena nebo v adresářích, které specifikuje, není požadovaný soubor nalezen, pokračuje vyhledávání v implicitní cestě. Tu specifikuje proměnná sys.path, jde o seznam řetězců reprezentujících adresáře. Obsah této proměnná je závislý na instalaci interpretru a jeho nastavení v modulu site. Může vypadat třeba takto: ['/usr/lib/python2.2', '/usr/lib/python2.2/plat-linux2'].

Je třeba důsledně dbát na to, aby nějaký soubor v pracovním adresáři neměl stejné jména jako nějaký standardní modul. Uzavřeli bychom si tak cestu k tomuto standardnímu modulu, protože při pokusu o zavedení tohoto modulu bychom ve skutečnosti obdrželi modul ze souboru v pracovním adresáři. Pro více informací o standardních modulech nahlédněte do sekce 6.2.

Pokud interpretr požadovaný modul nenalezne, dojde k výjimce, která se rozšíří z příkazu import6.4. Obdobně je tomu i v případě, kdy se požadovaný modul podařilo nalézt, ale při jeho inicializaci došlo k výjimce. Zde je třeba dávat pozor na to, že přestože modul nebyl korektně zinicializovaný, při dalším pokusu o jeho zavedení se již druhá inicializace konat nebude a modul bude možné používat nezinicializovaný.


>### Standardní moduly
Základní distribuce Pythonu obsahuje velké množství modulů (jsou popsány v samostatném dokumentu Python Library Reference). Díky nim je možné realizovat množství úloh spojených s internetem, unixovými databáze dbm, prací se soubory, operačním systémem a mnoho a mnoho dalších.

Některé moduly jsou přímo součástí interpretru, umožňují totiž přístup k operacím, které nejsou přímo součástí jádra prostředí, ale jsou mu velice blízká (např. v dané aplikaci závisí na rychlosti vykonávání nebo je třeba volat funkce operačního systému či dalších knihoven). Zahrnutí těchto modulů je závislé na konfiguraci a překladu interpretru. (Například modul Tkinter určený jako rozhraní ke grafické knihovně Tk je přítomný pouze na systémech s knihovnou Tk).

Mezi všemi moduly najdeme jeden, který nabízí samotné jádro běhového systému, modul sys a obsahuje ho každý interpretr. Jeho proměnné sys.ps1 a sys.ps2 umožňují v interaktivním módu nastavení primární a sekundární výzvy interpretru:

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print 'Ahoj!'
Ahoj!
C>
Jak již jistě víte, proměnná sys.path je seznam řetězců, který určuje cesty v nichž interpretr vyhledává moduly. Je inicializována z proměnné prostředí PYTHONPATH příp. je nastavena v modulu site. Jde o klasický seznam, který můžete měnit běžnými operacemi definovanými nad seznamy:

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

>### Funkce dir()
Interní funkci dir() použijete v případě, že chcete zjistit všechna jména, která jsou definována uvnitř nějakého objektu. Tato funkce vrací seznam řetězců setříděný podle abecedy, jeho používání reprezentuje následující příklad:

>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__stderr__',
 '__stdin__', '__stdout__', '_getframe', 'argv', 'builtin_module_names',
 'byteorder', 'copyright', 'displayhook', 'exc_info', 'exc_type',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'getdefaultencoding',
 'getdlopenflags', 'getrecursionlimit', 'getrefcount', 'hexversion',
 'maxint', 'maxunicode', 'modules', 'path', 'platform', 'prefix', 'ps1',
 'ps2', 'setcheckinterval', 'setdlopenflags', 'setprofile',
 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'version',
 'version_info', 'warnoptions']
Bez argumentů vrátí seznam jmen, které jsou definovány v aktuálním prostoru jmen:

>>> a = [1, 2, 3, 4, 5]
>>> import fibo, sys
>>> fib = fibo.fib
>>> dir()
['__name__', 'a', 'fib', 'fibo', 'sys']
Seznam vrácený funkcí dir() zahrnuje všechna jména definovaná v objektu, nejde tudíž pouze o proměnné, ale i o funkce, moduly, třídy apod. Do tohoto seznamu nejsou zahrnuta jména interních funkcí a proměnných (tj. těch definovaných modulem __builtin__). Pokud potřebujete seznam interních funkcí použijte

>>> import __builtin__
>>> dir(__builtin__)
['ArithmeticError', 'AssertionError', 'AttributeError',
 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
 'Exception', 'FloatingPointError', 'IOError', 'ImportError',
 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt',
 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError', 'OverflowWarning',
 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TypeError', 'UnboundLocalError',
 'UnicodeError', 'UserWarning', 'ValueError', 'Warning',
 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__',
 '__name__', 'abs', 'apply', 'buffer', 'callable', 'chr', 'classmethod',
 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr',
 'dict', 'dir', 'divmod', 'eval', 'execfile', 'exit', 'file', 'filter',
 'float', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len',
 'license', 'list', 'locals', 'long', 'map', 'max', 'min', 'object',
 'oct', 'open', 'ord', 'pow', 'property', 'quit', 'range', 'raw_input',
 'reduce', 'reload', 'repr', 'round', 'setattr', 'slice', 'staticmethod',
 'str', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange',
 'zip']

>### Balíčky
Balíčky jsou logickým rozšířením mechanismu Pythonových modulů. V Pythonu je totiž široce používána "tečková notace" a právě balíčky umožňují hiearchickou organizaci modulů.

Například modul se jménem A.B znamená modul pojmenovaný "B" v balíčku "A". Balíčky umožňují dekompozici rozsáhlých knihoven do menších souborů - modulů. Autoři jednotlivých modulů se nemusí zajímat o jména globálních proměnných jiných modulů v tomtéž balíčku, jazyk zajišťuje vzájemnou "izolaci" balíčků mezi sebou. Proto se například autoři jednotlivých modulů rozsáhlých balíčků (např. NumPy nebo Python Imaging Library) nemusí obávat střetu jmen svých globálních proměnných s proměnnými jiného autora.

Představte si modelovou situaci: chcete navrhnout balíček (kolekci modulů) pro manipulaci se zvukovými soubory a zvukovými daty obecně. Poněvadž existuje mnoho různých zvukových formátů, potřebujete vytvořit a spravovat kolekci modulů pro konverzi mezi těmito formáty. Také si můžete představit mnoho operací, které lze se zvukovými daty provádět (např. mixování stop, přidávání ozvěny, aplikování ekvalizéru ...). Postupem času si vytvoříte mnoho modulů pro tyto činnosti. Pro jejich organizaci je mechanismus balíčků naprosto ideální. Zde je možná struktura vašeho balíčku (zobrazená jako hiearchický souborový systém):

Sound/                          Hlavní balíček
      __init__.py               Inicializace balíčku
      Formats/                  Balíček pro konverzi souborových formátů
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      Effects/                  Balíček pro zvukové efekty
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      Filters/                  Balíček filtrů
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
Jistě se ptáte, co znamenají soubory __init__.py. Python podle nich rozpoznává adresáře obsahující balíčky. To zabraňuje nedorozuměním, kdy Python považoval libovolný adresář nacházející se v jeho cestě za balíček. V nejjednodušším případě je soubor __init__.py pouhopouhý prázdný soubor, můžete sem ale umístit inicializační kód balíčku nebo nastavit proměnnou __all__ (její význam je popisován později).

Uživatelé balíčku z něj mohou přímo importovat jednotlivé moduly:

import Sound.Effects.echo
Tento příkaz načte modul Sound.Effects.echo. Jeho proměnné a funkce však musí být odkazovány plným jménem:

Sound.Effects.echo.echofilter(input, output, delay=0.7, atten=4)
Jinou možností je přímé importování modulu z balíčku:

from Sound.Effects import echo
Tento příkaz také načte modul echo a učiní jej přístupným za použití jeho jména. Funkce v něm definované můžete používat třeba následovně:

echo.echofilter(input, output, delay=0.7, atten=4)
Další cestou je importování určité funkce nebo proměnné přímo:

from Sound.Effects.echo import echofilter
Tento příkaz opět načte modul echo, ale učiní jeho funkci echofilter() přístupnou přímo:

echofilter(input, output, delay=0.7, atten=4)
Na závěr podotkněme, že při importování nějakých jmen (proměnných, modulů apod.) za použití příkazu import můžeme na místě objektu, z něhož chceme import provést uvést pouze balíček nebo modul. Příkaz "from objekt_různý_od_modulu_či_balíčku import jeho_atribut" je považován za běhovou chybu a z místa jeho použití se rozšíří výjimka. Jako náhradu takovéto konstrukce lze použít "jeho_atribut = objekt_různý_od_modulu_či_balíčku.jeho_atribut".

>### Odkazování se na moduly uvnitř balíčku
Mnohdy se potřebuje jeden modul odkazovat na jiný modul téhož balíčku. Vyjděme z našeho modelového příkladu. Modul surround bude potřebovat nějakou funkci z modulu echo. V tomto případě platí následující: příkaz import se nejprve podívá do aktuálního balíčku a až poté prohledá standardní cestu (určenou proměnnou sys.path). Proto může modul surround jednoduše použít "import echo". Pokud by modul echo nebyl součástí aktuálního balíčku, přišly by na řadu standardní pravidla pro vyhledávání modulu.

Je-li balíček strukturovaný na podřízené balíčky (v modelovém příkladě například balíček Sound), neexistuje žádný způsob, jak se odkazovat na modul rodičovského balíčku, musíme použít jeho plné jméno. Pokud třeba modul Sound.Filters.vocoder potřebuje modul echo balíčku Sound.Effects, musí použít příkaz from Sound.Effects import echo.

>### Zásada
Síla programovacího jazyka není pouze v jeho syntaxi, ale především ve funkcích, které už někdo naprogramoval před vámi a vy je musíte jenom použít.

Python používá systém modulů - v podstatě se jedná o soubory, ve kterých jsou funkce uloženy a do vašeho programu je musíte naimportovat. Heslem Pythonu je „batterries included“ a znamená to, že opravdu spousta věcí je už hotová a dostupná.

Čím více modulů budete importovat, tím více vám váš program bude zabírat v paměti a jeho spouštění bude o něco pomalejší - neimportujte něco, co nepotřebujete.

Vyzkoušíme si např. některé funkce z modulu math

import math

print(math.sqrt(10))
Funkce sqrt() není standardně v základu Pythonu přítomna. Program by skončil výjimkou

NameError: name 'math' is not defined
Modul math obsahuje celou řadu zajímavých věcí, např. číslo PI

print(math.pi)
print(math.e)
Importovat můžete buď celé moduly, jako v předchozím příkladě, nebo jenom jednotlivé fukce, např. sin().

from math import sin

print(sin(math.pi/2))
Nyní něco ze světa prostorových dat

from shapely.geometry import Point

centroid = Point(0.0, 0.0) # vytvoříme nový objekt třídy "Point"
patch = centroid.buffer(10.0) # zavoláme jeho metodu buffer
print(patch.area) # a tiskneme jeho plochu
V předchozím příkladu jsme z modulu shapely, který nám umožňuje pracovat s vektorovými geometriemi naimportovali třídu Point, vytvořili jsme nový bod, okolo něj buffer o velikosti 10 a vytiskli plochu výsledné obalové zóny.

Trochu jsme tím nakoukli do světa objektově-orientovaného programování, blíže se s ním seznámíme v další části.

Nyní zkusíme ještě vytisknout vytvořený buffer ve formátu GeoJSON:

import json
from shapely.geometry import mapping

print(json.dumps(mapping(patch)))
V předchozím příkladu jsme na posledním řádku použili jako vstup pro funkci print() výstup z funkce json.dumps(), která zase dostala výstup z funkce mapping() - není to moc přehledné, ale podobné konstrukce se používají často.

Dokumentace k modulům
Je na čase, seznámit se s příkazem pydoc (nebo pydoc3), který jako parametr dostane modul a provede vás jeho dokumentací

$ pydoc shapely


Help on package shapely.geometry in shapely:

NAME
    shapely.geometry - Geometry classes and factories

FILE
    /home/jachym/.local/lib/python2.7/site-packages/shapely/geometry/__init__.py

PACKAGE CONTENTS
    base
    collection
    geo
    linestring
    multilinestring
    multipoint
    multipolygon

...
Google vám vždycky dobře poradí, pokud správně hledáte a seznam modulů distribuovaných spolu s jazykem Python najdete na dokumentační stránce jazyka Python

Vlastní moduly
Uložíte-li program do souboru, stává se tímto váš soubor modulem, který lze použít a naimportovat.

Vytvoříme soubor buffer.py s následujícím obsahem:

from shapely.geometry import Point
from shapely.geometry import mapping, shape

def udelej_buffer(geometry, velikost):
    """Vrátí buffer ve formátu GeoJSON pro zadanou geometrii
    """

    geometrie = shape(geometry)
    buffer = geometrie.buffer(velikost)
    return  mapping(buffer)
Nyní můžeme v jiném programu (nebo přímo v interpretu) náš modul použít:

>>> import buffer
>>> muj_bod = {"type": "Point", "coordinates": [0.0, 0.0]}
>>> buffer.udelej_buffer(muj_bod, 3)
{
    'type': 'Polygon',
    'coordinates': ((
        (3.0, 0.0),
        (2.9855541800165906, -0.29405142098868153),
        (2.9423558412096917, -0.5852709660483842),
        (2.8708210071966267, -0.8708540317633864),
        (2.771638597533861, -1.1480502970952682),
        (2.6457637930450657, -1.4141902104779915),
        (2.4944088369076365, -1.6667106990588052),
        (2.3190313600882124, -1.903179852490935),
        (2.1213203435596446, -2.1213203435596406),
        (1.903179852490939, -2.319031360088209),
        (1.6667106990588092, -2.4944088369),
        ...
    ))
}
Moduly nám tedy umožňují uklidit spolu související části programu do logických celků, rozsekat rozsáhlé programy do menších souborů a strukturovat tak kód pro přehlednější použití.

[Abecedný zoznam Pythonových modulov](https://docs.python.org/3.11/py-modindex.html)

### Dva typy modulů: programy a knihovny
Všechno to jsou soubory .py, zde rozdíl není.
Programy (skripty) jsou určeny primárně ke spouštění (představují vstupní bod nějaké aplikace).
Knihovny jsou určeny k importu do jiných knihoven a programů
Často ale můžeme tentýž modul využít
i jako skript (můžeme ho spustit a on udělá něco užitečného)
i jako knihovnu (můžeme ho importovat do jiných modulů)

Vlastne moduly video od Misa
https://www.youtube.com/watch?v=ea6R0ZygfLM 

>### Pridanie modulu do cesty Python
Druhou možnosťou, ktorú máte, je pridať modul na cestu, kde Python kontroluje moduly a balíky. Toto je trvalejšie riešenie, vďaka ktorému je modul dostupný v celom prostredí alebo v celom systéme, vďaka čomu je táto metóda prenosnejšia.

Ak chcete zistiť, akú cestu Python kontroluje, spustite interpret Pythonu z vášho programovacieho prostredia:

python3

Ďalej importujte modul sys:

import sys

Potom nechajte Python vytlačiť systémovú cestu:

print(sys.path)

Tu dostanete nejaký výstup s aspoň jednou systémovou cestou. Ak ste v programovacom prostredí, môžete získať niekoľko. Budete chcieť hľadať ten, ktorý sa nachádza v prostredí, ktoré práve používate, ale možno budete chcieť pridať modul aj do hlavnej cesty systému Python. To, čo hľadáte, bude podobné tomuto:

Output
'/usr/sammy/my_env/lib/python3.5/site-packages'
Teraz môžete presunúť svoj súbor hello.py do tohto adresára. Po dokončení môžete importovať modul ahoj ako zvyčajne:

import hello
...
Keď spustíte program, mal by sa dokončiť bez chyby.

Úprava cesty k vášmu modulu môže zabezpečiť, že budete mať prístup k modulu bez ohľadu na to, v ktorom adresári sa nachádzate. Je to užitočné najmä vtedy, ak máte viac ako jeden projekt odkazujúci na konkrétny modul.


