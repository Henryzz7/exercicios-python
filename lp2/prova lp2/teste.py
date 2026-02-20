from aluno import Aluno
from disciplina import Disciplina
from matricula import Matricula
from aluno_bolsista import BolsistaPos, BolsistaGraduacao
from folha import Folha
a1 = Aluno('Fulano', '01/01/2000')
a2 = Aluno('Ciclano', '02/02/2001')

d1 = Disciplina('CCET114', 'LP1', 60)
d2 = Disciplina('CCET115', 'LP2', 60)

m1 = Matricula(1, 2025, 1)
m2 = Matricula(2, 2025, 1)
m3 = Matricula(3, 2025, 2)

m1.aprovar_matricula(a1,d1)
m2.aprovar_matricula(a1,d2)
m3.aprovar_matricula(a2,d2)

a1.listar_disciplinas()

d2.listar_alunos()

b1 = BolsistaGraduacao('Bolsista Gra', '01/01/2020')
b2 = BolsistaPos('Bolsista Pos', '02/02/2023')

folha = Folha()
folha.adicionar_bolsista(b1)
folha.adicionar_bolsista(b2)

# Pagando antes do reajuste
folha.pagar_bolsas()

print(b1._total)
print(b2._total)

# Pagando depois do reajuste
folha.reajustar_bolsas()
folha.pagar_bolsas()

print(b1._total)
print(b2._total)

# Simulação de exceção

folha.adicionar_bolsista(a1) # Aluno não bolsista
folha.pagar_bolsas()
folha.reajustar_bolsas()