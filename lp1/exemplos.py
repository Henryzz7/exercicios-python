frutas2 = {'BANANA CUMPRIDA', 'ABACATE', 'ABACAXI'}

vogais = {'a','e','i','o','u'}
vogais = set('aeiou')
#frutas4 = [letra for item in frutas2 for letra in item if letra.lower() in 'aeiou']

frutas4 = [len([letra for letra in item if letra.lower() in 'aeiou']) for item in frutas2]
print(frutas4)

frutas6 = {len({letra for letra in item if letra.lower() in 'aeiou'}) for item in frutas2}
print(frutas6)

frutas5 = [item.count('A') + item.count('E') + item.count('I') + item.count('O') + item.count('U')
           for item in frutas2]

print(frutas5)

#dicionarios

dic = {f'{item}':item*item for item in range(11)}
print(type(dic))
print(dic)

#função geradora

f = (item for item in range(11))
print(next(f))


# for elemento in f:
#     print(elemento)