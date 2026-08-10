# Declaração de Classe

class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use 
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = '< DESCONHECIDO >', idade = 0):  # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f'Estado: nome = {self.nome}; idade = {self.idade}'

# Declaração de Objeto

g1 = Gafanhoto('Victor', 17)
g1.aniversario()
print(g1)

g2 = Gafanhoto('Sabrina', 17)
g2.aniversario()
print(g2)

print(g1.__doc__)

print(g1.__getstate__())
print(g1.__dict__)
