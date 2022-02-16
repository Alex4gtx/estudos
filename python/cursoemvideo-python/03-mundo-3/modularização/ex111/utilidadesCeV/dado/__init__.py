def leiadinheiro(prompt):
    """
    -> funciona igual ao input, porem melhorado
    :param prompt: coloque uma informação
    :return: retorna valor apenas financeiro
    """
    while True:
        fin = str(input(prompt)).strip().replace(',', '.')
        if fin.replace('.', '').isnumeric():
            numb = float(fin)
            break
        else:
            print(f'\033[1:31mErro! "{fin}" não é um preço válido!\033[m')
    return numb
