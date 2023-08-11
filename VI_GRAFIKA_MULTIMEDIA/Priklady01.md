Cvičenie
Napíšte funkciu vypis_delitele(cislo), ktorá vypíše do jedného riadka všetky delitele daného čísla.
napr.
>>> vypis_delitele(24)
1 2 3 4 6 8 12 24
Napíšte funkciu sucet_delitelov(cislo), ktorá vráti súčet všetkých deliteľov daného čísla. Funkcia nič nevypisuje, funkcia vracia (pomocou return) nejakú hodnotu.
napr.
>>> x = sucet_delitelov(24)
>>> x
60
Napíšte funkciu je_dokonale(cislo), ktorá pomocou funkcie sucet_delitelov() zistí, či je dané číslo dokonalé, t.j. že súčet všetkých menších deliteľov ako samotné číslo sa rovná samotnému číslu. Napr. delitele čísla 6 (menšie ako 6) sú 1, 2, 3. Ich súčet je 6. Preto je číslo 6 dokonalé. Funkcia nič nevypisuje, funkcia vracia (pomocou return) nejakú hodnotu.
napr.
>>> je_dokonale(6)
True
>>> je_dokonale(24)
False
Napíšte funkciu vsetky_dokonale(od, do), ktorá vypíše dokonalé čísla v danom intervale.
napr.
>>> vsetky_dokonale(1, 30)
6 je dokonale
28 je dokonale
Napíšte funkciu nsd(a, b), ktorá počíta najväčší spoločný deliteľ dvoch čísel. Funkcia nič nevypisuje, funkcia vracia (pomocou return) nejakú hodnotu.
napr.
>>> nsd(21, 15)
3
>>> nsd(1000000, 17)
1
odkrokujte vaše riešenie pomocou stránky http://www.pythontutor.com/visualize.html#mode=edit
Napíšte funkciu pocet_delitelov(cislo), ktorá pre dané číslo zistí počet všetkých deliteľov. Napr. delitele čísla 6 sú 1, 2, 3, 6, preto funkcia vráti 4. Funkcia nič nevypisuje, funkcia vracia (pomocou return) nejakú hodnotu.
napr.
>>> pocet_delitelov(6)
4
>>> pocet_delitelov(17)
2
Napíšte funkciu je_prvocislo(cislo), ktorá pomocou funkcie pocet_delitelov() zistí (vráti True alebo False), či je to prvočíslo (je deliteľné len 1 a samým sebou).
napr.
>>> je_prvocislo(6)
False
>>> je_prvocislo(17)
True
Napíšte funkciu vsetky_prvocisla(od, do), ktorá vypíše všetky prvočísla v danom intervale do jedného riadka.
napr.
>>> vsetky_prvocisla(1, 30)
2 3 5 7 11 13 17 19 23 29
odkrokujte vaše riešenie pomocou stránky http://www.pythontutor.com/visualize.html#mode=edit
Napíšte funkciu sucet_mocnin2(n), ktorá vráti súčet mocnín dvojky s exponentmi menšími ako n. Napr. sucet_mocnin2(5), vráti hodnotu 1+2+4+8+16, t.j. hodnotu 31.
otestujte
>>> for i in range(7):
        print(i, sucet_mocnin2(i))

0 0
1 1
2 3
3 7
4 15
5 31
6 63
pokúste sa odhadnúť, aký vzorec by vedel vypočítať rovnaký výsledok ako dáva funkcia sucet_mocnin2() ale bez cyklu.
Napíšte funkciu sucet_mocnin2a(n), ktorá vráti súčet prevrátených mocnín dvojky s exponentmi menšími ako n. Napr. sucet_mocnin2a(5), vráti hodnotu 1/1+1/2+1/4+1/8+1/16, t.j. hodnotu 1.9375.
otestujte
>>> for i in range(7):
        print(i, sucet_mocnin2a(i))

0 0
1 1.0
2 1.5
3 1.75
4 1.875
5 1.9375
6 1.96875
všimnite si, že výsledok sa pre väčšie n blíži k nejakej konštante
Napíšte funkciu kocka() bez parametrov, ktorá pri každom zavolaní vráti náhodné číslo z intervalu od 1 do 6.
otestujte
>>> for i in range(20):
        print(kocka(), end=' ')
