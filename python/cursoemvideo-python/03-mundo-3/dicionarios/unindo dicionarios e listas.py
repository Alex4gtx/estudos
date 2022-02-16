pessoas = list()
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if dados['sexo'] not in 'mMfF':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            break
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    while True:
        qt = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if qt in 'snSN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if qt in 'Nn':
        break
soma = 0
mulheres = list()
for c in pessoas:
    soma += c['idade']
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])
media = soma / len(pessoas)
homem = mulher = 0
for p in pessoas:
    if p['sexo'] == 'F' and p['idade'] > mulher:
        mulher = p['idade']
    if p['sexo'] == 'M' and p['idade'] > mulher:
        homem = p['idade']
print(30 * '-=')
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.\nB) A média de idade é de {media:.2f} anos.')
if len(mulheres) != 0:
    print('C) As mulheres cadastradas foram ', end='')
    for i, m in enumerate(mulheres):
        if i + 1 == len(mulheres):
            print(f'{m}.')
        else:
            print(f'{m}, ', end='')
else:
    print('C) Não possue mulheres cadastradas!')
print('D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['sexo'] == 'M' and p['idade'] == homem or p['sexo'] == 'F' and p['idade'] == mulher:
        count = 0
        for k, v in p.items():
            if count == 0:
                print(f'{k:>8} = {v}; ', end='')
                count += 1
            else:
                print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
