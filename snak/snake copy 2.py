#conf iniciais
import pygame
import random


pygame.init()
pygame.display.set_caption("jogo snake")
TELA_LARGURA,  TELA_ALTURA = 800,600
TELA = pygame.display.set_mode((TELA_LARGURA,TELA_ALTURA))
relogio = pygame.time.Clock()

ia_jogando = True
geracao = 0

#***cores RGB --- RED, GREEN , BLUE
preta = (0,0,0)
verde = (0,255,0)
branco = (255,255,255)
vermelho = (255,0,0)

#***parametros da cobrinha
tamanho_quadrado = 20
vel_game = 15

def desenhar_comida(tamanho,comida_x,comida_y):
    pygame.draw.rect(TELA,vermelho,[comida_x,comida_y,tamanho,tamanho])

def desenhar_cobrinha(tamanho ,pixels):
    for pixel in pixels:
        pygame.draw.rect(TELA,verde,[pixel[0], pixel[1],tamanho,tamanho])


def gerar_comida():
    comida_x = round(random.randrange(0,TELA_LARGURA - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0,TELA_ALTURA - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_pontos(pontuação):
    fonte = pygame.font.SysFont('comic_sans',30)
    texto = fonte.render(f"pontos: {pontuação}", True , branco)
    TELA.blit(texto,[1 ,1])


def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        return velocidade_x, velocidade_y
    if tecla == pygame.K_UP:
        velocidade_x = 0 
        velocidade_y = -tamanho_quadrado
        return velocidade_x, velocidade_y
    if tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
        return velocidade_x, velocidade_y
    if tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
        return velocidade_x, velocidade_y

def rodar_jogo():
    game_over = False

    x = TELA_LARGURA/2
    y = TELA_ALTURA/2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobrinha = 1
    pixels = []

    comida_x , comida_y = gerar_comida()

    while not game_over:
        TELA.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type== pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
        
        #comida
        desenhar_comida(tamanho_quadrado,comida_x,comida_y)

        #atualizar a posiçao da cobrinha
        if x < 0 or x >= TELA_LARGURA or y < 0 or y >= TELA_ALTURA:
            game_over = True
        x += velocidade_x
        y += velocidade_y


        if x == comida_x and y == comida_y:
                tamanho_cobrinha += 1

                #gerar nova comida
                comida_x,comida_y = gerar_comida()
                
        #cobrinha
        pixels.append([x,y])
        if len(pixels) > tamanho_cobrinha:
            del pixels[0]

        #se a cobrinha bateu em si propia
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                game_over = True

                
        #desenhar cobrinha
        desenhar_cobrinha(tamanho_quadrado,pixels)

        #pontos
        desenhar_pontos(tamanho_cobrinha - 1)

        #atualizaçao da tela
        pygame.display.update()


        relogio.tick(vel_game)


if __name__ == '__main__':
    rodar_jogo()