from presidente import Presidente
from gerente import Gerente
from cliente import Cliente
from sistema import Sistema

# Não autenticáveis
p = Presidente('Ronaldo', '12345678901', 90000)

# Autenticáveis
g = Gerente('Zidane', '98765432109', 80000, '123', 12)
c = Cliente()

sistema = Sistema()
if sistema.logar(g):
    print('Login realizado com sucesso')
else:
    print('Não deu')