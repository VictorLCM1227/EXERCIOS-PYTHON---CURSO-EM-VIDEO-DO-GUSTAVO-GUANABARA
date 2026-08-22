from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f'Olá, Sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo' 


c1 = Funcionario('Maria', 'Administração', 'Diretoria')
print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())