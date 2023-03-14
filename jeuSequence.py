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
        self.niveau_pause = 0.5
        self.partie_en_cours = False
        self.led_bleu = Pin(13, Pin.OUT)
        self.led_rouge = Pin(12, Pin.OUT)
        self.led_vert = Pin(10, Pin.OUT)
        self.btn_bleu = Pin(16, Pin.IN, Pin.PULL_UP)
        self.btn_rouge = Pin(17, Pin.IN, Pin.PULL_UP)
        self.btn_vert = Pin(18, Pin.IN, Pin.PULL_UP)
    
    