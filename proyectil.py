import pygame
import random
import math
from constantes import *
from funciones import *

class Proyectil():
    def __init__(self, screen, posicion, objetivo, horda, daño):
        #self.tamaño = dic["tamaño"]
        #self.constante_velocidad = 5 #dic["velocidad"]
        self.velocidad = 3
        self.daño = daño
        self.particulas = "" #dic["particulas"]
        self.posicion = list(posicion)
        self.objetivo = objetivo
        self.horda = horda
        self.rect = pygame.Rect(list(self.posicion) + [6, 6])
        self.estado = True

    def dibujar_proyectl(self,screen):
        pygame.draw.rect(screen, (200,240,200), self.rect)
    
    def definir_objetivo(self):
        if self.objetivo not in self.horda.lista_enemigos:
            for e in self.horda.lista_enemigos:
                if not e.rect.centery < 0:
                    self.objetivo = e
                else:
                    self.estado = False
    
    def calcular_trayectoria(self):
        if self.objetivo != None:
            dx = self.objetivo.rect.centerx - self.rect.centerx
            dy = self.objetivo.rect.centery - self.rect.centery
            angle = math.atan2(dx,dy)
            self.rect.centerx += math.sin(angle) * self.velocidad 
            self.rect.centery += math.cos(angle) * self.velocidad

    def comprobar_colision(self):
        if self.objetivo.rect.collidepoint(self.rect.center):
            self.dañar_enemigo()
            self.estado = False
        pass
    
    def dañar_enemigo(self):
        self.objetivo.vida -= self.daño

    def actualizar_proyectil(self,screen):
        if len(self.horda.lista_enemigos) > 0:
            self.definir_objetivo()
            self.calcular_trayectoria()
            self.dibujar_proyectl(screen)
            self.comprobar_colision()
        else:
            self.estado = False