import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
tela_largura = 800
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('Breakout')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Variáveis do jogo
paddle_largura = 100
paddle_altura = 10
paddle_x = (tela_largura - paddle_largura) / 2
paddle_y = tela_altura - 50
paddle_velocidade = 0

bola_raio = 10
bola_x = tela_largura / 2
bola_y = tela_altura / 2
bola_velocidade_x = 3 * random.choice((-1, 1))
bola_velocidade_y = -3

bloco_largura = 60
bloco_altura = 20
blocos = []

# Criação dos blocos
for linha in range(5):
    for coluna in range(13):
        bloco_x = 10 + coluna * (bloco_largura + 5)
        bloco_y = 10 + linha * (bloco_altura + 5)
        bloco = pygame.Rect(bloco_x, bloco_y, bloco_largura, bloco_altura)
        blocos.append(bloco)

# Loop principal do jogo
relogio = pygame.time.Clock()
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                paddle_velocidade = -6
            if evento.key == pygame.K_RIGHT:
                paddle_velocidade = 6
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                paddle_velocidade = 0

    # Movimentação do paddle
    paddle_x += paddle_velocidade
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > tela_largura - paddle_largura:
        paddle_x = tela_largura - paddle_largura

    # Movimentação da bola
    bola_x += bola_velocidade_x
    bola_y += bola_velocidade_y

    # Colisões com as paredes
    if bola_x < bola_raio or bola_x > tela_largura - bola_raio:
        bola_velocidade_x *= -1
    if bola_y < bola_raio:
        bola_velocidade_y *= -1
    if bola_y > tela_altura:
        # Reinicia a posição da bola
        bola_x = tela_largura / 2
        bola_y = tela_altura / 2
        bola_velocidade_y *= -1

    # Colisão com o paddle
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_largura, paddle_altura)
    bola = pygame.Rect(bola_x - bola_raio, bola_y - bola_raio, bola_raio * 2, bola_raio * 2)
    if bola.colliderect(paddle):
        bola_velocidade_y *= -1

    # Colisão com os blocos
    for bloco in blocos[:]:
        if bola.colliderect(bloco):
            blocos.remove(bloco)
            bola_velocidade_y *= -1
            break

    # Desenho dos elementos na tela
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, paddle)
    pygame.draw.circle(tela, VERMELHO, (int(bola_x), int(bola_y)), bola_raio)
    for bloco in blocos:
        pygame.draw.rect(tela, AZUL, bloco)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
