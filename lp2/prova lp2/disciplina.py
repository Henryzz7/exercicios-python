class Disciplina:

    def __init__(self, cod, nome, ch):
        self._cod = cod
        self._nome = nome
        self._ch = ch
        self._alunos = []

    def listar_alunos(self):
        print(f'Alunos da disciplina: {self._nome}')
        for alu in self._alunos:
            print(f' - {alu}')
    def adicionar_aluno(self, aluno):
        if aluno not in self._alunos:
            self._alunos.append(aluno)
    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, value):
        self._cod = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def ch(self):
        return self._ch

    @ch.setter
    def ch(self, value):
        self._ch = value

    def __str__(self):
        return self._nome