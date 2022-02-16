aluno = {}
aluno['Nome'] = str(input('Nome: ')).title().strip()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] <= 6:
    aluno['situação'] = 'Reprovado'
elif aluno['Media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print(30*'-=')
for k, v in aluno.items():
    print(f'-{k} é igual a {v}')
