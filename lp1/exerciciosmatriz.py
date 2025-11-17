
'''while True:
    n = int(input())
    if n == 0:
        break
    suspeitos = list(map(int, input().split()))

    sus_sort = suspeitos.copy()
    sus_sort.sort()

    maior = sus_sort[0]
    maior2 = sus_sort[0]

    aux = 0
    for i in range(1,n):
        if sus_sort[i] > maior2:
            maior2 = sus_sort[i]
        if maior < maior2:
            aux = maior2
            maior2 = maior
            maior = aux
    assassino = suspeitos.index(maior2)


    print(assassino+1)'''

