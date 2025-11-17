n = input()

frase = input()

lista = frase.split(' ')

contador = 0

for i in range(len(lista)):
    count = 0
    sublista = list(lista[i])
    for a in range(len(sublista)):
        if n == sublista[a]:
            count+=1
            break
    contador += count

porctg = contador/len(lista)*100

print(f'{porctg:.1f}')


