import moeda as md

value = float(input('Digite o preço: R$'))
aumento = int(input('Digite a porcentagem de aumento: '))
desconto = int(input('Digite a porcentagem de desconto: '))
md.resumo(value, aumento, desconto)
