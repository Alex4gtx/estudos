from time import sleep
from random import randint
from operator import itemgetter # esse operador troca um valor pelo outro, transforma um valor em chave ex

jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
             'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
print(f'{30 * "-="}\n{"  == RANKING DOS JOGADORES ==  "}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # itemgetter() 0 = chave, 1 = valor, result vira lista
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.4)
