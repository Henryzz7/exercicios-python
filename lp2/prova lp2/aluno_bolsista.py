from aluno import Aluno
class AlunoBolsista(Aluno):
    def __init__(self, nome, data, valor = 0):
        super().__init__(nome, data)
        self._valor_bolsa = valor
        self._total = 0

    def receber_bolsa(self):
        self._total += self._valor_bolsa

    # def reajustar_bolsa(self):
    #     pass
class BolsistaGraduacao(AlunoBolsista):

    def __init__(self, nome, data):
        super().__init__(nome, data, 700)

    def reajustar_bolsa(self):
        self._valor_bolsa *= 1.09


class BolsistaPos(AlunoBolsista):
    def __init__(self, nome, data):
        super().__init__(nome, data, 2100)

    def reajustar_bolsa(self):
        self._valor_bolsa *= 1.12

