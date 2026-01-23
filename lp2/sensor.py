class SemLeitura(Exception):
    pass

class Sensor:
    def __init__(self, id):
        self._id = id
        self._leituras = []

    def registrar_leitura(self, valor):
        self._leituras.append(valor)

    def get_media(self):
        try:
            if not self._leituras:
                raise SemLeitura('Sem leituras registradas')
            return sum(self._leituras)/len(self._leituras)
        except SemLeitura as sl:
            return sl
            pass

    
    
##        soma = 0
##        count = 0
##        for valor in self._leituras:
##            soma += valor
##            count +=1
##        return soma/count
