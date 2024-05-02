
from player import Player
from mapa import *
from vector import Vector
from resolver import Resolver
from grafo import Graph
from interface import *



import time

JOGADAS = [
    Vector(-1, -1),
    Vector(-1, 0),
    Vector(0, -1),
    Vector(0, 0),
    Vector(0, 1),
    Vector(1, 0),
    Vector(1, 1),
    Vector(-1, 1),
    Vector(1, -1),
]


class Jogo:

    def __init__(self):
        self.players = []
        self.n_players = 0
        self.run = True

    def proximasJogadas(self, player):
        """Cria tds as possiveis proximas coordenadas a partir do estado e velocidade do jogador

        Returns:
            Player: Jogador sbr o qual se vai criar as coordenadas
        """
        proximasJogadas = []

        for jogada in JOGADAS:
            proximasJogadas.append(player.estado + player.velocidade + jogada)

        return proximasJogadas

    def addPlayer(self, player):
        self.players.append(player)

    def getPlayers(self):
        return [self.players[i] for i in range(self.n_players)]

    def resetPlayers(self, mapa):
        for player in self.players:
            player.estado = mapa.start
            player.velocidade = Vector(0, 0)

