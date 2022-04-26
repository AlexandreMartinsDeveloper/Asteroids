import pygame

pygame.init()

velocity = 3                                # in Pixels
xPos, yPos = [5, 5]                         # initing Position elements
yHeight, xWidth = [700, 600]
windowGame = pygame.display.set_mode((yHeight,xWidth))
pygame.display.set_caption("Criando meu Primeiro Jogo em PyGame 'Asteroids'")
windowVisible = True

while windowVisible:
    pygame.time.delay(50)

    # Testando evento de encerramento do jogo clicando no botão fechar janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowVisible = False

    # Carregando evento de tecla pressionada para gerenciamento de controles do game
    moveOn = pygame.key.get_pressed()

    if moveOn[pygame.K_ESCAPE]:
        windowVisible = False

    if moveOn[pygame.K_UP]:
        if yPos > 0:
            yPos -= velocity
        else:
            yPos = xWidth

    if moveOn[pygame.K_DOWN]:
        if yPos < xWidth:
            yPos += velocity
        else:
            yPos = 0

    if moveOn[pygame.K_LEFT]:
        if xPos > 0:
            xPos -= velocity
        else:
            xPos = yHeight

    if moveOn[pygame.K_RIGHT]:
        if xPos < yHeight:
            xPos += velocity
        else:
            xPos = 0

    windowGame.fill((0,0,0)) #Criando Janela do Jogo - background: preto

    pygame.draw.circle(windowGame, (0, 255, 0), (xPos,yPos), 5)
    pygame.display.update()

pygame.quit()
