print(f'{40*"-"}\n{"LISTAGEM DE PREÇOS": ^40}\n{40*"-"}')
listagem = ('lapis', 'borracha', 'caderno', 'estojo')
preco = (1.75, 2.00, 15.90, 25.00)
for c, n in enumerate(listagem):
    print(f'{n:.<30}R${preco[c]: >8}')
print(40*'-')

# pode ser feito assim

print(f'\n{40*"-"}\n{"LISTAGEM DE PREÇOS": ^40}\n{40*"-"}')
listagem = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00)
for c, n in enumerate(listagem):
    if c % 2 == 0:
        print(f'{n:.<30}', end='')
    else:
        print(f'R${n: >8}')
print(40*'-')
