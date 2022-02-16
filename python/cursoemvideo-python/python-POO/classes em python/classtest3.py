from datetime import datetime as dt

class Pessoa:
    """cria um objeto Pessoa"""

    def __init__(self, nome, data_nasc, peso, altura):
        """inicializa classe Pessoa"""
        self.nome = nome
        self.data_nasc = data_nasc
        self.peso = peso
        self.altura = altura
        ano_atual = dt.today().year
        self.idade = ano_atual - self.data_nasc

    def ver_info(self):
        """mostra informações da classe atual"""
        print(f'Nome: {self.nome}\nIdade: {self.idade} anos\nAno de nascimento: {self.data_nasc}\n'
              f'Altura: {self.altura}m\nPeso: {self.peso}kg')



user1 = Pessoa('Alex Giovani Hirsch', 1997, 78, 1.83)
user1.ver_info()