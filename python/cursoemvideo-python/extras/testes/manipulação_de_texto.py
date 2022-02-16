print("""tem um tipo de texto que pode ser escrito de
modo diferenciado e melhorado usando 
docstring dentro de uma função print o que fica
mais facil, apos isso é só fechar docstring e função\n\n""")

frase = """    tem um tipo de texto que pode ser escrito de
modo diferenciado e melhorado usando 
docstring dentro de uma função print o que fica
mais facil, apos isso é só fechar docstring e função    """

print(frase.split(sep='\n', maxsplit=9))
print(frase.find('tipo'))
print(frase.capitalize())
print(len(frase.strip()))
print('facil' in frase)
print('carro' in frase)
print(frase.find('carro'))

frase2 = 'teste de manipulação de texto em python'
dividido = frase2.split()
print(dividido[0][3])

nome = 'alex giovani hirsch'
nome_s = nome.split()

print(f'nome formatado: {nome.title()}\nprimeiro nome: {nome_s[0].title()}\nquantidade de letras do primeiro nome: '
      f'{len(nome_s[0])}\nnome sem espaços: {nome_s[0] + nome_s[1] + nome_s[2]}')
print(f'numero de letras do nome todo com espaços: {len(nome)}\n'
      f'numero total sem espaços: {len(nome_s[0] + nome_s[1] + nome_s[2])}')
print(nome.capitalize())
print(nome.title())
print('-'.join(nome) + '\n', '-'.join(nome_s))
