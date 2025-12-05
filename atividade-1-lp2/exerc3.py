# A lista inicial pode receber qualquer valor além de inteiros

lista = list(input().split(','))

# lista_int vai receber somente os valores inteiros após a lista inicial ser processada
lista_int = []

# Guarda os inteiros na lista e, caso encontre algo que não possa ser convertido, retorna uma exceção com uma mensagem
for valor in lista:
    try:
         valor = int(valor)
         lista_int.append(valor)
    except ValueError:
        print(f'O valor inserido "{valor}" não pode ser convertido para inteiro.')
        pass

print(f'\nNova lista de inteiros gerada: {lista_int}')