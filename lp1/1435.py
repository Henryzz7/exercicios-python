n = int(input())

while n != 0:
    mat = []
    for i in range(n):
        linha = []
        for j in range(n):
            abaixo = n - i - 1
            acima = n - j - 1
            esquerda = i
            direita = j
            lista = [abaixo, acima, esquerda, direita]
            valor = min(lista)+1
            linha.append(valor)
        mat.append(linha)

    for i in range(n):
        for j in range(n):
            if j == n-1:
                print(f'{mat[i][j]:3d}')
            else:
                print(f'{mat[i][j]:3d}', end=' ')
    print()
    n = int(input())