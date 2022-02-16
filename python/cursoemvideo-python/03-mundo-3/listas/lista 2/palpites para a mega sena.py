from time import sleep
import random

print(f'{30*"-"}\n{"JOGO NA MEGA SENA":^30}\n{30*"-"}')
nj = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{" SORTEANDO ":=>15}{nj}{" JOGOS ":=<15}')
lista = []
for n in range(0, nj):
    num = list(range(1, 61))
    # noinspection PyRedeclaration
    n = list()
    for c in range(0, 6):
        x = random.choice(num)
        n.append(x)
        num.remove(x)
    n.sort()
    lista.append(n)
for i, c in enumerate(lista):
    print(f'Jogo {i + 1}: {c}')
    sleep(0.5)
print(f'{" < BOA SORTE! > ":=^30}')

# pode ser feito de outra forma

lista1 = list()
jogos = list()
print(f'{30*"-"}\n{"JOGO NA MEGA SENA":^30}\n{30*"-"}')
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista1:
            lista1.append(num)
            cont += 1
        if cont >= 6:
            break
    lista1.sort()
    jogos.append(lista1[:])
    lista1.clear()
    tot += 1
print(f'{" SORTEANDO ":=>15}{quant}{" JOGOS ":=<15}')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)
print(f'{" < BOA SORTE! > ":=^30}')
