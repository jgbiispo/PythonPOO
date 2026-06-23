# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instâncias
        self.nome = ""
        self.idade = 0

    # Métodos de Instâncias
    def aniversaro(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "João"
g1.idade = 19
g1.aniversaro()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Maria"
g2.idade = 32
print(g2.mensagem())