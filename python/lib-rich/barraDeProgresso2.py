from rich.console import Console
from time import sleep

console = Console()

def criar_arquivos():
    for i in range(10):
        with open(f'arquivo{i}.txt', 'w') as file:
            file.write('criamos um novo arquivo')
            sleep(1)
            console.log(f'Tarefa {i} finalizada!')


with console.status('[green]Realizando a tarefa....[/]') as arquivo:
    criar_arquivos()
