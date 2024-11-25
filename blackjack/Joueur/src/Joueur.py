#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Joueur.py
#  Joueur
#  Created by Ingenuity i/o on 2024/11/05
#
# "no description"
#
import ingescape as igs


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Joueur(metaclass=Singleton):
    def __init__(self):
        # attributes
        self.HandA = []
        self.enJeu = False
        
        self.score = 0

        # outputs
        self._ActionO = None

    # outputs
    @property
    def ActionO(self):
        return self._ActionO

    @ActionO.setter
    def ActionO(self, value):
        self._ActionO = value
        if self._ActionO is not None:
            igs.output_set_string("action", self._ActionO)


    def demanderPioche(self,sender_agent_name,sender_agent_uuid):
        arguments_list = ()
        if(self.enJeu):
            igs.service_call("Pioche","tirerCarte",arguments_list,"")
            igs.service_call("Gestionnaire","finTourJoueur",(),"")
        else:
            print("Ce n'est pas votre tour de jouer !")
    
    def rester(self):
        if(self.enJeu):
            print("Vous avez décidé de rester")  
            igs.service_call("Gestionnaire","joueurRester",(),"")
            igs.service_call("Gestionnaire","finTourJoueur",(),"")
        else:
            print("Ce n'est pas votre tour de jouer !")
        
    def ajouterMain(self,carte):
        print(carte)
        nomCarte = carte.split("|")[0]
        nomJoueur = carte.split("|")[1]
        conversion = {"Carreaux":"D","Piques":"S","Cœurs":"H","Trèfles":"C"}
        conversionNom = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "0",
            "Valet": "J", "Dame": "Q", "Roi": "K", "As": "A"}

        print("nom carte",nomCarte,"nom joueur",nomJoueur)

        url = "https://deckofcardsapi.com/static/img/"
        url += str(conversionNom[nomCarte.split(" ")[0]])
        url += conversion[nomCarte.split(" ")[2]]
        url += ".png"
        x=0
        if nomJoueur=="J2":
            x+=400
        x+=len(self.HandA)*30
        igs.service_call("Whiteboard","addImageFromUrl",(url,float(x),50.0),"")

        self.HandA.append(nomCarte)

        self.score = self.calculer_score(self.HandA)
        print("Votre main est désormais : ", self.HandA)
        print("Votre score est désormais : ", self.score)
        
        
        if(self.score > 21):
            print("Vous avez dépassé 21, perdu !")
            igs.service_call("Gestionnaire","defaiteJoueur",(),"")
    
    # Lancer un début de tour
    def jouerTour(self):
        print("C'est votre tour")
        self.enJeu = True
    
    # Finir un tour
    def finTour(self):
        print("Fin de votre tour")
        self.enJeu = False

    # Envoyer son score au gestionnaire
    def donnerScore(self):
        print("envoie du score",self.score)
        igs.output_set_int("score", self.score)

    # Calculer le score actuel en fonction de la main
    def calculer_score(self,main):
        valeurs = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Valet": 10, "Dame": 10, "Roi": 10, "As": 11
        }
        score = 0
        nombre_as = 0
        # Calcul initial du score
        for carte in main:
            valeur_carte = carte.split(" ")[0]  # Extrait la valeur de la carte (e.g., "2", "Valet", "As")
            score += valeurs[valeur_carte]
            if valeur_carte == "As":
                nombre_as += 1

        # Ajuster la valeur des As si nécessaire
        while score > 21 and nombre_as > 0:
            score -= 10
            nombre_as -= 1

        return score 

    # Remettre le joueur à l'état initial
    def reinitialiser(self):
        self.HandA = []
        self.enJeu = False
        self.score = 0