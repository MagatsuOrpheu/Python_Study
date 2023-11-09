"""
Listas são como vetores/matrizes (Arrays) de outras linguagens.
Com um diferencial de serem DINAMICAS e poder armazenar QUALQUER tipo de dado.
"""
"""
Java/C:
    - Possuem tamanho e tipo de dado fixo (sempre será do mesmo tipo e tamanho)

Python: 
    - Dinamico, ou seja, não possuí tamanho fixo, se limita ao uso máximo do tamanho da memória.
    - Qualquer tipo de dado pode ser adicionado a lista
    - São representadas por []
"""
a1 = [1, "a", True]
a2 = [1, 2, 3, 4, 5, 6]
a3 = list(range(11))
a4 = list('Jonathan')
a5 = [1, 55, 7, 223, 34, 78, 91, 13, 17, 1, 26, 77, 1, 98, 123, 9]
"""
carrinho = []
produto = ''
while produto != 'sair':
    print("Escreva um produto para adicionar ao carrinho, ou digite 'sair' para finalizar: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
print("Produtos dentro do carrinho: ")
for produto in carrinho:
    print(produto)

"""  # Carrinho de compras - teste
"""
print(a1, a2, a3, a4)
print(a1)
print(a2)
print(a3)
print(a4)

lista_pai = []
lista_pai.extend([a1, a2, a3, a4, a5])
for lista in lista_pai:
    print(lista)
"""  # imprimir todas as listas com um FOR
"""
Verificar se o valor está na lista:
def verificacao():
    num = 6
    if num in a3:
        print(f"Encontrei o numero {num}!")
    else:
        print(f"Não encontrei o numero {num}!")

    if 'a' in a4:
        print("True")
    else:
        print("False")


# verificacao()
"""  # Verificar se o valor está na lista
"""
Ordenar a lista:
def ordenacao():
    a5.sort()
    print(a5)

    a4.sort()
    print(a4)


# ordenacao()
"""  # Ordenar a lista
"""
Podemos consultar o numero de ocorrencias em uma lista
def consultar():
    print(a5.count(1))
    print(a4.count('a'))


# consultar()
"""  # Consultar o numero de ocorrencias
"""
Adicionar elementos em listas (append só recebe um elemento)
def adicionar():
    print(a5)
    a5.append(888)
    a5.append([1, 2, 3, 4])
    print(a5)
    a5.extend([5, 6, 7, 8, 9])
    print(a5)
    a5.insert(1, 'Novo valor')
    print(a5)


# adicionar()
"""  # Adicionar elementos em listas
"""
Juntar listas
def juntar():
    a6 = a5 + a4
    print(a6)


juntar()
"""  # Juntar listas
"""
Inverter a lista
def inverter():
    a4.reverse()
    print(a4)


inverter()
"""  # Inverter a lista
"""
Copiar a lista
def copiar():
    a6 = a4.copy()
    print(a6)
    
    
copiar()
"""  # Copiar a lista
"""
contar o tamanho da lista
def contar():
    print(len(a5))


contar()
"""  # Contar o tamanho da lista
"""
# remover e retornar o ultimo numero
def remover():
    print(a5)
    a5.pop(2)  # <- remove o item na posição informada e desloca os outros elementos
    a5.pop()  # <- remove o ultimo elemento
    print(a5)
    a5.clear()  # <- limpa completamente a lista
    print(a5)


remover()

"""  # Remove e retorna o ultimo elemento
"""
Repetir / multiplicar uma lista
def repetir():
    print(a2)
    b2 = a2 * 3
    print(b2)


repetir()
"""  # Repetir / multiplicar uma lista
"""
def dividir():
    lista = "Aqui vai um exemplo"
    print(lista)
    lista = lista.split()
    print(lista)

    lista2 = "Temos, aqui, um, outro, exemplo"
    print(lista2)
    lista2 = lista2.split(",")  # <- informo que o separador é a virgula
    print(lista2)

    lista3 = "".join(lista2)
    print(lista3)


dividir()
"""  # Dividir ou juntar elementos da lista
"""
Indices e valores
nomes = ['João', 'Ana', 'Maria', 'Julia', 'Gabriel']

# for nome in nomes:
#     print(nome)

# indice = 0
# while indice < len(nomes):
#     print(nomes[indice])
#     indice = indice + 1

for indice, nome in enumerate(nomes):
    print(indice, nome)
"""  # Enumerate, Indice e valores
"""
lista = list(range(2214))
print(lista.index(2))  # <- Retorna a posição (indice) do numero 2
# print(lista.index(2, 4))  # <- Procura a partir do indice 4, o numero 2 = ERRO
print(lista.index(6, 4, 8))  # <- procura o numero 6 entre o indice 6 e 8
"""  # Procurar elementos via indice

lista = [1, 2, 3, 4, 5, 6]
print(lista)

"""
nova = lista.copy()
print(nova)
nova.append(4)

print(lista)
print(nova)
"""  # Deep Copy = Ao utilizar o copy, criamos outra lista totalmente independente da outra

"""
nova = lista

print(nova)
nova.append(7)

print(nova)
print(lista)
"""  # Shallow Copy = Cria-se uma outra lista igual a outra, mas elas são interligadas. o que acontece em uma
# acontece na outra
