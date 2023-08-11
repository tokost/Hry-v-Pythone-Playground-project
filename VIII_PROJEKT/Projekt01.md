Doteraz sme programy písali imperatívne - urob tento príkaz, potom tamten
atď. Týmto spôsobom možno písať jednoduché a krátke programy. Väčšia
programy by však boli veľmi neprehľadné. Preto prejdeme na ďalší
programovací paradigma (spôsob ako niečo naprogramovať) - funkcionálne
štýl programovania. Náš program si rozdelíme na menšie časti
(podproblémy), ktoré riešime samostatne. Jednotlivé podproblémy
rieši funkcie. Pre funkcionálne štýl programovania môžeme použiť
všetko, čo sme sa naučili doteraz.

Funkcia zvyčajne prijíma argumenty (dáta, ktoré spracuje) a niečo vracia
- nejakú výslednú hodnotu pod. (Ale aj nemusí vracať nič ako napr. Funkcia
print()).


Ošetrenie chýb 

Vo väčšine programov, čo sme doteraz vytvorili, bola chyba pri vstupe
čísla. Ak sme zadali namiesto čísla napr. Písmeno, tak program spadol.

Teraz si ukážeme, ako takéto chyby ošetriť. Ošetrenie sa vykonáva
pomocou bloku try - except.

Syntax:

try:
    #blok príkazov
except jmeno_prvni_vyjimky:
    #blok príkazov
except jmeno_dalsi_vyjimky:
    #blok príkazov
#tu je buď koniec, alebo zachytenie ďalších výnimiek

Ak chceme zachytiť aj chybovú správu - musíme napísať:

except jmeno_vyjimky as chyba:
    #text výnimky sa uloží do premennej chyba

Chybám sa v Pythone (a v objektových jazykoch všeobecne) hovorí výnimky.
Tie základné sú nasledujúce:


	SyntaxError - chyba v zdrojovom kóde

	ZeroDivisionError - delenie nulou

	TypeError - nesprávne použitie dátových typov - napr.
	Sčítanie reťazca a čísla a pod.

	ValueError - nesprávna hodnota


Viac výnimiek tu (AJ): https://docs.python.org/...eptions.html

A teraz si ešte raz vylepšíme našu kalkulačku:

 Vyskúšať Upraviť Klikni pre editáciu{PYTHON}
print("Kalkulačka\n")
pokracovat = True
while pokracovat:
    prvni_cislo = int(input("Zadajte prvé číslo: "))
    druhe_cislo = int(input("Zadajte druhé číslo: "))
    print("1 - sčítanie")
    print("2 - odčítanie")
    print("3 - násobenie")
    print("4 - delenie")
    print("5 - umocňovanie")
    cislo_operace = int(input("Zadajte číslo operácie: "))
    if cislo_operace == 1:
        print("Ich súčet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Ich rozdiel je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Ich súčin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        print("Ich podiel je:", prvni_cislo / druhe_cislo)
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná voľba!")
    nezadano = True
    while nezadano:
        odpoved = input("\nPrajete si zadať ďalší príklad? y / n: ")
        if (odpoved == "y" or odpoved == "Y"):
            nezadano = False
        elif (odpoved == "n" or odpoved == "n"):
            nezadano = False
            pokracovat = False
        else:
            pass
input("\nStlačte ľubovoľný kláves...")
{/PYTHON}
{PYTHON}
print("Kalkulačka\n")
pokracovat = True
while pokracovat:
    prvni_cislo = int(input("Zadajte prvé číslo: "))
    druhe_cislo = int(input("Zadajte druhé číslo: "))
    print("1 - sčítanie")
    print("2 - odčítanie")
    print("3 - násobenie")
    print("4 - delenie")
    print("5 - umocňovanie")
    cislo_operace = int(input("Zadajte číslo operácie: "))
    if cislo_operace == 1:
        print("Ich súčet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Ich rozdiel je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Ich súčin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        print("Ich podiel je:", prvni_cislo / druhe_cislo)
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná voľba!")
    nezadano = True
    while nezadano:
        odpoved = input("\nPrajete si zadať ďalší príklad? y / n: ")
        if (odpoved == "y" or odpoved == "Y"):
            nezadano = False
        elif (odpoved == "n" or odpoved == "n"):
            nezadano = False
            pokracovat = False
        else:
            pass
input("\nStlačte ľubovoľný kláves...")
{/PYTHON}


Najprv vyrobíme funkciu na získanie čísla zo vstupu od užívateľa:

def nacti_cislo(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo = float(input(text_zadani))
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo

Program sa opakuje v cykle, kým nezadáme správny vstup. Riadok s
float() prevedie reťazec na desatinné číslo.

Ďalej vyrobíme funkciu na vstup "y" alebo
"n":

def dalsi_priklad():
    nezadano = True
    while nezadano:
        odpoved = input("\nPrajete si zadať ďalší príklad? y / n: ")
        if (odpoved == "y" or odpoved == "Y"):
            return True
        elif (odpoved == "n" or odpoved == "N"):
            return False
        else:
            pass

Skoro to isté ...

Ďalší na rade je voľba:

def volba(prvni_cislo, druhe_cislo):
    print("1 - sčítanie")
    print("2 - odčítanie")
    print("3 - násobenie")
    print("4 - delenie")
    print("5 - umocňovanie")
    cislo_operace = nacti_cislo("Zadaj voľbu: ", "Neplatné zadanie!\n")
    if cislo_operace == 1:
        print("Ich súčet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Ich rozdiel je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Ich súčin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        mezivysledek = 0
        try:
            mezivysledek = prvni_cislo / druhe_cislo
            print("Ich podiel je:", mezivysledek)
        except ZeroDivisionError:
            print("Delenie nulou!")
    elif cislo_operace == 5:
        print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
    else:
        print("Neplatná voľba!")

A ošetrenie delenie nulou. Išlo by aj len kontrolovať, či je druhé
číslo 0.

A teraz hlavné cyklus:

def main():
    print("Kalkulačka\n")
    pokracovat = True
    while pokracovat:
        prvni_cislo = nacti_cislo("Zadaj číslo: ", "Neplatné číslo!\n")
        druhe_cislo = nacti_cislo("Zadaj číslo: ", "Neplatné číslo!\n")
        volba(prvni_cislo, druhe_cislo)
        if dalsi_priklad():
            pass
        else:
            pokracovat = False
    input("\nStlačte ľubovoľný kláves...")
main()

Kompletný kód kalkulačky je k dispozícii nižšie na stiahnutie.

V budúcej lekcii, Viacrozmerné polia v Pythone , sa pozrieme na import knižníc a niekoľko si
ich predstavíme. A ukážeme si pythonovská veľkonočné vajíčka 
  

		
    
            
            Mal si s čímkoľvek problém? Stiahni si vzorovú aplikáciu nižšie a porovnaj ju so svojím projektom, chybu tak ľahko nájdeš.
        
    
            Stiahnuť

        Stiahnutím nasledujúceho súboru súhlasíš s licenčnými podmienkami

        
            
                
                Stiahnuť kalkulacka.zip
Zdroj: https://www.itnetwork.sk/python/zaklady/python-tutorial-funkcie-a-vynimky

### Kompletný projekt s GUI, DB SQLite a Tkinter 

Video https://www.youtube.com/watch?v=5qOnzF7RsNA

Zdrojový kód https://github.com/MariyaSha/RandomRecipePicker/tree/main 