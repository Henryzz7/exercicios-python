from cliente import Cliente
from endereco import Endereco
from conta import Conta
from agencia import Agencia
from emprestimo import Emprestimo

samuel = Cliente('Samuel', '192.839.489-59')
marcos = Cliente('Marcos', '111.111.111-11')

conta_1 = Conta(1, 1000, 200)
conta_2 = Conta(2, 1000, 500)
conta_3 = Conta(3, 3000, 300)

conta_1.associar_cliente(samuel, 'titular')
conta_2.associar_cliente(marcos, 'titular')
conta_3.associar_cliente(samuel, 'titular')

ag_centro = Agencia()
ag_centro.adicionar_conta(conta_1)
ag_centro.adicionar_conta(conta_2)
ag_centro.adicionar_conta(conta_3)

#Pelo conceito de encapsulamento
#temos que criar um método para acessar
#

print(conta_1._total_contas)

print(Conta.get_total_contas())














##ag_centro.listar_contas()
##ag_centro.fechar_agencia()

##
##ag_centro.fechar_conta(conta_2)
##ag_centro.desativar_conta(conta_3)
##samuel.get_listar_contas()
##ag_centro.listar_contas()

##empA = Emprestimo(conta_1, 1000, 4)
##empB = Emprestimo(conta_1, 2000, 5)
##emp.pagar_parcela()
##
##conta_1.listar_emprestimos()
##conta_1.transferir(conta_2, 1000)
##conta_1._historico.ver_extrato()
##conta_2._historico.ver_extrato()
##
##conta_2.ver_saldo()


##conta_master = Conta(1, 1000, 200)
##conta_will = Conta(2, 1000, 500)

##conta_master.associar_cliente(samuel, 'titular')
##conta_will.associar_cliente(samuel, 'dependente')
##conta_will.associar_cliente(marcos, 'titular')
##
##conta_will.get_listar_clientes()
##samuel.get_listar_contas()
