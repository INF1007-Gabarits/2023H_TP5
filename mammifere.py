from abc import ABC
from enum import Enum
from typing import List

from animal import Animal


class LongueurPoils(Enum):
    RASES = 0
    COURTS = 1
    LONGS = 2

    def __str__(self):
        return self.name


# TODO Je suis abstraite et j'hérite de Animal
class Mammifere():

    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_MAMMIFERE NOM_MAMMIFERE a NB_PATTES pattes et des poils LONGUEUR_POILS.
        pass


# TODO J'hérite de Mammifere
class Chat():

    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:

    def crier(self) -> str:
        # TODO Retournez le cri du chat: Miaou
        pass
