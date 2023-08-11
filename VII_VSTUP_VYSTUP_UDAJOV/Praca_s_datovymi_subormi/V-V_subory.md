>## Vstup a výstup údajov cez súbory

Okrem príkazov vstupu z klávesnice input() a výstupu na obrazovku print() Python poskytuje aj vstavané funkcie ktoré slúžia na vytváranie, písanie a čítanie súborov t.j. vstup a výstup z a do súborov. Súbory patria k základným typom dát jazyka Python. Súbory predstavujú prepojovacie rozhranie medzi kódom a pomenovanými oblasťami počítačovej pamäte. Súbory vykonávajú funkciu "zachovania" objektov. Umožňujú vám uložiť akékoľvek informácie s následným vyložením a spracovaním. Tu sa budeme zaoberať tým ako v Pythone nahrať súbor a spätne ho po spracovaní úložiť. Existujú dva typy súborov, s ktorými je v pythone možné pracovať, normálne textové súbory a binárne súbory. 
* **Textové súbory**: V tomto type súboru je každý riadok textu ukončený špeciálnym znakom nazývaným EOL (End of Line), čo je predvolene nový znak riadku ('\n') v pythone.
* **Binárne súbory**: V tomto type súboru neexistuje terminátor pre riadok a údaje sa ukladajú po ich konverzii do strojovo zrozumiteľného binárneho kódu.

### Režim prístupu
Režimy prístupu určujú typ operácií, ktoré sú možné vykonať na príslušnom súbore. Hovoria o tom, ako sa bude súbor používať po jeho otvorení. Tieto režimy tiež definujú ako budeme narábať s príslušným súborom :
1. **Read Only ('r')** : Otvorí textový súbor na čítanie. Ukazovateľ je umiestnená na začiatku súboru. Ak súbor neexistuje, vyvolá chybu I/O. Toto je tiež predvolený režim, v ktorom sa súbor otvára.
2. **Read and Write ('r+')** : Otvorenie súboru na čítanie a zápis. Ukazovateľ je umiestnená na začiatku súboru. Vyvolá chybu I/O, ak súbor neexistuje.
3. **Write Only ('w')** : Otvorenie súboru na zápis. Pre existujúci súbor sú údaje skrátené a prepísané. Označenie je umiestnená na začiatku súboru. Vytvorí súbor, ak súbor neexistuje.
4. **Write and Read ('w+')** : Otvorenie súboru na čítanie a zápis. Pre existujúci súbor sú údaje skrátené a prepísané. Označenie je umiestnená na začiatku súboru.
5. **Append Only ('a')** : Otvorenie súboru na zápis. Súbor sa vytvorí, ak neexistuje. Označenie je umiestnená na konci súboru. Zapisované dáta budú vložené na koniec, za existujúce dáta.
6. **Append and Read ('a+')** : Otvorenie súboru na čítanie a zápis. Súbor sa vytvorí, ak neexistuje. Rukoväť je umiestnená na konci pilníka. Zapisované dáta budú vložené na koniec, za existujúce dáta.

### Otvorenie súboru
Sa vykonáva pomocou funkcie **open()**. Pre túto funkciu nie je potrebné importovať žiadny modul. Daný súbor by sa mal nachádzať v rovnakom adresári kde je program ktorý ju používa alebo by mala byť pri súbore zadaná úplná cesta. 
~~~
File_object = open(r"...\full\adress\File_Name.txt","Access_Mode")
~~~
**Poznámka:** R sa umiestni pred názov súboru, aby sa zabránilo tomu, že znaky v reťazci názvu súboru budú považované za špeciálne znaky. Napríklad, ak je v adrese súboru \temp, potom sa \t považuje za znak tabulátora a zobrazí sa chyba neplatnej adresy. R robí reťazec surovým, to znamená, že hovorí, že reťazec neobsahuje žiadne špeciálne znaky. Za týmto účelom je možné použivať ako oddelovač adresárov aj dvojité lomítka \\
~~~
# Open function to open the file "LICENSE.txt"
# (same directory) in read mode and
                     
file1 = open("LICENSE.txt", "w")

# store its reference in the variable file1
# and "SW_licencia.txt" in C:\Users\tomast\Documents\sss-trencin\Vyuka\Aplikovana_Informatika\VIII_PRÁCA_SO_SÚBORMI in file2
                     
file2 = open(r"D:\Text\SW_licencia.txt", "w+")
~~~
#### Zatvorenie súboru
Funkcia close() zatvorí súbor a uvoľní pamäťové miesto získané týmto súborom. Používa sa v čase, keď súbor už nie je potrebný alebo ak sa má otvoriť v inom režime súboru.
~~~
File_object.close()
~~~
#### Zápis do súboru
Existujú dva spôsoby zápisu do súboru.

