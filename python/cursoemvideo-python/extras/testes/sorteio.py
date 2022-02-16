import random

lst_pessoas = ['alex', 'john', 'carlos', 'camila', 'jack', 'naiane', 'lesley']

num_pessoas = int(len(lst_pessoas))
premio_1 = 'notebook'
premio_2 = 'celular'
premio_3 = 'headset'

pessoa1 = random.choice(lst_pessoas)
lst_pessoas.remove(pessoa1)
pessoa2 = random.choice(lst_pessoas)
lst_pessoas.remove(pessoa2)
pessoa3 = random.choice(lst_pessoas)

print('{:-^40}'.format('resultado do sorteio'))
print(f'1°- Lugar: {pessoa1}, ganhou um {premio_1}\n2°- Lugar: {pessoa2}, ganhou um {premio_2}\n'
      f'3°- Lugar: {pessoa3}, ganhou um {premio_3}')
print('...\n\n')

lst_dezenas = list(range(1, 61))
lst_dez_pronta = []

dez1 = random.choice(lst_dezenas)
lst_dez_pronta.append(dez1)
lst_dezenas.remove(dez1)
dez2 = random.choice(lst_dezenas)
lst_dez_pronta.append(dez2)
lst_dezenas.remove(dez2)
dez3 = random.choice(lst_dezenas)
lst_dez_pronta.append(dez3)
lst_dezenas.remove(dez3)
dez4 = random.choice(lst_dezenas)
lst_dez_pronta.append(dez4)
lst_dezenas.remove(dez4)
dez5 = random.choice(lst_dezenas)
lst_dez_pronta.append(dez5)
lst_dezenas.remove(dez5)
dez6 = random.choice(lst_dezenas)
lst_dez_pronta.append(dez6)

resultado = str(sorted(lst_dez_pronta))
print(resultado)