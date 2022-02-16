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


def aumentar(n=0, taxa=10, format=False):
    """
    -> aumenta o valor em 10%
    :param n: (obrigatorio) recebe o valor
    :return: retorna o valor com um aumento de 10%
    """
    aumento = (n / 100) * taxa
    return n + aumento if format is False else moeda(n + aumento)


def diminuir(n=0, taxa=10, format=False):
    """
    -> diminui o valor por 10%
    :param n: (obrigatorio) recebe um valor
    :return: retorna o valor subtraido por 10%
    """
    p = (n / 100) * taxa
    return n - p if format is False else moeda(n - p)


def moeda(valor=0, moeda='R$'):
    """
    -> adiciona fomatação ao valor
    :param valor: (obrigatorio) recebe valor float ou int
    :return: retorna um valor formatado
    """
    val = f'{moeda}{valor:.2f}'.replace('.', ',')
    return val


def resumo(valor=0, aumento=10, reducao=10):
    """
    -> mostra valores formatados em uma lista de forma padrão.
    :param valor: (obrigatorio) insere um valor de preço inicial
    :param aumento: insere um aumento %
    :param redução: insere uma redução %
    :return: retorna tabela formatado padrão
    """
    print(f'{40*"-"}\n{"RESUMO DO VALOR":^40}\n{40*"-"}')
    print(f'{"Preço analizado:":<30}{moeda(valor):<10}\n'
          f'{"O dobro do preço:":<30}{dobro(valor, True):<10}\n'
          f'{"Metade do preço:":<30}{metade(valor, True):<10}\n'
          f'{str(aumento)+"% de aumento:":<30}{aumentar(valor, taxa=aumento, format=True):<10}\n'
          f'{str(reducao)+"% de redução:":<30}{diminuir(valor, taxa=reducao, format=True):<10}\n'
          f'{40*"-"}')