...
opravte tento testovací cyklus tak, že v postupnosti vypisovaných čísel za každé, ktoré je rovnaké ako predchádzajúce, vypíšete aj znak '*', napr.
>>> ... for i in range(20): ...
6 4 4 * 4 * 3 5 4 3 5 5 * 1 2 1 1 * 1 * 1 * 2 2 * 6 1
Napíšte funkciu pocet_samohlasok(text), ktorá pre zadaný znakový reťazec zistí počet samohlások, ktoré obsahuje.
napr.
>>> pocet_samohlasok('python')
2
>>> pocet_samohlasok('strc prst skrz krk')
0
Napíšte funkcie gula(x, y, r) a snehuliak(x, y, r). Funkcia gula() nakreslí biely kruh so stredom (x, y) a s polomerom r. Funkcia snehuliak() pomocou troch volaní gula() nakreslí snehuliaka, v ktorom spodná najväčšia guľa má stred (x, y) a polomer r. Stredná má polomer 2/3 veľkej a najmenšia je polovičná strednej. Otestujte na bledomodrom pozadí.
napr.
>>> snehuliak(200, 400, 90)
>>> snehuliak(400, 300, 45)
>>> snehuliak(100, 200, 30)
Napíšte funkciu karticka(x, y, text), ktorá do grafickej plochy nakreslí bledošedý obdĺžnik a do jeho stredu vypíše zadaný text. Stred kartičky má súradnice (x, y) a jej strany majú dĺžky 100 a 40. Font písma nech je napr. 'arial 14'.
otestujte náhodným vygenerovaním 10 kartičiek, napr. s textom 'Python'
otestujte náhodným vygenerovaním 10 kartičiek s textom súradníc kartičky, napr. v tvare '(354,211)'
Napíšte funkcie stvorec(x, y, a, farba), trojuholnik(x, y, a, farba) a domcek(x, y, a=50, farba1='blue', farba2='red'). Funkcia stvorec() nakreslí farebný štvorec s ľavým horným vrcholom na (x, y) a stranou a. Funkcia trojuholnik() nakreslí rovnoramenný trojuholník s ľavým dolným vrcholom v (x, y) so stranou aj výškou a. Funkcia domcek() nakreslí domček pomocou štvorca a trojuholníka.
otestujte vykreslením 10 domčekov na náhodných pozíciách
Napíšte funkcie kruh(x, y, r) a sustredne(n, x, y). Funkcia kruh() nakreslí na zadané súradnice kruh daného polomeru a vyplní ho náhodnou farbou. Funkcia sustredne() pomocou kruh() nakreslí n sústredných farebných kruhov s polomermi 5, 10, 15, 20, … Použite funkciu nahodna_farba() z prednášky.
otestujte niekoľkými volaniami sustredne() na náhodných pozíciách
Napíšte funkcie: kocka(x, y, a, farba), ktorá nakreslí farebný štvorec s daným stredom a danou stranou; funkcia rad(n, x, y, a) nakreslí vedľa seba n štvorcov (prvý ľavý z nich na zadaných súradniciach), pričom sú zafarbené rovnakou náhodnou farbou; funkcia pyramida(n, x, y, a) pomocou funkcie rad() nakreslí pyramídu výšky n, t.j. zloženú z n radov dĺžky 1, 2, 3, … n. Najvyššia kocka pyramídy je na zadaných súradniciach. Každý nižší rad kociek sa nakreslí o a nižšie a o a/2 odsunutý vľavo.
otestujte v ploche veľkosti 500x500 napr.
>>> pyramida(10, 250, 50, 40)
skuste zmeniť generátor náhodnej farby tak, aby sa vytvárali náhodné odtiene len jednej farby, napr. rgb(0, g, 0), kde g je náhodné číslo od 100 do 255 bude generovať len modré farby

>#### cez Zbalené pomenované parametre

Ďalší príklad tiež ilustruje takéto zbalené asociatívne pole:

