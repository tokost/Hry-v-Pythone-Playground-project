># Grafy

Táto časť sa zaoberá grafmi v pythone pomocou knižnice **Matplotlib** , čo je pravdepodobne najobľúbenejšia knižnica pre grafy a vizualizáciu údajov v Pythone. Pokiaľ túto knižnicu nemáme naištalovanú, je potrebné tento úkon vykonať. Najjednoduchší spôsob, ako nainštalovať matplotlib, je použiť príkaz pip tým že do terminálu zadáme nasledujúci príkaz: 

#### pip install matplotlib

### Vykreslenie jednej krivky
Pre začiatok si pomocou tejto knižnice vykreslíme lomenú čiaru:
~~~
# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/lomena_ciara.png)

Kód by mal byť zrejmý nakoľko boli vykonané nasledujúce kroky: 

* Definujte hodnoty osi x a zodpovedajúcej osi y ako zoznamy.
* Nakreslite ich na plátno pomocou funkcie .plot() .
* Pomenujte os x a os y pomocou funkcií .xlabel() a .ylabel() .
* Pomenujte svoj pozemok pomocou funkcie .title() .
* Nakoniec na zobrazenie grafu použijeme funkciu .show() .

### Vykreslenie dvoch alebo viacerých čiar na spolo+cnej ploche
~~~
import matplotlib.pyplot as plt

# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/dve_ciary.png)

* Tu nakreslíme dve čiary na ten istý graf. Rozlišujeme ich tak, že im dáme meno ( label ), ktoré sa odovzdáva ako argument funkcie .plot().
* Malý obdĺžnikový rámček s informáciami o type čiary a jej farbe sa nazýva legenda.

### Prispôsobenie podložiek
Tu diskutujeme o podklade do ktorého vykreslujeme grafy a niektorých základných spôsoboch ako ich prispôsobiť.
~~~
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Some cool customizations!')

# function to show the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/prisposobenie_podlozky.png)
Ako môžete vidieť, urobili sme niekoľko prispôsobení, ako napr 

* nastavenie šírky čiary, štýlu čiary, farby čiary.
* * nastavenie fixky, farba tváre fixky, veľkosť fixky.
prepísanie rozsahu osí x a y. Ak sa prepísanie neuskutoční, modul pyplot použije funkciu automatickej mierky na nastavenie rozsahu osi a mierky.

### Stĺpcový graf
~~~
import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

# heights of bars
height = [10, 24, 36, 40, 5]

# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
		width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/stlpcovy_graf.png)
* Tu používame funkciu plt.bar() na vykreslenie stĺpcového grafu.
* x-ové súradnice ľavej strany tyčí sa prenesú spolu s výškami tyčí.
* môžete tiež pomenovať súradnice osi x definovaním tick_labels

### Histogram

~~~
import matplotlib.pyplot as plt

# frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44,
		60,7,13,57,18,90,77,32,21,20,40]

# setting the ranges and no. of intervals
range = (0, 100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, range, color = 'green',
		histtype = 'bar', rwidth = 0.8)

# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')

# function to show the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/histogram.png)

* Tu použijeme funkciu plt.hist() na vykreslenie histogramu.
* frekvencie sú odovzdané ako vekový zoznam.
* Rozsah je možné nastaviť definovaním n-tice obsahujúcej minimálne a maximálne hodnoty.
* Ďalším krokom je „ bin “ rozsah hodnôt – to znamená rozdelenie celého rozsahu hodnôt do série intervalov – a potom spočítať, koľko hodnôt spadá do každého intervalu. Tu máme definovaných zásobníkov = 10. Celkovo je teda 100/10 = 10 intervalov.

### Bodový diagram
~~~
import matplotlib.pyplot as plt

# x-axis values
x = [1,2,3,4,5,6,7,8,9,10]
# y-axis values
y = [2,4,5,7,6,8,9,11,12,12]

# plotting points as a scatter plot
plt.scatter(x, y, label= "stars", color= "green",
			marker= "*", s=30)

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/bodovy_diagram.png)

* Tu používame funkciu plt.scatter() na vykreslenie bodového grafu.
* Ako čiaru definujeme x a príslušné hodnoty osi y aj tu.
* argument marker sa používa na nastavenie znaku, ktorý sa má použiť ako značka. Jeho veľkosť je možné definovať pomocou parametra s .

### Koláčový graf
~~~
import matplotlib.pyplot as plt

# defining labels
activities = ['eat', 'sleep', 'work', 'play']

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
		startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
		radius = 1.2, autopct = '%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/kolacovy_graf.png)

* Tu vykreslíme koláčový graf pomocou metódy plt.pie() .
* Najprv definujeme označenia pomocou zoznamu s názvom činnosti .
* Potom môže byť časť každého označenia definovaná pomocou iného zoznamu nazývaného rezy .
* Farba pre každý štítok je definovaná pomocou zoznamu s názvom farby .
* shadow = True zobrazí tieň pod každým štítkom v koláčovom grafe.
* počiatočný uhol otáča začiatok koláčového grafu o dané stupne proti smeru hodinových ručičiek od osi x.
* explode sa používa na nastavenie časti polomeru, s ktorým odsadíme každý klin.
* autopct sa používa na formátovanie hodnoty každého štítku. Tu sme nastavili zobrazovanie percentuálnej hodnoty len na 1 desatinné miesto.

