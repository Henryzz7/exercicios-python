n = int(input())
vet = []

for i in range(n):
    vet.append(int(input()))
campo = []

for j in range(n):
    if j == 0 == n-1:
        minas = vet[j]
    elif j == 0:
        minas = vet[j] + vet[j+1]
    elif n-1 > j > 0:
        minas = vet[j-1] + vet[j] + vet[j+1]
    else:
        minas = vet[j-1] + vet[j]
    campo.append(minas)

for a in range(len(campo)):
    print(campo[a])