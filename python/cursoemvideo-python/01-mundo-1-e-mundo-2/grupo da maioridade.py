from datetime import datetime

atual = datetime.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    p_ano = int(input('digite o ano de nascimento da {}° pessoa: '.format(pessoa)))
    idade = atual - p_ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('''\nAo todo tivemos {} pessoas maiores de idade
E tambem tivemos {} pessoas menores de idade'''.format(maior, menor))
