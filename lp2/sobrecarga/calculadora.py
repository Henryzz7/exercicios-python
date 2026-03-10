class Calculadora:
    def soma(self, *args):
        soma_str = ''
        soma_num = 0
        for i in args:
            if not i.isalpha():
                soma_num += i
            else:
                soma_str += i
        return f'Soma de números: {soma_num} | Soma de caracteres: {soma_str}'


teste = Calculadora()
print(teste.soma(2,3,5))