1. **write()** : Vloží reťazec str1 do jedného riadku v textovom súbore.
~~~
File_object.write(str1)
~~~
2. **writelines()** : Pre zoznam prvkov reťazca je každý reťazec vložený do textového súboru. Používa sa na vloženie viacerých reťazcov naraz.
~~~
File_object.writelines(L) pre L = [str1, str2, str3]
~~~
~~~
# Python program to demonstrate
# writing to file
                     
# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
                     
# Writing a string to file
file1.write(s)
                     
# Writing multiple strings
# at a time
                     
file1.writelines(L)
                     
# Closing file
file1.close()
                     
# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
                     
file1.close()
~~~
**Poznámka:** '\n' sa považuje za špeciálny znak pozostávajúci z dvoch bajtov. 

#### Zatvorenie súboru
Funkcia close() zatvorí súbor a uvoľní pamäťové miesto získané týmto súborom. Používa sa v čase, keď súbor už nie je potrebný alebo ak sa má otvoriť v inom režime súboru.
~~~
File_object.close()
~~~

##### Pridanie ďalších údajov k súboru
Keď je súbor otvorený v režime pridania ďalších údajov, ukazovateľ je umiestnený na konci súboru. Zapisované dáta budú vložené na koniec, za existujúce dáta. Pozrime sa na nižšie uvedený príklad, aby sme objasnili rozdiel medzi režimom zápisu a režimom pripojenia.
~~~
# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a") # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w") # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()
~~~
#### Použitie príkazu with
príkaz **with** sa v Pythone používa na to aby bol kód čistejší a oveľa čitateľnejší. Zjednodušuje správu používaných súborov. Na rozdiel od vyššie uvedených implementácií nie je potrebné volať file.close() Samotný príkaz with zabezpečuje správny prístup k zdrojom a ich uvoľnenie. Jeho syntax je :
~~~
with open filename as file:
~~~
~~~
# Program to show various ways to
# write data to a file using with statement
                     
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
                     
# Writing to file
with open("myfile.txt", "w") as file1:
                     
# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
                     
# Reading from file
with open("myfile.txt", "r+") as file1:
                     
# Reading form a file
print(file1.read())
~~~

#### Použitie príkazu for
Ak chcete zapisovať do súboru v Pythone pomocou príkazu for, môžete postupovať podľa týchto krokov:
1. Otvorte súbor pomocou funkcie open() s príslušným režimom ('w' pre zápis).
2. Príkaz for použite na zacyklenie údajov, ktoré chcete zapísať do súboru.
3. Na zápis údajov do súboru použite metódu write() objektu súboru.
4. Zatvorte súbor pomocou metódy close() objektu súboru.

V tomto príklade je súbor otvorený na zápis pomocou príkazu with open('file.txt', 'w') ako f. Dáta, ktoré sa majú zapísať, sú uložené v zozname nazývanom dáta. Príkaz for sa používa na zacyklenie každého riadku údajov v zozname. Príkaz f.write(riadok + '\n') zapíše každý riadok údajov do súboru so znakom nového riadku (\n) na konci. Nakoniec sa súbor automaticky zatvorí, keď sa skončí blok with.
~~~
# Open the file for writing
with open('file.txt', 'w') as f:
	# Define the data to be written
	data = ['This is the first line', 'This is the second line', 'This is the third line']
	# Use a for loop to write each line of data to the file
	for line in data:
		f.write(line + '\n')
		# Optionally, print the data as it is written to the file
		print(line)
# The file is automatically closed when the 'with' block ends
~~~
Náš kód otvorí súbor s názvom file.txt v režime zápisu pomocou bloku with, aby sa zabezpečilo aj správne zatvorenie súboru, keď sa blok skončí. Definuje zoznam reťazcov nazývaných data, ktoré predstavujú riadky, ktoré sa majú zapísať do súboru. Kód potom používa cyklus for na iteráciu cez každý reťazec v údajoch a zapisuje každý reťazec do súboru pomocou metódy write(). Kód ďalej pripojí ku každému reťazcu znaky nového riadku (0Dh-CR a 0A-LF), aby sa zabezpečilo, že každý reťazec bude napísaný na novom riadku v súbore. Kód voliteľne vytlačí každý reťazec pri zápise do súboru.

