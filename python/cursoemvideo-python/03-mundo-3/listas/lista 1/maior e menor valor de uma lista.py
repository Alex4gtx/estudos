valores = list(int(input('Digite um valor: ')) for c in range(0, 5))
print(f'{40*"~"}\nVocê digitou os valores {valores}')
mx = max(valores)
mn = min(valores)
print(f'o maior valor da lista é {mx} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mx:
        print(f'{i}... ', end='')
print(f'\no menor valor da lista é {mn} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mn:
        print(f'{i}... ', end='')
