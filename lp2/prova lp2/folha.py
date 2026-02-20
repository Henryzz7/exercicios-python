class Folha:
    def __init__(self):
        self._bolsistas = []

    def adicionar_bolsista(self, bolsista):
        self._bolsistas.append(bolsista)

    def pagar_bolsas(self):
        for b in self._bolsistas:
            try:
                b.receber_bolsa()
            except Exception as e:
                print(f'Erro no pagamento da bolsa do {b}')
    def reajustar_bolsas(self):
        for b in self._bolsistas:
            try:
                b.reajustar_bolsa()
            except Exception as e:
                print(f'Erro no reajuste da bolsa do {b}')