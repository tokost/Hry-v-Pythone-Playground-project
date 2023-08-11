Funkcie rozdelenie pokračovanie

## Časové funkcie

Python definoval modul „time“, ktorý nám umožňuje vykonávať rôzne operácie týkajúce sa času, jeho konverzií a reprezentácií, ktoré nachádzajú svoje využitie v rôznych aplikáciách v živote. Začiatok času sa začal merať od 1. januára, 00:00, 1970 a práve tento čas sa v Pythone označuje ako „ epocha“.

>### Operácie s časom v Pythone 

### Funkcia time.time()

Pythonovská funkcia time() sa používa na počítanie počtu sekúnd, ktoré uplynuli od začiatku epochy. 
~~~

# Python code to demonstrate the working of
# time()

# importing "time" module for time operations
import time

# using time() to display time since epoch
print ("Seconds elapsed since the epoch are : ",end="")
print (time.time())
~~~

### Funkcia time.gmtime().

Funkcia Pythonu gmtime() vracia štruktúru s 9 hodnotami, z ktorých každá predstavuje časový atribút v poradí. Prevádza sekundy na časové atribúty (dni, roky, mesiace atď.) do špecifikovaných sekúnd od epochy. Ak nie sú uvedené žiadne sekundy, čas sa počíta do súčasnosti. Tabuľka atribútov štruktúry je uvedená nižšie. 
~~~
Hodnoty atribútov indexu
 0 tm_rok 2008
 1 tm_mon 1 až 12
 2 tm_mday 1 až 31
 3 tm_hour 0 až 23
 4 tm_min 0 až 59
 5 tm_sec 0 až 61 (60 alebo 61 sú prestupné sekundy)
 6 tm_wday 0 až 6
 7 tm_yday 1 až 366
 8 tm_isdst -1, 0, 1, kde -1 znamená, že knižnica určuje DST
~~~
~~~
# Python code to demonstrate the working of gmtime()

import time

# using gmtime() to return the time attribute structure
print ("Time calculated acc. to given seconds is : ")
print (time.gmtime())

Vysledok:
Time calculated acc. to given seconds is : 
time.struct_time(tm_year=2016, tm_mon=8, tm_mday=2,
tm_hour=7, tm_min=12, tm_sec=31, tm_wday=1, 
tm_yday=215, tm_isdst=0)
~~~

### Funcie time.asctime() a time.ctime()

Funkcia Pythonu time.asctime() berie časovo priradený reťazec vytvorený gmtime() a vracia 24-znakový reťazec označujúci čas . Funkcia Pythonu time.ctime() vracia 24-znakový časový reťazec , ale ako argument berie sekundy a počíta čas do uvedených sekúnd . Ak neprejde žiadny argument, čas sa počíta do súčasnosti.
~~~
# Python code to demonstrate the working of
# asctime() and ctime()

# importing "time" module for time operations
import time
                      
# initializing time using gmtime()
ti = time.gmtime()
                      
# using asctime() to display time acc. to time mentioned
                      
print ("Time calculated using asctime() is : ",end="")
print (time.asctime(ti))
                      
# using ctime() to display time string using seconds
                      
print ("Time calculated using ctime() is : ", end="")
print (time.ctime())

Vysledok:

Time calculated using asctime() is : Tue Aug  2 07:47:02 2016
Time calculated using ctime() is : Tue Aug  2 07:47:02 2016
~~~

### Funkcia time.sleep()
Táto metóda sa používa na zastavenie vykonávania programu na čas špecifikovaný v argumentoch.
~~~
# Python code to demonstrate the working of
# sleep()
                      
# importing "time" module for time operations
import time
                      
# using ctime() to show present time
print ("Start Execution : ",end="")
print (time.ctime())
                      
# using sleep() to hault execution
time.sleep(4)
                      
# using ctime() to show present time
print ("Stop Execution : ",end="")
print (time.ctime())
                      
Vysledok :

Start Execution : Tue Aug  2 07:59:03 2016
Stop Execution : Tue Aug  2 07:59:07 2016
~~~

### Funkcia time.mktime()
V tomto príklade sme vytvorili objekt struct_time s n-ticou hodnôt pre každé z jeho polí, potom sme objekt odovzdali do time.mktime () , aby sme ho skonvertovali na číslo s pohyblivou rádovou čiarkou predstavujúce počet sekúnd epochy.
~~~
import time
                      
