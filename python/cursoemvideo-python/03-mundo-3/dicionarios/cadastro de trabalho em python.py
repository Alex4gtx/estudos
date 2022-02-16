from datetime import datetime
pessoa = {}
pessoa['Nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.today().year - ano
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['Idade'] + 32) - (datetime.today().year - pessoa['contratação'])
print(f'{30*"-="}')
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')
