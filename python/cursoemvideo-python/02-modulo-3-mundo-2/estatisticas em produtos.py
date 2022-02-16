totcompra = prodcaro = prodbarato = 0
pb_nome = ''
print(f'{(30*"-")}\n{"LOJÃO SUPER BARATÃO": ^30}\n{(30*"-")}')
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    totcompra += preco
    if prodbarato == 0:
        prodbarato = preco
        pb_nome = produto
    if preco > 1000:
        prodcaro += 1
    if preco <= prodbarato:
        pb_nome = produto
        prodbarato = preco
    sair = ' '
    while sair not in 'SNsn':
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sair in 'Nn':
        break
print(f'{" FIM DO PROGRAMA ":-^37}\nO total de compra foi R${totcompra:.2f}\n'
      f'Temos {prodcaro} custando mais de R$1000.00\nO produto mais barato foi {pb_nome} que custa R${prodbarato:.2f}')
