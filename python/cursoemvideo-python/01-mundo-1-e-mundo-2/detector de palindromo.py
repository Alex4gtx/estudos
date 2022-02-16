palavra = str(input('digite uma palavra: ')).strip()
p2 = ''
for p in palavra:
    p2 += p + ' '
p3 = p2.strip().split()
p3.reverse()
p4 = ''
for c in p3:
    p4 += c
print('o reverso da palara {} é {}.'.format(palavra, p4))
if palavra.lower() == p4:
    print('A palavra é um PALINDROMO!')
else:
    print('A palavra não é um palindromo')

# ou pode ser feito dessa forma

frase = str(input('digite uma palavra: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if frase == inverso:
    print('A palavra é um PALINDROMO!')
else:
    print('A palavra não é um palindromo')

# ou pode ser feito dessa forma

frase = str(input('digite uma palavra: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
if frase == inverso:
    print('A palavra é um PALINDROMO!')
else:
    print('A palavra não é um palindromo')
