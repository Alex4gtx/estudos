def dobro(n=0, format=False):
    """
    -> dobra o numero recebido
    :param n: (obrigatorio) recebe numero
    :return: retorna o dobro
    """
    return n * 2 if format is False else moeda(n * 2)


def metade(n=0, format=False):
    """
    -> descobre metade do numero
    :param n: (obrigatorio) recebe numero
    :return: retorna o valor pela metade
    """
    return n / 2 if format is False else moeda(n / 2)


def aumentar(n, taxa=10, format=False):
    """
    -> aumenta o valor em 10%
    :param n: (obrigatorio) recebe o valor
    :return: retorna o valor com um aumento de 10%
    """
    aumento = (n / 100) * taxa
    return n + aumento if format is False else moeda(n + aumento)


def diminuir(n, taxa=10, format=False):
    """
    -> diminui o valor por 10%
    :param n: (obrigatorio) recebe um valor
    :return: retorna o valor subtraido por 10%
    """
    p = (n / 100) * taxa
    return n - p if format is False else moeda(n - p)


def moeda(valor, moeda='R$'):
    """
    -> adiciona fomatação ao valor
    :param valor: (obrigatorio) recebe valor float ou int
    :return: retorna um valor formatado
    """
    val = f'{moeda}{valor:.2f}'.replace('.', ',')
    return val
