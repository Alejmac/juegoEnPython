import pygame
import random

#se inicializa
pygame.init()
#creamos la pantalla
pantalla = pygame.display.set_mode((800,600))
#titulo
pygame.display.set_caption("Invasion")
#icono
icono = pygame.image.load("sol.png")
pygame.display.set_icon(icono)


#jugador 
img_jugador= pygame.image.load("nave-espacial.png")
jugador_x= 368 
jugador_y = 536
jugador_x_cambio = 0

#variable enemigo 
img_enemigo= pygame.image.load("enemigo.png")
enemigo_x= random.randint(0,736) 
enemigo_y = random.randint(50,150)
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50

#funcionpara mostrar jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y ))

#funcionpara mostrar enemigo
def enemigo(x,y):
    pantalla.blit(img_enemigo,(x,y ))

#loop del juego
ejecutar = True
while ejecutar:
#cambiar el color de la pantalla
    #se establece el relleno de la pantalla
    pantalla.fill((205,144,228))
    #jugador_x += 0.1

    for evento in pygame.event.get():
        #evento para cerrar el programa 
        if evento.type == pygame.QUIT:
            ejecutar = False
        #eventi oresionar una tecla
        if evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.1
        #evento solar teclas 
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    jugador_x += jugador_x_cambio
    #mantener bordes al jugador 
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    
    #modificar ubicacion del enemigo
    enemigo_x += enemigo_x_cambio
    #mantener bordes al enemigo 
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.3
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.3
        enemigo_y += enemigo_y_cambio

    jugador(jugador_x,jugador_y)
    enemigo(enemigo_x,enemigo_y)

 
    #actualizar
    pygame.display.update()