Samozrejme python poskytuje nástroje a knižnice ktoré nám umožňujú pracovať aj s často používanými súbormi ako  [csv](https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/), súbormi [exelu](https://www.geeksforgeeks.org/python-writing-excel-file-using-openpyxl-module/), [wordu](https://theautomatic.net/2019/10/14/how-to-read-word-documents-with-python/), [xml](https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/), [json](https://www.geeksforgeeks.org/python-reading-ini-configuration-files/), [ini](https://www.geeksforgeeks.org/python-reading-ini-configuration-files/), [rpt](https://www.geeksforgeeks.org/reading-rpt-files-with-pandas/) atď.

My sa na tomto mieste nebudeme zaoberať všetkými typmi údajov a našu pozornosť budeme venovať iba importu a exportu najbežnejšieho formátu pre tabuľky a databázy ktorým je formát **CSV (Comma Separated Values)** Je to jedna z najbežnejších metód výmeny údajov medzi aplikáciami a populárny formát údajov používaný v Data Science. Ďalším dôvodom prečo sa ním budeme zaoberať je to že ho podporuje široká škála aplikácií. Súbor CSV ukladá tabuľkové údaje, v ktorých je každé údajové pole oddelené oddeľovačom ( vo väčšine prípadov čiarkou). Aby reprezentoval súbor CSV, musí byť uložený s príponou .csv

#### Čítanie zo súboru CSV
Python obsahuje **modul csv** na prácu so súbormi CSV. Najprv sa CSV súbor otvorí pomocou metódy open() v režime „r“ (určuje režim čítania pri otváraní súboru), ktorá vráti daný csv súbor ako objekt. Tento sa potom  načíta pomocou ďalšej metódy CSV modulu reader(), ktorá ako objekt vráti výsledok načítania. Čítanie sa uskutočňuje iteráciou cez jednotlivé riadky v zadanom CSV dokumente. Syntax príkazu je :
~~~
csv.reader(csvfile, dialect='excel', **fmtparams)
~~~
**Poznámka:** metóda open() sa používa spolu s kľúčovým slovom „with“.
~~~
# file_csv_read.py
import csv

# opening the CSV file
with open(r'C:\Users\tomast\Documents\sss-trencin\Vyuka\Aplikovana_Informatika\VII_VSTUP_VÝSTUP_ÚDAJOV\Praca_s_datovymi_subormi\Giants03.csv', mode='r') as file:
                    
# reading the CSV file
    csvFile = csv.reader(file)
                    
# displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
~~~
#### Zapisovanie údajov zoznamu do CSV súboru

Na vkladanie údajov do súboru CSV sa používa trieda csv.writer. Táto trieda vracia objekt zápisu, ktorý je zodpovedný za konverziu údajov od užívateľa na čiarkami oddelený reťazec. Objekt súboru CSV by sa mal otvoriť s formátovacím parametrom (fmtparams)newline = ' ' lebo inak sa znaky nového riadku zo zoznamu (poľa) ktoré sú v úvodzovkách nebudú správne interpretovať. Syntax príkazu je:
~~~
csv.writer(csvfile, dialekt='excel', **fmtparams)
~~~
Trieda csv.writer poskytuje dve metódy zápisu do CSV. Sú writerow() a writerows().
* **writerow()**: ktorá zapisuje naraz len jeden riadok. Pomocou tejto metódy je možné zapísať jeden riadok poľa (zoznamu).
~~~
Syntax: writerow(zoznam)
~~~
* **writeows()**: Táto metóda sa používa na zapisovanie viacerých riadkov naraz. Toto je možné použiť na písanie viacerých riadkov zoznamu naraz.
~~~
Syntax: writerows(riadky zoznamu)
~~~
~~~
# file_csv_write.py

# Python program to demonstrate
# writing to CSV

import csv

# field names
header = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
data = [
    ['Nikhil', 'COE', '2', '9.0'],

    ['Sanchit', 'COE', '2', '9.1'],

    ['Aditya', 'IT', '2', '9.3'],

    ['Sagar', 'SE', '1', '9.5'],

    ['Prateek', 'MCE', '3', '7.8'],

    ['Sahil', 'EP', '2', '9.1']
]

# meno csv suboru
filename = "countries.csv"

# zapis do csv suboru
with open(filename, 'w', encoding='UTF8', newline='') as csvfail:

	# vytvorenie obektu pre zapis do csv
    writer = csv.writer(csvfail)

    # zapis jedneho riadku - hlavicky csv suboru (nazvy poli v csv)
    writer.writerow(header)

    # zapis jednotlivych riadkov s udajmi
    writer.writerows(data)
~~~

#### Zapisovanie údajov slovníka do CSV súboru
Do CSV súboru môžeme zapísať aj údaje slovníka. Na tento účel poskytuje modul CSV triedu **csv.DictWriter**. Táto trieda vracia objekt Writer, ktorý mapuje slovníky na výstupné riadky.
~~~
Syntax: csv.DictWriter(csvfile, fieldnames, restval=”, extrasaction='raise', dialekt='excel', *args, **kwds)
~~~
csv.DictWriter poskytuje dve metódy zápisu do CSV. Sú to:

* **writeheader()**: táto metóda zapíše prvý riadok vášho súboru csv pomocou vopred špecifikovaných názvov polí.
~~~
Syntax: writeheader()
~~~
* **writerows()**: táto metóda zapíše všetky riadky, ale v každom riadku zapíše iba hodnoty (nie kľúče).
~~~
Syntax: writerows(moj_slovnik)