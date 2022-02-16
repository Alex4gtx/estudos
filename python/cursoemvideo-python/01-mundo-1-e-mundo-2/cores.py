print((10 * '\033[0:33m-=-') + '\n'+(5 * ' ')+'\033[0:31memprestimo bancario\n\033[m' + (10 * '\033[0:33m-=-'))

v_casa = float(input('\033[0:34mDigite o valor da casa: '))
salario = float(input('\033[0:34mDigite seu salario: '))
tempo = float(input('\033[0:34mQuantos anos pretende pagar? '))

po_salario = (salario / 100) * 30
tempo_m = tempo * 12
valor_mensal = v_casa / tempo_m

if valor_mensal < po_salario:
    print('\n\033[0:32mEmprestimo aprovado!\n\033[m')
    print('Você vai pagar durante {} Anos ({} Meses)'
          ' o valor de R${:.2f}'.format(int(tempo), int(tempo_m), valor_mensal))
else:
    print('\n\033[0:31mEmprestimo negado!\n\033[m')
    print('A parcela excedeu \033[0:31m30%\033[m do valor do seu salário.\nValor da parcela: R${:.2f}\n'
          'você pode pagar: R${:.2f}'.format(valor_mensal, po_salario))
print(20 * '\033[0:33m-=-')
