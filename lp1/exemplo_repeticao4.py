

'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0

for valores in [a,b,c,d,e]:
    resultado = valores%2
    if resultado == 0:
        count +=1
print(f'{count} valores pares')'''

'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count_par = 0
count_impar = 0
count_pos = 0
count_neg = 0

for valores in [a,b,c,d,e]:
    if valores > 0:
        count_pos +=1
    elif valores < 0:
        count_neg +=1
    resultado = valores%2
    if resultado == 0:
        count_par +=1
    else:
        count_impar +=1

print(f'{count_par} valor(es) par(es)')
print(f'{count_impar} valor(es) impar(es)')
print(f'{count_pos} valor(es) positivo(s)')
print(f'{count_neg} valor(es) negativo(s)')'''

'''x = int(input())

for valor in range(1,x +1):
    resultado = valor%2
    if resultado != 0:
        print(valor)'''


'''x = int(input())
y = int(input())

soma = 0
if x > y:
    for valor in range(x-1,y, -1):
        resultado = valor%2
        if resultado != 0:
            soma += valor
else:
    for valor in range(x + 1, y + 1,):
        resultado = valor % 2
        if resultado != 0:
            soma += valor
print(soma)'''

'''x = int(input())
i = 0

while i < 6:
    resultado = x%2
    if resultado != 0:
        print(x)
        i+=1
    x +=1'''

