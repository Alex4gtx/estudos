from random import randint

n1 = n2 = n3 = n4 = n5 = 0
for c in range(0, 5):
    n = randint(0, 10)
    if c == 0:
        n1 = n
    if c == 1:
        n2 = n
    if c == 2:
        n3 = n
    if c == 3:
        n4 = n
    if c == 4:
        n5 = n
numbers = (n1, n2, n3, n4, n5)
print('Os valores sorteados foram: ', end='')
for c, n in enumerate(numbers):
    print(n, end='')
    print(' ', end='')
sn = sorted(numbers)
print(f'\nO maior valor sorteado foi {sn[-1]}\nO menor valor sorteado foi {sn[0]}')

# ou pode ser feito assim

v1 = randint(0, 10)
v2 = randint(0, 10)
v3 = randint(0, 10)
v4 = randint(0, 10)
v5 = randint(0, 10)
numb = (v1, v2, v3, v4, v5)
for c, n in enumerate(numb):
    if c == 0:
        print('\nOs valores sorteados foram: ', end='')
    if c < 4:
            print(f'{n} ', end='')
    else:
        print(f'{n}')

nm = sorted(numb)
print(f'O maior valor sorteado foi {nm[-1]}\nO menor valor sorteado foi {nm[0]}')

# ou pode ser feito assim

t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)) # tuplas suportam funções
for n in range(0, 5):
    if n == 0:
        print('\nOs valores sorteados foram: ', end='')
    if n < 4:
        print(f'{t[n]},', end=' ')
    else:
        print(f'{t[n]}')
print(f'O maior valor sorteado foi {max(t)}\nO menor valor sorteado foi {min(t)}') # min pega o menor numero
#max pega o maior numero de uma () [] {}

