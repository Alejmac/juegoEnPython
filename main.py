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

#loop del juego
ejecutar = True
while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
    #cambiar el color de la pantalla
    pantalla.fill((205,144,228))
    pygame.display.update()