from utilidadesCeV import moeda as md
from utilidadesCeV.dado import leiadinheiro as ld

value = ld('Digite o preço: R$')
aumento = int(input('Digite a porcentagem de aumento: '))
desconto = int(input('Digite a porcentagem de desconto: '))
md.resumo(value, aumento, desconto)
