from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(Panel((self.nome, self.preco), title='Produto', style='white', width=20))

p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000)

p1.etiqueta()
p2.etiqueta()