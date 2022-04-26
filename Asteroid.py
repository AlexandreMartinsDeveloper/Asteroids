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
windowGame = pygame.display.set_mode((yHeight, xWidth))
pygame.display.set_caption("Criando meu Primeiro Jogo em PyGame 'Asteroids'")

initGame = False
while windowVisible:
    #pygame.time.delay(5)

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
            imageDefault = 'shiptop.png'
            pygame.mixer.music.play()
            yPos -= velocity
        else:
            yPos = xWidth

    if moveOn[pygame.K_DOWN]:
        if yPos < xWidth:
            imageDefault = 'shipdown.png'
            pygame.mixer.music.play()
            yPos += velocity
        else:
            yPos = 0

    if moveOn[pygame.K_LEFT]:
        if xPos > 0:
            imageDefault = 'shipleft.png'
            pygame.mixer.music.play()
            xPos -= velocity
        else:
            xPos = yHeight

    if moveOn[pygame.K_RIGHT]:
        if xPos < yHeight:
            imageDefault = 'shipright.png'
            pygame.mixer.music.play()
            xPos += velocity
        else:
            xPos = 0

    # Carregamento das imagens padrões do jogo - (Background/Elemento jogador)
    windowGame.blit(imageBackground, (0, 0))
    imageShip = pygame.image.load(imageDefault)
    windowGame.blit(imageShip, (xPos-25, yPos-33))
    windowGame.blit(imageAsteroid, (xPos_Rock, yPos_Rock))
    pygame.display.update()

pygame.quit()
