class Cliente:
    def __init__(self, nome, cpf, end=None):
        self._nome = nome
        self._cpf = cpf
        self._endereco = end
        self._lista_contas = []

    def __str__(self):
        return f'{self._nome} | {self._cpf} | {self._endereco}'

    
    def get_listar_contas(self):
        print(f'\n\nConta(s) do cliente {self._nome}: ')
        print('-----------------------------------')
        for associacao in self._lista_contas:
            print(associacao._conta)
