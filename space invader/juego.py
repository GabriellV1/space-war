import pygame
import random
import pygame
from jugador import Jugador
from enemigo import Enemigo

ANCHO, ALTO = 800, 600
FPS = 60


class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Space War")
        self.reloj = pygame.time.Clock()
        self.jugador = Jugador(ANCHO // 2, ALTO - 70)
        self.enemigos = []
        self.ejecutando = True
    
    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
        
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.jugador.mover("izquierda", ANCHO)
        if teclas[pygame.K_RIGHT]:
            self.jugador.mover("derecha", ANCHO)
    
    def generar_enemigos(self):
        if random.random() < 0.02:  
            self.enemigos.append(Enemigo(ANCHO))
    
    def actualizar(self):
        for enemigo in self.enemigos[:]:
            enemigo.mover()
            if enemigo.esta_fuera(ALTO):
                self.enemigos.remove(enemigo)
    
    def dibujar(self):
        self.pantalla.fill((0, 0, 0)) 
        self.jugador.dibujar(self.pantalla)
        for enemigo in self.enemigos:
            enemigo.dibujar(self.pantalla)
        pygame.display.flip()
    
    def ejecutar(self):
        while self.ejecutando:
            self.manejar_eventos()
            self.generar_enemigos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(FPS)
        pygame.quit()

