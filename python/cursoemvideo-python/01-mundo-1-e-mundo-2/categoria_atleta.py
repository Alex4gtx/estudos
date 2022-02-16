from datetime import date

nascimento = int(input('Digite sua data de nascimento: '))

atual = date.today().year
idade = atual - nascimento
cl = ''

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    cl = 'mirim'
elif idade <= 14:
    cl = 'infantil'
elif idade <= 19:
    cl = 'junior'
elif idade <= 25:
    cl = 'sênior'
else:
    cl = 'master'

print('Classificação: {}'.format(cl.upper()))