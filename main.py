import pygame
import random
import sqlite3
from constantes import *
from torres import *
from horda import *
from stats import *
from funciones import *

pygame.init()
# SCREENS
screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
pygame.display.set_caption("GAME") 
screen_mapa = pygame.Surface(SCREEN_MAPA)
screen_stats = pygame.Surface(SCREEN_STATS)
screen_torres = pygame.Surface(SCREEN_TORRES)
screen_info = pygame.Surface(SCREEN_INFO)
# CLOCK
clock = pygame.time.Clock()
frames = 0

def colocar_casillas():
    lista_casillas = []
    lista_caminos = []
    x = - tamaño_imagen_torres[0]
    y = - tamaño_imagen_torres[0]
    for fila in mapa:
        for casilla in fila:
            lista_caracteres = ["S","A","D","U","I","F"]
            if casilla == "X":
                lista_casillas.append(pygame.Rect(x,y,tamaño_imagen_torres[0],tamaño_imagen_torres[1]))
            elif casilla in lista_caracteres:
                lista_caminos.append({casilla:pygame.Rect(x,y,tamaño_imagen_torres[0],tamaño_imagen_torres[1])})
            x += tamaño_imagen_torres[0]
        x = 0
        y += tamaño_imagen_torres[1]
    return lista_casillas,lista_caminos

def dibujar_mapa(screen):
    for casilla in casillas:
        screen_mapa.blit(imagen_casilla,casilla)

# MAPA
mapa_actual = colocar_casillas()
casillas = mapa_actual[0]
lista_caminos = mapa_actual[1]
# OBJETOS
stats = Stats()
horda = Horda(tipo_de_enemigos,stats)
torres = Torres(tipo_de_torres,horda,stats)
#JUGADOR
input_nombre = ""
input_rect = pygame.Rect((350,50,100,50))
input_activo = False


flag_menu = True
flag_partida = False
flag_scores = False
flag_run = True
while flag_run:
    flag_menu = True
    while flag_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_run = False
                flag_menu = False
                flag_partida = False
                flag_scores = False
            if event.type == pygame.KEYDOWN:
                if input_activo:
                    if event.key == pygame.K_BACKSPACE:
                        input_nombre = input_nombre[:-1]
                    else:
                        input_nombre += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_activo = True
                else:
                    input_activo = False
                if boton_partida.collidepoint(pygame.mouse.get_pos()) and len(input_nombre) != 0:
                    flag_partida = True
                    flag_menu = False
                if boton_scores.collidepoint(pygame.mouse.get_pos()):
                    flag_menu = False
                    flag_scores = True
        menu_dibujar(screen,boton_partida,boton_scores,input_nombre,input_rect)
        pygame.display.flip()
    
    stats = Stats()
    horda = Horda(tipo_de_enemigos,stats)
    torres = Torres(tipo_de_torres,horda,stats)
    
    while flag_partida:
        clock.tick(FPS)
        frames += 1
        if frames > 60:
            frames = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_run = False
                flag_partida = False
                flag_menu = False
                flag_scores = False
            if event.type == pygame.MOUSEMOTION:
                pass        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_siguiente_oleada.collidepoint(event.pos):
                    enviar_oleada(stats,horda)
                if boton_abandonar.collidepoint(event.pos):
                    flag_partida = False
                    stats.registrar_stats(input_nombre)
            if event.type == pygame.MOUSEBUTTONUP:
                posicion = list(event.pos)
                torres.amortiguador_bonus = True      
            if event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_p:
                    pass
        #screens 
        screen.fill(SCREEN_COLOR)
        screen.blit(screen_mapa,(20,70))
        screen_mapa.fill((0,0,50))
        
        screen.blit(screen_stats,(248,10))
        screen_stats.fill((30,12,48))
        
        screen.blit(screen_torres,(590,10))
        screen_torres.fill((30,12,48))
        torres.mostrar_torres_disponibles(screen_torres)
        
        screen.blit(screen_info,(590,250))
        screen_info.fill((30,12,48))
        
        dibujar_botones_partida(screen)
        #mapa 
        dibujar_mapa(screen_mapa)
        #stats
        stats.stats_update(screen_stats)
        #torres update
        torres.update(screen_mapa,screen_torres,screen_info,frames,casillas)    
        #enemigos update
        horda.update(screen_mapa,lista_caminos,casillas,frames)
        
        if stats.vidas <= 0:
            stats.agregar_data(input_nombre)
            flag_partida = False

        pygame.display.flip()
    
    while flag_scores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_run = False
                flag_partida = False
                flag_menu = False
                flag_scores = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver_menu.collidepoint(pygame.mouse.get_pos()):
                    flag_menu = True
                    flag_scores = False
        scores_dibujar(screen,boton_volver_menu)
        mostrar_ranking(screen,establecer_ranking())
        pygame.display.flip()
    
pygame.quit()