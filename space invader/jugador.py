import pygame

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 5
        self.color = (0, 0, 255)  # Azul
    
    def mover(self, direccion, ancho_pantalla):
        if direccion == "izquierda" and self.x > 0:
            self.x -= self.velocidad
        if direccion == "derecha" and self.x < ancho_pantalla - self.ancho:
            self.x += self.velocidad
    
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
    