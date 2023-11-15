from torre import Torre
from torre_proyectil import TorreProyectil
from torre_azul import TorreAzul
from torre_bonus import *
import random 
from constantes import *

class Torres():
    def __init__(self,lista:list,horda,stats):
        self.tipo_torres = lista
        self.lista_torres = []
        self.horda = horda
        self.stats = stats
        self.torres_disponibles = []
        self.posicion_mouse = [0,0]
        self.torre_elegida = None
        self.amortiguador = True
        self.amortiguador2 = False
        self.amortiguador_bonus = True
        for e in tipo_de_torres:
            if e["tipo"] == 7:
                torre = TorreProyectil(self.tipo_torres[6],self.posicion_mouse,self.horda)
            elif e["tipo"] == 6:
                torre = TorreProyectil(self.tipo_torres[5],self.posicion_mouse,self.horda)
            elif e["tipo"] == 5:
                torre = TorreProyectil(self.tipo_torres[4],self.posicion_mouse,self.horda)  
            elif e["tipo"] == 4:
                torre = TorreProyectil(self.tipo_torres[3],[0,0],self.horda)
            elif e["tipo"] == 3:
                torre = TorreAzul(self.tipo_torres[2],[0,0],self.horda)
            elif e["tipo"] == 2:
                torre = Torre(self.tipo_torres[1],[0,0],self.horda)
            else:
                torre = Torre(self.tipo_torres[0],[0,0],self.horda)
            torre.rect.width = tamaño_torres_disponibles[0]
            torre.rect.height = tamaño_torres_disponibles[1]
            self.torres_disponibles.append(torre)

    
    def __str__(self):
        return "Gestor de Torres"
    
    def elegir_torre(self,screen):
        if self.torre_elegida == None and pygame.mouse.get_pressed()[0] and self.amortiguador:
            self.posicion_mouse = list(pygame.mouse.get_pos())
            self.posicion_mouse[0] -= 590
            self.posicion_mouse[1] -= 10
            for e in self.torres_disponibles:
                if e.rect.collidepoint(self.posicion_mouse) and self.stats.bonus > 0 and self.amortiguador_bonus:
                    if e.tipo == 7:
                        self.stats.sumar_vidas()
                        self.stats.restar_bonus()
                        self.amortiguador_bonus = False
                        
                    elif e.tipo == 6:
                        self.stats.aumentar_interes()
                        self.stats.restar_bonus()
                        self.amortiguador_bonus = False 
                    if e.tipo == 5: 
                        torre = TorreBonus(self.tipo_torres[4],self.posicion_mouse,self.horda)
                        self.torre_elegida = torre
                        self.amortiguador = False
                
                if e.tipo < 5 and e.rect.collidepoint(self.posicion_mouse) and self.stats.dinero >= e.precio:
                    self.amortiguador = False
                    if e.tipo == 4:
                        torre = TorreProyectil(self.tipo_torres[3],self.posicion_mouse,self.horda)
                    elif e.tipo == 3:
                        torre = TorreAzul(self.tipo_torres[2],self.posicion_mouse,self.horda)
                    elif e.tipo == 2:
                        torre = Torre(self.tipo_torres[1],self.posicion_mouse,self.horda)
                    else:
                        torre = Torre(self.tipo_torres[0],self.posicion_mouse,self.horda)
                    self.torre_elegida = torre
    
    def ubicar_torre(self,screen,casillas):
        if self.torre_elegida != None:
            self.posicion_mouse = list(pygame.mouse.get_pos())
            self.posicion_mouse[0] -= 20
            self.posicion_mouse[1] -= 70
            if screen.get_rect().collidepoint(self.posicion_mouse):
                self.torre_elegida.rect.center = self.posicion_mouse
                if self.torre_elegida.tipo == 5:
                    for e in self.lista_torres:
                        if (calcular_distancia(e.rect.center,self.torre_elegida.rect.center) <= self.torre_elegida.rango and
                        e.tipo != 5):
                            pygame.draw.line(screen,(250,200,200),e.rect.center,self.torre_elegida.rect.center,2)
                else:            
                    pygame.draw.circle(screen,(250,200,200),self.torre_elegida.rect.center,self.torre_elegida.rango,2)
                screen.blit(self.torre_elegida.apariencia[0],self.torre_elegida.rect.topleft)
            if pygame.mouse.get_pressed()[2]:
                self.torre_elegida = None
                self.amortiguador = True
    
    def añadir_torre(self,screen,casillas):
        if self.torre_elegida != None and pygame.mouse.get_pressed()[0]:
            self.posicion_mouse = list(pygame.mouse.get_pos())
            self.posicion_mouse[0] -= 20
            self.posicion_mouse[1] -= 70
            casilla_libre = True
            self.amortiguador2 = False
            for e in self.lista_torres:
                if e.rect.collidepoint(self.posicion_mouse):
                    casilla_libre = False
            for e in casillas:
                if e.collidepoint(self.posicion_mouse):
                    self.torre_elegida.rect.centerx = e.centerx
                    self.torre_elegida.rect.centery = e.centery
                    self.amortiguador2 = True
            if casilla_libre and pygame.mouse.get_pressed()[0] and self.amortiguador2:
                self.lista_torres.append(self.torre_elegida)
                if self.torre_elegida.tipo == 5:
                    self.stats.restar_bonus()
                else:
                    self.stats.restar_dinero(self.torre_elegida.precio)
                self.torre_elegida = None
                self.amortiguador = True
    
    def comprar_torre(self,screen_mapa,screen_torres,screen_info,casillas):
        self.mostrar_info_torre(screen_info)
        self.elegir_torre(screen_torres)
        self.ubicar_torre(screen_mapa,casillas)
        self.añadir_torre(screen_mapa,casillas)
    
    def quitar_torre(self):
        pass
    
    def inventario(self,contador):
        print(contador)
        if contador % 5 == 0:
            for e in self.lista_torres:
                print(e,"numero",contador)
                contador += 1
        
    def mejorar_torre(self):
        pass
    
    def mostrar_torres_disponibles(self,screen):
        x = 0
        y = 0
        contador = 0
        for e in self.torres_disponibles:
            e.rect.topleft = [x,y]
            if (e.tipo < 5 and self.stats.dinero >= e.precio or 
                e.tipo >= 5 and self.stats.bonus > 0):
                screen.blit(e.apariencia[2],(e.rect.topleft))
            else:
                screen.blit(e.apariencia[3],(e.rect.topleft))
            if contador == 2 or contador == 3:
                y += e.rect.height
                x = 0
            else:
                x += e.rect.width
            contador += 1
    
    def mostrar_info_torre(self,screen):
        self.posicion_mouse = list(pygame.mouse.get_pos())
        self.posicion_mouse[0] -= 590
        self.posicion_mouse[1] -= 10
        for e in self.torres_disponibles:
                if e.rect.collidepoint(self.posicion_mouse):
                    if e.tipo == 5:
                        texto_torre = font_system.render("+ 25% de daño en rango.",True,color_texto)
                        screen.blit(texto_torre,(10,10))
                    elif e.tipo == 6:
                        texto_torre = font_system.render("+ 3% de interés.",True,color_texto)
                        screen.blit(texto_torre,(10,10))
                    elif e.tipo == 7:
                        texto_torre = font_system.render("+ 10 vidas.",True,color_texto)
                        screen.blit(texto_torre,(10,10))
                    else:
                        precio_torre = font_system.render(f"PRECIO: {e.precio}",True,color_texto)
                        screen.blit(precio_torre,(10,10))
                        daño_torre = font_system.render(f"DAÑO: {e.daño}",True,color_texto)
                        screen.blit(daño_torre,(10,40))
                        reload_torre = font_system.render(f"FRECUENCIA: {int(60/e.reload)} / s",True,color_texto)
                        screen.blit(reload_torre,(10,70))
                        if e.tipo == 3:
                            reduccion_torre = font_system.render(f"CONGELAMIENTO: {int(e.reduccion*100)}%",True,color_texto)
                            screen.blit(reduccion_torre,(10,100))

    
    def update(self,screen1,screen2,screen3,frames,casillas):
        self.comprar_torre(screen1,screen2,screen3,casillas)
        for e in self.lista_torres:
            e.actualizar_torre(screen1,frames,self.lista_torres)

