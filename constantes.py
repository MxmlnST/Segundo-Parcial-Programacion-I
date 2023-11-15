import pygame

FPS = 60
COLUMNAS = 25
# SCREENS
SCREEN_X = 800
SCREEN_Y = 600
SCREEN_COLOR = [0,0,20]
SCREEN_MAPA = [528,528]
SCREEN_STATS = [300, 55]
SCREEN_TORRES = [200, 200]
SCREEN_INFO = [200, 300]
# COLORES
ROJO = (255, 0, 0)
VERDE = (0, 355, 0)
AZUL = (0, 0, 255)
LASER_VERDE = (166, 253,67)
LASER_AZUL = (78, 252, 252)
LASER_ROJO = (252, 78, 81)
# BOTONES
TAMAÑO_BOTONES = (300,100)
TAMAÑO_BOTONES_PARTIDA = (100,50)
boton_partida = pygame.Rect(250,200,300,100)
boton_scores = pygame.Rect(250,400,300,100)
boton_volver_menu = pygame.Rect(250,450,300,100)
boton_abandonar = pygame.Rect(10,10,100,50)
boton_siguiente_oleada = pygame.Rect(120,10,100,50)
# TORRES Y ENEMIGOS
posicion_inicio_enemigo = [[48,-20],[72,-20]]
tamaño_imagen_torres = [24, 24]
tamaño_enemigos = [24, 24]
tamaño_torres_disponibles = [SCREEN_TORRES[0]/3,SCREEN_TORRES[0]/3]
# FUENTES
pygame.font.init()
font_system = pygame.font.SysFont("Courier", 15,True)
font_courier = pygame.font.SysFont("Courier", 30,True)
color_texto = (230,206,234)
# IMAGENES

imagen_casilla = pygame.image.load("casilla.png")
imagen_casilla = pygame.transform.scale(imagen_casilla,(tamaño_imagen_torres))

imagen_torre_verde = pygame.image.load("torre_verde.png")
imagen_torre_verde = pygame.transform.scale(imagen_torre_verde,(tamaño_imagen_torres))
imagen_torre_verde_enojada = pygame.image.load("torre_verde_enojada.png")
imagen_torre_verde_enojada = pygame.transform.scale(imagen_torre_verde_enojada,(tamaño_imagen_torres))

imagen_torre_roja = pygame.image.load("torre_roja.png")
imagen_torre_roja = pygame.transform.scale(imagen_torre_roja,(tamaño_imagen_torres))
imagen_torre_roja_enojada = pygame.image.load("torre_roja_enojada.png")
imagen_torre_roja_enojada = pygame.transform.scale(imagen_torre_roja_enojada,(tamaño_imagen_torres))

imagen_torre_azul = pygame.image.load("torre_azul.png")
imagen_torre_azul = pygame.transform.scale(imagen_torre_azul,(tamaño_imagen_torres))
imagen_torre_azul_enojada = pygame.image.load("torre_azul_enojada.png")
imagen_torre_azul_enojada = pygame.transform.scale(imagen_torre_azul_enojada,(tamaño_imagen_torres))

imagen_boca = pygame.image.load("boca.png")
imagen_boca = pygame.transform.scale(imagen_boca,(tamaño_imagen_torres))

