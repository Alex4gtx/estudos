# listas
pessoas = []
dados = []

# gerencia adição de usuarios
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    # verifica se usuario quer continuar
    q = 'q'
    while q not in 'snSN':
        q = str(input('Quer continuar? [S/N] ').strip().upper())
    if q in 'nN':
        break

# comparação entre maior e menor peso
menor = []
maior = []
for c, p in enumerate(pessoas):
    if c == 0:
        menor.append(p[:])
        maior.append(p[:])
    else:
        if p[1] <= menor[0][1]:
            if p[1] == menor[0][1]:
                menor.append(p[:])
            else:
                menor.clear()
                menor.append(p[:])
        elif p[1] >= maior[0][1]:
            if p[1] == maior[0][1]:
                maior.append(p[:])
            else:
                maior.clear()
                maior.append(p[:])

# mostra o resultado dos dados na tela
print(f'{30*"-="}\nAo todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior[0][1]:.1f}Kg. Peso de ', end='')
# faz a formatação dos nomes da lista maior
for c, m in enumerate(maior):
    if c + 1 == len(maior):
        print(f'{m[0]}.')
    else:
        print(f'{m[0]}, ', end='')
print(f'\nO menor peso foi de {menor[0][1]:.1f}Kg. Peso de ', end='')
# faz a formatação dos nomes da lista menor
for c, m in enumerate(menor):
    if c + 1 == len(menor):
        print(f'{m[0]}.')
    else:
        print(f'{m[0]}, ', end='')

# ou pode ser feito assim

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(dados[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print(f'{30*"-="}\nAo todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai:.1f}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{m[0]}] ', end='')
print(f'O menor peso foi de {men:.1f}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{m[0]}] ', end='')
