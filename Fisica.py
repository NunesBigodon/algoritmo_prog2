from Pessoa import Pessoa

class Fisica(Pessoa):

    MAIORIDADE = 18

    def __init__(self, nomeF, enderecoF, cpfF):
        # self.nome = nomeF
        # self.endereco = enderecoF
        Pessoa.__init__(self, nomeF, enderecoF)
        self.cpf = cpfF

    def imprimir(self):
        Pessoa.imprimir(self)
        print("CPF: " + self.cpf)

    @staticmethod
    def toFisica(pessoa, cpf):
        f = Fisica( pessoa.nome, pessoa.endereco, cpf)
        return f
