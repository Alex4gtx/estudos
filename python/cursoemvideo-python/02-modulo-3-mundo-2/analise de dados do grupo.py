m_idade = p_homens = m_mulher20 = 0
while True:
    idade = int(input(f'{(30*"-")}\n{"CADASTRE UMA PESSOA": ^30}\n{(30*"-")}\nIdade: '))
    sexo = ' '
    while sexo not in 'MFmf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        m_idade += 1
    if sexo == 'F' and idade < 20:
        m_mulher20 += 1
    elif sexo == 'M':
        p_homens += 1
    sair = str(input((30*'-')+'\nQuer continuar? [S/N] ')).strip().upper()
    if sair == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {m_idade}\nAo todo temos {p_homens} homens cadastrados')
print(f'E temos {m_mulher20} mulheres com menos de 20 anos')