Ďalšie variaty statických grafov od jednoduchších až k priestorovým pri ktorých je použitá knižnica **matpotlib** nájdeme v [**tomto**](https://coobas.gitlab.io/python-fjfi/en/posts/matplotlib.html) príspevku. Skôr však než túto knižnicu použijeme, treba ju mať nainštalovanú. To urobíme napr. v git shell-y príkazom pip install matplotlib.

### Vykreslenie kriviek danej rovnice
~~~
# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# setting the x - coordinates
x = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)

# plotting the points
plt.plot(x, y)

# function to show the plot
plt.show()
~~~
![](./Grafy_Obrazky_Video_Audio/graf_rovnice.png)

Tu používame **NumPy** , čo je univerzálna knižnica na spracovanie poľa v pythone. 
 
* Na nastavenie hodnôt osi x používame metódu np.arange() , v ktorej prvé dva argumenty sú pre rozsah a tretí pre krokové zvyšovanie. Výsledkom je pole NumPy.
* Aby sme získali zodpovedajúce hodnoty osi y, jednoducho použijeme preddefinovanú metódu np.sin() v poli NumPy.
* Nakoniec body vykreslíme tak, že do funkcie plt.plot() odovzdáme polia x a y .

V tejto časti sme sa zaoberovali rôznymi typmi grafov, ktoré môžeme vytvoriť pomocou knižnice matplotlib. Treba spomenúť že ešte existuje viac druhov grafov ako napr.viacnásobné, 2D, 3D a pod., ktoré sme nespomínali. Tie najvýznamnejšie sú diskutované [tu](https://www.geeksforgeeks.org/graph-plotting-python-set-2/) a [tu](https://www.geeksforgeeks.org/graph-plotting-python-set-3/)



V prípade že potrebujeme vytvoriť graf pomocou štatistických údajov, je na to určená knižnica [Seaborn](https://www.geeksforgeeks.org/plotting-graph-using-seaborn-python/), čo je najpopulárnejšia štatistická vizualizačná knižnica v Pythone.

Niekedy a to najmä pri prezentáciach je žiadaná interaktívna vizualizácia údajov v jazyku Python. Na to nám slúži knižnica [Bokeh](https://www.geeksforgeeks.org/python-bokeh-plotting-a-line-graph/) ktorá svoje výstupy zobrazuje pomocou internetového prehliadača. Ďalšie príklady s vykreslením rôznych objektov nájdeme tu: [1](https://www.geeksforgeeks.org/python-bokeh-plotting-ellipses-on-a-graph/), [2](https://www.geeksforgeeks.org/python-bokeh-plotting-dots-on-a-graph/), [3](https://www.geeksforgeeks.org/python-bokeh-plotting-diamond-dots-on-a-graph/, [4](https://www.geeksforgeeks.org/python-bokeh-plotting-diamond-crosses-on-a-graph/), [5](https://www.geeksforgeeks.org/python-bokeh-plotting-diamonds-on-a-graph/

># Grafika
V súvislosti s kresliacimi funkciami pre grafiku spomenieme dva základné produkty.Tým prvým je **turtle** ktorý využíva rovnomennú knižnicu a poskytuje Pythonu kresliacu plochu a funkcie ktoré nám umožnujú po nej kresliť. Môžeme použiť funkcie ako turtle.forward(…) a turtle.right(…), ktoré môžu korytnačku pohybovať. Bežne používané metódy korytnačiek sú:

| Metóda     |Parameter|    Popis
|------------|-----------|------------------------------------|
| Turtle()   | žiadne | Vytvorí a vráti nový objekt korytnačky
| forward()  | hodnota| Posunie korytnačku dopredu o zadanú hodnotu
| backward() | hodnota| Posunie korytnačku dozadu o zadanú hodnotu
| right()    | uhol   |Otočí korytnačku v smere hodinových ručičiek
| left()     | uhol   |Otočí korytnačku proti smeru hodinových ručičiek
| penup()    | žiadne |Zdvihne pero korytnačky
| pendown()  | žiadne |Položí pero korytnačky
| up()       | žiadne |Zdvihne pero korytnačky
| down()     | žiadne |Položí pero korytnačky
| color()    |názov farby|Zmení farbu pera korytnačky
|fillcolor() |názov farby|Zmení farbu, ktorú korytnačka použije na vyplnenie
| heading()  | žiadne |Vráti aktuálny nadpis
| position() | žiadne |Vráti aktuálnu polohu
| goto()     |  x, y  |Presuňte korytnačku do polohy x,y
|begin_fill()| žiadne |Zapamätajte si počiatočný bod vyplneného mnohouholn=ika
| end_fill() | žiadne |Zatvorte mnohouholník a vyplňte ho aktuálnou farbou výplne
| dot()      | žiadne |Nechajte bodku na aktuálnej pozícii
| stamp()    | žiadne |Zanecháva dojem tvaru korytnačky na aktuálnom miest
| shape()    |názov tvaru|Mala by byť „šípka“, „klasický“, „korytnačka“ alebo „kruh“

Všetky funkcie turtle nájdeme [tu](https://docs.python.org/3/library/turtle.html)

Kreslenie pomocou korytnačky

Aby sme mohli využívať metódy a funkcie korytnačiek, musíme importovať korytnačku.“turtle“ sa dodáva so štandardným balíkom Python a nemusí sa inštalovať externe. Postup na spustenie programu korytnačky pozostáva zo 4 krokov:  

1. Importujte sa modul korytnačky
2. Vytvorí sa korytnačka na ovládanie.
3. Nakreslí sa pracovná plocha na kreslenie pomocou metód korytnačky.
4. Spustí sa turtle.done().

Po importovaní všetkých funkcii turtle niektorým z príkazov
~~~
from turtle import *
# or
import turtle
~~~
musíme vytvoriť novú kresliacu plochu (okno) a korytnačku. Okno nazvime ako wn a korytnačku ako skk. Takže kódujeme ako: 
~~~
wn = korytnačka.Screen()
wn.bgcolor("svetlozelena")
wn.title("korytnačka")
skk = korytnačka.Turtle()
~~~
Keď už máme vytvorené okno a korytnačku, môžeme korytnačku posúvať. Ak by sme sa posunuli o 100 pixelov vpred v smere skk, napíšeme príkaz: 
~~~
skk.forward(100)
~~~
Následne dokončíme program funkciou
~~~ 
turtle.done() 
~~~
a máme hotovo! vytvorili program, ktorý nakreslí čiaru dlhú 100 pixelov. Pomocou korytnačích metód môžeme nakresliť rôzne tvary a vyplniť rôzne farby. Existuje množstvo funkcií a programov, ktoré je možné kódovať pomocou knižnice korytnačiek v pythone.

## Tkinter

Program ktorý pracuje s grafickým oknom (v grafickom režime) vieme vytvoriť aj pomocou knižnice **Tkinter**. Ako uvidíme neskôr táto knižnica sa často používa aj na vykreslovanie grafického rozhrania pre vstup a výstup údajov (GUI - Graphical User Interface). 

Grafické okno sa tu ale nevytvorí samo. Preto musíme na začiatku zadať špeciálne príkazy ktoré ho vytvoria:
~~~
import tkinter      # vytvorí premennú tkinter, pomocou 
                    # ktorej budeme mať prístup (bodkovou # notáciou) k funkciám v module

canvas = tkinter.Canvas()   # vytvorí plátno grafickej aplikácie
                            # - priradili sme ho do premennej 
                            # canvas (mohlo sa to volať hocijako # inak, ale takto budeme lepšie 
                            # rozumieť aj cudzím programom)
canvas.pack()       #  umiestni naše plátno do grafickej 
                    # aplikácie (do okna) - teraz je plátno 
                    # pripravené, aby sme do neho mohli kresliť

canvas.mainloop()   # grafická aplikácia vďaka tomuto príkazu v
                    # operačnom systéme naozaj „žije“, t.j. 
                    # reaguje na klikanie, presúvanie, zmenu 
                    # veľkosti, prekresľovanie, …
~~~
Zoznam metod wignetov v Tkinter:
https://www.plus2net.com/python/tkinter.php

Keď takto vytvorený program spustíme (z editora klávesom F5), otvorí sa nové okno so šedou prázdnou plochou.

Ako to funguje ?

1. príkaz import tkinter oznámi, že budeme pracovať s modulom tkinter, ktorý obsahuje všetky grafické príkazy
    * týmto príkazom vznikla nová premenná tkinter, ktorá obsahuje referenciu na tento modul, t.j. všetky funkcie a premenné, ktoré sú definované v tomto module, sú prístupné pomocou tejto premennej a preto k nim budeme pristupovať tzv. bodkovou notáciou, t.j. vždy uvedieme meno premennej tkinter, za tým bodku a meno funkcie alebo premennej, napr. tkinter.Canvas
2. práve zápis tkinter.Canvas() vytvorí grafickú plochu a aby sme s touto plochou mohli ďalej pracovať, uložíme si jej referenciu do premennej canvas (mohli by sme ju nazvať napríklad aj plocha alebo jednoducho g)
    * nezabudnite uviesť okrúhle zátvorky: vďaka nim sa zavolá funkcia, ktorá vytvorí nové okno, bez týchto zátvoriek zápis tkinter.Canvas označuje len referenciu na nejakú funkciu bez jej zavolania
3. kým nezadáme aj príkaz canvas.pack(), grafická plocha sa ešte nezobrazí - volanie canvas.pack() zabezpečí zobrazenie nového okna aj s novovytvorenou grafickou plochou
    * opäť nesmieme zabudnúť zapísať aj okrúhle zátvorky, lebo inak sa grafická plocha nezobrazí (len prázdne grafické okno)

Základné funkcie Tkinter v Pythone:
https://www.educative.io/answers/what-are-the-basic-functions-of-tkinter-in-python 

Ttorial Tkinter:
https://www.pythontutorial.net/tkinter/


Všetky potrebné informácie vrátane funkcii ktoré tkinter ponúka nájdeme v nasledovných materiáloch:
* [tkinter— Rozhranie Pythonu pre Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
* [Grafické používateľské rozhranie s Tk](https://docs.python.org/3/library/tk.html)

Všetky grafické príkazy pracujú s grafickou plochou, ku ktorej máme prístup prostredníctvom premennej canvas. Tieto príkazy sú v skutočnosti funkciami, ktoré budeme volať s nejakými parametrami. Všeobecný tvar väčšiny grafických príkazov je:
~~~
canvas.create_utvar(x, y, x, y, ..., param=hodnota, param=hodnota, ...)
~~~
kde
* bodka za premennou canvas označuje bodkovú notáciu, teda to že budeme pracovať s funkciou, ktorá sa nachádza v (resp. patrí k) plátnu canvas
* create_utvar je meno funkcie na vytvorenie grafického objektu, napr. create_line (nakreslí úsečku), create_rectangle (nakreslí obdĺžnik), create_oval (nakreslí elipsu), create_polygon (nakreslí polynóm), create_image (vloží obrázok (grafický súbor))…
* parametre príkazov začínajú postupnosťou súradníc bodov (dvojíc x a y) na pracovnej ploche , za ktorými môžu nasledovať pomenované parametre. Rôzne príkazy vyžadujú rôzny počet zadaných bodov v rovine.
* param=hodnota je dvojica: meno doplnkového parametra (napr. fill, width, …) a jej hodnota (napr. 'red', 5, 'Arial 20', …) - väčšinou takto zadávame farbu útvaru, hrúbku kreslenej čiary a pod.
    * všimnite si, že pri zadávaní doplnkových parametrov nedávame medzeru ani pred ani za znak rovnosti.

### Súradnicová sústava
Je oproti súradnicovej sústave, ktorú poznáme z matematiky, trochu pozmenená:
* x-ová os prechádza po hornej hrane plátna grafickej plochy zľava doprava
* y-ová os prechádza po ľavej hrane plátna zhora nadol
* počiatok (0, 0) je v ľavom hornom rohu plátna
* môžeme používať aj záporné súradnice, vtedy označujeme bod, ktorý je mimo grafickú plochu

Tak, ako sme vytvorili plátno pomocou tkinter.Canvas(), jej rozmery sú 379x265 pixelov, preto pravý dolný roh má súradnice (378, 264).

![](./Grafy_Obrazky_Video_Audio/suradnicovy_system.png)
Suradnicový systém s ktorým pracuje Tkinter
[Manipulacia so suradnicami](https://www.plus2net.com/python/tkinter-place.php)

Pre všetky grafické príkazy platí, že keď vynecháme nejaké doplnkové parametre, tak tieto budú mať nastavené svoje inicializované (náhradné, default) hodnoty (často takýmito náhradnými hodnotami sú napr. fill='black' alebo width=1) Veľkosť grafickej plochy je zatiaľ 378x264 bodov (pixelov), ale neskôr uvidíme, ako jednoducho môžeme túto veľkosť zmeniť.

### Kreslenie základných grafických útvarov

#### Úsečky a lomené čiary

Základný formát príkazu:
~~~
canvas.create_line(x1, y1, x2, y2, ...)
~~~
Príkaz musí dostať aspoň dve dvojice súradníc. Grafický objekt potom postupne pospája všetky tieto body a vytvorí jednu lomenú čiaru. Napr.
~~~
canvas.create_line(100, 50, 30, 150)
~~~
nakreslí jednu úsečku s koncovými vrcholmi (100, 50), (30, 150). Ak do príkazu uvedieme viac bodov, napr.
~~~
canvas.create_line(100, 50, 30, 150, 160, 120, 180, 40)
~~~
nakreslí sa lomená čiara (4 vrcholy, čo sú 3 úsečky):

_images/03_18.png

Skúsme túto istú lomenú čiaru zapísať trochu inak. Najprv pomenujme jednotlivé vrcholy a zapíšme:
~~~
a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
~~~
Z matematiky by sme mohli týmto zápisom rozumieť tak, že napr. a je vrchol, ktorého súradnice sú (100, 500). Naozaj to v Pythone funguje a premenná a naozaj obsahuje dvojicu čísel. Čo je ešte lepšie, že takto označené vrcholy (premenné a, b, …) môžeme použiť pri kreslení lomenej čiary:
~~~
canvas.create_line(a, b, c, d)
~~~
Čo je ešte zaujímavejšie, takéto dvojice môžeme použiť napr. aj vo for-cykle. Zakreslime do každého vrcholu tejto krivky červený znak plus:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_line(a, b, c, d)

for bod in a, b, c, d:
    canvas.create_text(bod, text='+', fill='red')
canvas.mainloop()
~~~
A vidíme, že takéto dvojice naozaj fungujú ako vymenované hodnoty pre for-cyklus. Premenná cyklu bod potom postupne nadobúda tieto hodntoty, teda dvojice čísel. Tento bod sa potom použije pre vypisovanie znaku pomocou create_text:

_images/03_19.png

Ak by sme tento postup chceli použiť pre kreslenie malých krúžkov v každom vrchole, museli by sme v tele cyklu premennú bod, ktorá je typu dvojica čísel, previesť na dve premenné x a y. Našťastie funguje priraďovací príkaz, ktorý dokáže dvojicu priradiť do dvoch premenných. Môžeme zapísať:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_line(a, b, c, d)

for bod in a, b, c, d:
    x, y = bod
    canvas.create_oval(x-5, y-5, x+5, y+5, outline='red')
canvas.mainloop()
~~~

_images/03_20.png

Tento cyklus môžeme zapísať ešte o trochu zaujímavejšie:
~~~
for x, y in a, b, c, d:
    canvas.create_oval(x-5, y-5, x+5, y+5, outline='red')
~~~
Namiesto jednej premennej cyklu (premenná bod) sme tu uviedli dve (premenné x a y). Python v tomto prípade postupne berie vymenované hodnoty a každú jednu rozoberie na dve čísla a priradí ich do x a y.

#### Polygon
Polygonom voláme oblasť, ktorá je ohraničená zadanou lomenou čiarou (aspoň s troma vrcholmi) a vyplní sa nejakou farbou. Body zadávame podobne ako pre create_line, len dva body by bolo zrejme málo. Táto oblasť bude zafarbená čiernou farbou, prípadne ju môžeme zmeniť, napr.
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_polygon(a, b, c, d, fill='blue')
canvas.mainloop()
~~~
a vyzerá to takto:

_images/03_21.png

#### Obdĺžnik
Týmto príkazom sa umiestni obdĺžnik, ktorého strany sú rovnobežné so súradnicovými osami, t.j. hranami grafickej plochy. Základný tvar je:
~~~
canvas.create_rectangle(x1, y1, x2, y2)
~~~
Hodnoty (x1, y1) a (x2, y2) sú súradnice dvoch ľubovoľných vrcholov tohto obdĺžnika, ktoré sú v obdĺžniku protiľahlé. Vyskúšajme:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 80, 200, 160)
canvas.mainloop()
~~~
Grafická plocha je teraz:

_images/03_04.png

Uvedomte si, že (50, 80) a (200, 160) sú dva protiľahlé vrcholy obdĺžnika, Ďalšie dva vrcholy sú (50, 160) a (200, 80). Veľkosti strán obdĺžnika sú 150 a 80.

Pomocou pomenovaného parametra outline='farba' nastavíme farbu obrysu kresleného obdĺžnika, napr.
~~~
canvas.create_rectangle(100, 120, 250, 200, outline='red')
~~~
Tento nový obdĺžnik vyzerá takto:

_images/03_05.png

ďalší pomenovaný parameter width=číslo nastaví hrúbku obrysu kresleného obdĺžnika. Napr.
~~~
canvas.create_rectangle(130, 100, 280, 180, outline='blue', width=5)
~~~
Tretí obdĺžnik má hrubší modrý obrys:

_images/03_06.png

Asi najužitočnejším pomenovaným parametrom pre kreslenia obdĺžnika je nastavenie farby výplne fill='farba'. Všetky doterajšie obdĺžniky boli nakreslené bez výplne (hovoríme, že mali tzv. priesvitnú výplň). Štvrtý obdĺžnik bude mať žltú výplň:
~~~
canvas.create_rectangle(80, 70, 230, 150, fill='yellow')
~~~

Všetky štyri obdĺžniky majú rovnaké rozmery ale rôzne nastavené niektoré parametre. Kompletný program:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 80, 200, 160)
canvas.create_rectangle(100, 120, 250, 200, outline='red')
canvas.create_rectangle(130, 100, 280, 180, outline='blue', width=5)
canvas.create_rectangle(80, 70, 230, 150, fill='yellow')
canvas.mainloop()
~~~
Grafická plocha:

_images/03_07.png

Pri kreslení grafických objektov je vhodné pracovať s premennými, v ktorých máme uložené napr. súradnice nejakých bodov, alebo veľkosti útvarov. Zapíšme nakreslenie obdĺžnika, v ktorom ľavý horný roh má súradnice (x, y), jeho šírka je s a výška v:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 50, 50
s, v = 100, 55
farba = 'red'
canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
x, y = 160, 70
canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
canvas.mainloop()
~~~

Všimnite si, že oba nakreslené obdĺžniky majú rovnaké rozmery a farbu, zmenili sme len polohu. Samotné vykreslenie create_rectangle() je v oboch prípadoch rovnaké:

_images/03_08.png

Na minulej prednáške sme sa naučili pracovať s for-cyklami. Nakreslime rad rovnakých obdĺžnikov, ktoré budú uložené vedľa seba. Aby sa nám vedľa seba zmestilo viac obdĺžnikov, zväčšíme aj rozmery grafickej plochy:
~~~
import tkinter

canvas = tkinter.Canvas(width=600, height=300)
canvas.pack()

x, y = 10, 50
s, v = 30, 50
farba = 'red'
for i in range(15):
    canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
    x = x + s + 2
canvas.mainloop()
~~~

Všimnite si riadok, v ktorom sa vytvára grafická plocha tkinter.Canvas(...). Pridali sme do neho definovanie veľkosti plátna na šírku 600 a výšku 300. Rad obdĺžnikov vyzerá takto:

_images/03_09.png

Pridajme ďalší cyklus, vďaka ktorému sa tento riadok obdĺžnikov nakreslí viackrát pod seba, pričom striedame dve farby výplne:
~~~
import tkinter

canvas = tkinter.Canvas(width=600, height=300)
canvas.pack()

y = 10
s, v = 30, 50
farba, farba2 = 'red', 'blue'
for j in range(5):
    x = 10
    for i in range(15):
        canvas.create_rectangle(x, y, x+s, y+v, fill=farba)
        x = x + s + 2
    y = y + v + 2
    farba, farba2 = farba2, farba
canvas.mainloop()
~~~
Dostávame:

_images/03_10.png

#### Farby v grafickej ploche

Skôr, ako prejdeme na ďalšie grafické objekty, vysvetlime si, ako sa pre tkinter pracuje s farbami.

Zatiaľ sme používali tieto základné mená farieb (zopár sme ich ešte pridali):
* 'red' - červená
* 'blue' - modrá
* 'yellow' - žltá
* 'green' - zelená
* 'black' - čierna
* 'white' - biela
* 'gray' - šedá
* 
Preddefinovaných mien farieb je výrazne viac. tkinter používa zaužívané mená farieb z HTML stránok. Môžeme ich nájsť napr. na internete: HTML Color Names. Vyskúšajte niekoľko farieb z tohto zoznamu, ktoré sa vám páčia, či budú fungovať aj v našich programoch (napr. pri vyfarbovaní obdĺžnikov).

Iste ste už počuli o tzv. RGB modeli farieb. Môžeme predpokladať, že všetky farby v počítači sú namiešané z troch základných farieb: červenej, zelenej a modrej (teda Red, Green, Blue). Farba závisí od toho, ako je v nej zastúpená každá z týchto troch farieb. Zastúpenie jednotlivej farby vyjadrujeme číslom od 0 do 255 (zmestí sa do jedného bajtu, teda ako 2-ciferné šestnástkové číslo). Napr. žltá farba vznikne, ak namiešame 255 červenej, 255 zelenej a 0 modrej. Ak budeme zastúpenie každej farby trochu meniť, napríklad 250 červenej, 240 zelenej a hoci 100 modrej, stále to bude žltá, ale v inom odtieni.

Pri kreslení v tkinter zadávame farby buď menami alebo zakódujeme ich RGB-trojicu do šestnástkovej sústavy ako 3 dvojciferné čísla (spolu 6 cifier). Pred takéto šestnástkové číslo musíme ešte na začiatok pridať znak ‚#‘, aby to tkinter odlíšil od mena farby. Môžete s týmto poexperimentovať napr. na stránke: Colors RGB - RGB Calculator. Na tejto stránke pri nastavovaní rôznych hodnôt pre zložky RGB dostávame rôzne výsledné farby a zakaždým vidíme zodpovedajúcu 16-ovú reprezentáciu ako 6-ciferné 16-ové číslo, pred ktorým je znak '#'.

Vyskúšajte takto vytvoriť nejaké dve zaujímavé farby a otestujte to v našom poslednom programe s piatimi radmi obdĺžnikov. Napr. ak nastavíte:
~~~
farba, farba2 = '#60ce40', '#ffbb00'
~~~
dostaneme takýto obrázok:

_images/03_11.png

Ak máme dané nejaké tri čísla, ktoré reprezentujú RGB, napr.
~~~
r, g, b = 205, 92, 9
~~~
a chceme z nich vyrobiť farbu pre tkinter, môžeme využiť formátovací reťazec, ktorý dokáže previesť číslo do 16-ovej sústavy:
~~~
f'#{r:02x}{g:02x}{b:02x}'
~~~
Formátovací parameter 02x na tomto mieste znamená, že dané číslo sa prevedie do 16-ovej sústavy s dvoma ciframi, pričom sa toto číslo doplní zľava 0, ak bolo iba jednociferné. Vďaka tomuto zápisu vieme v našich programoch veľmi elegantne vygenerovať ľubovoľné RGB. Pozmeňme tento program tak, že namiesto striedania dvoch farieb, každý jeden obdĺžnik zafarbíme náhodnou farbou. Zrejme každá farebná zložka bude náhodné číslo od 0 do 255, t.j. random.randrange(256). Ešte sme upravili obdĺžniky tak, aby mali rovnakú výšku ako šírku, teda budú to štvorčeky:
~~~
import tkinter
import random

canvas = tkinter.Canvas(width=600, height=300)
canvas.pack()

x0, y0 = 10, 10
s = 30
for y in range(y0, 250, s+2):
    for x in range(x0, 550, s+2):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        farba = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_rectangle(x, y, x+s, y+s, fill=farba)
canvas.mainloop()
~~~
Všimnite si, že sme tu aj trochu inak organizovali for-cykly. Dostávame nejako takto zafarbené štvorčeky:

_images/03_12.png

#### Elipsa

Kreslenie elíps je v tkinter veľmi blízke kresleniu obdĺžnikov: elipsu budeme totiž definovať prostredníctvom „neviditeľného“ obdĺžnika, v ktorom bude táto elipsa vpísaná. Takže, ak máme program, v ktorom máme nakreslené nejaké obdĺžniky a príkazy create_rectangle() nahradíme create_oval, tak presne na týchto miestach sa nakreslia elipsy.

Preto
~~~
canvas.create_oval(x1, y1, x2, y2)
~~~
Nakreslí elipsu, ktorá by bola vpísaná v
~~~
canvas.create_rectangle(x1, y1, x2, y2)
~~~
Môžeme vyskúšať:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 80, 200, 160)
canvas.create_oval(50, 80, 200, 160, outline='red')
canvas.mainloop()
~~~
a vidíme:

_images/03_13.png

Samozrejme, že keď vpíšeme elipsu do štvorca, dostávame kružnicu s priemerom veľkosti strany štvorca. Otestujeme kreslenie niekoľkých kružníc, ktoré majú spoločný stred ale rôzne polomery. Ak by sme mali daný stred (x, y) a polomer r, tak kružnicu nakreslíme:
~~~
canvas.create_oval(x-r, y-r, x+r, y+r)
~~~
Vyskúšajme:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 190, 130
for r in range(10, 130, 10):
    canvas.create_oval(x-r, y-r, x+r, y+r)
canvas.mainloop()
~~~
a sústredné kružnice vyzerajú takto:

_images/03_14.png

Keďže ďalšie parametre príkazu create_oval sú rovnaké ako pre obdĺžniky, môžeme vyfarbiť tieto kružnice na striedačku dvoma farbami:
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 190, 130
f1, f2 = 'red', 'blue'
for r in range(10, 130, 10):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=f1)
    f1, f2 = f2, f1
canvas.mainloop()
~~~
Žiaľ, vidíme len naposledy nakreslený najväčší kruh:

_images/03_15.png

Keďže sme začali kresliť od najmenších kruhov, každý ďalší väčší prekryje všetky predchádzajúce.

Asi najelegantnejšie riešenie tohto problému bude to, keď nakreslíme všetky kruhy v opačnom poradí: od najväčšieho po najmenší. Využijeme štandardnú funkciu reversed(), pomocou ktorej otočíme poradie postupnosti čísel range(10, 130, 10):
~~~
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 190, 130
f1, f2 = 'red', 'blue'
for r in reversed(range(10, 130, 10)):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=f1)
    f1, f2 = f2, f1
canvas.mainloop()
~~~
a očakávaný výsledok:

_images/03_16.png

Využijeme program, v ktorom sme nakreslili niekoľko radov náhodne zafarbených štvorčekov. Nahradíme v ňom create_rectangle volaním create_oval:
~~~
import tkinter
import random

canvas = tkinter.Canvas(width=600, height=300)
canvas.pack()

x0, y0 = 10, 10
s = 30
for y in range(y0, 250, s+2):
    for x in range(x0, 550, s+2):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        farba = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_oval(x, y, x+s, y+s, fill=farba)
canvas.mainloop()
~~~
Dostávame:

_images/03_17.png

#### Obrázok

Aby sme do plochy mohli nakresliť nejaký obrázok, musíme najprv vytvoriť „obrázkový objekt“ (pomocou tkinter.PhotoImage() prečítať obrázok zo súboru) a až tento poslať ako parameter do príkazu na kreslenie obrázkov canvas.create_image().

Obrázkový objekt vytvoríme špeciálnym príkazom:
~~~
premenna = tkinter.PhotoImage(file='cesta_a_meno_suboru')
~~~
v ktorom meno suboru je súbor s obrázkom vo formáte png alebo gif. Takýto obrázkový objekt môžeme potom vykresliť do grafickej plochy ľubovoľný počet-krát.

Samotná funkcia canvas.create_image() na vykreslenie obrázka má tri parametre: prvé dva sú súradnice stredu vykresľovaného obrázka a ďalší pomenovaný parameter určuje obrázkový objekt. Príkaz má tvar:
~~~
canvas.create_image(x, y, image=premenna)
~~~
Napr.
~~~
obr = tkinter.PhotoImage(file='Suunto01.jpg')
canvas.create_image(500, 100, image=obr)
~~~
Musíte sa uistiť, že obrázok je v rovnakom adresári ako váš súbor skriptu python. Aby sa obrázok zobrazil, potrebujeme možnosti image=logoa compound='top'v tk.Label metóde, ktorá povie tkinteru, aby zobrazil obrázok a text spolu tak, aby bol obrázok navrchu.

#### Dialogové okno pre GUI

~~~
# Radio button, Check button, Combobox a list box

from tkinter import *
from tkinter.ttk import Combobox
window = Tk()

# radio button
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=2)
r1.place(x=100, y=50)
r2.place(x=180, y=50)

# check bitton
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text="Cricket", variable=v1)
C2 = Checkbutton(window, text="Tennis", variable=v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)

