valores = tuple(int(input('Digite um numero: '))for c in range(0, 4)) #novo jeito de repetição
print(f'Você digitou os valores {valores}')

par = numb = ''
for n in valores:
    ns = str(n)
    if ns not in numb and valores.count(n) > 1 and n != 9:
        print(f'O valor {n} apareceu {valores.count(n)} vezes')
        numb += ns
    if n % 2 == 0:
        par += str(n) + ', '

print(f'O valor 9 apareceu {valores.count(9)} vezes') # count conta quantas vezes o valor apareceu
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu na Tupla')
print(f'Os valores pares digitados foram {par}')
