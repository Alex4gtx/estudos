lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um numero: ')))
    q = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if q in 'Nn':
        break
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'{30*"-="}\nA lista completa é {lista}\nA lista de pares é {par}\nA lista de impares é {impar}')
