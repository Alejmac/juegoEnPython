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
jugador_x= 0 
jugador_y = 0

#funcionpara mostrar jugador
def jugador():
    pantalla.blit(img_jugador,(jugador_x,jugador_y ))

#loop del juego
ejecutar = True
while ejecutar:
#cambiar el color de la pantalla
    #se establece el relleno de la pantalla
    pantalla.fill((205,144,228))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

    jugador()
    pygame.display.update()