# Create a struct_time object representing a date and time
my_time = time.strptime("2023-05-10 14:30:00", "%Y-%m-%d %H:%M:%S")
                      
# Convert the struct_time object to a floating-point number seconds_since_epoch = time.mktime(my_time)
print("Seconds since epoch:", seconds_since_epoch)
                      
Vysledok:

Seconds since epoch: 1683709200.0
~~~

### Funkcia time.localtime()
V tomto príklade voláme time.localtime() bez argumentu, aby sme získali aktuálny miestny čas ako struct_time.
~~~
import time
                      
current_time = time.localtime()
                      
print(current_time)
                      
Vysledok:

time.struct_time(tm_year=2023, tm_mon=5, tm_mday=10,
tm_hour=12, tm_min=42, tm_sec=51, tm_wday=2, tm_yday=130, tm_isdst=0)
~~~

### Funkcia time.strftime().
Ako prvý argument berie formátovací reťazec, ktorý špecifikuje požadovaný formát výstupného reťazca.
~~~
import time
                      
now = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(formatted_time)
                      
Vysledok:

2023-05-10 13:42:04
~~~

>### Operácie s dátumom v Pythone 

Aj v Pythone je možná manipulácia s dátumom. Uskutočňuje sa to pomocou modulu „datetime“ a použitím jej triedy „date“. Prito je možné použiť aj dve konštanty MINYEAR a MAXYEAR.

###  konštanta MINYEAR 

MINYEAR zobrazuje minimálny rok , ktorý je možné poznať pomocou triedy dátumu.

### MAXYEAR
MAXYEAR zobrazuje prvý rok , ktorý môže byť vyjadrený pomocou triedy dátumu.
~~~
# Python code to demonstrate the working of
                   
# MINYEAR and MAXYEAR
                   
# importing built in module datetime
import datetime
                   
from datetime import date
                   
# using MINYEAR to print minimum representable year
print ("Minimum representable year is : ",end="")
print (datetime.MINYEAR)
                   
# using MAXYEAR to print maximum representable year
print ("Maximum representable year is : ",end="")
print (datetime.MAXYEAR)
                   
Vysledok:

Minimum representable year is : 1
Maximum representable year is : 9999
~~~

### Funkcia date(yyyy-mm-dd)
Táto funkcia vracia reťazec s odovzdanými argumentmi v poradí rok, mesiace a dátum.

### Funkcia today()
Vráti dátum súčasného dňa vo formáte rrrr-mm-dd.
~~~
# Python code to demonstrate the working of
# date() and today()
                   
 # importing built in module datetime
import datetime
                   
from datetime import date
                   
# using date() to represent date
print ("The represented date is : ",end="")
print (datetime.date(1997,4,1))
                   
# using today() to print present date
print ("Present date is : ",end="")
print (date.today())
                   
Vysledok:

The represented date is : 1997-04-01
Present date is : 2016-08-02
~~~

### Funkcia fromtimestamp(sec)
Vráti dátum vypočítaný z dvoch , ktoré uplynuli od epoch uvedených v argumentoch.

### Funkcia min()
Vráti minimálny dátum , ktorý môže byť reprezentovaný osvedčeným dátumom.

### Funkcia max()
Vráti prvý dátum , ktorý môže byť reprezentovaný osvedčeným dátumom.
~~~
# Python code to demonstrate the working of
# fromtimestamp(), min() and max()
                   
# importing built in module datetime
import datetime
from datetime import date
                   
# using fromtimestamp() to calculate date
print ("The calculated date from seconds is : ",end="")
print (date.fromtimestamp(3452435))
                   
# using min() to print minimum representable date
print ("Minimum representable date is : ",end="")
print (date.min)
                   
# using max() to print minimum representable date
print ("Maximum representable date is : ",end="")
print (date.max)
                   
Vysledok:

The calculated date from seconds is : 1970-02-09
Minimum representable date is : 0001-01-01
Maximum representable date is : 9999-12-31
~~~

>### Operácie s kalendárom

### Funkcie calendar(), month(), isleap()…

