soma = 0
while True:
    numb = float(input('digite um numero: '))
    soma += numb
    if numb == 999:
        break
print(f'a soma dos seguntes numeros é igual a {soma:.2f}')
print(f'{soma:-^30}')
