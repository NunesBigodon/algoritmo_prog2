#LISTAS
lst_carro = ['Hyundai HB20','Hyundai HB20S','Hyundai Tucson']
lst_qnt = ['1', '3', '4']
lst_preço = ['47.999', '55.390', '139.900']


#FUNCOES
print(lst_carro)
def imprimir():
    print('Mostrando o elemento do indice 1')
    print(lst_carro[1])

def retirar():
    del lst_carro[1]
    print(lst_carro)

#CHAMANDO A FUNCAO
imprimir()
retirar()

