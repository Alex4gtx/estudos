def c(char=0, back=0):
    """
    -> facilita ao implementar cores nos códigos
    CORES: (caractere/fundo) preto = 1, vermelho = 2, verde = 3, amarelo = 4, azul = 5, lilas = 6, ciano = 7, branco = 8
    :param char: (opcional) cod de cor 1 a 8
    :param back: (opcional) cod de cor 1 a 8
    :return: cor, se vazio retorna cor original do prompt
    """
    opt = list(range(1, 9))
    lstc = list(range(30, 39))
    lstb = list(range(40, 49))
    result = '\033['
    if char > 0:
        if char in opt:
            for i, c in enumerate(lstc):
                if char == i + 1:
                    result += str(c)
    if char > 0 and back > 0:
        result += ';'
    if back > 0:
        if back in opt:
            for i, c in enumerate(lstb):
                if back == i + 1:
                    result += str(c)
    result += 'm'
    if char == 0 and back == 0:
        return print(result)
    else:
        return print(result, end='')
