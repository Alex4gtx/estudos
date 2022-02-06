arquivo = r"C:\Games\parrot\dicionarios\Nova pasta (2)\Top2Billion-probable-v2.txt"


def getlines(arquivo, linha_inicio, quatidade_linha, encoding='utf8'):
    #-> Permite buscar em um arquivo de texto gigante de até mais de 20gb sem exceder a memoria ram, e armazenar uma certa quantidade de dados #por linhas em forma de uma lista.

    #arquivo(str) = diretório onde o arquivo se encontra ex: r"C:\user\usuario\desktop\arquivo.txt"
    #linha_inicio(int) = o numero da linha onde vai iniciar a captura de dados.
    #quantidade_linha(int) = quantidade de dados por linha que vai ser capturado após o linha_inicio.
    #encoding(str) = codificação ex: 'utf8' etc.

    #return(list) = [dados]

    resultado = list()
    with open(arquivo, encoding=encoding) as dicionario:
        flag = False
        end_line = linha_inicio + (quatidade_linha - 1)
        for i, line in enumerate(dicionario):
            if i == linha_inicio:
                flag = True
            if flag:
                resultado.append(line.strip())
                if i == end_line:
                    return resultado


resultado = getlines(arquivo, 10000, 100)
print(resultado)
