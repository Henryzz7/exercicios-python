padrao = '654321'

'''while True:
    entrada = input()
    if entrada == padrao:
        break
    elif entrada != padrao:
        print('Senha incorreta')
        continue

print('Senha correta')'''


while True:
    try:
        reclamacao = int(input())
        if reclamacao == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break