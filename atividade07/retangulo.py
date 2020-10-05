class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular(self, altura, largura, resultado):
        self.altura = 4.0
        self.largura = 1.70
        self.resultado = (self.altura * self.largura)

    def imprimir(self, resultado):
        print(f' Altura = {self.altura} \nLargura = {self.largura}')
        print(f'Algura * Largura = {self.resultado}')
        

p1 = Retangulo("", "")
p1.calcular("", "", "")
p1.imprimir("")
