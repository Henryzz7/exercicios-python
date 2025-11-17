# Questão 2 prova n1p1

n = int(input())
for i in range(n):
    caverna = input()
    vet = []
    for j in caverna:
        vet.append(j)
    pilha = []
    tesouro = 0
    for x in vet:
        if x == '{':
            pilha.append(x)
        elif x == '}':
            if len(pilha) > 0:
                pilha.pop()
                tesouro +=1
    print(tesouro)