import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def kruh(r, x, y):
    canvas.create_oval(x-r, y-r, x+r, y+r)

kruh(50, 100, 100)
Funkcia kruh() definuje nakreslenie kruh s daným polomerom a stredom, ale nijako nevyužíva ďalšie parametre na definovanie farieb a obrysu kruhu. Doplňme do funkcie zbalené pomenované parametre:

def kruh(r, x, y, **param):
    canvas.create_oval(x-r, y-r, x+r, y+r)
Toto označuje, že kruh() môžeme zavolať s ľubovoľnými ďalšími pomenovanými parametrami, napr. kruh(..., fill='red', width=7). Tieto parametre ale chceme ďalej poslať do funkcie create_oval(). Určite sem nemôžeme poslať param, lebo toto je premenná typu dict a create_oval() s tým pracovať nevie. Tu by sa nám zišlo premennú param rozbaliť do viacerých pomenovaných parametrov: Rozbaľovací operátor pre pomenované parametre sú dve hviezdičky **, teda zapíšeme:

def kruh(r, x, y, **param):
    canvas.create_oval(x-r, y-r, x+r, y+r, **param)
a teraz funguje aj

kruh(50, 100, 100)
kruh(30, 150, 100, fill='red')
kruh(100, 200, 200, width=10, outline='green')
Takýto rozbaľovací parameter by sme vedeli využiť aj v predchádzajúcom príklade s funkciou vypis():

>>> p1 = {'meno':'Janko Hrasko', 'vek':5, 'vyska':7, 'vaha':0.3, 'bydlisko':'Pri poli'}
>>> vypis(**p1)
volam sa Janko Hrasko
     vaha = 0.3
     vek = 5
     vyska = 7
     bydlisko = Pri poli
>>> p2 = {'vek':25, 'narodeny':'Terchova', 'popraveny':'Liptovsky Mikulas'}
>>> vypis('Juraj Janosik', **p2)
volam sa Juraj Janosik
     popraveny = Liptovsky Mikulas
     vek = 25
     narodeny = Terchova

### Príklady s turtle

~~~
# Python program to draw square
# using Turtle Programming
import turtle
skk = turtle.Turtle()
 
for i in range(4):
    skk.forward(50)
    skk.right(90)
     
turtle.done()
~~~

~~~
# Python program to draw star
# using Turtle Programming
import turtle
star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
	star.right(144)
	star.forward(100)
	
turtle.done()
~~~

~~~
# Python program to draw hexagon
# using Turtle Programming
import turtle
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
	polygon.forward(side_length)
	polygon.right(angle)
	
turtle.done()

~~~
~~~
import turtle

# Initialize the turtle
t = turtle.Turtle()

# Set the turtle's speed
t.speed(1)

# Draw the parallelogram
for i in range(2):
	t.forward(100)
	t.left(60)
	t.forward(50)
	t.left(120)
~~~
~~~
import turtle

# Set up the turtle screen and set the background color to white
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle and set its speed to the fastest possible
pen = turtle.Turtle()
pen.speed(0)

# Set the fill color to red
pen.fillcolor("red")
pen.begin_fill()

# Draw the circle with a radius of 100 pixels
pen.circle(100)

# End the fill and stop drawing
pen.end_fill()
pen.hideturtle()

# Keep the turtle window open until it is manually closed
turtle.done()

~~~
~~~
import turtle #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(90)
		size = size + 5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)

~~~
~~~
# Python program to user input pattern
# using Turtle Programming
import turtle #Outside_In
import turtle
import time
import random

print ("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
	squares = int(num_str)

angle = 180 - 180*(squares-2)/squares

turtle.up

x = 0
y = 0
turtle.setpos(x, y)


numshapes = 8
for x in range(numshapes):
	turtle.color(random.random(), random.random(), random.random())
	x += 5
	y += 5
	turtle.forward(x)
	turtle.left(y)
	for i in range(squares):
		turtle.begin_fill()
		turtle.down()
		turtle.forward(40)
		turtle.left(angle)
		turtle.forward(40)
		print (turtle.pos())
		turtle.up()
		turtle.end_fill()

time.sleep(11)
turtle.bye()

~~~
~~~
# Python program to draw
# Spiral Helix Pattern
# using Turtle Programming

import turtle
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)

