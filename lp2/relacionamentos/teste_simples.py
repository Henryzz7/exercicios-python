from cliente import Cliente
from endereco import Endereco
from conta import Conta

end1 = Endereco('69918-822', 'Rua Fonte Nova', 'Rio Branco')
end2 = Endereco('69900-000', 'Av Ceará', 'Rio Branco')
end3 = Endereco('69918-553', 'Av Getúlio Vargas', 'Rio Branco')

samuel = Cliente('Samuel', '192.839.489-59', end1)
marcos = Cliente('Marcos', '111.111.111-11', end2)

##print(end1)
##print()
##print(samuel)
##print(marcos)

conta_samuel = Conta(1, samuel, 1000, 200)
conta_marcos = Conta(2, marcos, 0, 500)
conta3 = Conta(3, 'Teste', 0, 1000)
conta_maria = Conta(4, samuel, 1000, 500)

##print(conta_samuel)
##print(conta_marcos)
##print(conta3)
##print(conta_maria)

conta_samuel.ver_saldo()
conta_samuel.depositar(200)
conta_samuel.transferir(conta_marcos, 100)

conta_samuel._historico.ver_extrato()
