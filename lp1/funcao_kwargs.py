def f_dicionario(**kwargs):
    for chave, valor in kwargs.items():
        print(f'Chave:Valor = {chave}:{valor}')

f_dicionario(pessoa1='João', pessoa2='Ana')
