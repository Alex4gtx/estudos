from datetime import date

atual = date.today().year

nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))

if idade == 18:
    print('Você tem que se alistar \033[0:31mIMEDIATAMENTE!\033[m')
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda faltam \033[1:32m{}\033[m anos para o alistamento'.format(18 - idade))
else:
    print('\033[1:33mVocê deveria ter se alistado há {} anos.'.format(idade - 18))
