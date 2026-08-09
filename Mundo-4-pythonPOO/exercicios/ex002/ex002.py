# Declaração de Classe

class Gafanhoto:

    def __init__(self, n = '< DESCONHECIDO >', i = 0):  # Método Construtor
        # Atributos de Instância
        self.nome = n
        self.idade = i

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


# Declaração de Objeto

g1 = Gafanhoto('Victor', 17)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto('Sabrina', 17)
g2.aniversario()
print(g2.mensagem())
