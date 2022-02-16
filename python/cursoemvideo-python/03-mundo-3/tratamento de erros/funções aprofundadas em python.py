def leiaint(text=''):
    """
    -> filtra apenas numeros inteiros, mostra erros personalizados
    :param text: (opcional) pode ser colocado um texto como o do input
    :return: retorna numero inteiro apenas
    """
    while True:
        try:
            n = int(input(text))
        except ValueError:
            print('\033[31mErro! Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não informar o número!\033[m')
            return 0
        else:
            return n


def leiafloat(text=''):
    """
        -> filtra apenas numeros flutuantes, mostra erros personalizados
        :param text: (opcional) pode ser colocado um texto como o do input
        :return: retorna numero de ponto flutuante apenas
        """
    while True:
        try:
            n = float(input(text))
        except ValueError:
            print('\033[31mErro! Por favor, digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não informar o número!\033[m')
            return 0.0
        else:
            return n


i = leiaint('DIGITE UM NUMERO INTEIRO: ')
f = leiafloat('DIGITE UM NUMERO REAL: ')
print(f'o valor inteiro digitado foi {i} e o valor real foi {f}')
