nome_c = str(input('digite seu nome: ')).strip()

print('analisando seu nome...'.capitalize())
print('Seu nome em maiuscula é {}'.format(nome_c.upper()))
print('Seu nome em minusculo é {}'.format(nome_c.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome_c) - nome_c.count(' ')))
print(f'seu primeiro nome: {nome_c.split()[0]}\nquantidade de letras do primeiro nome: {len(nome_c.split()[0])}')