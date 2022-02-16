jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
lst = list()
partidas = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
for q in range(0, partidas):
    lst.append(int(input(f'Quantos gols na partida {q + 1}? ')))
jogador['Gols'] = lst[:]
jogador['Total'] = sum(jogador['Gols'])
print(f'{30*"-="}\n{jogador}\n{30*"-="}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'{30*"-="}\nO jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for c, p in enumerate(jogador['Gols']):
    print(f'    => Na partida {c + 1}, fez {p} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