turtle.exitonclick()

~~~

~~~

# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
~~~

~~~
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)
~~~

### Priklady na Tkinter

~~~
#import tkinter module
import tkinter as tk

# inicializovanie okna - minimalna sucast akejkolvek aplikacie Tkinter
# ktorá pomáha vytvárať inštanciu aplikácie. Tk  pomáha zostaviť 
# základné stavebné bloky aplikácie, ako je okno aplikácie, kde sú 
# umiestnené všetky widgety.
okno = tk.Tk()

#vytvorenie okna urcenej velkosti
# okno.geometry("300x300")

#pridaj nazov okna
tk.Label(text="Hello from Educative !!!").pack()

# opakuj vytvaranie okna v slucke dokola az kym ho nezatvorime x-om
okno.mainloop()
~~~
~~~
# Rozdiel medzi importom tkinter as tk a importom z tkinter

# import tkinter as tk	sluzi na import iba metody tk
# from tkinter import * sluzi na import vsetkych funkcii
# import tkinter
win = Tk() 
win.geometry("750x250")
entry = Text(win, width=24)
entry.insert(INSERT, "Hello World!")
entry.tag_add("start", "1.0", "end")
entry.tag_configure("start", background="blue", foreground="white")
entry.pack()
win.mainloop()
~~~
~~~
import tkinter

top = tkinter.Tk()

# pracovna plocha - platno (Canvas)
C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()
~~~

1. Napíšte program, ktorý nakreslí pyramídu: tvoria ju 3 na sebe položené obdĺžniky veľkosti 100x20, 60x20, 20x20, tieto obdĺžniky sú vycentrované.

Napíšte program, ktorý nakreslí podobnú pyramídu z predchádzajúceho príkladu, pričom všetky obdĺžniky majú výšku 10 a ich šírky sú postupne 200, 180, 160, … 60, 40, 20.

Napíšte program, ktorý nakreslí rad n modrých kruhov: všetky sú tesne vedla seba a majú polomery 20. Napr. pre n = int(input('zadaj pocet: ')).

Podobný príklad ako (3), ale výplne kruhov sú troch rôznych farieb: postupne sa striedajú 'red', 'yellow', 'blue'. Kreslenie kruhov zapíšte tak, aby sa nekreslil ich čierny obrys.

Napíšte program, ktorý najprv prečíta polomer kružnice (input('polomer: ')), potom ju nakreslí do stredu grafickej plochy a do neho pomocou canvas.create_rectangle() nakreslí vpísaný štvorec (jeho vrcholy ležia na obvode kružnice).

V priečinku, v ktorom je nainštalovaný Python, nájdite súbor 'rgb.txt'. Zvoľte si z neho nejakých 5 zaujímavých farieb a ich mená vypíšte pod sebou nejakým hrubým fontom, napr. canvas.create_text(x, y, text=meno_farby, font=..., fill=meno_farby).

Napíšte program, ktorý pre tri zadané hodnoty, napr. r1, r2, r3 = 20, 40, 60 nakreslí snehuliaka, ktorý sa skladá z troch bielych kruhov s polomermi r1, r2, r3. Snehuliak je nakreslený v strede grafickej plochy na bledomodrom pozadí.

Napíšte program, ktorý nakreslí rovnoramenný trojuholník so základňou a a výškou v. Hodnoty a a v program prečíta zo vstupu (input()).

Napíšte program, ktorý nakreslí takýto domček: skladá sa z červenej strechy (rovnoramenný trojuholník so základňou 50 a výškou 50) a modrého štvorca (veľkosti 50x50). Ľavý horný vrchol štvorca nech je na súradniciach napr. x, y = 10, 80.

Využite predchádzajúci príklad (9) a nakreslite n domčekov vedľa seba (s malou medzerou medzi nimi). n prečítate zo vstupu (input()).

