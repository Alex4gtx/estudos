pessoas = [] # lista mestre
dado = [] # lista de dados temporario
for c in range(0, 3): # repete 3x
    dado.append(str(input('Nome: ')).strip().title()) # pede string nome e armazena na lista dado | indice 0
    dado.append(int(input('senha: '))) # pede valor inteiro e armazena na lista dado | indice 1
    pessoas.append(dado[:]) # adiciona uma copia [:] da lista dado dentro da lista pessoa
    dado.clear() # limpa a lista dado | clear é um metodo usado para limpar tudo o que ha dentro de uma lista
print(pessoas) # mostra lista pronta
for p in pessoas: # laço mostra os dados de uma lista dentro de outra lista
    print(f'o usuario {p[0]} com a senha {p[1]} foi cadastrado.') # mostra nome e idade p[0] e p[1]

flag = True
while flag:
    user = str(input('insira o nome de usuario: '))
    passw = int(input('insira a senha: '))
    for u in pessoas:
        if user in u and passw in u:
            flag = False
            print(f'usuario {u[0]}, login com sucesso!')
