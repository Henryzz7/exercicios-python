class Aluno:
    def __init__(self, nome, data):
        self._nome = nome
        self._data = data
        self._disciplinas = []

    def listar_disciplinas(self):
        print(f'Disciplinas do aluno: {self._nome}')
        for disc in self._disciplinas:
            print(f' - {disc}')

    def adicionar_disciplina(self, disciplina):
        if disciplina not in self._disciplinas:
            self._disciplinas.append(disciplina)
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    def __str__(self):
        return self._nome