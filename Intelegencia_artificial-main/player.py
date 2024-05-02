
from vector import Vector

MAX_SPEED = 5

class Player:
    
    def __init__(self):
        self.estado = Vector(0,0)
        self.velocidade = Vector(0,0)
        self.alg_selected = 0        
    
    def __str__(self):
        return f"Player: Estado -> {self.estado}\tVelocidade -> {self.velocidade}"
        
    def aumentaVelocidade(self,vector):
        if not self.velocidade.x >= MAX_SPEED:
            self.velocidade.x += vector.x
        if not self.velocidade.y >= MAX_SPEED:
            self.velocidade.y += vector.y

    
    def jogada(self,jogada):
        self.aumentaVelocidade(jogada)
        self.estado += self.velocidade