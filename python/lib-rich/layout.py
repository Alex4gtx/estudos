from rich import print
from rich.layout import Layout
from rich.panel import Panel #forma de estilizar layout
# ratio = percentual de ocupação da tela no console
layout = Layout()
layout.split_column(
    Layout(Panel('meu app', style='on green'), ratio=3),
    Layout(name='topo', ratio=2),
    Layout(name='baixo', ratio=2),
    Layout(Panel('Criador: Alex', style='purple'), ratio=3)
)

layout['topo'].split_row(
    Layout(Panel('esquerda')),
    Layout(Panel('Direita'))
)
print(layout)
