import pygame
import sqlite3
from constantes import *

class Stats():
    def __init__(self):
        self.oleada = 0
        self.vidas = 20
        self.dinero = 300
        self.score = 0
        self.interes = 0.03
        self.bonus = 0
    
    def __str__(self):
        return (f"VIDAS: {self.vidas}\n"
                f"OLEADA: {self.oleada}\n"
                f"BONUS: {self.bonus}\n"
                f"DINERO: {self.dinero}\n"
                f"INTERES: {self.interes}"
                f"SCORE: {self.score}")
    
    def sumar_dinero(self,precio):
        self.dinero += precio 
    
    def restar_dinero(self,precio):
        self.dinero -= precio
    
    def aumentar_interes(self):
        self.interes += 0.03
    
    def cobrar(self):
        self.dinero = int(self.dinero * (1 + self.interes))
    
    def sumar_vidas(self):
        self.vidas += 10
    
    def restar_vida(self):
        self.vidas -= 1
    
    def sumar_bonus(self):
        self.bonus += 1
    
    def restar_bonus(self):
        self.bonus -= 1
    
    def sumar_oleada(self):
        self.oleada += 1
    
    def sumar_score(self,precio,velocidad,tipo):
        self.score += precio * velocidad * tipo
    
    def stats_update(self,screen):
        text_dinero = font_system.render(f"DINERO: {self.dinero}", True, color_texto)
        screen.blit(text_dinero,(50,5))

        text_interes = font_system.render(f"INTERES: {int(self.interes*100)} %", True, color_texto)
        screen.blit(text_interes,(50,23))

        text_score = font_system.render(f"SCORE: {self.score}", True, color_texto)
        screen.blit(text_score,(50,40))
        
        text_oleada = font_system.render(f"OLEADA: {self.oleada}", True, color_texto)
        screen.blit(text_oleada,(200,5))

        text_vidas = font_system.render(f"VIDAS: {self.vidas}", True, color_texto)
        screen.blit(text_vidas,(200,23))

        text_bonus = font_system.render(f"BONUS: {self.bonus}", True, color_texto)
        screen.blit(text_bonus,(200,40))
    
    def registrar_stats(self,nombre):
        with open('scores.csv', 'a',encoding="UTF-8") as archivo:
            archivo.write(f"{nombre},{self.oleada},{self.score}\n")