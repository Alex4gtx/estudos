from random import randint

print((15*'=-') + '\nVAMOS JOGAR PAR OU IMPAR\n' + (15*'=-'))
r = 0
pi = ''
com_op = ''
while True:
    valor = int(input('Diga um valor: '))
    opcao = str(input('Par ou impar? [P/I] ')).strip().upper()
    comp = randint(1, 11)
    soma = valor + comp
    if soma % 2 == 0:
        pi = 'P'
        t = 'DEU PAR'
    else:
        pi = 'I'
        t = 'DEU IMPAR'
    if opcao == 'P':
        com_op = 'I'
    elif opcao == 'I':
        com_op = 'P'
    print((30*'-')+f'\nvocê jogou {valor} e o computador jogou {comp}. total de {soma} {t}\n'+(30*'-'))
    if com_op == pi:
        break
    else:
        print('Você VENCEU!\nVamos jogar novamente...\n'+(15*'=-'))
        r += 1
print(f'Você PERDEU!\n{(15*"=-")}\nGAME OVER! Você venceu {r} vezes.')