Napíšte program, ktorý nakreslí n žltých kruhov na náhodných pozíciách, pričom v strede každého sú postupne čísla 1, 2, …, n.

Napíšte program, ktorý si najprv vyžiada nejaké slovo (input()) a potom ho vypíše ho stredu plochy nejakým veľkým fontom. Zvoľte nejaké zaujímavé písmo, ktorého meno sa skladá z viac slov, napr. 'Cooper Black', 'Brush Script MT' alebo 'Courier New'… Keďže meno fontu je teraz viacslovné, doplnkový parameter font='...' musíte zmeniť na zápis napr. takto font=('Courier New', 40, 'bold')

Napíšte program, ktorý vypíše (print()) tabuľku hodnôt: v prvom stĺpci je uhol v stupňoch (z intervalu od 0 do 360 s krokom 30), v druhom je vypočítaný sin() a v treťom cos() tohto uhla. Na prevod medzi stupňami a radiánmi môžete použiť hodnotu premennej math.pi. Výsledok zaokrúhľujte na 2 desatinné miesta (round(číslo, 2)).

Body na kružnici so stredom (x0, y0) a polomerom r sa dajú vyjadriť vzorcom:

x = x0 + r * cos(uhol)
y = y0 + r * sin(uhol)
kde uhol je číslo od 0 do 360 stupňov (pozor na radiány). Ak budete takto vypočítané body postupne spájať úsečkami (napr. pomocou canvas.create_line()), dostanete kružnicu. Nakreslite týmto postupom kružnicu, pričom otestujte kreslenie pre rôznu hustotu bodov na kružnici (pre rôzne hodnoty zväčšovania uhla, napr. s krokom 30, alebo 10 alebo 2, …).
Ak v programe z predchádzajúcej úlohy (14) nebudeme spájať susedné vrcholy, ktoré ležia na obvode kružnice, ale budeme spájať tieto vrcholy so stredom kružnice (zvoľte žlté hrubé pero) a na koniec nakreslíme žltý kruh (canvas.create_oval()) s rovnakým stredom ako naša kružnica ale s menším polomerom, dostaneme slnko s lúčmi. Napíšte program:

pocet lucov: 10
dlzka lucov od stredu: 150
velkost slnka: 80
# nakreslí žlté slnko

16. Zvoľte si nejaký zaujímavý obrázok vo formáte .png alebo .gif (vyhľadajte napr. na webe) a nakreslite ho 10-krát na náhodných pozíciách.

Napíšte program, ktorý vypíše nejaký zadaný text na rôzne miesta grafickej plochy tak, aby každý mal iný font, inú farbu aj veľkosť.

napr.

text = 'programovanie'
# vykreslenie tohto textu rôznymi fontami
ak sa meno fontu skladá z viac slov, napr. 'Cooper Black', 'Brush Script MT' alebo 'Courier New'… musíme pomenovaný parameter font='...' zmeniť na zápis napr. takto font=('Courier New', 40)

Napíšte program, ktorý nakreslí pyramídu: tvoria ju 3 na sebe položené obdĺžniky veľkosti 100x20, 60x20, 20x20, tieto obdĺžniky sú vycentrované. Zafarbite ich tromi rôznymi farbami.

Napíšte program, ktorý nakreslí podobnú pyramídu z predchádzajúceho príkladu, pričom všetky obdĺžniky majú výšku 10 a ich šírky sú postupne čísla 200, 180, 160, … 60, 40, 20. Obdĺžniky zafarbujte náhodnými farbami.

Napíšte program, ktorý nakreslí rad n kruhov: všetky sú tesne vedľa seba a striedajú sa polomery 20 a 30. Zvoľte nejaké tri farby, ktoré sa pritom striedajú. Mená farieb vyberte zo stránky Colors RGB tak, aby boli v 16-ovom tvare '#......'. Kreslenie kruhov zapíšte tak, aby sa nekreslil ich čierny obrys.

napr.

n = 12
r = 15
# vykreslenie n kruhov vedla seba
Napíšte program, ktorý pre zadaný polomer r nakreslí do stredu grafickej plochy kružnicu a do nej pomocou canvas.create_rectangle() nakreslí vpísaný štvorec (jeho vrcholy musia ležať na obvode kružnice).

