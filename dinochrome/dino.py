import pygame
import random
import os
import time

TELA_ALTURA = 700
TELA_LARGURA = 900

BACKGROUND = pygame.image.load(os.path.join('IMGS', 'background.png'))
CACTO_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('IMGS','cacto.png')))
DINO_IMGS = [
            pygame.transform.scale2x(pygame.image.load(os.path.join('IMGS','dino.1.png'))),
            pygame.transform.scale2x(pygame.image.load(os.path.join('IMGS','dino.2.png'))),
            pygame.transform.scale2x(pygame.image.load(os.path.join('IMGS','dino.3.png')))
            ]
pygame.font.init()
FONTE_PRINC = pygame.font.SysFont('comic_sans', 40, False, False)

'''
dino jump
cacto vir
cenario mover um pouco
contagem de pontos
velocidade almentar conforme o tempo passa
'''



class Dino:
    VELOCIDADE_ANIMACAO = 5
    IMGS = DINO_IMGS
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.altura = self.y
        self.velocidade = 0
        self.comtagem_imagem = 0
        self.imagem = self.IMGS[0]
    
    def jump(self):
        self.velocidade = -10 # no pygame 'pular' é igual a diminuir o 'y'
        self.altura = self.y


    def desenhar(self,tela):
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[2]
        self.contagem_imagem = 0

        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo =self.imagem.get_rect(center=pos_centro_imagem)
        tela.blit(self.imagem, retangulo.topleft)


    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)

class Cacto:
    VELOCIDADE = 5

    def __init__(self,x):
        self.x = x
        self.passou = False 
        self.IMAGEM_CACTO = CACTO_IMG
        self.altura = 80
        self.pos_base = 0

    def definir_altura(self):
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE
    
    def desenhar(self,tela):
        tela.blit(self.IMAGEM_CACTO, (self.x, self.pos_base))

    def colidir (self,dino):
        dino_mask = dino.get_mask()
        cacto_mask = pygame.mask.from_surface(self.IMAGEM_CACTO)

        distancia_cacto = (self.x - dino.x, self.pos_base - round(dino.y))

        cacto_ponto = dino_mask.overlap(cacto_mask,distancia_cacto)

        if cacto_ponto:
            return True
        else:
            return False
        
class Background:
    VELOCIDADE = 10
    LARGURA = BACKGROUND.get_width()
    IMAGEM = BACKGROUND

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))


def desenhar_tela(tela, dinos, cactos, pontos):
    tela.blit(BACKGROUND, (0, 0))
    for dino in dinos:
        dino.desenhar(tela)
    for cacto in cactos:
        cacto.desenhar(tela)

    texto = FONTE_PRINC.render(f"Pontuação: {pontos}", 1, (0, 0, 0))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    
    pygame.display.update()

def main():

    dinos = [Dino(230,350)]
    background = Background(730)
    cactos = [Cacto(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        for dino in dinos:
                            Dino.jump()

        background.mover()

        adicionar_cacto = False
        remover_cactos = []
        for cacto in cactos:
            for i, dino in enumerate(dinos):
                if cacto.colidir(dino):
                    dinos.pop(i)
                if not cacto.passou and dino.x > cacto.x:
                    cacto.passou = True
                    adicionar_cacto = True
            cacto.mover()
            if cacto.x + cacto.IMAGEM_CACTO.get_width() < 0:
                remover_cactos.append(cacto)
            
        if adicionar_cacto:
            pontos += 1
            cactos.append(Cacto(600))
            
        for cacto in remover_cactos:
                cactos.remove(cacto)
        for i, dino in enumerate(dinos):
            if (dino.y + dino.imagem.get_height()) > background.y or Dino.y < 0:
                dinos.pop(i)
        desenhar_tela(tela, dinos, cactos, pontos)

if __name__ == '__main__':
    main()