Python definuje vstavaný modul „ calendar “, ktorý spracováva operácie súvisiace s kalendárom.
Operácie s kalendárom : 
1. **calendar(year, w, l, c )** - Táto funkcia zobrazuje rok, šírku znakov, č. riadkov za týždeň a separácie stĺpcov.
2. **firstweekday()** - Táto funkcia vráti číslo dňa prvého týždňa . Štandardne 0 (pondelok).
~~~

                      # Python code to demonstrate the working of
                     

                      # calendar() and firstweeksday()
                     

                      
                     

                      # importing calendar module for calendar operations
                     

                      import calendar
                     

                      
                     

                      # using calendar to print calendar of year
                     

                      # prints calendar of 2012
                     

                      print ("The calendar of year 2012 is : ")
                     

                      print (calendar.calendar(2012,2,1,6))
                     

                      
                     

                      #using firstweekday() to print starting day number
                     

                      print ("The starting day number in calendar is : ",end="")
                     

                      print (calendar.firstweekday())
                     

Vystup:

The calendar of year 2012 is : 
                                  2012

      January                   February                   March
Po Ut St Št Pi So Ne Po Ut St Št So Ne Po Ut St Št Pi So Ne
                   1 1 2 3 4 5 1 2 3 4
 2 3 4 5 6 7 8 6 7 8 9 10 11 12 5 6 7 8 9 10 11
 9 10 11 12 13 14 15 13 14 15 16 17 18 19 12 13 14 15 16 17 18
16 17 18 19 20 21 22 20 21 22 23 24 25 26 19 20 21 22 23 24 25
23 24 25 26 27 28 29 27 28 29 26 27 28 29 30 31
30 31

       apríl máj jún
Po Ut St Št Pi So Ne Po Ut St Št So Ne Po Ut St Št Pi So Ne
                   1 1 2 3 4 5 6 1 2 3
 2 3 4 5 6 7 8 7 8 9 10 11 12 13 4 5 6 7 8 9 10
 9 10 11 12 13 14 15 14 15 16 17 18 19 20 11 12 13 14 15 16 17
16 17 18 19 20 21 22 21 22 23 24 25 26 27 18 19 20 21 22 23 24
23 24 25 26 27 28 29 28 29 30 31 25 26 27 28 29 30
30

        júl august september
Po Ut St Št Pi So Ne Po Ut St Št So Ne Po Ut St Št Pi So Ne
                   1 1 2 3 4 5 1 2
 2 3 4 5 6 7 8 6 7 8 9 10 11 12 3 4 5 6 7 8 9
 9 10 11 12 13 14 15 13 14 15 16 17 18 19 10 11 12 13 14 15 16
16 17 18 19 20 21 22 20 21 22 23 24 25 26 17 18 19 20 21 22 23
23 24 25 26 27 28 29 27 28 29 30 31 24 25 26 27 28 29 30
30 31

      október november december
Po Ut St Št Pi So Ne Po Ut St Št So Ne Po Ut St Št Pi So Ne
 1 2 3 4 5 6 7 1 2 3 4 1 2
 8 9 10 11 12 13 14 5 6 7 8 9 10 11 3 4 5 6 7 8 9
15 16 17 18 19 20 21 12 13 14 15 16 17 18 10 11 12 13 14 15 16
22 23 24 25 26 27 28 19 20 21 22 23 24 25 17 18 19 20 21 22 23
29 30 31 26 27 28 29 30 24 25 26 27 28 29 30
                                                    31

Počiatočné číslo dňa v kalendári je: 0
~~~

3. **isleap (year)** - Táto funkcia kontroluje, či je rok uvedený v argumente skokový alebo nie .
4. **leapdays (year1, year2)** - Táto funkcia vráti počet prestupných dní medzi zadanými rokmi v argumentoch.
~~~

                      # Python code to demonstrate the working of
                     

                      # isleap() and leapdays()
                     

                      
                     

                      # importing calendar module for calendar operations
                     

                      import calendar
                     

                      
                     

                      # using isleap() to check if year is leap or not
                     

                      if (calendar.isleap(2008)):
                     

                      	print ("The year is leap")
                     

                      else : print ("The year is not leap")
                     

                      
                     

                      #using leapdays() to print leap days between years
                     

                      print ("The leap days between 1950 and 2000 are : ",end="")
                     

                      print (calendar.leapdays(1950, 2000))
                     
