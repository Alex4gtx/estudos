prompt = int(input('digite um numero que eu direi se é par ou impar: '))

calculo = prompt % 2

if calculo == 0:
    print('O numero {} é par!'.format(prompt))
else:
    print('O numero {} é impar!'.format(prompt))
