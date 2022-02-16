print('Gerador de PA\n'+(10*'-='))
primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
c = 9
print(f'{primeiro} > ', end='')
while c > 0:
    primeiro += razao
    print(f'{primeiro}', end='')
    print(' > ' if c > 1 else ' = pausa', end='')
    c -= 1
    if c == 0:
        c = int(input('\nQuantos termos você quer mostrar a mais? '))

# ou pode ser assim

print('Gerador de PA\n'+(10*'-='))
primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
c = 9
ca = 10
print(f'{primeiro} > ', end='')
while c != 0:
    while c > 0:
        primeiro += razao
        print(f'{primeiro}', end='')
        print(' > ' if c > 1 else ' = pausa', end='')
        c -= 1
    c = int(input('\nQuantos termos você quer mostrar a mais? '))
    ca += c
print('progressão finalizada com {} termos motrados.'.format(ca))
