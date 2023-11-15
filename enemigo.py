import pygame
import random
from constantes import *
from funciones import *

class Enemigo():
    def __init__(self,tipo:dict,oleada,posicion_inicial):
        self.nombre = ""
        self.tipo = tipo["tipo"]
        self.color = tipo["color"]
        self.tamaño = tipo["tamaño"]
        self.velocidad = tipo["velocidad"]
        self.reduccion_de_velocidad = 1
        self.vida_inicial = tipo["vida"]
        self.precio = 4
        self.precio += oleada
        if oleada > 1:
            self.vida_inicial = int(tipo["vida"] * oleada**2 *0.7)
        self.vida = self.vida_inicial
        self.posicion_inicial = posicion_inicial 
        self.rect = pygame.Rect(self.posicion_inicial+self.tamaño)
        self.estado = True
        self.checkpoint_inicial = "A"
        self.checkpoint = self.checkpoint_inicial
        self.salida = None
        self.imagen = tipo["apariencia"]
    
    def moverse(self,casillas,frames,stats):
        if frames % 2 == 0:
            match self.checkpoint:
                case "A":
                    self.rect.centery += self.velocidad * self.reduccion_de_velocidad
                case "U":
                    self.rect.centery -= self.velocidad * self.reduccion_de_velocidad
                case "D":
                    self.rect.centerx += self.velocidad * self.reduccion_de_velocidad
                case "I":
                    self.rect.centerx -= self.velocidad * self.reduccion_de_velocidad
                case "F":
                    self.rect.topleft = self.posicion_inicial
                    self.checkpoint = "A"
                    stats.restar_vida()
                case "S":
                    self.rect.centery += self.velocidad * self.reduccion_de_velocidad
            self.reduccion_de_velocidad = 1
    
    def definir_trayectoria(self,lista_caminos):
        for e in lista_caminos:
            rect_objeto = list(e.values())[0]
            if self.rect.collidepoint(rect_objeto.center):
                var = list(e.keys())[0]
                match var:   
                    case "A":
                        if not self.checkpoint == "A":
                            self.rect.topleft = rect_objeto.topleft
                        self.checkpoint = "A"
                    case "U":
                        if not self.checkpoint == "U":
                            self.rect.topleft = rect_objeto.topleft
                        self.checkpoint = "U"
                    case "D":
                        if not self.checkpoint == "D":
                            self.rect.topleft = rect_objeto.topleft
                        self.checkpoint = "D"
                    case "I":
                        if not self.checkpoint == "I":
                            self.rect.topleft = rect_objeto.topleft
                        self.checkpoint = "I"
                    case "F":
                        if not self.checkpoint == "F":
                            self.rect.topleft = rect_objeto.topleft
                        self.checkpoint = "F"
    
    def dibujar_enemigo(self,screen,frames):
        rect_dibujo = self.rect.copy()
        if self.tipo != 7:
            rect_dibujo.width *= 0.5
            rect_dibujo.height *= 0.5
        else:
            rect_dibujo.width *= 0.75
            rect_dibujo.height *= 0.75
        rect_dibujo.center = self.rect.center
        
        if frames <= 10:
            rect_dibujo.inflate_ip(-2,2)
        elif frames <= 20:
            rect_dibujo.inflate_ip(-2,4)
        elif frames <= 30:
            rect_dibujo.inflate_ip(2,2)
        elif frames <= 40:
            rect_dibujo.inflate_ip(4,0)
        elif frames <= 50:
            rect_dibujo.inflate_ip(4,-2)
        
        if self.tipo == 7:
            pygame.draw.ellipse(screen,self.color,rect_dibujo)
        else:
            pygame.draw.rect(screen,self.color,rect_dibujo,2)
        self.dibujar_vida(screen,rect_dibujo)
    
    def dibujar_vida(self,screen,rect):
        porcentaje_vida = calcular_porcentaje(self.vida, self.vida_inicial)
        variable = rect.topleft[0] + rect.width * porcentaje_vida / 100
        if self.vida > 0:
            pygame.draw.line(screen,(111,218,2),(rect.topleft[0], rect.y - (rect.height*0.20)),
                            (variable, rect.y - (rect.height*0.20)), 2)
    
    def morir(self,stats):
        if self.vida <= 0:
            self.estado = False
            if self.tipo == 7:
                    stats.sumar_bonus()
            stats.sumar_dinero(self.precio)
            stats.sumar_score(self.precio,self.velocidad,self.tipo)
    
    def enemigo_update(self,screen,lista_caminos,casillas,frames,stats):
        self.morir(stats)
        self.definir_trayectoria(lista_caminos)
        self.moverse(casillas,frames,stats)
        self.dibujar_enemigo(screen,frames)
