from Professor import Professor
from Matricula import Matricula

class Curso:
    def __init__(self):
        self.Matricula = Matricula()
        self.Professor = Professor()
        self.titulo = ''
        self.descricao = ''
        self.valor = ''
        self.sala = ''

    def cadastrarCurso(self):
        print('CURSO OFERECIDO')
        self.Matricula.matricular()
        self.titulo = str(input('Título: '))
        self.descricao = str(input('Descrição: '))
        self.valor = float(input('Valor: '))
        self.sala = str(input('Sala: '))

    def exibirCurso(self):
        print('CURSO OFERECIDO')
        self.Matricula.exibirMatricula()
        print('Título:',self.titulo)
        print('Descrição:',self.descricao)
        print('Valor:',self.valor)
        print('Sala:',self.sala)

CadastroCurso = Curso
CadastroCurso.cadastrarCurso()
