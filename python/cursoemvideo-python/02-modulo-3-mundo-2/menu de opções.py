from time import sleep

valor1 = int(input('primeiro valor: '))
valor2 = int(input('segundo valor: '))
sair = False
while not sair:
    print('\t[ 1 ] somar\n\t[ 2 ] multiplicar\n\t[ 3 ] maior\n\t[ 4 ] Novos numeros\n\t[ 5 ] sair do programa')
    opcao = int(input('\033[0:33m>>>>>\033[m Qual é a sua opção? '))

    if opcao == 0 or opcao > 5:
        print('\033[1:31mOpção invalida\033[m, tente novamente.')
    else:
        if opcao == 1:
            print('a soma entre valor {} + {} = {}'.format(valor1, valor2, valor1+valor2))
        if opcao == 2:
            print('o resultado de {} x {} = {}'.format(valor1, valor2, valor1 * valor2))
        if opcao == 3:
            maior = ''
            if valor1 > valor2:
                maior = 'o maior é ' + str(valor1)
            elif valor1 < valor2:
                maior = 'o maior é ' + str(valor2)
            else:
                maior = 'ambos são iguais'
            print('entre {} e {} {}'.format(valor1, valor2, maior))
        if opcao == 4:
            print('informe os numeros novamente:')
            valor1 = int(input('primeiro valor: '))
            valor2 = int(input('segundo valor: '))
        if opcao == 5:
            sair = True
    print(10 * '=-=')
print('Finalizando...')
sleep(2)
print(10*'=-=')
print('Fim do programa! volte sempre!')
