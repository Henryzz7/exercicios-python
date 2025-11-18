from functools import reduce

# fatura = [('Net', 199.9),('Ifood', 999.87),('Gasolina', 678.0),('Formigão', 400)]
#
# def organizar(lista):
#     lista_modificada = list(map(lambda x,y : x[0],x[1], lista))
#     return lista_modificada
# print(organizar(fatura))


t = (1,2,[50,40])
t[2] += [30,20]
print(t)