jogadores = list()
while True:
    jogador = dict()
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    lst = list()
    partidas = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
    for q in range(0, partidas):
        lst.append(int(input(f'Quantos gols na partida {q + 1}? ')))
    jogador['Gols'] = lst[:]
    jogador['Total'] = sum(jogador['Gols'])
    jogadores.append(jogador.copy())
    while True:
        sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if sair in 'NnSs':
            break
        else:
            print('Erro! Insira apenas S ou N.')
    if sair == 'N':
        break
print(f'{30*"-="}\n{jogadores}\n{30*"-="}\ncod nome{" "*14}gols{10*" "}total\n{42*"-"}')
for i, jog in enumerate(jogadores):
    print(f'{i+1:>3} {jog["Nome"]:<18}{str(jog["Gols"]):<14}{jog["Total"]}')
qut = 0
while qut != 999:
    print(f'{42*"-"}')
    qut = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if qut != 999 and qut <= len(jogadores):
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[qut - 1]["Nome"]}:')
        for c, p in enumerate(jogadores[qut - 1]['Gols']):
            print(f'    No jogo {c + 1}, fez {p} gols.')
        print(f'Foi um total de {jogadores[qut - 1]["Total"]} gols.')
    elif qut > len(jogadores) and qut != 999:
        print(f'Erro! não existe jogador com o código {qut}!')
