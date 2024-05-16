import pygame

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

#funcionpara mostrar jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y ))

#loop del juego
ejecutar = True
while ejecutar:
#cambiar el color de la pantalla
    #se establece el relleno de la pantalla
    pantalla.fill((205,144,228))
    #jugador_x += 0.1

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
        #se activa a escucha de las teclas
        if evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.1

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    jugador_x += jugador_x_cambio
    jugador(jugador_x,jugador_y)
    pygame.display.update()