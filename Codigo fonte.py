#------------------------------importes------------------------------#
import pygame 
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
    pygame.mixer.init()
#------------------------------fim importes--------------------------#

#codigo fonte inicio#
diretorio-principal = os.path.dirname(_file_)
    diretorio-imagens = os.path.join(diretorio-principal,'imagens')
        diretorio-audios = os.path.join(diretorio-principal, 'audios')

            #tela#
            LARGURA = 640
            ALTURA = 480
            BRANCO = (255,255,255)
            tela = pygame.display.set_mode((LARGURA, ALTURA))
            pygame.display.set_caption('Teste')
            #tela fim#

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, '')).convert_alpha()

   som_colisao = pygame.mixer.Sound(os.path.join(diretorio_audios, ''))
        som_colisao.set_volume(1)

    som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_audios, ''))
        som_pontuacao.set_volume(1)

colidiu = False

escolha_obstaculo = choice([0, 1])

pontos = 0

velocidade_jogo = 10            

        
    tela.blit(texto_pontos, (520, 30))

    pygame.display.flip()