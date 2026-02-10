from funcionario import Funcionario
from gerente import Gerente
from controle import Controle

f1 = Funcionario('Fulano', '11111111111', 10000)
g1 = Gerente('Beltrano', '99999999999', 20000, '123', 10)

f1.redefinir_salario()
g1.redefinir_salario()
print(f1.get_bonificacao)
print(g1.get_bonificacao)

Controle.update_total(f1)
Controle.update_total(g1)

print(Controle.get_total())

Controle.update_total('aaaaaaaa')
