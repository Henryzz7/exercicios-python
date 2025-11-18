def geradora():
    for i in range(1,11):
        yield i

iterador = geradora()
# Iterando 2 vezes
print(f'Fora do laço: {next(iterador)}')

# Gera novamente ou reinicia o iterador
iterador = geradora()

# Iterando em toda a estrutura

while True:
    try:
        print(f'Dentro do laço: {next(iterador)}')

    except:
        print('Final do iterador')
        break



iterador = geradora()
lista = list(iterador)
print(f'Lista gerada: {lista}')