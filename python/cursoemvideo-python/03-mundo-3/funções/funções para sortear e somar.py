from random import randint


def sorteia():
    """sorteia 5 numeros"""
    lst = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
    print('Sorteando 5 valores da lista ', end='')
    for n in lst:
        print(f'{n} ', end='')
    print('pronto!')
    return lst


def somapar(lst):
    """soma apenas o numero par da lista"""
    sp = 0
    for n in lst:
        if n % 2 == 0:
            sp += n
    print(f'Somando os valores pares de {str(lst)}, temos {sp}')


somapar(sorteia())
