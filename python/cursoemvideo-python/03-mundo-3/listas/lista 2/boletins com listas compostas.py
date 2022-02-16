alunos = []
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])
    q = str(input('Quer continuar? [S/N] '))[0]
    if q in 'Nn':
        break
print(f'{30*"-="}')
for c, d in enumerate(alunos):
    if c == 0:
        print(f'{"No.":<3}{"NOME":<17}{"MÉDIA"}\n{30*"-"}')
    print(f'{c:<3}{d[0]:<17}{d[3]:.1f}')
n_aluno = 0
while n_aluno != 999:
    print(35 * '-')
    n_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n_aluno == 999:
        print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
    else:
        print(f'Notas de {alunos[n_aluno][0]} são [{alunos[n_aluno][1]}, {alunos[n_aluno][2]}]')
