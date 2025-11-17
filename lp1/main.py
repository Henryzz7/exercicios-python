import decimal
import math

'''n = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.0, 0.50, 0.25, 0.10, 0.01]

print("NOTAS:")
for nota in notas:
    quantidade = 0
    if n - nota >= 0:
        quantidade = n // nota
        n = n % nota
        print(f"{int(quantidade)} nota(s) de R$ {float(nota)}")
    else:
        print(f"{int(quantidade)} nota(s) de R$ {float(nota)}")

print("MOEDAS:")
for moeda in moedas:
    quantidade = 0
    if n - moeda >= 0.00:
        quantidade = n // moeda
        n = n % moeda
        print(f"{int(quantidade)} moeda(s) de R$ {float(moeda):.2f}")
    else:
        print(f"{int(quantidade)} moeda(s) de R$ {float(moeda):.2f}")'''


'''n = int(input())
i = 0
for i in range(0, n):
    input()
print("Ciencia da Computacao")'''

'''p1, c1, p2, c2 = map(int, input().split())

result1 = p1 * c1
result2 = p2 * c2
if result1 == result2:
    print(0)
elif result1 > result2:
    print(-1)
else:
    print(1)'''


# letra = input().upper()
#
# az = [chr(i)for i in range(ord('A'), ord('Z') + 1)]
# index = 0
# for lt in az:
#     index+=1
#     if letra == lt:
#         print(index)


# A, B, C = map(float, input().split())
#
# if A == 0:
#     print("Impossivel calcular")
# else:
#     delta = (B**2) - (4*A*C)
#     if delta > 0:
#         x1 = (-B + math.sqrt(delta))/(2*A)
#         x2 = (-B - math.sqrt(delta)) / (2 * A)
#         print(f"R1 = {x1:.5f}")
#         print(f"R2 = {x2:.5f}")
#     elif delta == 0:
#         x1 = (-B + math.sqrt(delta)) / (2 * A)
#         print(f"R1 = {x1:.5f}")
#     else:
#         print("Impossivel calcular")
