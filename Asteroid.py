import pygame

pygame.init()

velocity = 3                                # in Pixels
xPos, yPos = [5, 5]                         # initing Position elements
yHeight, xWidth = [700, 600]
windowVisible = True
windowGame = pygame.display.set_mode((yHeight,xWidth))
pygame.display.set_caption("Criando meu Primeiro Jogo em PyGame 'Asteroids'")

while windowVisible:
    pygame.time.delay(50)

    # Testando evento de abortar o jogo e sair do Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowVisible = False

    windowGame.fill((0,0,0)) #Criando Janela do Jogo - background: preto

    pygame.draw.circle(windowGame, (0, 255, 0), (xPos,yPos), 5)
    pygame.display.update()

pygame.quit()
