from aluno import Aluno
class Matricula:

    def __init__(self, id, ano, semestre):
        self._id = id
        self._ano = ano
        self._semestre = semestre
        self._status = False
        self._aluno = None
        self._disciplina = None

    def aprovar_matricula(self, aluno, disciplina):
        self._aluno = aluno
        self._disciplina = disciplina

        self._aluno.adicionar_disciplina(self._disciplina)
        self._disciplina.adicionar_aluno(self._aluno)
        self._status = True
