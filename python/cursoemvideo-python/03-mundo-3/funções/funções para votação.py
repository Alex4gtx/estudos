def voto(ano):
    """
    retorna idade e se é possivel votar
    :param ano: insira ano de nascimento
    :return: NEGADO, OPCIONAL e OBRIGATORIO
    """
    from datetime import datetime
    d_atual = datetime.now().date().year
    idade = d_atual - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'NÃO VOTA.'
    elif idade <= 17:
        return 'VOTO OPCIONAL.'
    elif idade < 65:
        return 'VOTO OBRIGATÓRIO.'
    else:
        return 'VOTO OPCIONAL.'


# programa principal
print(voto(int(input("Em que ano você nasceu? "))))