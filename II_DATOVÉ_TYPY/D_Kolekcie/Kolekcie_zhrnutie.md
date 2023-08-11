## Kolekcie - zhrnutie

>### Pointa: kedy použiť zoznam, kedy n-ticu, kedy množinu a kedy slovník ? 

**Tu je NÁVOD:**

Kolekcie jazyka Python (všeobecne polia)

V programovacom jazyku Python existujú štyri typy údajov kolekcie:

**List - zoznam** je kolekcia, ktorá je ***usporiadaná a meniteľná***. Umožňuje duplicitné prvky.\
**Tuple - n-tica** je kolekcia, ktorá je ***usporiadaná a nemenitelná***. Umožňuje duplicitné členy.\
**Set - Množina** je kolekcia, ktorá je ***neusporiadaná, nemeniteľná a neindexovaná***. Žiadni duplicitní členovia. Aj keď sú položky sady nemenné, môžete ich ale kedykoľvek odstrániť a/alebo pridať\
**Dictionary - Slovník** je kolekcia, ktorá je ***usporiadaná a vymeniteľná**. Žiadni duplicitní členovia.\

> Pri výbere typu kolekcie je užitočné pochopiť vyššie uvedené vlastnosti každého typu.

Výber správneho typu pre konkrétny súbor údajov môže znamenať zachovanie významu poľa a môže znamenať zvýšenie efektívnosti alebo bezpečnosti kódu.

Vložiť sem príklady na nazorné ukážky !

>### Pointa: kedy použiť zoznam, kedy n-ticu, kedy množinu a kedy slovník ? 

**Tu je NÁVOD:**

rozhodujú priority kritérii ne/usporiadaná a ne/menitelná

* ak má byť **neusporiadaná**
    * alebo nemenitelná -> **set**
    * a menitelná -> **dictionary**
    
* ak má má byť **usporiadaná**
    * alebo nemenitelná -> **tuple** 
    * a menitelná -> **list**
     
  

