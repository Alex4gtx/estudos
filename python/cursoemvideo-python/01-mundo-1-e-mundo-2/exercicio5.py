salario = float(input('digite o salario: '))
print('Seu salario atual é de R${:.2f}'.format(salario))

if salario > 1250.00:
    p = 10
    print('Seu salario é acima de R$1250.00, logo terá um aumento de {}%'.format(p))
else:
    p = 15
    print('Seu salario é abaixo de R$1250.00, logo terá um aumento de {}%'.format(p))

salario = (salario / 100) * p + salario

print('Seu novo salario é de R${:.2f}'.format(salario))
