print('Gerador de PA\n'+(10*'-='))
primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
c = 9
print(f'{primeiro} > ', end='')
while c > 0:
    primeiro += razao
    print(f'{primeiro}', end='')
    print(' > ' if c > 1 else ' = fim', end='')
    c -= 1
