lst_value = []
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > lst_value[-1]:
        lst_value.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lst_value):
            if n <= lst_value[pos]:
                lst_value.insert(pos, n)
                print(f'Adicionado na posicão {pos} da lista...')
                break
            pos += 1
print(f'{30*"-="}\nOs valores digitados em orden foram {lst_value}')
