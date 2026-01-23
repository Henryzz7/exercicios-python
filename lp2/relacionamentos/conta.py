from cliente import Cliente
from historico import Historico

class SaldoInsuficienteError(Exception):
    pass
class Conta:
    #Método de inicialização dos objetos do tipo Conta
    #Características de identificação da conta
    def __init__(self, numero, cliente=None, saldo, limite):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico() #Referência da classe Historico

    #Métodos de controle de acesso

    def get_titular(self):
        return self._titular
    def set_titular(self, nome):
        self._titular = nome

    def get_historico(self):
        return self._historico

    #Método de controle de acesso com anotações (forma pythônica)
    @property
    def limite(self):
        return self._limite
    #Características comportamentais (o que podemos executar)

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    def sacar(self, valor):
        try:
            if valor > self._saldo + self._limite:
                raise SaldoInsuficienteError('Operação não realizada. Valor é maior que saldo + limite. ')
                # return False
            else:
                self._saldo -= valor
                self._historico._transacoes.append(f'Saque de {valor} realizado.')
                return True
        except SaldoInsuficienteError as sie:
            print(sie)





    def depositar(self, valor):
        self._saldo += valor
        self._historico._transacoes.append(f'Depósito de {valor} realizado.')

    def ver_saldo(self):
        if self._saldo < 0:
            print(f'Conta número: {self._numero} | Saldo: {self._saldo} | usando limite: '
                  f'{self._limite} com saldo de '
                  f'{self._limite + self._saldo}')
        else:
            print(f'Conta número: {self._numero} | Saldo: {self._saldo}')

    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            self._historico._transacoes.append(f'Transferência de {valor} realizada.')
            return True
        else:
            return False

    def __str__(self):
        return f'Conta número: {self._numero}, Titular: {self._titular}'
