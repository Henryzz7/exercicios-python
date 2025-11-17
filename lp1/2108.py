n = input()
maior = 0

while True:

    if n == '0':
        break

    lista = n.split(' ')
    contador = []


    for i in range(len(lista)):
        tamanho = len(lista[i])
        if tamanho >= maior:
            maior = tamanho
            palavra = lista[i]
        contador.append(str(tamanho))
    caracters = '-'.join(contador)
    print(caracters)

    n = input()
print()
print('The biggest word: ' + palavra)