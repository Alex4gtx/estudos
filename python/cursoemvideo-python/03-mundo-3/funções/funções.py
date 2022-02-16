def ftitle(titulo): # funcão definida 'def' com o nome 'ftitle' e recebe o parametro 'titulo'
    """formata um titulo de um programa""" # docstring = um tipo de comentario usado apenas para a função
    print(f'{40 * "-"}\n{str(titulo).upper():^40}\n{40 * "-"}') # codigos


def line(): # função simples sem parametros
    """mostra 40 linhas -= """
    print(40 * '-=')


def lst_s(*numb): # '*' * recebe numb = * é usado quando não se sabe a quantidade de parametros a receber //
    """cria uma lista de numeros personalizados""" # // pode ser colocado antes ou depois numb*
    lista = list(numb)
    return lista # return é usado para retornar dados


def mst_line(lista):
    """mostra valores de lista em linhas diferente"""
    for l in lista:
        print(l)


def dobra(lst):
    """dobra o valor de uma lista"""
    c = 0
    while c < len(lst):
        lst[c] *= 2
        c += 1


# programa principal
ftitle('alex giovani hirsch')
line()
print(lst_s(1, 3, 5))

mst_line(lst_s(2, 4, 6, 7, 34, 12))
