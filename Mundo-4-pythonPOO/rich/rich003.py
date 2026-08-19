from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')

tabela.add_column('Nome', justify='left', style='red')
tabela.add_column('Preço', justify='center', style='blue')

tabela.add_row('Frango', 'R$1.50')
tabela.add_row('Batata', '[green]R$4.50[/]')

print(tabela)