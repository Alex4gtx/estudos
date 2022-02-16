nome = 'camila'
idade = 21
peso = 60

print('nome: {}\nidade: {}\npeso: {}\n'.format(nome , idade, peso).title())

print('|{:20}|'.format(nome.title()))
print('|{:<20}|'.format(nome.title()))
print('|{:>20}|'.format(nome.title()))
print('|{:^20}|'.format(nome.title()))

print(f'|{nome.title():=^20}|')
print(f'{nome * 4:_^60}')

print(f'nome: {nome.title()}\nidade: {idade}\npeso: {peso}')

print('hello my name is Alex', end=' ')
print('and i was learning python language! :D')

exe1 = 'exercicio_1'
print(f'\n\n{exe1:-^80}')

n1 = 34
n2 = 90
n3 = -23
n4 = 22

resultado = n1**2 / (23 - n4) + n3 // n2
r1 = 23 - n4
r2 = 34**2
r3 = r2 / r1
r4 = n3 // n2

print(f'{n1}² / (23 - {n4}) + {n3} // {n2}\n{n1}² / {r1} + {n3} // {n2}\n{r2} / {r1} + {n3} // {n2}', end='\n')
print(f'{r3} + {r4}\n = {resultado}')

