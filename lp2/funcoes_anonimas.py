
#Exemplo de lp1
# entrada = list(map(int, input().split()))
# print(entrada)

#Exemplo com lambda

lista = [1,2,3,4,5]

quadrados = list(map(lambda x : x**2, lista))

print(quadrados)

teste = [5,6,7,8,9]
soma = list(map(lambda x,y: x+y, lista,teste))
print(soma)

filtro = list(filter(lambda x : x%2 != 0, lista))
print(filtro)

