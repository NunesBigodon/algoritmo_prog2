from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, nomeJ, enderecoJ, cnpjJ):
        Pessoa.__init__(self, nomeJ, enderecoJ)
        self.cnpj = cnpjJ 

    def imprimir(self):
        Pessoa.imprimir(self)
        print("CNPJ: " + self.cnpj)

    @staticmethod
    def toJuridica(pessoa, cnpj):
        f = Juridica( pessoa.nome, pessoa.endereco, cnpj)
        return f 
