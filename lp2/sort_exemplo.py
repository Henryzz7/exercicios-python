lista = [('ovos', 3), ('miragina', 10), ('cafe', 5)]

lista.sort(key = lambda tupla : tupla[0])
print(lista)

matriz = [[1,2,3], [4,5,6,7], [8,9]]
matriz.sort(reverse=True, key = lambda lista : len(lista))
print(matriz)