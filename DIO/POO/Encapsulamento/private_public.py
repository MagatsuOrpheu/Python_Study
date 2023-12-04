class Conta:
    def __init__(self, agencia, saldo = 0):
        self._saldo = saldo  # <- _saldo é privado 
        self.agencia = agencia  # <- agencia é publico
        self._cartao = 16657787  # <- _cartao é privado
        self.nome = 'Fulano da Silva'  # <- nome é publico


    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        print(f'Seu saldo é: {self._saldo}')
    


conta = Conta('0001', 100)
conta.depositar(100)
conta.mostrar_saldo()