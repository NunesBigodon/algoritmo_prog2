########### IMPORTS #############

from list_dict import lstAluno
from list_dict import lstDisciplina
from professor import Professor
from list_dict import *
from pessoa import Pessoa
#################################

class Aluno(Pessoa):
    pass

    def Nomes(self, nome):
        print(">>>>>> Digite seu NOME/MATRÍCULA e poderá ver sua nota <<<<<<<")
        print("")
        print(lstAluno)
        self.nome = input("Digite seu nome: ")
        if self.nome in lstAluno.values() or self.nome in lstAluno.keys():
            print("Aluno encontrado.")
        else:
            print('Aluno não encontrado.')
        
    def verNota(self):
    
        for ind, nota in enumerate(lstDisciplina):
            print(ind,' = ', nota)

        materia = input("Qual desejas ver a nova: ")
        indice = ind
        if materia or indice in lstDisciplina:
            alunoN = input("Digite seu nome: ")
            if alunoN in list_nome:
                for x in range(len(list_nome)):
                    print('Aluno: ',list_nome[x],'>>>','Disciplina:',list_disc[x],'>>>','Nota:',list_notas[x])
            else:
                print("Nenhuma nota foi registrada.")
        else:
            print("Matéria não encontrada.")

        