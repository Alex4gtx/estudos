sexo = ''
while sexo != 'M' and sexo != 'F':
    r = str(input('informe seu sexo [M/F]: ')).upper().strip()[0]
    sexo = r
    if r not in 'MF':
        print('dados invalidos. por favor, ', end='')
print('Sexo {} registrado com sucesso!'.format(sexo))

# pode ser feito de outra forma

sexo = str(input('informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MFmf':
    sexo = str(input('dados invalidos. por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
