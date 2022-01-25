def filtro_nrepeat(lista_valor, n_palavras=0):
    """
    --> esta função adiciona todas as combinações possiveis de valores sem repetir o valor dentro da tupla.
    lista_valor(str/int) = recebe uma lista com valores.
    n_palavras(int) = recebe a quantidade total de valores que quer combinar.
    return = retorna uma lista com combinações dentro de tuplas.
    """
    from itertools import product #classe do modulo utilizado para criar combinações.

    if n_palavras == 0 or n_palavras == 1 or n_palavras > len(lista_valor):
        n_palavras = len(lista_valor)

    combinacao_n = product(lista_valor, repeat=n_palavras) #instância da classe product.
    lst_original = list(combinacao_n) #coloca os resultados brutos em uma lista.
    resultado_1 = list() #resultado porém em tuplas dentro de uma lista.

    # -filtra os resultados com valores diferentes dos repetidos-
    for ia in range(len(lst_original)):
        tmp = list()
        for ib in range(len(lst_original[ia])):
            tmp.append(lst_original[ia][ib])
        for index in range(len(tmp)):
            flag = False
            if tmp.count(tmp[index]) > 1:
                flag = True
                break
        if flag:
            None #não vai adicionar
            tmp.clear
        else:
            resultado_1.append(lst_original[ia]) #vai adicionar
            tmp.clear
        
        # -converte tuplas em listas
        last_result = list()
    for comb in resultado_1:
        lst_tmp = list()
        for i, c in enumerate(comb):
            lst_tmp.insert(i, c)
        last_result.append(lst_tmp[:])
        lst_tmp.clear
    resultado_1.clear #limpa lista anteriora para economizar memória
    return last_result


def reverse_str(lista_lista_str):
    """
    lista_lista_str = list[['value 1', 'value 2'], ['value 3', 'value 4']]

    recebe uma lista composta por uma lista e com valores separados por espaços
    e os transformam em list[['1 value', '2 value'], ['3 value', '4 value']]

    return = nothing
    """
    for indx1, lst_v in enumerate(lista_lista_str):
        for indx2, value in enumerate(lst_v):
            p = value.split()
            p.reverse()
            p = ' '.join(p)
            lista_lista_str[indx1][indx2] = p
