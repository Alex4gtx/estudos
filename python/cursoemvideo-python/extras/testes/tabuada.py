numero = int(input('veja a tabuada do numero\ndigite o numero: '))

print('\n' + 11 * '-')
print(f'{numero} x {1} = {numero * 1}\n{numero} x {2} = {numero * 2}\n{numero} x {3} = {numero * 3}\n'
      f'{numero} x {4} = {numero * 4}\n{numero} x {5} = {numero * 5}\n{numero} x {6} = {numero * 6}\n'
      f'{numero} x {7} = {numero * 7}\n{numero} x {8} = {numero * 8}\n{numero} x {9} = {numero * 9}\n'
      f'{numero} x {10} = {numero * 10}')
print(11 * '-' + '\n')

lst_tabuada = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10]

for numb in lst_tabuada:
    print(f'{numero} x {numb} = {numero * numb}')

print('TABUADA DE 1 A 9:')
for a in range(1, 10):
    print('--' * 5)
    for b in range(1, 11):
        print('{} x {} = {}'.format(a, b, a * b))
