flag = False
count = soma = 0
while not flag:
    inp = int(input('digite um numero [999 para parar]: '))
    if inp == 999:
        flag = True
    else:
        soma += inp
        count += 1
print('voce digitou {} numeros e a soma entre eles foi {}'.format(count, soma))

# ou pode ser feito assim

num = cont = soma = 0
num = int(input('digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um numero [999 para parar]: '))
print('voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))