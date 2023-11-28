import msvcrt
from time import *

def pm_or_am():
    type = input("Entrez le type d'affichage de l'heure (AM/PM) :")
    return type

def dalarme(heure_alarme,minute_alarme,seconde_alarme,heure,minute,seconde):
    if heure_alarme == heure and minute_alarme == minute and seconde_alarme == seconde:
        print(f"\nL'alarme a soner")

def afficher_heure(heure_base, alarme):
    heure = heure_base[0] ; minute = heure_base[1] ; seconde = heure_base[2]
    heure_alarme = alarme[0] ; minute_alarme = alarme[1] ; seconde_alarme = alarme[2]
    dernier_temps = time()
    affichage = pm_or_am()
    while True:
        #Pour arreter la boucle infinie
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            if key.lower() == 'q':
                print(" La touche 'q' a été enfoncée. Arrêt du programme.")
                break
        temps_actuel = time()
        temps_ecoule = temps_actuel - dernier_temps
        
        #Formate l'Heurre
        if affichage == "AM":
            if heure > 12 :
                heure -=12
            if heure_alarme >12:
                heure_alarme -=12
                
        #Mise a jour de L'Heure
        if temps_ecoule >= 1:
            seconde += 1  
            dernier_temps = temps_actuel  
            if seconde >= 60:
                minute += seconde // 60
                seconde -= 60
                if minute >= 60:
                    heure += minute // 60
                    minute -= 60
                    if heure >= 24:
                        heure -= 24
            print(f"\r\033[K{heure:02d}:{minute:02d}:{seconde:02d}", end="", flush=True)
            
        #D'eclanchement de l'alarme
        dalarme(heure_alarme,minute_alarme,seconde_alarme,heure,minute,seconde)
            
        sleep(1)


heure = (13, 30, 0)
halarme = (13,30,10)
afficher_heure(heure,halarme)