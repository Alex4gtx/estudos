def ficha(nome='<desconhecido>', gols=0):
    """
    -> Ficha de jogador, retorna valores.
    :param nome: (opcional) (srting) recebe nome do jogador
    :param gols: (opcional) (int) recebe gols do jogador
    :return:
    """
    nome = nome.title()
    gols = str(gols)
    if gols[0] not in '0123456789' or gols == 0:
        gols = 0
    else:
        gols = int(gols)
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


ficha(str(input('nome: ')), input('gols: '))
