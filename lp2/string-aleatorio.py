import random

# Definição da Função
def random_string(palavra):
    lista = list(palavra)
    random.shuffle(lista)
    return lista

# Altera o primeiro com o último e o segundo com o penúltimo
def customiza_string(palavra):
    lista = list(palavra)
    resultado = lista[len(lista)-2:] + lista[2:-2] + lista[:2]
    return resultado

def imprime():
    print('Função que retorna None')

print(imprime())

# Chamada da Função
palavra = 'Teste'
print(''.join(random_string(palavra)))

print(customiza_string(palavra))