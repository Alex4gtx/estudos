from time import sleep


def maior(*numb):
    """mostra o maior numero da sequência"""
    numb = list(numb)
    print(f'{30 * "-="}\nAnalisando os valores passados...')
    for n in numb:
        print(f'{n} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(numb)} valores ao todo.\nO maior valor informado foi {max(numb)}.')


# programa principal
maior(2, 7, 4, 7, 8, 9, 26, 10, 3, 1)
maior(4, 3, 9, 6, 1)
