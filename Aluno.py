from Pessoa import Pessoa
from Matricula import Matricula

class Aluno(Pessoa):
    def __init__(self):
        self.matricula = Matricula()
        self.cod = ''
        self.interesse = ''
        self.desconto = ''

    def cadastrarAluno(self):
        super().cadastrar()
        self.cod = int(input('Código: '))
        self.interesse = str(input('Interesse: '))
        self.desconto = float(input('Desconto: '))

    def exibirAluno(self):
        super().exibir()
        print('Código:', self.cod)
        print('Interesse:', self.interesse)
        print('Desconto:', self.desconto)


CadastroAluno = Aluno()
CadastroAluno.cadastrarAluno()
CadastroAluno.exibirAluno()