napr.

r = 180
# nakresli kruznicu s polomerom r a do nej vpisany stvorec
Napíšte program, ktorý pre tri zadané hodnoty r1, r2, r3 nakreslí snehuliaka, ktorý sa skladá z troch „skoro“ bielych kruhov s týmito polomermi. Snehuliak je nakreslený v strede grafickej plochy na bledomodrom pozadí. Farbu bielych kruhov zvoľte tromi rôznymi odtieňmi bielej.

napr.

r1, r2, r3 = 20, 40, 60
# nakresli snehuliaka
Napíšte program, ktorý nakreslí rovnoramenný trojuholník so základňou a a výškou v. Hodnoty a a v program prečíta zo vstupu (input()).

napr.

a, v = 200, 170
# nakresli trojuholnik
Napíšte program, ktorý nakreslí takýto domček: skladá sa z červenej strechy (rovnostranný trojuholník so základňou z) a modrého štvorca (veľkosti a x a). Ľavý horný vrchol štvorca nech je na súradniciach (x, y) a strecha nech je vycentrovaná.

napr.

x, y = 50, 120
z, a = 100, 80
# nakresli domček
Napíšte program, ktorý nakreslí n žltých kruhov na náhodných pozíciách, pričom v strede každého sú postupne čísla 1, 2, …, n. Polomer kruhov nech je r.

napr.

n = 30
r = 20
# nakresli n kruhov s číslami
Najprv zadefinujte päť vrcholov do premenných a, b, c, d, e, v ktorých budú súradnice bodov v rovine (ako dvojice čísel). Potom pomocou jediného volania create_line() nakreslite tento domček tak, aby sa po každej čiare prešlo len raz. Ako parametre create_line() použite týchto 5 premenných.

_images/03_22.png
napr.

a = (..., ...)
b =
c =
d =
e =
# nakresli domcek jednym tahom
Podobne ako v úlohe (10) využijete päť vrcholov v premenných a, b, c, d, e. Zadefinujte ešte premennú f, ktorá bude obsahovať súradnice priesečníku uhlopriečok štvorca. Pomocou piatich volaní create_polygon() zafarbite každý trojuholník v domčeku inou farbou (len tie najmenšie trojuholníky v obrázku, nemyslíme napr. trojuholník abc). Zabezpečte, aby sa pri kreslení polygonov urobili ich čierne obrysy. V tejto úlohe nevolajte create_line().

Body na kružnici so stredom (x0, y0) a polomerom r sa dajú vyjadriť vzorcom:

x = x0 + r * math.cos(math.radians(uhol))
y = y0 + r * math.sin(math.radians(uhol))
kde uhol je číslo od 0 do 360 stupňov. Ak budete takto vypočítané body postupne spájať úsečkami (napr. canvas.create_line()), dostanete kružnicu. Nakreslite týmto postupom kružnicu, pričom otestujte kreslenie pre rôznu hustotu bodov na kružnici (pre rôzne hodnoty zväčšovania uhla, t.j. krok, napr. s krokom 30, alebo 10 alebo 2, …). Napr.

x0, y0 = 300, 200
r = 150
krok = 30
# nakresli kružnicu
V programe z predchádzajúcej úlohy (12) nebudete spájať susedné vrcholy, ktoré ležia na obvode kružnice, ale budeme spájať tieto vrcholy so stredom kružnice (zvoľte žlté hrubé pero). Na koniec nakreslite žltý kruh (canvas.create_oval()) s rovnakým stredom ako naša kružnica ale s menším polomerom. Takto dostanete slnko s lúčmi. Napíšte program:

x0, y0 = 200, 170
pocet_lucov = 10
dlzka_lucov = 150
velkost_slnka = 80
farba_pozadia = 'navy'
# nakreslí žlté slnko
14. Zvoľte si nejaký zaujímavý obrázok vo formáte .png alebo .gif (napr. The Python Logo) a nakreslite ho 10-krát na náhodných pozíciách.


