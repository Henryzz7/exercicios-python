from conta import Conta

conta1 = Conta(1, 'Limeira', 150.5, 10)
# print(type(conta1))
print(id(conta1))

conta2 = Conta(2, 'Kauã', 5678, 1000)
# print(id(conta2))

conta3 = conta1

print(id(conta3))


#Definir características em tempo de execução não é correto

# conta1.titular = 'Limeira'
# conta1.saldo = 150.5
# conta1.numero = 1
print()
#
print(conta1.titular)
conta1.ver_saldo()
# print(conta1.saldo)
# print(conta1.limite)
#
print()
# conta2.titular = 'Kauã'
# conta2.saldo = 5678
# conta2.numero = 2
# conta2.limite = 1000
#
print(conta2.titular)
conta2.ver_saldo()
# print(conta2.saldo)
# print(conta2.limite)
print()

conta1.depositar(500)
conta1.ver_saldo()
if conta1.sacar(661):
    print('Saque com sucesso')
else:
    print('Saldo insuficiente')
print()
conta1.ver_saldo()



conta3.depositar(100)
conta3.ver_saldo()
print()

if conta1.transferir(conta2, 760.5):
    print('Transferência realizada com sucesso')
else:
    print('Saldo insuficiente')
conta1.ver_saldo()
conta2.ver_saldo()

# print(conta1.__dict__)
# print(dir(Conta))

print(conta2)