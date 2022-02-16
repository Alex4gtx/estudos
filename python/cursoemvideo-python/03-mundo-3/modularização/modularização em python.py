from uteis import uteis as ut

num = int(input('digite um valor: '))
fat = ut.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {ut.dobro(num)}\nO triplo de {num} é {ut.triplo(num)}')