Priklady s Tkinter http://www.scspp.sk/evka/informa1G/ukazka.pdf 

~~~
# kalkulacka s tkinter

from tkinter import *

ws = Tk()
ws.title('Calculator')
ws.geometry('250x400+500+100')
ws.resizable(0,0)

# global variables
num = ''

# functions
def display(number):
    global num 
    num = num + str(number)
    scr_lbl['text'] = num
    

def clear_scr():
    global num
    num = ''
    scr_lbl['text'] = num


def equal_btn():
     global num
     add=str(eval(num))
     scr_lbl['text'] = add
     num=''
def equal_btn():
     global num
     sub=str(eval(num))
     scr_lbl['text'] = sub
     num=''     
def equal_btn():
     global num
     mul=str(eval(num))
     scr_lbl['text'] = mul
     num=''
def equal_btn():
     global num
     div=str(eval(num))
     scr_lbl['text'] = div
     num=''    

var = StringVar()

# frames 
frame_1 = Frame(ws) 
frame_1.pack(expand=True, fill=BOTH)

frame_2 = Frame(ws)
frame_2.pack(expand=True, fill=BOTH)

frame_3 = Frame(ws)
frame_3.pack(expand=True, fill=BOTH)

frame_4 = Frame(ws)
frame_4.pack(expand=True, fill=BOTH)

# label
scr_lbl = Label(
    frame_1,
    textvariable='',
    font=('Arial', 20),
    anchor = SE,
    bg = '#595954',
    fg = 'white' 
    )

scr_lbl.pack(expand=True, fill=BOTH)

# buttons
key_1 = Button(
    frame_1,
    text='1',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(1)
    )

key_1.pack(expand=True, fill=BOTH, side=LEFT)

key_2 = Button(
    frame_1,
    text='2',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(2)
    )

key_2.pack(expand=True, fill=BOTH, side=LEFT)

key_3 = Button(
    frame_1,
    text='3',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(3)
    )

key_3.pack(expand=True, fill=BOTH, side=LEFT)

key_add = Button(
    frame_1,
    text='+',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('+')
    )

key_add.pack(expand=True, fill=BOTH, side=LEFT)

key_4 = Button(
    frame_2,
    text='4',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(4)
    )

key_4.pack(expand=True, fill=BOTH, side=LEFT)

key_5 = Button(
    frame_2,
    text='5',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(5)
    )

key_5.pack(expand=True, fill=BOTH, side=LEFT)

key_6 = Button(
    frame_2,
    text='6',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(6)
    )

key_6.pack(expand=True, fill=BOTH, side=LEFT)

key_sub = Button(
    frame_2,
    text='-',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('-')
    )

key_sub.pack(expand=True, fill=BOTH, side=LEFT)

key_7 = Button(
    frame_3,
    text='7',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(7)
    )

key_7.pack(expand=True, fill=BOTH, side=LEFT)

key_8 = Button(
    frame_3,
    text='8',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(8)
    )

key_8.pack(expand=True, fill=BOTH, side=LEFT)

key_9 = Button(
    frame_3,
    text='9',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(9)
    )

key_9.pack(expand=True, fill=BOTH, side=LEFT)

key_mul = Button(
    frame_3,
    text='*',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('*')
    )

key_mul.pack(expand=True, fill=BOTH, side=LEFT)


key_clr = Button(
    frame_4,
    text='C',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = clear_scr 
    )

key_clr.pack(expand=True, fill=BOTH, side=LEFT)

key_0 = Button(
    frame_4,
    text='0',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display(0)
    )

key_0.pack(expand=True, fill=BOTH, side=LEFT)

key_res = Button(
    frame_4,
    text='=',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = equal_btn
    )

key_res.pack(expand=True, fill=BOTH, side=LEFT)

key_div = Button(
    frame_4,
    text='/',
    font=('Arial', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = lambda: display('/')
    )

key_div.pack(expand=True, fill=BOTH, side=LEFT)

ws.mainloop()
~~~





[Hra Snake v Pythone s Tkinter](https://www.root.cz/clanky/hra-snake-naprogramovana-v-pythone-s-pomocou-tkinter/)