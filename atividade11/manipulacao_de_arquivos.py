

"""
Construir um algoritmo que permite que o usuário
informe uma lista de produtos para serem comprados em
um supermercado ( lista de compras). Os nomes dos
produtos devem ser salvos em um arquivo de texto e a
lista poderá ser modificada sempre que o usuário quiser.
"""

lista_mercado = []
frases = lista_mercado

menu = """
===================================
    SUPER MERCADO SENAC
===================================

    1 - Comprar produtos
    2 - Listar produtos comprados

===================================
Escolha: """


def comprar():
    print("Para finalizar a compra digite [finalizar]")
    while True:
        arquivo = open("arq.txt", "a")
        testando = input("Produtos a serem comprados: ")
        if testando == "finalizar":
            print("Finalizado")
            break
        else:
            lista_mercado.append("\n")
            lista_mercado.append(testando)
            arquivo.writelines(frases)

def listar():
    print("================================")
    print("Lista de produtos comprados")
    print("================================")
    arquivo = open("arq.txt", "r")
    for index, prod in enumerate(arquivo):
        print(index, " = ", prod)


while True:
    escolha = input(menu)
    if escolha == '1':
        comprar()
    if escolha == '2':
        listar()