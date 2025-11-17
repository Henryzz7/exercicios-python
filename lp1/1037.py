# num = float(input())
#
# if 0 <= num <= 25.00000:
#     print(f"Intervalo [0,25]")
# elif 25.00000 < num <= 50.00000:
#     print(f"Intervalo (25,50]")
# elif 50.00000 < num <= 75.00000:
#     print(f"Intervalo (50,75]")
# elif 75.00000 < num <= 100.00000:
#     print(f"Intervalo (75,100]")
# else:
#     print("Fora de intervalo")

# codigo, quantidade = map(int, input().split())
#
# if codigo == 1:
#     total = quantidade * 4.00
#     print(f"Total: R$ {total:.2f}")
# elif codigo == 2:
#     total = quantidade * 4.50
#     print(f"Total: R$ {total:.2f}")
# elif codigo == 3:
#     total = quantidade * 5.00
#     print(f"Total: R$ {total:.2f}")
# elif codigo == 4:
#     total = quantidade * 2.00
#     print(f"Total: R$ {total:.2f}")
# elif codigo == 5:
#     total = quantidade * 1.50
#     print(f"Total: R$ {total:.2f}")
# else:
#     print("Lanche indisponível")


'''n1, n2, n3, n4 = map(float, input().split())

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/ 10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 < media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media2 = (media + nota_exame)/2
    if media2 >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media2:.1f}")
    elif media2 <= 4.9:
        print("Aluno reprovado.")
        print(f"Media final: {media2:.1f}")'''

p1 = input()
p2 = input()
p3 = input()

if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if p3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if p2 == 'inseto':
        if p3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if p3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
