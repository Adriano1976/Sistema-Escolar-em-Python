class Salario:

    def __init__(self):
        self.salarioBruto = 0.0
        self.salarioLiquido = 0.0
        self.inss = 0.0
        self.irrf = 0.0
        self.planoSaude = 125

    def calcularInss(self, inssD):
        self.inss = self.salarioBruto * inssD

    def calcularIrrf(self, irrfD):
        self.irrf = (self.salarioBruto - self.inss) * irrfD

    def calcularSalarioLiquido(self):
        self.salarioLiquido = self.salarioBruto - (self.inss + self.irrf) - self.planoSaude

        return [self.salarioBruto, self.salarioLiquido, self.inss, self.irrf, self.planoSaude]


CalcularSalario = Salario()
CalcularSalario.calcularSalarioLiquido()
