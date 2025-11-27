class FahrenheitError(Exception):
    pass

def fahrenheit_para_celsius(fahrenheit):
    try:
        if fahrenheit < -459.67:
            raise FahrenheitError()
        else:
            c = 5*(fahrenheit - 32)/9
    except FahrenheitError:
        print('O valor inserido é menor que o zero absoluto.')
        pass
    else:
        print(f'O valor convertido para celsius é: {c:.2f}°C')
        return c


fahrenheit = float(input('Entre com a temperatura em fahrenheit: '))
fahrenheit_para_celsius(fahrenheit)
