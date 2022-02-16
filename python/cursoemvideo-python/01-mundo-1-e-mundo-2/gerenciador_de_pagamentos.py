print('{:=^40}'.format(' LOJAS ALEX '))
p_total = float(input('Preço das compreas: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('escolha uma opção: '))

op_1 = p_total - (p_total / 100) * 10
op_2 = p_total - (p_total / 100) * 5
op_4 = p_total + (p_total / 100) * 20

if opcao == 1:
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p_total, op_1))
elif opcao == 2:
    print('sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p_total, op_2))
elif opcao == 3:
    print('o valor da sua compra vai custar R${:.2f} e será parcelada em 2x de R${:.2f}'.format(p_total, p_total / 2))
elif opcao == 4:
    parcelas = int(input('quantas parcelas? '))
    prest = op_4 / parcelas
    print('''Sua compra será parcelada em {}x de R${:.2f} COM JUROS
Sua compra de R${:.2f} vai custar R${:.2f} no final.'''.format(parcelas, prest, p_total, op_4))
else:
    print('\033[1:31mOPÇÃO INVALIDA! Tente novamente.')
