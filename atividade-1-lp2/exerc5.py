
class NotLetterError(Exception):
    pass

class NotUpperError(Exception):
    pass


def verificando_string(valor):
        try:
            string = valor.replace(' ', '')
            if string.isalpha() == True:
                if string.isupper() == True:
                    pass
                else:
                    raise NotUpperError()
            else:
                raise NotLetterError()
        except NotLetterError:
            print(f'"{valor}" possui dígitos ou símbolos.')
        except NotUpperError:
            print(f'"{valor}" possui letras minúsculas.')
        else:
            return print(f'"{valor}" é composta apenas por letras maiúsculas.')


verificando_string('TUDO CERTO1a')