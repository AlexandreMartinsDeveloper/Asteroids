import pygame

pygame.init()

velocity = 3                                                        # Definição em Pixel´s
windowVisible = True                                                # Visibilidade da Janela do Jogo
yHeight, xWidth = [800, 600]                                        # Definição das Dimensões da Janela
xPos, yPos = [yHeight/2, xWidth/2]                                  # Definição inicial posição Central da Nave
xPos_Rock, yPos_Rock = [25, 33]                                     # Definição Posicionamento inicial Asteroid na Tela

imageDefault = 'shiptop.png'                                        # Inicialização da Imagem da Nave a ser Carregada
pygame.mixer.music.load('SoundMotor.mp3')                           # Inicialização arquivo de áudio dos motores
imageBackground = pygame.image.load('space.png')                    # Inicialização do Background da Tela do Game
imageAsteroid = pygame.image.load('asteroid2.png')                  # Inicialização da Imagem Asteroid elemento Opositor
imageExplosion = pygame.image.load('explosion.png')                 # Inicialização da Imagem Explosão durante a Colisão
windowGame = pygame.display.set_mode((yHeight, xWidth))
pygame.display.set_caption("Criando meu Primeiro Jogo em PyGame 'Asteroids'")

initGame = False                                                    # Setando Início do Jogo sem movimento
while windowVisible:

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
            initGame = True
            imageDefault = 'shiptop.png'
            pygame.mixer.music.play()
            yPos -= velocity
        else:
            yPos = xWidth

    if moveOn[pygame.K_DOWN]:
        if yPos < xWidth:
            initGame = True
            imageDefault = 'shipdown.png'
            pygame.mixer.music.play()
            yPos += velocity
        else:
            yPos = 0

    if moveOn[pygame.K_LEFT]:
        if xPos > 0:
            initGame = True
            imageDefault = 'shipleft.png'
            pygame.mixer.music.play()
            xPos -= velocity
        else:
            xPos = yHeight

    if moveOn[pygame.K_RIGHT]:
        if xPos < yHeight:
            initGame = True
            imageDefault = 'shipright.png'
            pygame.mixer.music.play()
            xPos += velocity
        else:
            xPos = 0

    if initGame:

        if xPos_Rock < yHeight:
            xPos_Rock += 1
        else:
            xPos_Rock = 0

        if yPos_Rock < xWidth:
            yPos_Rock += 1
        else:
            yPos_Rock = 0

        if imageDefault == 'shiptop.png':
            if yPos > 0:
                yPos -= 1
            else:
                yPos = xWidth

        if imageDefault == 'shipdown.png':
            if yPos < xWidth:
                yPos += 1
            else:
                yPos = 0

        if imageDefault == 'shipright.png':
            if xPos < yHeight:
                xPos += 1
            else:
                xPos = 0

        if imageDefault == 'shipleft.png':
            if xPos > 0:
                xPos -= 1
            else:
                xPos = yHeight

    # Carregamento das imagens padrões do jogo - (Background/Elemento jogador)
    windowGame.blit(imageBackground, (0, 0))
    imageShip = pygame.image.load(imageDefault)
    windowGame.blit(imageShip, (xPos-25, yPos-33))
    windowGame.blit(imageAsteroid, (xPos_Rock, yPos_Rock))

    if (yPos_Rock > yPos - 35 and yPos_Rock < yPos + 35) and (xPos_Rock > xPos - 35 and xPos_Rock < xPos + 35):
        windowGame.blit(imageExplosion, (xPos-50, yPos-50))
        initGame = False

    pygame.display.update()

pygame.quit()
