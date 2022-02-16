numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para a conversão:
\033[1:33m[ 1 ]\033[mconverter para BINARIO
\033[1:33m[ 2 ]\033[mconverter para OCTAL
\033[1:33m[ 3 ]\033[mconverter para HEXADECIMAL''')
opcao = int(input('Escolha sua opção: '))

if opcao == 1:
    tipo = '\033[1:34mBINARIO\033[m'
    resultado = bin(numero)
elif opcao == 2:
    tipo = '\033[1:34mOCTAL\033[m'
    resultado = oct(numero)
elif opcao == 3:
    tipo = '\033[1:34mHEXADECIMAL\033[m'
    resultado = hex(numero)

print('Convertido para {} é igual a {}'.format(tipo, resultado[2:]))
