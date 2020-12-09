########### IMPORTS #############
from list_dict import *
from pessoa import Pessoa
#################################

class Professor(Pessoa):
    pass

    def loginProf(self, prof):
        for ip, np in enumerate(profLogin.items()):
            print(ip, ' = ', np)
        prof = input("Número da matrícula: ")

        if prof in profLogin.values():
            print("Você logou no modo Professor(a).")
            print(">>>>>>>><<<<<<<<")
        else:
            print("Matrícula não registrada.")

    def addNota(self):
        print("")
        print("Escolha o aluno...")
        print(">>>>>>>><<<<<<<<")
        for i, m in enumerate(lstAluno):
            print(i, ' = ', m)
        aluno = input("Aluno: ")
        if aluno in lstAluno:
            list_nome.append(aluno)
            for l, n in enumerate(lstDisciplina):
                print(l,' = ',n)

            print("")   
            disciplina = input("Digite a disciplina: ")
            if disciplina in lstDisciplina:
                list_disc.append(disciplina)
                print("")
                print(f"[Digite a nova do aluno {aluno} para a matéria {disciplina}]")
                notas = int(input("Nota: "))
                lstDisciplina[disciplina] = str(notas)
                if aluno in lstAluno:
                    print("Nota adicionadada")
                    list_notas.append(notas)
                    for x in range(len(list_nome)):
                        print('Aluno: ',list_nome[x],'/','Disciplina:',list_disc[x],'/','Nota:',list_notas[x])
                else:
                    print("Erro ao adicionar a nota.")
            else:
                print("Disciplina não registrada.")
        else:
            print("Esse aluno não está inscrito.")
            
