import pygame
from constantes import *
from funciones import *
from proyectil import *

class Torre():
    def __init__(self,tipo:dict,posicion,horda):
        self.nivel = 1
        self.tipo = tipo["tipo"]
        self.rango = tipo["rango"]
        self.daño = tipo["daño"]
        self.precio = tipo["precio"]
        self.apariencia = tipo["apariencia"]
        self.reload = tipo["reload"]
        self.color_proyectil = tipo["color_proyectil"]
        self.id_imagen = 0
        self.horda = horda
        self.rect = pygame.Rect(posicion[0],posicion[1], tipo["tamaño"][0], tipo["tamaño"][1])
        self.rect.center = self.rect.topleft
        self.objetivo = None
        self.bonus = 1
    
    def __str__(self):
        return f"Precio: ${self.precio}\nDaño: {self.daño}"
    
    def dibujar_torre(self,screen):
        posicion_mouse = list(pygame.mouse.get_pos())
        posicion_mouse[0] -= 20
        posicion_mouse[1] -= 70
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(posicion_mouse):
            circle = pygame.draw.circle(screen, (245,130,125),self.rect.center,self.rango,3)
        if self.objetivo == None:
            self.id_imagen = 0
        else:
            self.id_imagen = 1
        screen.blit(self.apariencia[self.id_imagen],self.rect.topleft)
    
    def elegir_objetivo(self):
        if self.objetivo == None:
            for e in self.horda.lista_enemigos:
                if calcular_distancia(e.rect.center,self.rect.center) <= self.rango:
                    self.objetivo = e
                    break
        elif (calcular_distancia(self.objetivo.rect.center,self.rect.center) > self.rango or 
                                self.objetivo not in self.horda.lista_enemigos):
            self.objetivo = None
    
    def atacar(self,screen,frames,lista_torres):
        if self.objetivo != None and frames % self.reload == 0 and self.objetivo.rect.centery > 0:
            pygame.draw.line(screen,self.color_proyectil,self.rect.center,self.objetivo.rect.center, 3)
            self.dañar_enemigo(lista_torres)
    
    def calcular_bonus(self,lista_torres):
        self.bonus = 1
        for e in lista_torres:
            if e.tipo == 5 and calcular_distancia(e.rect.center,self.rect.center) <= e.rango:
                self.bonus += e.daño
        return self.bonus
    
    def dañar_enemigo(self,lista_torres):
        if self.objetivo != None:
            if self.objetivo.vida <= 0:
                self.objetivo = None
            else:
                self.calcular_bonus(lista_torres)
                self.objetivo.vida -= self.daño * self.bonus
        
    def actualizar_torre(self,screen,frames,lista_torres):
        self.dibujar_torre(screen)
        self.elegir_objetivo()
        self.atacar(screen,frames,lista_torres)