# Possibilitar formas diferentes de criar objetos
class Sobrecarga:
    def __init__(self, *args):
        self._tam = len(args)
        self._lista = args
        self.__str__()

    def __str__(self):
        if self._tam == 0:
            return 'Obj sem argumento'
        elif self._tam == 1:
            return 'Obj com um parâmetro'
            
##    def __init__(self):
##        print('Dois')
##    def __init__(self):
##        print('Três')

teste = Sobrecarga()
print(teste)
