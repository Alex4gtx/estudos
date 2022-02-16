matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(30*'-=')
pares = tcoluna = 0
for d in matriz:
    for n in d:
        if n % 2 == 0:
            pares += n
    tcoluna += d[2]
print(f'A soma dos valores pares é {pares}\nA soma dos valores da terceira coluna é {tcoluna}.\n'
      f'O maior valor da segunda linha é {max(matriz[1])}.')