torre_azul_disponible = pygame.image.load("torre_azul_disponible.png")
torre_azul_disponible = pygame.transform.scale(torre_azul_disponible,(tamaño_torres_disponibles))
torre_roja_disponible = pygame.image.load("torre_roja_disponible.png")
torre_roja_disponible = pygame.transform.scale(torre_roja_disponible,(tamaño_torres_disponibles))
torre_verde_disponible = pygame.image.load("torre_verde_disponible.png")
torre_verde_disponible = pygame.transform.scale(torre_verde_disponible,(tamaño_torres_disponibles))
torre_no_disponible = pygame.image.load("torre_no_disponible.png")
torre_no_disponible = pygame.transform.scale(torre_no_disponible,(tamaño_torres_disponibles))
boca_disponible = pygame.image.load("boca_disponible.png")
boca_disponible = pygame.transform.scale(boca_disponible,(tamaño_torres_disponibles))
boca_no_disponible = pygame.image.load("boca_no_disponible.png")
boca_no_disponible = pygame.transform.scale(boca_no_disponible,(tamaño_torres_disponibles))
torre_bonus = pygame.image.load("torre_bonus.png")
torre_bonus = pygame.transform.scale(torre_bonus,(tamaño_torres_disponibles))
torre_bonus_no_disponible = pygame.image.load("torre_bonus_no_disponible.png")
torre_bonus_no_disponible = pygame.transform.scale(torre_bonus_no_disponible,(tamaño_torres_disponibles))
interes = pygame.image.load("interes.png")
interes = pygame.transform.scale(interes,(tamaño_torres_disponibles))
interes_no_disponible = pygame.image.load("interes_no_disponible.png")
interes_no_disponible = pygame.transform.scale(interes_no_disponible,(tamaño_torres_disponibles))
corazon = pygame.image.load("corazon.png")
corazon = pygame.transform.scale(corazon,(tamaño_torres_disponibles))
corazon_no_disponible = pygame.image.load("corazon_no_disponible.png")
corazon_no_disponible = pygame.transform.scale(corazon_no_disponible,(tamaño_torres_disponibles))

imagen_jugar = pygame.image.load("jugar.png")
imagen_jugar = pygame.transform.scale(imagen_jugar,TAMAÑO_BOTONES)
imagen_ranking = pygame.image.load("ranking.png")
imagen_ranking = pygame.transform.scale(imagen_ranking,TAMAÑO_BOTONES)
imagen_volver_al_menu = pygame.image.load("volver_al_menu.png")
imagen_volver_al_menu = pygame.transform.scale(imagen_volver_al_menu,TAMAÑO_BOTONES)
imagen_siguiente_oleada = pygame.image.load("siguiente_oleada.png")
imagen_siguiente_oleada = pygame.transform.scale(imagen_siguiente_oleada,TAMAÑO_BOTONES_PARTIDA)
imagen_abandonar = pygame.image.load("abandonar.png")
imagen_abandonar = pygame.transform.scale(imagen_abandonar,TAMAÑO_BOTONES_PARTIDA)

tipo_de_torres = [{"tipo":1,
                    "apariencia":[imagen_torre_verde,imagen_torre_verde_enojada,torre_verde_disponible,torre_no_disponible],
                    "rango":tamaño_imagen_torres[1] * 2.5,
                    "velocidad":2,
                    "posicion":[],
                    "daño":60,
                    "tamaño": tamaño_imagen_torres,
                    "color_proyectil":LASER_VERDE,
                    "precio": 150,
                    "reload":2},
                
                    {"tipo":2,
                    "apariencia":[imagen_torre_roja,imagen_torre_roja_enojada,torre_roja_disponible,torre_no_disponible],
                    "rango":tamaño_imagen_torres[1] * 2,
                    "velocidad":4,
                    "posicion":[],
                    "daño":2000,
                    "tamaño": tamaño_imagen_torres,
                    "color_proyectil":LASER_ROJO,
                    "precio": 400,
                    "reload":5},
                
                    {"tipo":3,
                    "apariencia":[imagen_torre_azul,imagen_torre_azul_enojada,torre_azul_disponible,torre_no_disponible],
                    "rango":tamaño_imagen_torres[1] * 2.5,
                    "velocidad":2,
                    "posicion":[],
                    "daño":60,
                    "tamaño": tamaño_imagen_torres,
                    "color_proyectil":LASER_AZUL,
                    "precio": 400,
                    "reload":1},
                
                    {"tipo":4,
                    "apariencia":[imagen_boca,imagen_boca,boca_disponible,boca_no_disponible],
                    "rango":tamaño_imagen_torres[1] * 4.5,
                    "velocidad":2,
                    "posicion":[],
                    "daño":30000,
                    "tamaño": tamaño_imagen_torres,
                    "color_proyectil":ROJO,
                    "precio": 2000,
                    "reload":60},
                
                    {"tipo":5,
                    "apariencia":[torre_bonus,torre_bonus,torre_bonus,torre_bonus_no_disponible],
                    "rango":tamaño_imagen_torres[1] * 4.5,
                    "velocidad":None,
                    "posicion":[],
                    "daño":0.25,
                    "tamaño": tamaño_imagen_torres,
                    "color_proyectil":None,
                    "precio": 1,
                    "reload":None},
                
                    {"tipo":6,
                    "apariencia":[interes,interes,interes,interes_no_disponible],
                    "rango":tamaño_imagen_torres[1] * 4,
                    "velocidad":None,
                    "posicion":[],
                    "daño":0.25,
                    "tamaño": tamaño_imagen_torres,
                    "color_proyectil":None,
                    "precio": 1,
                    "reload":None},
                
                    {"tipo":7,
                    "apariencia":[corazon,corazon,corazon,corazon_no_disponible],
                    "rango":tamaño_imagen_torres[1] * 4,
                    "velocidad":None,
                    "posicion":[],
                    "daño":None,
                    "tamaño": tamaño_imagen_torres,
                    "color_proyectil":None,
                    "precio": 1,
                    "reload":None}
                    ]

