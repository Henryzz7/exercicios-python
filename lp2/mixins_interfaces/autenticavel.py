import abc

class AutenticavelInterface(abc.ABC):
    '''
    Esta interface define a regra para autenticação do sistema
    '''
    @abc.abstractmethod
    def autenticar(self, senha):
        '''
        Este método deve verificar a senha dos usuários
        '''
        pass