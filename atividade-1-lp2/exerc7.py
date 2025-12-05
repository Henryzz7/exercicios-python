class RespostaInvalidaError(Exception):
    pass

while True:
    try:
        entrada = input('Deseja continuar [S/N]: ')
        if entrada.isalpha():
            if entrada == 'S' or entrada == 's':
                print('FIM')
                break
            elif entrada == 'N' or entrada == 'n':
                print('Encerrando...')
                break
            else:
                raise RespostaInvalidaError()
        else:
            raise RespostaInvalidaError()
    except RespostaInvalidaError:
        print('Entrada invalida')
        pass

