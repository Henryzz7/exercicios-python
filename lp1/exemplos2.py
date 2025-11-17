import time

n = 10**8
#iterativo
inicial = time.time()
vetor = []
for i in range(n):
    vetor.append(i)
#print(vetor)

final = time.time()
print(round(final-inicial,2))
#list-comprehension
inicial = time.time()
vetor = []
vetor = [i for i in range(n)]

final = time.time()
print(round(final-inicial,2))

#função geradora
inicial = time.time()

vetor= []
vetor = (i for i in range(n))

for i in vetor:
    continue
final = time.time()
print(round(final-inicial, 2))