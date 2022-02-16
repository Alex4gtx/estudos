def algumafuncao(a, b, c):
    """
    essa função faz alguma coisa.
    :param a: recebe algo
    :param b: recebe lista algo
    :param c: recebe outher
    :return: retora resultado x
    """ # docstring """ """ cliqcar enter para aparecer padrão
    print('hello world!')


help(algumafuncao) # interactive help


def soma(a, b, c=0): # c=0 definido parametro opcional
    """
    faz a soma de a+b+c, c pode ser omitido levando valor de 0
    :param a: recebe numeros float e int (obrigatório)
    :param b: recebe numeros float e int (obrigatório)
    :param c: recebe numeros float e int (opcional)
    :return r: resultado da soma
    """
    global a # global: substitui a variavel local e passa a ser global
    r = a + b + c  # r é uma variavel local
    return r # return: retorna valor

a = 6
k = 2 # variavel global

