# Dátové typy

Každá premenná je určitým dátovým typom. V jazyku Python nie je nutné pri vytváraní premennej deklarovať aj jej typ, ale možné to samozrejme je. Dátové typy je vhodné určiť kvôli tomu, aby sme interpreteru dali vedieť, s akými dátami má pracovať aby nedošlo k chybám. Samozrejme aj nám, sa značne uľahčuje práca a hladanie chýb keď máme presné informácie, vieme s čím pracujeme. 

## Čísla

### Celé čísla (integer, skratka int) 
– dátový typ celých čísel, ktorý teoreticky nemá limit na dĺžku hodnoty (limitom bude vždy systém, v ktorom sa pracuje). Celé čísla môžeme zapisovať v rôznych číselných sústavách: 
#### binárna sústava (dvojková)
– pred čísla dávame predponu 0b (0B) – print(0b15)
bin1 = bin(43)
bin2 = 0b10110110
bin3 = 14
print('bin1 =', bin1, 'bin2 =', bin2, 'bin3 =', bin(bin3)[2:]) # bin1 = 0b101011 bin2 = 182 bin3 = 1110

#### decimálna sústava (desiatková)
– print(15)
dec1 = 18
dec2 = int(67)
print('dec1 =', dec1, 'dec2 =', dec2) # dec1 = 18 dec2 = 67
print(type(dec1)) # <class 'int'>

#### oktálna sústava (osmičková) 
– pred čísla dávame predponu 0o (0O) – print(0o15)
okt1 = 0o24
okt2 = 24
okt3 = oct(10)
print('okt1 =', okt1, 'okt2 =', oct(okt2), 'okt3 =', okt3) # okt1 = 20 okt2 = 0o30 okt3 = 0o12

#### hexadecimálna sústava (šestnástková)
– pred čísla dávame predponu 0x (0X) – print(0x15)
hex1 = 0x142
hex2 = 16
hex3 = hex(32)
print('hex1 =', hex1, 'hex2 =', hex2, 'hex3 =', hex3) # hex1 = 322 hex2 = 16 hex3 = 0x20

### Desatinné čísla (floatI)
– desatinné čísla sa píšu s bodkou
flt1 = 24.8
flt2 = float(18 / 4)
flt3 = 5.476e9
print('flt1 =', flt1, 'flt2 =', flt2, 'flt3 =', flt3) # flt1 = 24.8 flt2 = 4.5 flt3 = 5476000000.0

## Boleánsky typ (boolean)

tento dátový typ môže mať len dve možnosti – True alebo False
používame ich napríklad pri logických operátoroch
pravda = bool(True) # Určenie typu boolean
nepravda = False # Bez určenia typu - fungovať bude ako False
print(type(pravda)) # Vypísanie dátového typu:  <class 'bool'>


### Komplexné čísla  (complex)
– komplexné čísla sa skladajú s reálnej časti a imaginárnej (15j)
cmp1 = 4j
cmp2 = 7 + 4j
cmp3 = cmp1 + cmp2
print('cmp1 =', cmp1, 'cmp2 =', cmp2, 'cmp3 =', cmp3) # cmp1 = 4j cmp2 = (7+4j) cmp3 = (7+8j)

## Reťazce (string)
– určitý rad znakov, príkladom použitia je print("Miesto dvojitých úvodzoviek môžeme použiť jednoduché úvodzovky")

uvodnyText = str("Vitajte na našom webe")
print(type(uvodnyText)) # <class 'str'>

## Zoznam (list)
>Pre určitý zoznam, napríklad mien platí zápis v ktorom sú jednotlivé prvky oddelené čiarkami a uyatvorené v hranatých zátvorkách: 

list = ["Matej", "Gabriel", "Zuzana"]
~~~
list = ["Matej", "Gabriel", "Zuzana"]
print(list)
print(type(list))  
~~~
Ako náhle ich uvedieme v okrúhlych zátvorkách pojde o datový typ tuple. Ten však môžeme konvertovať na zoynam pomocou funkcie list().
~~~
# zapis mien v datovom type tuple
tuple=("Matej", "Gabriel", "Zuzana")
print(tuple)
print(type(tuple))

# prevod tuple na list pomocou funkcie list()
zoznam = list(("Matej", "Gabriel", "Zuzana")) # je potrebne uviest v dvoch okruhlych zatvorkach
print(zoznam)
print(type(zoznam))
~~~

## N-tice (tuple)

>### podobne ako pri reťazcoch, obsahuje znaky resp. sa tu môžu nachádzať aj hodnoty

hrac = ("Apolonius", "44", "14.547", "12", "Farmári")

V našom príklade sa uchovávajú napr. informácie o charaktere v počítačovej hre: meno hráča, úroveň, množstvo peňazí, počet ocenení a trieda 

K zobrazeniu uložených informáci pristupujeme pomocou príkazu print(tuple[0]) a zadan=im indexu v hranatých zátvorkách. V tomto prípade sa vypíše len meno hráča nakoľko indexovanie začína od 0.
~~~
hrac = ("Apolonius", "44", "14.547", "12", "Farmári")
print(hrac[0]) # Vypíšeme meno hráča, ktoré sa nachádza na pozícií 0
print(type(hrac)) # <class 'tuple'>
~~~

## Sety (set)

>### zbierka podobná ako zoznam, len bez poradia alebo indexovania

set = {"Nemocnica", "Škola", "Polícia", "74.14"}

Výpis množiny vykonáme príkazom print(set) kedy v každom novom behu programu sa zobrazí zoznam prvkoov v inom poradí.
~~~
set = {"Nemocnica", "Škola", "Polícia", "74.14"} # Vytvorenie setu bez určenia typu
print(set) # Zobrazenie stále v inom poradí
print(type(set)) # <class 'set'>
~~~
## Slovník (dictionary)

>#### slovník je podobný n-ticiam, len v tomto prípade sa označuje, ktorá hodnota čo znamená
ziaci= {"Adam": "12", "Adela": "11", "Martin": "12"}

V tomto príklade sme menu priradili hodnotu veku. 

K jednotlivým dátam môžeme napr. pristúpiť pomocou funkcie get a pokiaľ by sme ho chceli zobraziť použijeme konštrukciu print(ziaci.get("Adela")). V tomto prípade sa vypíše vek Adely = 11
~~~
ziaci= {"Adam": "12", "Adela": "11", "Martin": "12"} # Vytvorenie slovníka bez priradenia typu 
print(ziaci.get("Adela")) # Zobrazí vek Adely
print(type(ziaci)) # <class 'dict'>
~~~