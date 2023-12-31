from machine import Pin
from time import sleep
import random

class Partie():
    "classe qui comprend les informations sur la partie "
   
    # Constructeur de la classe
    def __init__(self):
        self.nomJoueur = ""
        self.pointage = 0
        self.sequence_en_cours = []
        self.sequence_joueur = []
        self.niveau_pause = 0.5
        self.partie_en_cours = False
        self.led_bleu = Pin(13, Pin.OUT)
        self.led_rouge = Pin(12, Pin.OUT)
        self.led_vert = Pin(10, Pin.OUT)
        self.btn_bleu = Pin(16, Pin.IN, Pin.PULL_UP)
        self.btn_rouge = Pin(17, Pin.IN, Pin.PULL_UP)
        self.btn_vert = Pin(18, Pin.IN, Pin.PULL_UP)
    
    def afficherPartie(self):
        print("Votre nom : "+ self.nomJoueur)
        print("Votre pointage : " + str(self.pointage) + " points")
             
    def affichage_regles(self):
        print("|------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|                                          Travail pratique 2 - Jeux séquence - Abdelhadi Mejdoubi                                                                 |")
        print("|------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("| Le principe du jeu est de reproduire une séquence de lumières LED donnée par l’ordinateur.                                                                       |")
        print("| Quand la séquence est réussie par le joueur, une nouvelle séquence de lumières LED est donnée par l’ordinateur en ajoutant une lumière LED de plus aléatoirement.|")
        print("| Et ainsi de suite jusqu’à ce que le joueur atteigne le maximum de 20 séquences ou que le joueur se trompe dans la séquence.                                      |")          
        print("|------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("")
    
    def niveau_difficulte(self):
        print("")
        print("Veuillez choisir un niveau:")
        print("Bouton bleu: facile (pause = 1 seconde)")
        print("Bouton rouge: intermédiaire (pause = 0.5 seconde)")
        print("Bouton vert: difficile (pause = 0.25 seconde)")
        print("")
        while True:
            if not self.btn_bleu.value():
                self.niveau_pause = 1
                print("Vous avez choisi le niveau facile.")
                print("")
                break
            elif not self.btn_rouge.value():
                self.niveau_pause = 0.5
                print("Vous avez choisi le niveau intermédiaire.")
                print("")
                break
            elif not self.btn_vert.value():
                self.niveau_pause = 0.25
                print("Vous avez choisi le niveau difficile.")
                print("")
                break            
    
    def clignotage_LED(self):
        for i in range(3):
            self.led_bleu.value(1)
            self.led_rouge.value(1)
            self.led_vert.value(1)
            sleep(0.5)
            self.led_bleu.value(0)
            self.led_rouge.value(0)
            self.led_vert.value(0)
            sleep(0.5)
 
    def nouvelle_sequence(self):
        self.sequence_en_cours.append(random.choice(["bleu", "rouge", "vert"]))
        print("Séquence numéro", str(len(self.sequence_en_cours)))  
        sleep(self.niveau_pause)
        for couleur in self.sequence_en_cours:
            if couleur == "bleu":
                self.led_bleu.value(1)
                sleep(self.niveau_pause)
                self.led_bleu.value(0)
                sleep(self.niveau_pause)
            elif couleur == "rouge":
                self.led_rouge.value(1)
                sleep(self.niveau_pause)
                self.led_rouge.value(0)
                sleep(self.niveau_pause)
            elif couleur == "vert":
                self.led_vert.value(1)
                sleep(self.niveau_pause)
                self.led_vert.value(0)
                sleep(self.niveau_pause)
                
    def jouer(self):
        # Affichage des règles et du nom du joueur
        self.affichage_regles()
        self.nomJoueur = input("Veuillez entrer votre nom : ")
        # Demander le niveau de difficulté
        self.niveau_difficulte()
        
        # Début de la partie
        self.partie_en_cours = True
        while self.partie_en_cours and len(self.sequence_en_cours) < 20:
            self.nouvelle_sequence()
            # Attendre la réponse du joueur
            self.sequence_joueur = []
            for i in range(len(self.sequence_en_cours)):
                while True:
                    if not self.btn_bleu.value():
                        self.sequence_joueur.append("bleu")
                        self.led_bleu.value(1)
                        sleep(self.niveau_pause)
                        self.led_bleu.value(0)
                        break
                    elif not self.btn_rouge.value():
                        self.sequence_joueur.append("rouge")
                        self.led_rouge.value(1)
                        sleep(self.niveau_pause)
                        self.led_rouge.value(0)
                        break
                    elif not self.btn_vert.value():
                        self.sequence_joueur.append("vert")
                        self.led_vert.value(1)
                        sleep(self.niveau_pause)
                        self.led_vert.value(0)
                        break
                        
            # Vérifier si la réponse est correcte
            if self.sequence_joueur == self.sequence_en_cours:
                self.pointage += 1
                print("Bonne réponse !")
                print("")
                if(self.pointage == 20):
                    print("Bravo, vous avez réussi le jeu Simon")
                    print("")
            else:
                self.partie_en_cours = False
                print("Mauvaise réponse. La partie est terminée.")
                print("")
                
        # Clignotage des LED pour signaler la fin de partie si le joueur a fait une erreur ou s'il a atteint le nombre maximum de séquence
        self.clignotage_LED()
        
        # Affichage du nom du joueur et le pointage final
        self.afficherPartie()
        
        # Vider la sequence à la fin de la partie et mettre le pointage à 0
        self.sequence_en_cours = []
        self.pointage = 0
        
        # Demander au joueur s'il veut recommencer une partie
        while True:
            print("")
            reponse = input("Voulez-vous recommencer une partie ? (Oui/Non) : ")
            if reponse.lower() == "oui":
                self.jouer()
                break
            elif reponse.lower() == "non":
                self.partie_en_cours = False
                break
            else:
                print("Veuillez répondre par 'Oui' ou 'Non'.")
partie  = Partie()
partie.jouer()  