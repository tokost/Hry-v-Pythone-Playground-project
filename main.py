import pygame   # vlozenie kniznice pre tvorbu hier 
import sys      # vlozenie kniznice pre systemove volania ako napr. sys.exit()

# vytvorenie okna hry v ktorom sa to bude vsetko odohravat
     
if __name__ == "__main__":   # je dobrym zvykom na zaciatok dat tuto konstrukciu
                            # ktora ze ked sa bude vykonavat tento subor tak sa bude
                            # vykonavat telo ktore je v podmienke if
    pygame.init()   # INICIALIZACIA FONTU ak sa bude pouzivat font treba hned davat sem
                            
    clock = pygame.time.Clock() # add. 6 implementacia strankovania t.j. zmeny obrazkov zmenou celych
                    # stranok na ktorych sa vytvorene obrazky nachadzaju cize FPS
                            
# pred tym ako pouzijeme nejaky obrazok do nizsie vytvoreneho okna napr. pozadie 
# musime si ho najprv nacitat pred vytvorenim okna
    bg = pygame.image.load("assets/background.jpg")    # add. 3 pred lomitkom je cesta z tohoto adresara

    ship = pygame.image.load("assets/ship.png")        # add. 4 podobne ako v prvom kroku ideme vytvorit lodku
#    ship_coordinates=(220, 720)        # kedze tuto lodku musime niekde umiestnit a budeme s nou hybat dame ju do premennej
    ship_coordinates_x = 220    # kvoli rieseniu pohybu t.j. pridavaniu a uberaniu x sme to rozdelili
    ship_coordinates_y = 720    # a z jedneho riadku vznikli dva jeden pre x a druhy pre y       
    
    meteor =  pygame.image.load("assets/Meteor1.png")    # nacitanie obrazka meteoritu
    meteor_coordinates_x = 220    # priprava na pohyb meteoritu smerom dole z tejto pozicie 
    meteor_coordinates_y = 10     # urobi sa to obdobne iba pridavanim coordinaty y  
    score = 0
    
        # priprava na pocitanie score v pravom hornom rohu v nejakom font-e              
    game_font = pygame.font.SysFont("comicsans", 50)    # bacha musi tam byt zvoleny font nainstalovany, 50 je velkost

# VSETKO NAD TYMTO JE GLOBALNA UROVEN     
    
# 1. VYTVORENIE FIXNEHO co do velkosti OKNA PRE HRU    
    window = pygame.display.set_mode((500, 800))   # prikaz na vytvorenie okna pomocou kniznice pygame v pixloch
                                            # SPUSTENIE SA ROBI PRIKAZOM python main.py - okno iba blikne
    while True:     # DVOJBODKA NA KONCI SA DAVA ked ide o konstrukciu a nasleduje blok prikazov                             
#        pygame.event.get():             # k tomu pre otvorenim musim osetrit stlacenie kriziku v pravom rohu

# 9. GENERUJEME HODNOTU SCORE KTORA SA MUSI TIEZ OBNOVOVAT A PRETO JE PRED 5. A 6.
        score_text = game_font.render(f"Score {score}", True, (255,255,255)) # render umozni vytvorit nieco pomocou fontu
                                        # 3. parameter je farba pomocou RGB
                            # POZOR AK SA NIECO NEZOBRAZUJE ZNAMENA TO ZE TO NENI PRED UPDATE-om napr. tu

# 2. OSETRENIE KRIZIKA T.J. UKONCENIA HRY
        for event in pygame.event.get():     # pomocou for budem prechadzat cez jednotlive eventy
            if event.type == pygame.QUIT:  # a budeme sa pytat ci je event rovny QUIT t.j. ukonceniu
                pygame.quit() # ak je rovny konstante t.j. vnutorne priradenemu cislu pre QUIT tak vypni okno   
                sys.exit()               # ale my potrebujeme sucasne aj beh celej hry v CPU ukoncit

# 6. OVLADANIE LODKY SA ROBI CEZ VSTUPY Z KLAVESNICE
        keys=pygame.key.get_pressed()   # neni to pole je to SLOVNIK a ma hodnotu ano alebo nie t.j.
                                        # slovnik: jednej premennej zodpoveda niekolko hodnoy ano:nie 
                                        # ci je klavesa smerom hore stlacena alebo klav. smerom dole
        if keys[pygame.K_LEFT]:     # riesime stlacenie do lava resp. do prava pomocou K
                                    # K je tiez konstanta tak ako aj ostatne tlacitka
            if ship_coordinates_x > 3:    # musime ale zarucit aby lodka nevybehl az okna t.j. dat obmedzenia
                ship_coordinates_x -= 5   # a pri straceni sa odpocita nejaka hodnota coordinaty napr. 5
            
        if keys[pygame.K_RIGHT]:    # detto pre sipku v pravo len s tym ze pridame 5-ku
           if ship_coordinates_x < 425:
                ship_coordinates_x += 5

# 8. VYTVORIME PADANIE METEORITU t.j vertikalny pohyb podobne ako posuv ktory je horizontalny pohyb

        meteor_coordinates_y += 2
                
# 3. VLOZENIE POZADIA DO OKNA
        window.blit(bg, (0, 0))       # vytvorenemu pozadiu a oknu sme priradili premenne bg a windov
                                    # aby sme s nimi mohli pracovat t.j. ich mohli neustale aktualizovat
                                    # a vlozit obrazok bg do laveho horneho rohu - parameter dest

# 4. VLOZENIE LODKY DO OKNA - OBBRAZKY POZADIA A LODKY SA PREKRYJU S TYM ZE LODKA JE NA POPREDI
#        window.blit(ship, ship_coordinates) # tak ako sme pridali do okna pozadie pridame aj lodku                                 
        window.blit(ship, (ship_coordinates_x, ship_coordinates_y))  # sme to doplnili o zmenu polohy

# 7. ZOBRAZENIE METEORITU
#        window.blit(meteor, (250, 400)) # musi byt pred update-om a zdrzanim ako lod a pod. inac nezobrazi
                                        # iba preblikne a my to ani nezbadame ako keby ho tam nedal !!!
        window.blit(meteor, (meteor_coordinates_x, meteor_coordinates_y))   # posunieme ho hore lebo musi padat
# 10. VLOZENIE SKORE KTORE JE BIELE DO OKNA        
        window.blit(score_text, (250, 30)) # 2. parameter je pozicia kde bude ulozeny
                                            # aby nebola chyba treba font inicializovat


# 5. ZABEZPECENIE OBNOVY OKNA S OBRAZKAMI ABY SA VYTVORIL DOJEM STALOSTI A NEPREBLIKAVALO TO
        pygame.display.update()             # aby neprebliklo a zostalo tak dookola prikaz updatujem
 
# 6. NASTAVENIE ZDRZANIA 60 TIKOV POCAS KTOREHO SA 60x ZMENI OBRAZOK A EV. SA VYTVORI SA ILUZIA POHYBU
        clock.tick(60)   # umistnime sem na koniec to strankovanie ktore sa robi cez hodiny
                            # tato funkcia iba caka aby sa napr. 60x t.j. za 1sec. zmenil obr.
                            
# skusam git lokalne
# a pokracujem v skusani
  
  
    