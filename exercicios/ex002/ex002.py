# Declaração de Classe
class Gafanhoto:
    """
    Classe que representa um gafanhoto da academia. Que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)

    Metodos disponiveis:
    aniversario(): Aumenta 1 ano na idade da pessoa.
    """
    def __init__(self, nome = "", idade = 0): # Método Construtor
        # Atributos de Instâncias
        self.nome = nome
        self.idade = idade

    # Métodos de Instâncias
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos."

# Declaração de Objetos
g1 = Gafanhoto("João", 19)
g1.aniversario()

g2 = Gafanhoto("Maria", 17)

print(g1)
print(g2)