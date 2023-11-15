import pygame
from constantes import *
from torre import Torre
from proyectil import *

class TorreProyectil(Torre):

    def __init__(self,tipo:dict,posicion,horda):
        super().__init__(tipo,posicion,horda)
        self.lista_proyectiles = []
        self.disparar = False
    
    def elegir_objetivo(self):
        if self.objetivo == None:
            for e in self.horda.lista_enemigos:
                if calcular_distancia(e.rect.center,self.rect.center) <= self.rango and e.rect.centery > 0:
                    self.objetivo = e
                    break

        elif (calcular_distancia(self.objetivo.rect.center,self.rect.center) > self.rango or
        self.objetivo not in self.horda.lista_enemigos):
            self.objetivo = None
    
    def spawnear_proyectil(self,screen,frames,lista_torres):
        if frames == 60:
            self.disparar = True
        if self.objetivo != None and self.disparar:
            daño = self.daño * self.calcular_bonus(lista_torres)
            proyectil = Proyectil(screen,self.rect.center,self.objetivo,self.horda,daño)
            self.lista_proyectiles.append(proyectil)
            self.disparar = False
    
    def proyectil_update(self,screen):
        for e in list(self.lista_proyectiles):
            if e.estado == False:
                self.lista_proyectiles.remove(e)
            else:
                e.actualizar_proyectil(screen)
    
    def actualizar_torre(self,screen,frames,lista_torres):
        self.dibujar_torre(screen)
        self.elegir_objetivo()
        self.spawnear_proyectil(screen,frames,lista_torres)
        self.proyectil_update(screen)