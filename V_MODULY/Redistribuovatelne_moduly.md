Vytvorenie redistribuovatelnych modulov
https://naucse.python.cz/lessons/intro/distribution/

Instalacia modulov
https://mamut.spseol.cz/nozka/python/moduly/

>### Časté otázky o moduloch Python
Pozrime sa na niektoré často kladené otázky týkajúce sa modulov Pythonu.

Aké sú vstavané moduly v Pythone?
V Pythone je veľa vstavaných modulov. Niektoré z dôležitých sú - čas. Môžete spustiť príkaz help(modules) v prostredí Pythonu, aby ste získali zoznam dostupných modulov.

Aký je rozdiel medzi modulom a balíkom - knižnicou v Pythone?

Balík Python je zbierka modulov pythonu. Modul Python je jeden súbor python, zatiaľ čo balík python je adresár s viacerými skriptami pythonu a súborom __init__.py definujúcim podrobnosti balíka.

Kde nájdem zoznam modulov Pythonu?
Zoznam modulov Python nájdete na ich oficiálnej stránke indexu modulov Python. Ak však hľadáte moduly Pythonu, ktoré máte k dispozícii, môžete spustiť príkaz help(modules) v prostredí Pythonu, aby ste získali zoznam dostupných modulov.

Kde nájdem zoznam balíkov - knižníc Pythonu?

Skontrolujte toto úložisko GitHub, kde nájdete zoznam najdôležitejších modulov pythonu a naučte sa ich prostredníctvom ich špecifických návodov a vzorových programov.

Ako môžem importovať modul z iného adresára?
Keď sa pokúšame importovať modul python, pozrie sa do aktuálneho adresára a umiestnenia premennej PATH. Ak sa teda váš python súbor nenachádza v týchto umiestneniach, dostanete ModuleNotFoundError. Riešením je importovať modul sys a potom pridať požadovaný adresár do jeho premennej cesty. Nižšie uvedený kód zobrazuje chybu, keď sa pokúšame importovať z iného adresára a ako to opravujem pridaním jeho adresára do premennej cesty.

$ python3.7
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import test123
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'test123'
>>> import sys
>>> sys.path.append('/Users/pankaj/temp')
>>> import test123
>>> test123.x
10
>>> test123.foo()
foo
>>> 

>### Zoznam modulov Pythonu
Existujú tisíce modulov Pythonu a každý deň sa vyvíjajú ďalšie. Napísali sme návody pre veľa populárnych modulov Pythonu. Ak sa chcete naučiť tieto moduly, postupujte podľa odkazov v tabuľke nižšie.

Python Modules
Python os module
Python sys module
Python time
Python MySQL
Python CSV
Python multiprocessing
Python pickle
Python time sleep
Python queue
Python unittest
Python socket
Python SimpleHTTPServer
Python json
Python signal
Python random
Python System Command
Python Daemon Thread
Python Copy
Python threading module
Python struct
Python logging
Python subprocess
Python argparse
Python functools
Python itertools
Python getopt
Python ftp
Python tarfile
Python lxml
Python ConfigParser
Python datetime
Python decimal module
Python collections
Python zipfile
Python pdb
Python io
Python fractions
Python AST
Python HTTP
Python xmltodict
Python gzip
Python HTML Parser
Python inspect module
Python Send Email
Python tempfile
Python SQLite
Python shutil
Python timeit
Python getpass module
Python urllib
Python pytz
Python pendulum
Python arrow module
Referencie:

https://docs.python.org/3/tutorial/modules.html
https://docs.python.org/3/py-modindex.html

