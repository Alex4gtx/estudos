class Clientes:
    def __init__(self, nome, email, plano): # atributos
        """
        ->> classe de usuário
        :param nome: recebe nome do usuario
        :param email: recebe email
        :param plano: recebe plano
        """
        self.nome = nome
        self.email = email
        self.lst_planos = ['free', 'basic', 'premium'] # lista se torna uma caracteristica porem sem ter atributos
        self.plano = ''
        # caracteristicas podem ser acessados ppor qualquer função dentro da classe,
        # // se for colocado self antes, self.caracteristica
        if plano in self.lst_planos:
            self.plano = plano
        else:
            print('Erro! plano invalido!')

    def mudar_plano(self, novo_plano):
        """
        ->> faz a mudança de plano do cliente
        :param novo_plano: insira plano
        :return: mudança do self.plano
        """
        if novo_plano in self.lst_planos:
            self.plano = novo_plano
        else:
            print('plano invalido!')

    def ver_filme(self, filme, plano_filme):
        """
        ->> assistir o filme
        :param filme: nome do filme
        :param plano_filme: tipo do plano do usuario
        :return: o filme para cada tipo de plano diferente
        """
        if self.plano == plano_filme:
            print(f'ver filme {filme}')
        elif self.plano == 'premium':
            print(f'ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print(f'faça um upgrade para premium para ver esse filme')
        else:
            print('plano invalido!')


cliente1 = Clientes('alex', 'alexgiovani35@gmail.com', 'basic')
cliente1.ver_filme('mercenários', 'premium')
cliente1.mudar_plano('premium')
cliente1.ver_filme('mercenários', 'premium')
