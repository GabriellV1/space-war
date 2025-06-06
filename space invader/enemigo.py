import random
import pygame

class Enemigo:
    def __init__(self, ancho_pantalla):
        self.ancho = 40
        self.alto = 40
        self.x = random.randint(0, ancho_pantalla - self.ancho)
        self.y = random.randint(-100, -40)
        self.velocidad = random.randint(1, 3)
        self.color = (255, 0, 0)  #rojo
    
    def mover(self):
        self.y += self.velocidad
    
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))  # Rectángulo 
    def esta_fuera(self, alto_pantalla):
        return self.y > alto_pantalla