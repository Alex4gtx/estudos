from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title='Filmes favoritos')

table.add_column("none", justify='left', style='red')
table.add_column('data de lançamento', style='green')
table.add_column('faturamento', style='purple')

table.add_row('Piratas do caribe', '2005', '1599999')
table.add_row('star wars', '2009', '345464')
table.add_row('avatar', '2009', '56555555')
table.add_row('vingadores', '2020', '20000')

console.print(table)
