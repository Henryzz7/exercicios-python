n = int(input())

for a in range(n):
    linha = input()
    vetor = list(linha)
    num1 = ''.join(vetor[2:4])
    num2 = ''.join(vetor[5:8])
    num3 = ''.join(vetor[11:13])
    soma = int(num1) + int(num2) + int(num3)
    print(soma)
