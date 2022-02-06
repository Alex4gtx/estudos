def getlines(arquivo, linha_inicio, quatidade_linha, encoding='utf8'):
    """-> Permite buscar em um arquivo de texto gigante de até mais de 20gb sem exceder a memoria ram,
    e armazenar uma certa quantidade de dados #por linhas em forma de uma lista.
    arquivo(str) = diretório onde o arquivo se encontra
    linha_inicio(int) = o numero da linha onde vai iniciar a captura de dados.
    quantidade_linha(int) = quantidade de dados por linha que vai ser capturado após o linha_inicio.
    encoding(str) = codificação ex: 'utf8' etc.
    return(list) = [dados]"""

    from tqdm import tqdm

    resultado = list()
    with open(arquivo, encoding=encoding) as dicionario:
        flag = False
        end_line = linha_inicio + (quatidade_linha - 1)
        for i, line in tqdm(enumerate(dicionario), 'Captando linhas', unit='lines'):
            if i == linha_inicio:
                flag = True
            if flag:
                resultado.append(line.strip())
                if i == end_line:
                    return resultado


def escrever_dados(arquivo, lista_dados, encoding='utf8'):
    """ Escreve dados em um novo arquivo de texto
    arquivo(str) = diretório onde o arquivo se encontra
    lista_dados(list) = lista que será colocada no arquivo
    encoding(str) = codificação ex: 'utf8' etc."""

    from tqdm import tqdm
    from time import sleep

    try:
        with open(arquivo, 'a', encoding=encoding) as f_obj:
            for d in tqdm(lista_dados, 'Escrevendo Dados', unit='lines', colour='green'):
                f_obj.write(d + '\n')      
    except FileNotFoundError:
        print(f'Arquivo ({arquivo}) não encontrado, criando arquivo...')
        sleep(1.5)
        print(f'Arquivo ({arquivo}) criado com sucesso!')
        with open(arquivo, 'w', encoding='utf8') as f_obj:
            for d in tqdm(lista_dados, 'Escrevendo Dados', unit='lines', colour='green'):
                f_obj.write(d + '\n')
        

arquivo = r"C:\Games\parrot\dicionarios\Nova pasta (2)\Top2Billion-probable-v2.txt"
resultado = getlines(arquivo, 200, 10, 'ansi')
escrever_dados('teste.txt', resultado)

print('\nfim\n')
