class Pessoa:

    def __init__(self):
        self.nome = ''
        self.rg = ''
        self.cpf = ''
        self.anoNasc = ''
        self.mesNasc = ''
        self.diaNasc = ''
        self.sexo = ''

    def cadastrar(self):
        self.nome = str(input('Nome: '))
        self.rg = str(input('RG: '))
        self.cpf = str(input('CPF: '))
        print('Data de Nascimento')
        self.anoNasc = int(input('Ano: '))
        self.mesNasc = int(input('Mês: '))
        self.diaNasc = int(input('Dia: '))
        self.sexo = str(input('Sexo: '))

    def exibir(self):
        print('Nome:', self.nome)
        print('RG:', self.rg)
        print('CPF:', self.cpf)
        print('Data de Nascimento')
        print('Ano:', self.anoNasc)
        print('Mês:', self.mesNasc)
        print('Dia:', self.diaNasc)
        print('Sexo[M/F]:', self.sexo)

if __name__ == '__main__':
    PessoaCadastro = Pessoa()
    PessoaCadastro.cadastrar()
    PessoaCadastro.exibir()
