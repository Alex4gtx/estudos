exp = list(str(input('Digite sua expressão: ')).strip())
if exp.count('(') == exp.count(')'):
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')
