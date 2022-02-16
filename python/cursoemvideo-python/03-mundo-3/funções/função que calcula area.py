def area():
    """chama prompt, calcula e mostra a area de um terreno em m²"""
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    area = largura * comprimento
    print(f'A área de um terreno de {largura:.1f}x{comprimento:.1f} é de {area:.1f}m².')


# programa principal
print(f'{"controle de terrenos":^40}\n{40 * "-"}')
area()
