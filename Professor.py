from Funcionario import Funcionario
import pickle

class Professor(Funcionario):
    def __init__(self):
        self.formacao = ''
        self.nivel = ''
        self.disciplina = ''
        super().__init__()

    def cadastrarProfessor(self):
        super().cadastrarFuncionario()
        self.formacao = str(input('Formação: '))
        self.nivel = str(input('Nível: '))
        self.disciplina = str(input('Disciplina: '))
        pickle.dump(super().cadastrarFuncionario, open('professor.pickle', 'ab'))
        pickle.dump(self.formacao, open('professor.pickle', 'ab'))
        pickle.dump(self.nivel, open('professor.pickle', 'ab'))
        pickle.dump(self.disciplina, open('professor.pickle', 'ab'))

    def exibirProfessor(self):
        super().exibirFuncionario()
        print('Formação:',self.formacao)
        print('Nível:',self.nivel)
        print('Disciplina:',self.disciplina)

professorCadastro = Professor()
professorCadastro.cadastrarProfessor()
