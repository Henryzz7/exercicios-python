# n = int(input())
#
# for a in range(n):
#
#     mensagem = input()
#     lista = list(mensagem)
#     nova_Mensagem = []
#     for i in range(len(mensagem)):
#         if ord('A') <= ord(lista[i]) <= ord('Z') or ord('a') <= ord(lista[i]) <= ord('z'):
#             codigo = ord(lista[i])
#             nova_Mensagem.append(chr(codigo+3))
#         else:
#             nova_Mensagem.append(lista[i])
#     nova_Mensagem.reverse()
#
#     indice = len(mensagem)//2
#
#     descript = nova_Mensagem[:indice]
#
#     for j in range(indice, len(nova_Mensagem)):
#         codigo = ord(nova_Mensagem[j])
#         descript.append(chr(codigo-1))
#
#     print(''.join(descript))

n = int(input())

for i in range(n):
    result = ''
    entrada = input()
    # 1° passo:
    for j in range(len(entrada)):
        if entrada[j].isalpha(): #96 < ord(entrada[j]) < 123 or 64 < ord(entrada[j] < 91
            caracter = chr(ord(entrada[j]) + 3)
            result += caracter
        else:
            result += entrada[j]

    #2° passo
    # Com list
    # result = list(result)
    # result.reverse()
    # print(''.join(result))

    result = result[::-1]

    #3° passo

    metade = len(result) // 2
    result_final = result[:metade]
    for j in range(metade, len(result)):
        caracter = chr(ord(result[j]) - 1)
        result_final += caracter

    print(result_final)

