lanche = ('macarrão', 'refri', 'sorvete', 'pizza', 'suco', 'cerveja', 'carne', 'agua', 'licor')
liqu = ('refri', 'suco', 'cerveja', 'agua', 'licor')
for pos, c in enumerate(lanche):
    if c in liqu:
        m = 'tomar'
    else:
        m = 'comer'
    print(f'Eu vou {m} {c}. na posição {pos}')
print(sorted(lanche))
print(lanche)

a = (1, 4, 6, 3)
b = (3, 4, 9, 0, 1) # uma tupla é imutavel
c = a + b
print(c)
print(sorted(c)) # sorted ordena todos itens de uma lista ou tupla de forma temporaria
print(len(c)) # len conta todos os elementos de uma lista ou tupla
print(c.count(4)) # count conta quantos elementos do mesmo valor possui
print(c.index(4))
print(c.index(1, 1)) # index mostra o indice do elemento de uma tupla ou lista
del a # pode deletar tudo ate tuplas
print(a)
