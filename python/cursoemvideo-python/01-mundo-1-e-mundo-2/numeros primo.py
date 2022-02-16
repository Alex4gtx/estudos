num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('o numero {} é um numero primo.'.format(num))
else:
    print('o numero {} não é um numero primo.'.format(num))
