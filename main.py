from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

p = Pessoa("Julia", "Av. Ipiranga")
f = Fisica("Maria", "Av. Protasio Alves", "111.222.333-44")
j = Juridica("Mercado do João", "Av. A, 132", "11.222.333/0001-44")

p.imprimir()
p = Fisica( p.nome, p.endereco, "0")

p2 = Pessoa.toPessoa( f )

p2.imprimir()

f.imprimir()
j.imprimir()

j = Pessoa.toPessoa( j )

j.imprimir()

print( "Maioridade: " + str(  Fisica.MAIORIDADE ) )

j2 = Juridica.toJuridica( p , "11.222.000/0001-33" )
j2.imprimir() 
