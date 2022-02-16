numb1 = 0
numb2 = 1
c = 4
mem = 0
print(('-'*30) + '\nsequencia de fibonacci\n' + ('-'*30))
print(f'{numb1} - {numb2} - ', end='')
while c != 0:
    numb1 = numb1 + numb2
    numb2 = numb1 + numb2
    print(f'{numb1} - {numb2}', end='')
    print(' - ' if c > 1 else ' = Fim\n', end='')
    c -= 1

# ou pode ser feito assim

t1 = 0
t2 = 1
count = 3
print(('-'*30) + '\nsequencia de fibonacci\n' + ('-'*30))
n = int(input('quantos termos você quer mostrar? '))
print(f'{t1} - {t2}', end='')
while c <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' - fim')
