import random

def par(x):
    return x%2 ==0
valor = ['a','b','c']
def imprime():
    random.shuffle(valor)
    #valor = random.randint(1,5)
    print(valor)

imprime()
print(valor)
# while True:
#     x = int(input())
#     if par(x):
#         print(f'{x} é par')
#     else:
#         print(f'{x} não é par')