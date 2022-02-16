lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    v = 'q'
    while v not in 'NnSs':
        v = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if v == 'N':
        break
lista.sort(reverse=True)
print(f'{30*"="}\nVocê digitou {len(lista)} elementos.\nOs valores em orden decrescente são {lista}')
if 5 in lista:
    print('O numero 5 faz parte da lista')
else:
    print('o numero 5 não faz parte de uma lista')
