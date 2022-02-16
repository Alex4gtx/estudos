palavras = ('alex', 'python', 'gang', 'carro', "hunter", 'palavra')
vogais = 'AaEeIiOoUu'
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for c in p:
        if c in vogais:
            print(f'{c} ', end='')
