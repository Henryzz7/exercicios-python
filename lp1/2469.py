n = int(input())
notas = list(map(int, input().split()))
frequencia = [0]*101

for i in range(n):
    frequencia[notas[i]] += 1

maior = 0
indice = 0
for i in range(len(frequencia)):
    if frequencia[i] >= maior:
        maior = frequencia[i]
        indice = i
print(indice)
