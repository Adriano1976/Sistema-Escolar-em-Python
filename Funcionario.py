from Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = ''
        self.setor = ''
        self.cargo = ''
        self.nivel = ''

    def cadastrarFuncionario(self):
        self.matricula = int(input('Matrícula: '))
        self.cadastrar()
        self.setor = str(input('Setor: '))
        self.cargo = str(input('Cargo: '))
        self.nivel = int(input('Nível: '))

    def exibirFuncionario(self):
        print()
        print('Matrícula:', self.matricula)
        self.exibir()
        print('Setor:', self.setor)
        print('Cargo:', self.cargo)
        print('Nível:', self.nivel)

jose = Funcionario()
jose.cadastrarFuncionario()
jose.exibirFuncionario()

