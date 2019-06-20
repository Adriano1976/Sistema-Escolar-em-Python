from Curso import Curso

class Matricula:
    def __init__(self):
        self.curso = Curso()
        self.id = ''
        self.mesMatricula = ''
        self.anoMatricula = ''

    def matricular(self):
        self.id = int(input('Matrícula: '))
        self.mesMatricula = int(input('Mês: '))
        self.anoMatricula = int(input('Ano: '))

    def exibirMatricula(self):
        print('Matrícula:',self.id)
        print('Mês:',self.mesMatricula)
        print('Ano:',self.anoMatricula)

Matricular = Matricula()
Matricular.cadastrarMatricula()


