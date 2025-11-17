while True:
    procurado, linha = input().split()
    if procurado == '0' == linha:
        break
    nova_linha = linha.replace(procurado, '')
    if nova_linha == '':
        print('0')
    else:
        print(int(nova_linha))

