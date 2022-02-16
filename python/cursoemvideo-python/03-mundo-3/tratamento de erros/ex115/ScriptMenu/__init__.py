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


def menu(lst_opcoes):
    """
    -> menu formatado e colorido
    :param lst_opcoes: (obrigatorio) insira uma lista com as opções em ordem
    :return: menu formatado
    """
    print(f'{40*"-"}\n{"MENU PRINCIPAL":^40}\n{40*"-"}')
    for n in range(1, 4):
        c(4)
        print(f'{n} - \033[m', end='')
        c(5)
        print(str(lst_opcoes[n-1]), end='')
        c(0)
    print(40*'-')


def intopc(text):
    """
    -> entrada de opção do usuario
    :param text: insira o texto igual a função input
    :return: retorna numero inteiro da opção escolhida
    """
    while True:
        try:
            c(3)
            n = int(input(text + '\033[m'))
        except KeyboardInterrupt:
            c(2)
            print('Erro! O usuario não quis informar a opção!', end='')
            c()
        except:
            c(2)
            print('Erro! Por favor, digite um número inteiro válido!', end='')
            c()
        else:
            return n


def check_op(str_opcao):
    """
    -> mostra opção escolhida formatada
    :param n: (obrigatório) digite o texto da opção
    :return: retorna opção formatado
    """
    print(f'{40*"-"}\n{str_opcao:^40}\n{40*"-"}')


def msg_end():
    """
    :return: retorna mensagem de fim do programa formatado
    """
    print(f'{40*"-"}\n{"Saindo do sistema... Até logo!":^40}\n{40*"-"}')
