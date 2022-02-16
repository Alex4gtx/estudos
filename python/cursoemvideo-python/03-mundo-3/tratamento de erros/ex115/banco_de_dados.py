from ScriptMenu import c


def init_banco_dados():
    """
    -> inicializa, verifica e/ou cria um arquivo de banco de dados
    :return: arquivo databank.txt
    """
    try:
        a = open('databank.txt')
        a.close()
    except FileNotFoundError:
        a = open('databank.txt', 'w')
        a.close()
        c(4)
        print('Arquivo (databank.txt) criado com sucesso!', end='')
        c()
    except:
        c(6)
        print('Erro! arquivo pode estar corrompido!', end='')
        c()
    else:
        c(6)
        print('Banco de dados (databank.txt) encontrado!', end='')
        c()
