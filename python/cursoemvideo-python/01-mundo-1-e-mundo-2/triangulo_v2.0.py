prompt = 'Digite um comprimento de um lado do triâgulo: '
n1 = float(input(prompt))
n2 = float(input(prompt))
n3 = float(input(prompt))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('os segmentos a cima podem formar um triângulo.')
    if n1 == n2 == n3:
        print('o triângulo é equilátero!')
    elif n1 != n2 != n3 != n1:
        print('o triângulo é ESCALENO!')
    else:
        print("o triângulo é ISÓSCELES!")
else:
    print('os segmentos acima não podem formar um triângulo.')
