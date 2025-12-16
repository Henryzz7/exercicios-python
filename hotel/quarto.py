class Quarto:

    def __init__(self, numero, hospedes, camas):
        self._numero = numero
        self._hospedes = hospedes
        self._camas = camas
        self._reservado = False

    #Garantir que os quartos sejam reservados se disponíveis
    def reservar_quarto(self):
        if self._reservado:
            print("Quarto indisponível.")
        else:
            self._reservado = True
            print('Quarto reservado com sucesso.')

    def liberar_quarto(self):
        self._reservado = False
        print('Quarto liberado.')