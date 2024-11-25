#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Gestionnaire.py
#  Gestionnaire
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


class Gestionnaire(metaclass=Singleton):
    def __init__(self):
        
        #Stocke si chaque joueur est dans la partie ou non
        self.stateJoueurs=[True,True]
        self.scores=[0,0]
        
        self._WhiteboardoutputO = None

    # outputs
    @property
    def WhiteboardoutputO(self):
        return self._WhiteboardoutputO

    @WhiteboardoutputO.setter
    def WhiteboardoutputO(self, value):
        self._WhiteboardoutputO = value
        if self._WhiteboardoutputO is not None:
            igs.output_set_string("whiteboardOutput", self._WhiteboardoutputO)

    # Lancer une partie
    def Lancerpartie(self):
        igs.service_call("J1","reinitialiser",(),"")
        igs.service_call("J2","reinitialiser",(),"")
        self.stateJoueurs=[True,True]
        self.scores=[0,0]
        igs.output_set_impulsion("clear")

        igs.service_call("J1","jouerTour",(),"")
        igs.output_set_string("whiteboardOutput", "Tour de J1") 
        igs.output_set_string("whiteboardColor", "#308834")     
        igs.service_call("Whiteboard","addText",("Main de J1",10.0,0,"red"),"")
        igs.service_call("Whiteboard","addText",("Main de J2",400.0,0,"black"),"")

    
    def Donnermain(self, sender_agent_name, sender_agent_uuid):
        carte = self.pioche.Tirercarte()
        return carte
    
    # Gérer la fin d'un tour
    def finTourJoueur(self,sender_agent_name):
        print("fin tour",sender_agent_name)
        #Check si les deux restent
        if(self.stateJoueurs[0]==False and self.stateJoueurs[1]==False):
            igs.service_call("J1","donnerScore",(),"")
            
        else:
            if(sender_agent_name=="J1"):
                igs.service_call("J1","finTour",(),"")
                #Check si J2 reste
                if self.stateJoueurs[1]:
                    igs.service_call("J2","jouerTour",(),"")
                    igs.output_set_string("whiteboardOutput", "Tour de J2") 
                else:
                    igs.service_call("J1","jouerTour",(),"")
                    igs.output_set_string("whiteboardOutput", "Tour de J1")    
            else:
                igs.service_call("J2","finTour",(),"")
                #Check si J1 reste
                if self.stateJoueurs[0]:
                    igs.service_call("J1","jouerTour",(),"")
                    igs.output_set_string("whiteboardOutput", "Tour de J1") 
                else:
                    igs.service_call("J2","jouerTour",(),"")
                    igs.output_set_string("whiteboardOutput", "Tour de J2") 

    # Finir la partie
    def defaiteJoueur(self,sender_agent_name):
        igs.service_call("J1","finTour",(),"")
        igs.service_call("J2","finTour",(),"")
        if(sender_agent_name=="J1"):
            igs.output_set_string("whiteboardOutput", "Victoire de J2")
        else:
            igs.output_set_string("whiteboardOutput", "Victoire de J1")


    # Sortir un joueur du jeu si il décide d'arrêter
    def joueurRester(self,sender_agent_name):
        if(sender_agent_name=="J1"):
            self.stateJoueurs[0]=False
            igs.output_set_string("whiteboardChat", "J1 a décidé d'en rester là")
        else:
            self.stateJoueurs[1]=False
            igs.output_set_string("whiteboardChat", "J2 a décidé d'en rester là")

    # Mettre à jouer le score de J1
    def setScoreJ1(self,value):
        print("Score j1",value)
        self.scores[0]=int(value)
        igs.service_call("J2","donnerScore",(),"")

    # Mettre à jouer le score de J2
    def setScoreJ2(self,value):
        print("Score j2",value)
        self.scores[1]=int(value)
        self.findWinner()

    # Vérifier qui a gagné
    def findWinner(self):
        print(self.scores)
        if self.scores[0] > self.scores[1]:
            igs.output_set_string("whiteboardOutput", "Victoire de J1 !")
        elif self.scores[1] > self.scores[0]:
            igs.output_set_string("whiteboardOutput", "Victoire de J2 !")
        else:
            igs.output_set_string("whiteboardOutput", "Egalite !")