# combo box
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=150)

# list box
lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=150)

# text field
txtfld = Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=65, y=200)

# button
btn = Button(window, text="This is Button widget", fg='blue')
btn.place(x=70, y=230)
lbl = Label(window, text="This is Label widget",
            fg='red', font=("Helvetica", 16))
lbl.place(x=50, y=20)

window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
~~~
![](./Grafy_Obrazky_Video_Audio/gui_screen.png)

Vytváranie niektorých prvkov rozhrania nájdeme [Tu](https://www.geeksforgeeks.org/python-gui-tkinter/) a [tu](https://likegeeks.com/python-gui-examples-tkinter-tutorial/)

### Parametre grafickej plochy

Pri vytváraní grafickej plochy (pomocou tkinter.Canvas()) môžeme nastaviť veľkosť plochy ale aj farbu pozadia grafickej plochy. Môžeme uviesť tieto parametre:
* bg= nastavuje farbu pozadia (z anglického „background“)
* width= nastavuje šírku grafickej plochy
* height= výšku plochy
Napr.
~~~
canvas = tkinter.Canvas(bg='white', width=400, height=200)
~~~
Vytvorí bielu grafickú plochu, ktorá má šírku 400 a výšku 200.

Tieto parametre plochy môžeme meniť aj dodatočne, aj vtedy, keď je už v ploche niečo nakreslené. Vtedy použijeme takýto formát:
~~~
>>> canvas['bg'] = 'yellow'
>>> sirka = int(canvas['width'])      # zapamätaj si momentálnu šírku plochy
>>> canvas['width'] = 600             # zmeň šírku
>>> canvas['height'] = 400            # zmeň výšku
~~~

### Zmeny nakreslených útvarov

Všetky útvary, ktoré kreslíme do grafickej plochy si systém pamätá tak, že ich dokáže dodatočne meniť (napr. ich farbu), posúvať po ploche, ale aj mazať. Všetky útvary sú na ploche vykresľované presne v tom poradí, ako sme zadávali jednotlivé grafické príkazy: skôr nakreslené útvary sú pod neskôr nakreslenými a môžu ich prekrývať.

Každý grafický príkaz (napr. canvas.create_line()) je v skutočnosti funkciou, ktorá vracia celé číslo - identifikátor nakresleného útvaru. Toto číslo nám umožní neskoršie modifikovanie, resp. jeho zmazanie.

#### Zmazanie nakresleného útvaru

Na zrušenie ľubovoľných grafických objektov z grafickej plochy slúži funkcia:
~~~
funkcia canvas.delete(oznacenie)
~~~
kde parameter oznacenie je identifikátor prísluňého útvaru:
* číselný identifikátor
* pridelený štítok (tag)
* reťazec 'all' označuje všetky útvaru v ploche
Napr.

kde identifikátor je návratová hodnota príkazu kreslenia útvaru
ak ako identifikátor použijeme reťazec 'all', príkaz zmaže všetky doteraz nakreslené útvary
Napr.
~~~
id1 = canvas.create_line(10, 20, 30, 40)
id2 = canvas.create_oval(10, 20, 30, 40)
canvas.create_text(100, 100, text='ahoj', tag='t')
canvas.create_rectangle(80, 90, 120, 110, fill='gray', tag='t')
...
canvas.delete(id1)
canvas.delete('t')
~~~
Zmaže prvý grafický objekt, t.j. úsečku, pričom druhý objekt kružnica ostáva bez zmeny. Druhý príkaz zmaže oba textový objekt aj obdĺžnik, ktorým sme pridelili štítok ‚t‘.

#### Posúvanie útvarov

Pomocou identifikátora útvaru alebo jeho štítku (vtedy ich môže byť aj viac) môžeme ľubovoľným smerom útvary posúvať. Ostatné útvary sa pri tom nehýbu.
~~~
canvas.move(oznacenie, dx, dy)
~~~
kde
* označenie je buď identifikátor alebo štítok grafických útvarov (bude fungovať aj reťazec 'all')
* dx a dy označujú číselné hodnoty zmeny súradníc útvaru, t.j. posun v smere osi x a v smere osi y
Napr.

posúvaný útvar môže byť ľubovoľne komplikovaný (môže sa skladať aj z väčšieho počtu bodov), príkaz canvas.move() posunie všetky vrcholy útvaru
ak ako identifikátor použijeme reťazec 'all', príkaz posunie všetky doteraz nakreslené útvary
Napr.
~~~
id1 = canvas.create_line(10, 20, 30, 40)
id2 = canvas.create_oval(10, 20, 30, 40)
canvas.create_text(100, 100, text='ahoj', tag='t')
canvas.create_rectangle(80, 90, 120, 110, fill='gray', tag='t')
...
canvas.move(id1, -5, 10)
canvas.move('t', -5, 10)
~~~
posunie prvý nakreslený útvar, teda úsečku, druhý útvar (kružnicu) pri tom nehýbe, zároveň s tým posunie naraz obdĺžnik s textom.

#### Zmena parametrov útvaru

Táto funkcia umožňuje meniť ľubovoľné pomenované parametre už nakresleným útvarom. Jeho tvar je:
~~~
canvas.itemconfig(oznacenie, parametre)
~~~
kde
* označenie je buď identifikátor alebo štítok grafických útvarov
* parametre sú pomenované parametre v rovnakom formáte, aký bol pri ich vytváraní

#### Zmena súradníc útvarov

Okrem posúvania útvarov im môžeme zmeniť aj ich kompletnú postupnosť súradníc. Napr. pre canvas.create_line() alebo canvas.create_polygon() môžeme zmeniť aj počet bodov útvaru. Tvar tejto funkcie je:
~~~
canvas.coords(oznacenie, postupnost)
~~~
kde
* označenie je buď identifikátor alebo štítok grafických útvarov
* postupnost je ľubovoľná postupnosť súradníc, ktorá je vhodná pre daný útvar - táto postupnosť musí obsahovať párny počet čísel (celých alebo desatinných)
Napr.
~~~
i1 = canvas.create_line(10, 20, 30, 40)
canvas.coords(i1, 30, 40, 50, 60, 70, 90)
~~~

### Kombinácia Turtle a Tkinter

Turtle Python funguje v dvoch režimoch, samostatne a zabudovaná do nejakého väčšieho programu vztvoreného pomocou Tkinter. Namiesto Turtle a Screen, keď používate turtle embedded, pracujete s RawTurtle, TurtleScreena a voliteľne aj s ScrolledCanvas. Rozhranie tkinter si vytvoríte podľa potreby pomocou plátna, ktoré obsahuje vašu korytnačiu grafiku. Vkladanie Turtle do Tkinter sa robí tak že sa korytnačka nahradí s RawTurtle. Príklad ako sa to dá urobiť námjdeme [tu](https://stackoverflow.com/questions/54246872/how-to-combine-tkinter-and-turtle) odkaze.

Iný príklad takéhoto riešenia nájdeme [tu](https://stackoverflow.com/a/44639041/5771269) alebo [tu](https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/).

Pri zámere skombinovať Turtle a Tkinter však vyvstáva otázka kedy a za akým účelom to urobiť ? Je vhodné kombinovať tieto dva grafické rozhrania ak Tkinter sám v sebe ponúka funkcionalitu Turtle a ponúka aj niečo naviac !

