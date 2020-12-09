########### IMPORTS #############
from list_dict import *
from professor import Professor
from pessoa import Pessoa
#################################



class ProfessorNovo(Pessoa):
    pass

    def cadProf(self):
        maxl = 4

        self.nome = input("Seu nome: ")
        self.matricula = str(input("Matricula: "))
        if len(self.matricula) == maxl:
            profLogin[self.nome] = str(self.matricula)
        else:
            print("Erro. Número inválido")
