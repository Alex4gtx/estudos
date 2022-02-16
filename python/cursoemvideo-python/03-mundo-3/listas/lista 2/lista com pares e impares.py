lista = [list(), list()]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'{30*"-="}\nOs valoras pares digitados foram: {lista[0]}\nOs valoras impares digitados foram: {lista[1]}')
