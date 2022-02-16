matriz = []
x = y = 0
for c in range(1, 10):
    matriz.append(int(input(f'Digite um valor para [{x}, {y}] ')))
    if y == 2:
        x += 1
        y = 0
    else:
        y += 1
print(f'''{30*"-="}
[ {matriz[0]: ^4} ][ {matriz[1]: ^4} ][ {matriz[2]: ^4} ]
[ {matriz[3]: ^4} ][ {matriz[4]: ^4} ][ {matriz[5]: ^4} ]
[ {matriz[6]: ^4} ][ {matriz[7]: ^4} ][ {matriz[8]: ^4} ]''')

# ou pode ser feito assim

matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz1[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz1[l][c]}:^5]', end='')
    print()
