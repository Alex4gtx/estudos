def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial de um numero n.
    """
    lst = list(range(1, n))
    lst.reverse()
    tmp = n
    for numb in lst:
        tmp = tmp * numb
    if show:
        print(f'{n}', end='')
        for numb in lst:
            print(f' x {numb}', end='')
        print(f' = {tmp}')
    else:
        return tmp


fatorial(7, True)
help(fatorial)
