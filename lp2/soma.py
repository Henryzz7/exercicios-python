# Soma com valores default
# def soma(x=0, y=0, z=0):
#     return x+y+z

# Soma com quantidade arbitrária de parâmetros
def soma_arbitraria(*args):
    resultado = 0
    for x in args:
        resultado += x
    return resultado

soma_anonima = lambda x=0,y=0 : x+y
soma_anonima_arbitraria = lambda *args : sum(args)

print(soma_anonima(10))
print(soma_anonima_arbitraria(10,20,30,40,50,60,70,80,90))

funcao_ternario = lambda x, y : x/y if y!=0 else x
print(funcao_ternario(1,3))

lista = ['Pedro', 'Ana', 'João']
funcao_exemplo_comprehension = lambda nomes : [nome.upper() for nome in nomes]
print(funcao_exemplo_comprehension(lista))