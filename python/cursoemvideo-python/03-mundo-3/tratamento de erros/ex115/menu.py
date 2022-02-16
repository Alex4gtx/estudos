import ScriptMenu as Sm
from time import sleep
from banco_de_dados import init_banco_dados
import user_system as Us

# programa principal
init_banco_dados() # inicializa banco de dados
lst_opcoes = ['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do sistema']
opcoes = list(range(1, len(lst_opcoes) + 1))
while True:
    Sm.menu(lst_opcoes) # cabeçalho
    o = Sm.intopc('Sua opção: ') # entrada do usuario para acessar opções
    if o == len(lst_opcoes): #opção sair sempre deve estar no final da lista de opções
        break
    if o not in opcoes: # erro opção inválida
        Sm.c(2)
        print('Erro! Digite uma opção válida!', end='')
        Sm.c()
    else:
        if o == 1: # opção 1
            Sm.check_op('PESSOAS CADASTRADAS')
            Us.ver_pessoas('databank.txt')
        if o == 2: # opção 2
            Sm.check_op('NOVO CADASTRO')
            dados = Us.input_dados()
            Us.cadastrar_p(dados, 'databank.txt')
    sleep(1)
Sm.msg_end() # fim do programa
