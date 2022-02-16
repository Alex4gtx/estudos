n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('Tirando {} e {}, a media do aluno é {:.1f}'.format(n1, n2, media))

if media < 5.0:
    print('O aluno está \033[0:31mREPROVADO!\033[m')
elif media <= 6.9:
    print('O aluno está de \033[0:33mRECUPERAÇÂO!\033[m')
else:
    print('O aluno esta \033[0:32mAPROVADO!\033[m')