tipo_de_enemigos = [{"tipo":1,
                    "color":[196,24,26], #ROJO
                    "tamaño":tamaño_enemigos,
                    "velocidad":2,
                    "vida":400,
                    "posicion":posicion_inicio_enemigo,
                    "apariencia":imagen_torre_verde},
                
                    {"tipo":2,
                    "color":[46,196,24], #VERDE
                    "tamaño":tamaño_enemigos,
                    "velocidad":2,
                    "vida":400,
                    "posicion":posicion_inicio_enemigo,
                    "apariencia":imagen_torre_verde},
                
                    {"tipo":3,
                    "color":[175,196,24], #AMARILLO
                    "tamaño":tamaño_enemigos,
                    "velocidad":2,
                    "vida":400,
                    "posicion":posicion_inicio_enemigo,
                    "apariencia":imagen_torre_verde},
                
                    {"tipo":4,
                    "color":[173,24,196], #VIOLETA
                    "tamaño":tamaño_enemigos,
                    "velocidad":2,
                    "vida":400,
                    "posicion":posicion_inicio_enemigo,
                    "apariencia":imagen_torre_verde},
                
                    {"tipo":5,
                    "color":[24,68,196], #AZUL
                    "tamaño":tamaño_enemigos,
                    "velocidad":3,
                    "vida":400,
                    "posicion":posicion_inicio_enemigo,
                    "apariencia":imagen_torre_verde},

                    {"tipo":6,
                    "color":[140,140,140], #GRIS
                    "tamaño":tamaño_enemigos,
                    "velocidad":2,
                    "vida":400,
                    "posicion":posicion_inicio_enemigo,
                    "apariencia":imagen_torre_verde},
                
                    {"tipo":7,
                    "color":[240,220,200],
                    "tamaño":tamaño_enemigos,
                    "velocidad":2,
                    "vida":600,
                    "posicion":posicion_inicio_enemigo,
                    "apariencia":imagen_torre_verde}
                    ]

mapa = ["  SS                  ",
        "XX  XXXXXXXXXXXXXXXXXX",
        "XX D                AX",
        "XXD                A X",
        "XXXXXXXXXXXXXXXXXXX  X",
        "XXA                I X",
        "XX A                IX",
        "XX  XXXXXXXXXXXXXXXXXX",
        "XX D               AXX",
        "XXD               A XX",
        "XXXXXXXXXXXXXXXXXX  XX",
        "XXA            IXX  XX",
        "XX A          I XX  XX",
        "XX  XXXXXXXXXX  XX  XX",
        "XX  XXXXXXXXXX U  I XX",
        "XX  XXXXXXXXXXU    IXX",
        "XX  XXXXXXXXXXXXXXXXXX",
        "XX  XXXXXXXXXXXXXXXXXX",
        "XX  XXXXXD            F",
        "XX  XXXXX D           F",
        "XX D     U XXXXXXXXXXX",
        "XXD       UXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXX",
        ]
