import sys
import traceback

class ValorNegativoError(Exception):
    pass

while True:
    try:
        y = input("Entre com um valor numérico: \n")
        d = int(y)
        if d < 0:
            raise ValorNegativoError('Não entrar com valores negativos')
        x = 5 / d
        print(x)
    except ValorNegativoError as vne:
        print(str(vne))
    except ValueError as ve:
        #Imprimindo a mensagem interna da exceção
        print(str(ve))
        #Imprimir a tupla da exceção
        print(sys.exc_info())
        print('\nValor inadequado. Tente novamente...\n')
        #Impressão da mensagem completa da exceção
        traceback.print_exc()
    except ZeroDivisionError as zde:
        print('\nImpossível dividir por zero, tente novamente...\n')
    except EOFError as eofe:
        print('\nPrograma interrompido pelo teclado\n')
        break
    else:
        print('Deu certo!')
        break
    finally:
        print(f'\nO valor inserido foi o: {y}\n')