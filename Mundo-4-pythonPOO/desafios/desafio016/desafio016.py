from rich import print
from rich import inspect

class Funcionario:
    def __init__(self, nome, setor, cargo):
        #atributos de classe
        empresa = "Curso em vídeo"

        #Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f':handshake: Olá, Sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}' 

    

Funcionario.empresa = 'Hostnet'

c1 = Funcionario('Maria', 'Administração', 'Diretoria')
print(c1.apresentacao())
# inspect(c1, methods=True, dunder=True)

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())

inspect(Funcionario)