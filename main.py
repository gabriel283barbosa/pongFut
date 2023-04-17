import pygame
pygame.init()
window = pygame.display.set_mode([1280,720])
title = pygame.display.set_caption("pongFut")

placar1 = 0
placar1_img = pygame.image.load("assets/score/0.png")
placar2 = 0
placar2_img = pygame.image.load("assets/score/0.png")


loop = True

#imagens
campo = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_muveUp = False
player1_muveDown = False

player2 = pygame.image.load("assets/player2.png")
player2_y = 310

bola = pygame.image.load("assets/ball.png")
bola_x = 617
bola_y = 337
direcao_bola = -9
direcao_bola_y = 7

vencedor = pygame.image.load("assets/win.png")

def movimentacao_player1():
    global player1_y

    if player1_muveUp:
        player1_y -= 10
    elif player1_muveDown:
        player1_y +=10
    else:
        player1_y +=0
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def movimentacao_player2():
    global player2_y
    player2_y = bola_y
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575
def movimentaçao_bola ():
    global bola_x
    global bola_y
    global  direcao_bola
    global  direcao_bola_y
    global  placar1
    global  placar2
    global placar2_img
    global placar1_img

    bola_x += direcao_bola
    bola_y += direcao_bola_y
    #verificação se a bola bateu no player 1
    if bola_x < 120:
        if player1_y < bola_y + 23:
            if player1_y + 146 > bola_y:
                direcao_bola *= -1
    #verificação se a bola bateu no player 2
    if bola_x > 1100:
        if player2_y < bola_y + 23:
            if player2_y + 146 > bola_y:
                direcao_bola *= -1

    #verifica se a bola saiu da borda
    if bola_y > 685:
        direcao_bola_y *= -1

    elif bola_y<= 0:
        direcao_bola_y *= -1

#verificando se a bola ja passou (foi feito ponto)
    if bola_x < -50:
        bola_x = 617
        bola_y = 337
        direcao_bola *= -1
        placar1 +=1
        placar1_img = pygame.image.load("assets/score/" + str(placar1) + ".png")

    elif bola_x >1300:
        bola_x = 617
        bola_y = 337
        direcao_bola *= -1
        placar2 +=1

        placar2_img = pygame.image.load("assets/score/"+ str(placar2)+ ".png")

def draw():
    if placar1 == 9 or placar2 == 9:
        window.blit(vencedor, (300, 330))
    else:
        window.blit(campo,(0 ,0))
        window.blit(bola, (bola_x, bola_y))
        window.blit(player2, (1150, player2_y))
        window.blit(player1, (50, player1_y))
        window.blit(placar1_img, (500,50))
        window.blit(placar2_img,(710,50))
        movimentacao_player1()
        movimentaçao_bola()
        movimentacao_player2()
while loop:
    #fecha o jogo
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

        #função andar player_1
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_muveUp = True
            elif events.key == pygame.K_s:
                player1_muveDown = True

        #verificar se o player soltou a tecla
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_muveUp = False
            elif  events.key == pygame.K_s:
                player1_muveDown = False

    draw()
    pygame.display.update()

    #dev @annaLepattol
    #GIT