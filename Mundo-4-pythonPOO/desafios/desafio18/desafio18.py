from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__(self, titulo, quantidade_participantes):
        self.quantidade_participantes = quantidade_participantes
        self.titulo = titulo

    def analisar(self):
        preco = 82.40
        carne_por_pessoa = 0.4
        quantidade_carne = carne_por_pessoa * self.quantidade_participantes
        custo_total = quantidade_carne * preco
        preco_pessoa = preco * carne_por_pessoa
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade_participantes} convidados[/]\n'
        conteudo += f'Cada participante comerá {carne_por_pessoa}Kg e cada Kg custa R${preco:.2f}\n' 
        conteudo += f'Recomendo [blue]comprar {quantidade_carne:.3f}kg[/] de carne\n'
        conteudo += f'O custo total será de [green]R${custo_total:.2f}[/]\n'
        conteudo += f'Cada pessoa pagará [yellow]R${preco_pessoa:.2f}[/] para participar.\n'
        analise = Panel(conteudo, title=self.titulo, width=70)
        print(analise)

c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()

# 400g por pessoa
# preco 82,40