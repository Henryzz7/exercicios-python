n = int(input())

mat = []
# n == quadras
for i in range(n+1):
    linha = []
    linha = list(map(int, input().split()))
    mat.append(linha)

seguro = []

for i in range(n):
    for j in range(n):
        camera = 0
        camera += mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]
        if camera >= 2:
            seguro.append('S')
        else:
            seguro.append('U')

vet = []

for i in range(n):
    for j in range(n):

print(vet)

# 00 01
# 10 11
#
# 01 02
# 11 12

'''        for a in range(i,i+1):
            esquina = []
            for s in range(j,j+1):
                esquina.append(mat)
                quadra'''