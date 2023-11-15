import pygame
from constantes import *
from funciones import *
from torre import Torre

class TorreAzul(Torre):

    def __init__(self,tipo:dict,posicion,horda):
        super().__init__(tipo,posicion,horda)
        self.reduccion = 0.5
        self.lista_objetivos = []
    
    def elegir_objetivo(self):
        #if len(self.lista_objetivos) != 0:
            for e in list(self.lista_objetivos):
                if (calcular_distancia(e.rect.center,self.rect.center) > self.rango or
                    e.reduccion_de_velocidad >= 0.5):
                    self.lista_objetivos.remove(e)
            for e in self.horda.lista_enemigos:
                if (calcular_distancia(e.rect.center,self.rect.center) <= self.rango and
                    e.rect.centery > 0 and e.reduccion_de_velocidad >= 0.5 and 
                    len(self.lista_objetivos) < 5):
                    self.lista_objetivos.append(e)

        # if self.objetivo == None:
        #     for e in self.horda.lista_enemigos:
        #         if calcular_distancia(e.rect.center,self.rect.center) <= self.rango:
        #             self.objetivo = e
        #             if self.objetivo.reduccion_de_velocidad >= 0.5:
        #                 break
        #             else:
        #                 self.objetivo = None
        # elif (calcular_distancia(self.objetivo.rect.center,self.rect.center) > self.rango and
        #     self.objetivo.reduccion_de_velocidad >= 0.5):
        #     self.objetivo = None
    
    def atacar(self,screen,frames,lista_torres):
        for e in list(self.lista_objetivos):
            self.objetivo = e
            if self.objetivo.reduccion_de_velocidad >= 0.5:
                pygame.draw.line(screen,self.color_proyectil,self.rect.center,self.objetivo.rect.center, 3)
                self.objetivo.reduccion_de_velocidad = self.reduccion
                self.dañar_enemigo(lista_torres)
            else:
                self.lista_objetivos.remove(e) 
            self.objetivo = None
            

        # if self.objetivo != None:
        #     pygame.draw.line(screen,self.color_proyectil,self.rect.center,self.objetivo.rect.center, 3)
        #     if self.objetivo.reduccion_de_velocidad >= 0.5:
        #         self.objetivo.reduccion_de_velocidad = self.reduccion
        #     else:
        #         self.objetivo = None
        # self.dañar_enemigo(lista_torres)
    
    # def actualizar_torre(self,screen,frames):
    #     self.dibujar_torre(screen)
    #     self.elegir_objetivo()
    #     self.atacar(screen)