Vysledok:

The year is leap
The leap days between 1950 and 2000 are : 12
~~~

5. **month (year, month, w, l)** - Táto funkcia vytlačí mesiac konkrétneho roka uvedeného v argumentoch. Na to sú potrebné 4 argumenty, rok, mesiac, šírka znakov a nie. riadkov zaberaných za týždeň .
~~~

                      # Python code to demonstrate the working of
                     

                      # month()
                     

                      
                     

                      # importing calendar module for calendar operations
                     

                      import calendar
                     

                      
                     

                      # using month() to display month of specific year
                     

                      print ("The month 5th of 2016 is :")
                     

                      print (calendar.month(2016,5,2,1))
                     
Vysledok:

Piaty mesiac 2016 je:
      máj 2016
Po Ut St Št Pá So Ne
                   1
 2 3 4 5 6 7 8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
~~~
Video k tomu najdete na https://youtu.be/sZoW6hXxADM 

### Ďalšie funkcie kalendára (monthrange(), prcal(), weekday()…
1. **monthrange(year, month)** - Táto funkcia vráti dve celé čísla, prvé, počiatočné číslo dňa v týždni (0 ako pondelok), druhé, počet dní v mesiaci .

2. **prcal(rok, š, d, c)** - Táto funkcia tiež vytlačí kalendár konkrétneho roka, ale nie je potrebná operácia „print“.
~~~

                    # Python code to demonstrate the working of
                   

                    # monthrange() and prcal()
                   

                    
                   

                    # importing calendar module for calendar operations
                   

                    import calendar
                   

                    
                   

                    # using monthrange() to print start week day and
                   

                    # number of month
                   

                    print ("The start week number and no. of days of month : ",end="")
                   

                    print (calendar.monthrange(2008, 2))
                   

                    
                   

                    # using prcal() to print calendar of 1997
                   

                    print ("The calendar of 1997 is : ")
                   

                    calendar.prcal(1997, 2,1,6)
                   
Vysledok:

The start week number and no. of days of month : (4, 29)
The calendar of 1997 is : 
                                  1997

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                      1  2
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9
13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16
20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23
27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30
                                                    31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                1  2  3  4                         1
 7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8
14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15
21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22
28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
28 29 30 31               25 26 27 28 29 30 31      29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
27 28 29 30 31            24 25 26 27 28 29 30      29 30 31
~~~

3. **prmonth(year, month, w, l)** - Táto funkcia vytlačí aj mesiac konkrétneho roka , ale nie je potrebná operácia „print“.
~~~

~~~

4. **setfirstweekday(num)** - Táto funkcia nastavuje počiatočné číslo dňa v týždni.
~~~

                    # Python code to demonstrate the working of
                   

                    # prmonth() and setfirstweekday()
                   

                    
                   

                    # importing calendar module for calendar operations
                   

                    import calendar
                   

                    
                   

                    # using prmonth() to print calendar of 1997
                   

                    print ("The 4th month of 1997 is : ")
                   

                    calendar.prmonth(1997, 4, 2, 1)
                   

                    
                   

                    
                   

                    # using setfirstweekday() to set first week day number
                   

                    calendar.setfirstweekday(4)
                   

                    
                   

                    print ("\r")
                   

                    
                   

                    # using firstweekday() to check the changed day
                   

                    print ("The new week day number is : ",end="")
                   

                    print (calendar.firstweekday())
                   
Vysledok:

The 4th month of 1997 is : 
     April 1997
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
 
The new week day number is : 4
~~~

5. **weekday(year, month, date)** - Táto funkcia vráti číslo dňa v týždni (0 je pondelok) dňa uvedeného v jej argumentoch.
~~~

                    # Python code to demonstrate the working of
                   

                    # weekday()
                   

                    
                   

                    # importing calendar module for calendar operations
                   

                    import calendar
                   

                    
                   

                    # using weekday() to print day number of date
                   

                    print ("The day number of 25 April 1997 is : ",end="")
                   

                    print (calendar.weekday(1997,4,25))
                   
Vysledok:

The day number of 25 April 1997 is : 4
~~~
Video k tomu najdete na https://youtu.be/sZoW6hXxADM 
