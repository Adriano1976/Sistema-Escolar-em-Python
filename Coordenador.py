from Professor import Professor

class Coordenador(Professor):
    def __init__(self):
        self.area = ''
        self.plusSalario = 0.0
        super().__init__()

    def cadastrarCoordenador(self):
        super().cadastrarProfessor()
        self.area = str(input('Área: '))
        self.plusSalario = float(input('Salário do Coordenador: '))

    def exibirCoordenador(self):
        super().exibirProfessor()
        print('Área de Atuação:',self.area)
        print('Salário do Coordenador:',self.plusSalario)

CadastroCoordenador = Coordenador
CadastroCoordenador.cadastrarCoordenador()