frase1 = 'Teste de conjunto'
# c= 0
# vogais_unicas = {i: for i in frase if i in 'aeiou'}
# print(vogais_unicas)

frequencia = {}

frase2 = 'Teste de list-comprehension'
for i in frase2:
    if i in 'aeiou':
        if i in frequencia.keys():
            frequencia[i] += 1
        else:
            frequencia[i] = 1
print(frequencia)
fd = {}
fd = {i:frase2.count(i) for i in frase2 if i in 'aeiou'}
print(fd)