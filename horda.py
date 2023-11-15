from enemigo import Enemigo
import random
from constantes import *

class Horda():
    def __init__(self,lista:list,stats): #horda_actual, horda_siguiente
        self.lista_tipos = lista
        self.lista_enemigos = []
        self.stats = stats
    
    def generar_horda(self): #cambiar oleada por self.stats.oleada
        contador = 0
        if self.stats.oleada % 5 == 0:
            id_lista = len(self.lista_tipos) - 2
        else:
            id_lista = random.randint(0,len(self.lista_tipos)-3)
        posicion = posicion_inicio_enemigo[0]
        for i in range(30):
            if i > 14:
                posicion = posicion_inicio_enemigo[1]
                if i == 15:
                    contador = 0
                elif i == 29 and self.stats.oleada % 5 == 0:
                    id_lista = 6
            enemigo = Enemigo(self.lista_tipos[id_lista],self.stats.oleada,posicion)
            enemigo.rect.y -= 2 * enemigo.tamaño[1] * contador
            self.lista_enemigos.append(enemigo)
            contador += 1
    
    def eliminar_enemigo(self):
        for e in list(self.lista_enemigos):
            if e.estado == False:
                self.lista_enemigos.remove(e)
    
    def update(self,screen,lista_caminos,casillas,frames):
        self.eliminar_enemigo()
        for e in self.lista_enemigos:
            e.enemigo_update(screen,lista_caminos,casillas,frames,self.stats)
