tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', "sete", "oito", 'nove', 'dez', 'onze', 'doze',
         "treze", 'catorze', 'quinze', "dezesseis", 'dezessete', "dezoito", 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while num not in range(0, 21):
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Você digitou o numero {tupla[num]}')
    c = ' '
    while c not in 'SNsn':
        c = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if c == "S":
            break
    if c == 'N':
        break
