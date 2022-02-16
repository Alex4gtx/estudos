idade_total = 0
mulher_menor = 0
nome_h = ''
idade_h = 0

for p in range(1, 5):
    print((4*'-')+' '+str(p)+'ª PESSOA '+(4*'-'))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    idade_total += idade

    if sexo == 'F' and idade < 20:
        mulher_menor += 1

    if sexo == 'M':
        if idade == 0:
            nome_h = nome
            idade_h = idade
        if idade > idade_h:
            nome_h = nome
            idade_h = idade

media_idade = idade_total / 5

print('\nAmedia de idade do grupo é de {:.1f} anos.'.format(media_idade))
print('O homen mais velho tem {} anos e se chama {}.'.format(idade_h, nome_h))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher_menor))
