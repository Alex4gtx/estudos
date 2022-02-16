# calsses em python (POO)

class ControleRemoto: # toda a classe pela pep precisa começar com letras maiusculas, Pessoas ou ControlesRemotos.
    def __init__(self, cor, altura, profundidade, largura): # __init__ serve para inicializar recebe informações, self = ele mesmo, a propia classe, e recebem atributos
        self.cor = cor # self: self.cor é uma caracteristica da classe, parametro da classe é obrigatório
        self.altura = altura # caracteristicas padrões que possuem em uma classe
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao): # pode ser passado parâmetros ou não
        if botao == '>':
            print('próximo canal')
        elif botao == '<':
            print('voltar ao canal anterior')


controle1 = ControleRemoto('preto', '12cm', '3cm', '3cm') # instancia da classe controle1 criada
print(controle1.cor) #caracteristicas ficam sem ()

controle1.passar_canal('>') # metodos e funções recebem ()