numero = int(input('digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('analisando numero {}'.format(numero))
print('unidades: {}'.format(u))
print('dezenas: {}'.format(d))
print('centenas: {}'.format(c))
print('milhares: {}'.format(m))
