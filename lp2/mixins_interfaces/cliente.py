from autenticavel import AutenticavelInterface
class Cliente(AutenticavelInterface):
    def autenticar(self, senha):
        if senha == '123456':
            return True
        else:
            return False