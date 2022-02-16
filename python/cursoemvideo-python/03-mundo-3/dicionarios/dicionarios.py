pessoas = {'nome': 'Alex', 'sexo': 'M', 'idade': 24}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'{"NORMAL":-^30}')
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
print(f'{"apos valor apagado":-^30}')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(f'{"apos mudança de valor":-^30}')
pessoas['nome'] = 'james'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(f'{"apos adicionar um valor":-^30}')
pessoas['peso'] = 78.2
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(50*"--")

brasil = []
estado1 = {'UF': 'Rio Grande do Sul', 'sigla': 'RS'}
estado2 = {'UF': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(f'\n{estado1}\n{estado2}\n')
print(brasil[0]['UF'])
print(brasil[1]['sigla'])
print(30*'--')

estado = dict()
brazil = list()
for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brazil.append(estado.copy())
print(brazil)
for i in brazil:
    for k, v in i.items():
        print(f'O campo {k} tem valor {v}.')
