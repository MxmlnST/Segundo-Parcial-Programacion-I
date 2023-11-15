import pygame
from torre import Torre
from constantes import *
from funciones import *

class TorreBonus(Torre):
    def __init__(self,tipo:dict,posicion,horda):
        super().__init__(tipo,posicion,horda)
        self.apariencia[self.id_imagen] = pygame.transform.scale(self.apariencia[self.id_imagen],
                                                                (tamaño_imagen_torres))
    
    def dibujar_torre(self,screen,lista_torres):
        posicion_mouse = list(pygame.mouse.get_pos())
        posicion_mouse[0] -= 20
        posicion_mouse[1] -= 70
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(posicion_mouse):
            for e in lista_torres:
                if calcular_distancia(e.rect.center,self.rect.center) <= self.rango and e.tipo != 5:
                    pygame.draw.line(screen,(250,200,200),e.rect.center,self.rect.center,2)
        screen.blit(self.apariencia[self.id_imagen],self.rect.topleft)
    
    def actualizar_torre(self,screen,frames,lista_torres):
        self.dibujar_torre(screen,lista_torres)

