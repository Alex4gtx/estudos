numb = int(input('Digite um numero para calcular seu fatorial: '))
numb2 = numb - 1
mem1 = str(numb)+'!'
mem2 = ''
while numb2 != 0:
    result = numb * numb2
    numb = result
    if numb2 == 1:
        mem2 += str(numb2)
    else:
        mem2 += str(numb2) + ' x '
    numb2 -= 1
print(mem1+' = '+mem2+' = '+str(result))

# ou pode ser feito assim

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('{}! = '. format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
