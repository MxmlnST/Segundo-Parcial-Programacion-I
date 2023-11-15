import pygame
import sqlite3
from constantes import *
import re

def corregir_mouse_pos(lista:list,screen1,screen2)->list:
    "Retorna pygame.mouse.get_pos corregido para cada surface"
    posicion = list(pygame.mouse.get_pos())
    posicion[0] -= 20
    posicion[1] -= 70
    if screen1.get_rect().collidepoint(posicion):
        return posicion
    posicion = list(pygame.mouse.get_pos())
    posicion[0] -= 590
    posicion[1] -= 10
    if screen2.get_rect().collidepoint(posicion):
        return posicion    
    #return list(pygame.mouse.get_pos())

def simplificar_fraccion(numerador:int,denominador:int)->float:
    """Simplifica una fracción. Retorna una lista con el numerador(lista[0]) y el
    denominador(lista[1]) reducidos."""
    factores = lambda posicion:filter(lambda num: posicion % (num) == 0, range(1,posicion+1))
    mcd = max(filter(lambda num: num in factores(abs(denominador)),factores(abs(numerador))))
    return [int(numerador/mcd),int(denominador/mcd)]

def calcular_distancia(coordenada1:list,coordenada2:list)->int:
    "Calcula la distancia entre dos puntos."
    return ((coordenada1[0] - coordenada2[0])**2 + (coordenada1[1] - coordenada2[1])**2)**(1/2)

def calcular_porcentaje(incognita:int,total:int)->float:
    return incognita * 100 / total

################ MENU ############
def menu_dibujar(screen,boton_partida,boton_scores,input_nombre,input_rect):
    screen.fill((0,0,50))
    
    texto_arriba_nombre = font_courier.render("Ingresa tu nombre para jugar.",True,(230,206,234))
    screen.blit(texto_arriba_nombre,(150,10))
    
    pygame.draw.rect(screen,(191,130,200),input_rect,2)
    texto_nombre = font_courier.render(input_nombre,True,(71,33,67))
    screen.blit(texto_nombre,(input_rect.x + 5,input_rect.y + 5))
    input_rect.w = max(100,texto_nombre.get_width() + 10)
    
    screen.blit(imagen_jugar,boton_partida.topleft)
    
    screen.blit(imagen_ranking,boton_scores.topleft)
################ SCORES ############
def scores_dibujar(screen,boton_volver_menu):
    screen.fill((0,0,50))    
    screen.blit(imagen_volver_al_menu,boton_volver_menu.topleft)

##### BOTONES PARTIDA ##########

def enviar_oleada(stats,horda):
    stats.oleada += 1
    stats.cobrar()
    horda.generar_horda()

def abandonar():
    pass

def dibujar_botones_partida(screen):
    screen.blit(imagen_siguiente_oleada,boton_siguiente_oleada.topleft)
    screen.blit(imagen_abandonar,boton_abandonar.topleft)

###### SCORES ########
def ordenar_descendente(lista:list,index:int)->list:
    "Ordena de manera ascendente a los heroes de la lista según la key proporcionada."
    lista_recibida = list(lista)
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista_recibida[0]
        for elemento in lista_recibida[1:]:
            if elemento[index] < pivot[index]:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = ordenar_descendente(lista_iz,index)
    lista_iz.append(pivot) 
    lista_de = ordenar_descendente(lista_de,index)
    return lista_iz + lista_de

def establecer_ranking():
    try:
        lista = []
        with open('scores.csv', 'r',encoding="UTF-8") as archivo:
            for linea in archivo.readlines():
                linea = re.split(",",re.sub("\n","",linea))
                lista.append(linea)
            lista = ordenar_descendente(lista,1)
            return lista
    except FileNotFoundError:
        pass
            

def mostrar_ranking(screen,lista:list):
    try:
        y = 10
        x = 200
        campos = font_courier.render(f"{'NOMBRE': <10}{'OLEADA': <10}{'SCORE': <10}",True,(230,206,234))
        screen.blit(campos,(x,y))
        x -= 40
        if type(lista) == list:
            for i in range(min(5,len(lista))):
                y += 40
                puesto = font_courier.render(f"{i+1}- {lista[i][0]: <10}{lista[i][1]: <10}{lista[i][2]: <10}",True,(230,206,234))
                screen.blit(puesto,(x,y))
    except FileNotFoundError:
        pass