contagem = ''
for c in range(0, 51, 2):
    contagem += str(c) + ' '
contagem += 'ACABOU!'
print(contagem)

# pode ser feito dessa forma tambem

for f in range(0, 51, 2):
    print(f, end=' ')
print('ACABOU!')
