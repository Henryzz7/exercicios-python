#função geradora
def geradora(lista):
    for i in lista:
        if i < 0:
            yield 'negativo'
        elif i == 0:
            yield 'zero'
        elif i % 2 == 0:
            yield 'par'
        else:
            yield 'impar'
    

entrada = list(map(int, input().split()))

#print(next(geradora(entrada)))
func = geradora(entrada)
for x in geradora(entrada):
    
