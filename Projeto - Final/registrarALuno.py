########### IMPORTS #############
from list_dict import profLogin
from list_dict import lstAluno
from professor import Professor
from pessoa import Pessoa
#################################

class Alunonovo(Pessoa):
    pass

    def cadAlunoN(self):
        
        input("Bem vindo professor.....")
        self.matricula = input("Número da matrícula: ")
        if self.matricula in profLogin.values():
            print("Logado com sucesso.")
        else:
            print("Matrícula não registrada.")

        maxl = 4
        self.nome = input("Nome do novo aluno: ")
        matriculaN = str(input("Matricula: "))
        if len(matriculaN) == maxl: 
            lstAluno[self.nome] = str(matriculaN)
        else:
            print("Erro. Número inválido.")
