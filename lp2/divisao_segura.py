def divisao_segura(x, y):
    try:
        divisao = int(x)/int(y)
    except ValueError as ve:
        return 'Valor Indevido'
    except ZeroDivisionError as ze:
        return'Divisão por zero'

while True:
    try:
        resultado = []
        entrada = input().split()
        for i in range(0, len(entrada)-1, 2):
            resultado.append(divisao_segura(entrada[i], entrada[i+1]))
        print(resultado)
    except EOFError as eof:
        break
    except KeyboardInterrupt as kie:
        break

