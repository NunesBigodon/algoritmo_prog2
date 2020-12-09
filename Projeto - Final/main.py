########### IMPORTS #################
from aluno import Aluno
from professor import Professor
from registrarALuno import Alunonovo
from pessoa import Pessoa
from registrarProfessor import ProfessorNovo
#####################################


menu1 = """
    =-=-=-= Menu Aluno =-=-=-=
 
    1 - Ver notas

    =-=-=-=-= _______ =-=-=-=-
Escolha: """

menu = """
=-=-=-=-= Menu Faculdade -=-=--=-=
=                                =
=  1 - Login Aluno               =
=  2 - Login Professor           =
=  3 - Registrar novo aluno      =
=  4 - Registrar novo professor  =
=                                =
-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-

Escolha: """


Escolha = 0
while True:
    e = input(menu)
    if e == '1':
        p1 = Aluno('Aluno test', '98989')
        p1.Nomes("")
        g = input(menu1)
        if g == '1':
            p1.verNota()
    if e == '2':
        p2 = Professor('Professor test', '23232')
        p2.loginProf('')
        p2.addNota()
    if e == '3':
        p3 = Alunonovo("Novo aluno", '99977')
        p3.cadAlunoN()
    if e == '4':
        p4 = ProfessorNovo("Caysson", '9999')
        p4.cadProf()