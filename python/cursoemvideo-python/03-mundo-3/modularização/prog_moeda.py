import moeda as md

value = float(input('Digite o preço: R$'))
print(f'A metade de {md.moeda(value)} é {md.metade(value, format=True)}\n'
      f'O dobro de {md.moeda(value)} é {md.dobro(value, format=True)}\n'
      f'Aumentando 10%, fica {md.aumentar(value, format=True)}\n'
      f'Diminuindo 10%, fica {md.diminuir(value, format=True)}')
