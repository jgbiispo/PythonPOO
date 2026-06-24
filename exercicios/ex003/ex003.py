class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"Conta {self.id} de {self.titular} criada com sucesso")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        print(f"Saque de {valor} realizado com sucesso")


    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem saldo R$ {self.saldo:,.2f}"



c1 = ContaBancaria(123, "Maria", 1000)
print(c1)
c1.sacar(500)
c1.depositar(300)
print(c1)
c1.sacar(3500)
print(c1)

