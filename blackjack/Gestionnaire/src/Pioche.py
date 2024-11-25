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
        self.pioche = [
    "2 de ♠️", "3 de ♠️", "4 de ♠️", "5 de ♠️", "6 de ♠️", "7 de ♠️", "8 de ♠️", "9 de ♠️", "10 de ♠️", "Valet de ♠️", "Dame de ♠️", "Roi de ♠️", "As de ♠️",
    "2 de ♥️", "3 de ♥️", "4 de ♥️", "5 de ♥️", "6 de ♥️", "7 de ♥️", "8 de ♥️", "9 de ♥️", "10 de ♥️", "Valet de ♥️", "Dame de ♥️", "Roi de ♥️", "As de ♥️",
    "2 de ♦️", "3 de ♦️", "4 de ♦️", "5 de ♦️", "6 de ♦️", "7 de ♦️", "8 de ♦️", "9 de ♦️", "10 de ♦️", "Valet de ♦️", "Dame de ♦️", "Roi de ♦️", "As de ♦️",
    "2 de ♣️", "3 de ♣️", "4 de ♣️", "5 de ♣️", "6 de ♣️", "7 de ♣️", "8 de ♣️", "9 de ♣️", "10 de ♣️", "Valet de ♣️", "Dame de ♣️", "Roi de ♣️", "As de ♣️"
]
        self.CartesA = None

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

    # services
    def Tirercarte(self):
        random.shuffle(self.pioche)
        carte = self.pioche.pop()
        return carte


