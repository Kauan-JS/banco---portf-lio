class ContaBancaria:
    """Cria uma conta bancaria para deposito ou saque"""
    def __init__(self, ID, Nome, saldo = 0):
        self.ID = ID
        self.Titular = Nome
        self.saldon = saldo
    
    def __str__(self):
        return f'A conta {self.ID} de {self.Titular} tem o saldo de R${self.saldon:.2f}'
    
    def Deposito(self,valor):
        self.saldon += valor

    def Saque(self, valor):
        if valor > self.saldon:
            print(f"Saque de R${valor} NEGADO! SALDO INSUFICIENTE!")
        else:
            self.saldon -= valor
 
    
hamaki = ContaBancaria(610562, 'Hamaki', 5000)
hamaki.Deposito(100)
hamaki.Saque(5200)
hamaki.Saque(500)
print(hamaki)


    
