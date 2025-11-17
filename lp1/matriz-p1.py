# Questão 1 da prova n1p1

n = int(input())

while n > 0:
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            camada = min(i, j, n-i-1, n-j-1)
            valor = (n+1)//2 - camada
            linha.append(valor)
        matriz.append(linha)

    for i in range(n):
        for j in range(n):
            if j == n-1:
                print(f'{matriz[i][j]:3d}')
            else:
                print(f'{matriz[i][j]:3d}', end=' ')
    print()
    n = int(input())