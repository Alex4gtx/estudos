lst_value = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lst_value:
        print('\033[1:31mValor duplicado!\033[m não vou adicionar...')
    else:
        lst_value.append(valor)
        print('\033[1:32mValor adicionado com sucesso...\033[m')
    q = 'q'
    while q not in 'SNsn':
        q = str(input('Quer continuar? [S/N] ')).upper()[0]
    if q == 'N':
        break
lst_value.sort()
print(f'{40*"-="}\nVocê digitou os valores {lst_value}')
