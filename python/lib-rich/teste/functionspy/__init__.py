def input_valueVerification(moedas_dict):
    while True:
        value = str(input('digite o comando da primeira moeda: '))

        if value in moedas_dict:
            print(f'A moeda {value} foi escolhida')
            return {value: moedas_dict[value]}
        else:
            print('O código inserido é inválido')


def tabelaEscolha(moedas_dict):
    from rich.table import Table
    from rich.console import Console

    table = Table(title='Cotações')
    console = Console()

    table.add_column('Comandos',justify='center')
    table.add_column('Moedas')

    table.add_row('btc', moedas_dict['btc'])
    table.add_row('brl', moedas_dict['brl'])
    table.add_row('dl', moedas_dict['dl'])

    return console.print(table)


moedas = {'dl': 'Dolar Americano', 'btc': 'Bitcoin', 'brl': 'Real'}
