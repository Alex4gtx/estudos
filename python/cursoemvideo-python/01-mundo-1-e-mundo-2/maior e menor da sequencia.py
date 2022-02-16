menor_p = 0
maior_p = 0
for p in range(1, 6):
    peso = float(input('peso da {}ª pessoa: '.format(p)))
    if menor_p == 0:
        menor_p = peso
    if peso >= maior_p:
        maior_p = peso
    elif peso < maior_p and peso <= menor_p:
        menor_p = peso

print('\no maior peso lido foi de {}\no menor peso lido foi de {}'.format(maior_p, menor_p))
