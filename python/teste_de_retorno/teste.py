import pygame
import os


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.largura, self.altura = 640, 480
        self.tela = pygame.display.set_mode((self.largura,self.altura))
        pygame.display.set_caption('teste de jogos e visual code')
        self.relogio = pygame.time.Clock()

        self.loop_principal = True
        self.preto = (0, 0, 0)
    
    def eventos_controles(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop_principal = False
                self.loop_menu = False
    
    def atualizar_tela(self):
        pygame.display.flip()



j = Jogo()

while j.loop_principal:
    j.eventos_controles()
    j.atualizar_tela()
