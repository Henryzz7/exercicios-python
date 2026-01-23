from cliente import Cliente
from endereco import Endereco
from conta import Conta

samuel = Cliente('Samuel', '192.839.489-59')
marcos = Cliente('Marcos', '111.111.111-11')

conta_master = Conta(1, 1000, 200)
conta_will = Conta(2, 1000, 500)

conta_master.associar_cliente(samuel, 'titular')
conta_will.associar_cliente(samuel, 'dependente')
conta_will.associar_cliente(marcos, 'titular')

conta_will.get_listar_clientes()
samuel.get_listar_contas()
