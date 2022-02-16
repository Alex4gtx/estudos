def ihelp(inp_func):
    """
    -> interactive help system
    :param inp_func: (obrigatório) recebe dados como função ou biblioteca
    :return: retorna uma ajuda para cada função ou biblioteca com ide
    """
    from time import sleep
    print(f'\033[1:44m{40*"~"}\n{"Acessando o manual do comando "+inp_func:^40}\n{40*"~"}')
    sleep(0.5)
    print(f'\033[7:40m')
    help(inp_func)
    print('\033[m', end='')


def intro():
    """
    -> introdução
    :return: retorna intodução de forma bonita
    """
    print(f'\033[42m{40*"~"}\n{"Sistema de ajuda pyHELP":^40}\n{40*"~"}')
    print('\033[m', end='')


def endh():
    """
    -> mostra uma mensagem de fim formatada e bonita
    :return: retorna função print formatado
    """
    print(f'\033[41m{40 * "~"}\n{"ATÉ LOGO!":^40}\n{40 * "~"}')
    print('\033[m')


# programa principal
while True:
    intro()
    inp = str(input('Funçao ou biblioteca > '))
    if inp.upper() == 'FIM':
        break
    else:
        ihelp(inp)
endh()
