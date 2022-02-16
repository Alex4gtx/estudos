v50 = v20 = v10 = v1 = 0
print(f'{(30*"=")}\n{" BANCO ALEX ":^30}\n{(30*"=")}')
dinheiro = int(input('Que valor você quer sacar? R$'))
while True:
    if dinheiro >= 50:
        v50 += 1
        dinheiro -= 50
    else:
        if dinheiro < 50 and dinheiro >= 20:
            v20 += 1
            dinheiro -= 20
        else:
            if dinheiro < 20 and dinheiro >= 10:
                v10 += 1
                dinheiro -= 10
            else:
                if dinheiro < 10 and dinheiro >= 1:
                    v1 += 1
                    dinheiro -= 1
                else:
                    break
if v50 != 0:
    print(f'Total de {v50} notas de R$50')
if v20 != 0:
    print(f'Total de {v20} notas de R$20')
if v10 != 0:
    print(f'Total de {v10} notas de R$10')
if v1 != 0:
    print(f'Total de {v1} notas de R$1')
print(f'{30*"="}\nVolte sempre ao BANCO ALEX! Tenha um bom dia!')

# ou pode ser feito assim

print(f'{(30*"=")}\n{" BANCO ALEX ":^30}\n{(30*"=")}')
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(f'{30*"="}\nVolte sempre ao BANCO ALEX! Tenha um bom dia!')
