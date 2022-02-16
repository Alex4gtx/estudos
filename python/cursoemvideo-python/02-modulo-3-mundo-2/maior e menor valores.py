sair = True
cont = soma = maior = menor = 0
while sair:
    num = float(input('digite um numero: '))
    if maior == 0 and menor == 0:
        maior = menor = num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    soma += num
    cont += 1
    s = str(input('quer continuar? [S/N] ')).upper().strip()
    if s == 'N':
        sair = False
media = soma / cont
print('voce digitou {} numeros e a media foi {}'.format(cont, media))
print('o maior valor foi {} e o menor valor foi {}\n'.format(int(maior), int(menor)))

# ou pode ser feito assim

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = float(input('digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('digite um numero: '))
media = soma / quant
print(f'voce digitou {quant} numeros e a media foi {media}\no maior valor foi {maior} e o menor valor foi {menor}\n')
