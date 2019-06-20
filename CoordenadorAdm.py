from Funcionario import Funcionario
from Salario import Salario


class coordenadorAdm(Funcionario, Salario):
    def __init__(self):
        self.area = ''
        self.plusSalario = ''

    def cadastrarCoordenadorAdm(self):
        self.cadastrarFuncionario()
        self.area = str(input('Área: '))
        self.plusSalario = float(input('Salário: '))

    def exibirCoordenadorAdm(self):
        self.exibirFuncionario()
        print('Área:', self.area)
        print('Salário:', self.plusSalario)

    def calcularPlusSalario(self):
        self.calcularSalario()
