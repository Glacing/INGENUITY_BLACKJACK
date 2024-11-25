#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Pioche.py
#  Pioche
#  Created by Ingenuity i/o on 2024/11/05
#
# "no description"
#
import ingescape as igs
import random

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Pioche(metaclass=Singleton):
    def __init__(self):
        # attributes
        self.CartesA = None
        self.Cartes = [
            "2 de Piques", "3 de Piques", "4 de Piques", "5 de Piques", "6 de Piques", "7 de Piques", "8 de Piques", "9 de Piques", "10 de Piques", "Valet de Piques", "Dame de Piques", "Roi de Piques", "As de Piques",
            "2 de Cœurs", "3 de Cœurs", "4 de Cœurs", "5 de Cœurs", "6 de Cœurs", "7 de Cœurs", "8 de Cœurs", "9 de Cœurs", "10 de Cœurs", "Valet de Cœurs", "Dame de Cœurs", "Roi de Cœurs", "As de Cœurs",
            "2 de Carreaux", "3 de Carreaux", "4 de Carreaux", "5 de Carreaux", "6 de Carreaux", "7 de Carreaux", "8 de Carreaux", "9 de Carreaux", "10 de Carreaux", "Valet de Carreaux", "Dame de Carreaux", "Roi de Carreaux", "As de Carreaux",
            "2 de Trèfles", "3 de Trèfles", "4 de Trèfles", "5 de Trèfles", "6 de Trèfles", "7 de Trèfles", "8 de Trèfles", "9 de Trèfles", "10 de Trèfles", "Valet de Trèfles", "Dame de Trèfles", "Roi de Trèfles", "As de Trèfles"
        ]
        # outputs
        self._CarteO = None

    # outputs
    @property
    def CarteO(self):
        return self._CarteO

    @CarteO.setter
    def CarteO(self, value):
        self._CarteO = value
        if self._CarteO is not None:
            igs.output_set_string("carte", self._CarteO)

    # Tirer une carte du paquet
    def Tirercarte(self,sender_agent_name,sender_agent_uuid):
        random.shuffle(self.Cartes)
        carte = self.Cartes.pop()
        return carte
    
    # Remettre la pioche en état initial
    def reinitialiser(self):
        self.CartesA = None
        self.Cartes = [
            "2 de Piques", "3 de Piques", "4 de Piques", "5 de Piques", "6 de Piques", "7 de Piques", "8 de Piques", "9 de Piques", "10 de Piques", "Valet de Piques", "Dame de Piques", "Roi de Piques", "As de Piques",
            "2 de Cœurs", "3 de Cœurs", "4 de Cœurs", "5 de Cœurs", "6 de Cœurs", "7 de Cœurs", "8 de Cœurs", "9 de Cœurs", "10 de Cœurs", "Valet de Cœurs", "Dame de Cœurs", "Roi de Cœurs", "As de Cœurs",
            "2 de Carreaux", "3 de Carreaux", "4 de Carreaux", "5 de Carreaux", "6 de Carreaux", "7 de Carreaux", "8 de Carreaux", "9 de Carreaux", "10 de Carreaux", "Valet de Carreaux", "Dame de Carreaux", "Roi de Carreaux", "As de Carreaux",
            "2 de Trèfles", "3 de Trèfles", "4 de Trèfles", "5 de Trèfles", "6 de Trèfles", "7 de Trèfles", "8 de Trèfles", "9 de Trèfles", "10 de Trèfles", "Valet de Trèfles", "Dame de Trèfles", "Roi de Trèfles", "As de Trèfles"
        ]


