def ver_pessoas(arquivo):
    """
    -> mostra arquivos txt
    :param arquivo: (obrigatorio) str/digite o arquivo com sua extensão
    :return: retorna leitura de dados
    """
    from user_system.sistema_cor import c
    try:
        with open(arquivo, 'r') as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                l = line.split()
                nome = ''
                for p in l[:-1]:
                    nome += p + ' '
                print(f'{nome:<30}{l[-1]} anos')
    except:
        c(2)
        print('Erro de leitura de dados! O arquivo pode estar corrompido.', end='')
        c()


def cadastrar_p(dados, arquivo):
    """
    -> recebe dados e realiza cadastro
    :param dados: str
    :param arquivo: arquivo de texto
    :return: cadastro
    """
    from user_system.sistema_cor import c
    try:
        with open(arquivo, 'a') as f_obj:
            f_obj.writelines(dados)
    except:
        c(2)
        print('Erro de esrita de dados! O arquivo pode estar corrompido.', end='')
        c()


def input_dados():
    """
    -> entrada de dados de usuario nome/idade
    :return: retorna string pronta com nome e idade para serem salvos na função cadastrar_p
    """
    from user_system.sistema_cor import c
    dado = ''
    while True:
        try:
            while True:
                nome = str(input('Nome: ')).strip().title()
                if nome.isalpha():
                    break
                else:
                    c(2)
                    print('Erro! Insira um nome válido!', end='')
                    c()
        except:
            c(2)
            print('Erro!', end='')
            c()
        else:
            dado += nome + ' '
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            c(2)
            print('Erro! Insira apenas números inteiros!', end='')
            c()
        else:
            dado += str(idade)
            break
    return dado + '\n'
