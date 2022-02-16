import math

a1 = math.trunc(984644.785739857937483570378578350694566000000)
a2 = 23.5
print(a1)
print(str(math.floor(a2)))
print('o valor de pi é {:.4f}'.format(math.pi))

print('o numero inteiro de 12,567 é {}'.format(math.trunc(12.567)))

numero = int(input('insira o numero: '))
print(f'O antecessor do numero {numero} é {numero - 1}, e o seu sucessor é {numero + 1}.')
#outra forma
print('O antecessor do numero {} é {}, e o seu sucessor é {}.'.format(numero, (numero-1), (numero+1)))

print(f'o dobro é {numero*2}, o triplo é {numero*3} e a raiz quadrada é {numero**(1/2)}')

valores = []
while True:
    numb = input('Média Aritmetica\n(para saber o resultado, digite: = )\ndigite o numero: ')
    if numb == '=':
        break
    if not numb:
        continue
    else:
        valores.append(float(numb))
        print(valores)

val_soma = sum(valores)
media = val_soma / int(len(valores))

print(f'A media aritmetica dos seguintes valores {valores}, é igual a {media}')