'''x = int(input())
y = int(input())
soma = 0

if x > y:
    for valor in range(y, x + 1):
        resto = valor % 13
        if resto != 0:
            soma += valor
elif x < y:
    for valor in range(x, y + 1):
        resto = valor % 13
        if resto != 0:
            soma += valor

print(soma)'''

'''e, f, c = map(int, input().split())

garrafas = e + f
total = 0

while garrafas >= c:
    resto = garrafas%c
    bebidas = garrafas // c
    garrafas = bebidas + resto
    total += bebidas

print(total)'''

'''n = int(input())
valor = n
sorte = False
while n >= 10:
    ultimo = n%10
    sobra = n//10
    penultimo = (sobra)%10
    n = sobra
    if ultimo == 3 and penultimo == 1:
        sorte = True
        break
if sorte == True:
    print(f'{valor} es de Mala Suerte')
else:
    print(f'{valor} NO es de Mala Suerte')'''



