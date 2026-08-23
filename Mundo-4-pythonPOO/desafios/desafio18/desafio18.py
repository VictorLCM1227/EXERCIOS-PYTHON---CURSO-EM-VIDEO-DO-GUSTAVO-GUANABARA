from rich import print
from rich.panel import Panel


class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    # Método construtor
    def __init__(self, titulo, quantidade_participantes):
        # Atributos de Instãncia
        self.titulo = titulo
        self.quantidade_participantes = quantidade_participantes

    def __str__(self):
        return f'Esse é o {self.titulo} com {self.quantidade_participantes} pessoas participando.'

    def calcular_quantidade_carne(self) ->float:
        return self.quantidade_participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) ->float:
        return self.calcular_quantidade_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) ->float:
        return self.calcular_custo_total() / self.quantidade_participantes
        

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidade_participantes} convidados[/]\n'
        conteudo += f'Cada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:.2f}\n' 
        conteudo += f'Recomendo [blue]comprar {self.calcular_quantidade_carne():.3f}kg[/] de carne\n'
        conteudo += f'O custo total será de [green]R${self.calcular_custo_total():,.2f}[/]\n'
        conteudo += f'Cada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar.\n'
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()

c2 = Churrasco('Festa do fim de ano', 80)
c2.analisar()

# 400g por pessoa
# preco 82,40