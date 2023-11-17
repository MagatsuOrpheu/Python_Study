# listas são representadas por colchetes

# lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]  # Int
# lista2 = ['a', 'b', 'c', 'k', 'j', 'u', ' ']  # Strings
# lista3 = list(range(11))
# lista4 = list('teste')

"""
lesas = list(range(16))
num = 20
if num in lesas:
    print('Estou na lista')
else:
    print('Não estou na lista')
"""

"""
# Organizar a lista
# listaEx = [1, 5, 0, 22, 12, 3, 8, 15, 33]
# listaEx.sort()
# print(listaEx)
"""

"""
# Podemos contar o numero de ocorrencias em uma lista
lista1 = [1, 4, 7, 1, 3, 56, 7, 2, 3, 2]
lista2 = list('Testando')
# print(lista1.count(19))
# print(lista2.count('e'))
"""

"""
# Podemos adicionar um elemento em listas utilizando a função append, mas somente um por vez
# print(lista1)
# lista1.append(10001)
# print(lista1)
"""

"""
# Podemos adicionar uma lista dentro de outra lista, seja ela de qualquer tipo de dado
# lista1.append(list('Interna'))
# print(lista1)
# if ['I', 'n', 't', 'e', 'r', 'n', 'a'] in lista1:
#     print('Estamos na lista')
# else:
#     print('Não estamos na lista')
"""

"""
# Para adicionar mais de um elemento na lista por vez, devemos utilizar a função extend
# lista1.extend([100, 200, 300, 400])
# print(lista1)
"""

"""
# Podemos inserir um novo valor informando a sua posição (OBS: o valor inicial da posição não é substituido, é apenas deslocado para a próxima posição)
# lista1.insert(1, 10002)
# print(lista1)
"""

"""
# Podemos concatenar duas listas em uma só
# listaA = [1, 2, 3, 4]
# listaB = list('ABCD')
# listaC = listaA + listaB
# listaA = listaA + listaB
# listaA.extend(listaB)
# print(listaA)
"""

"""
# Podemos inverter uma lista utilizando a função reverse (ou podemos utilizar Slice)
# listaA = [1, 2, 3, 4, 5]
# listaA.reverse()
# print(listaA[::-1])
"""

"""
# Podemos copiar utilizando a função copy
# listaA = [1, 2]
# listaB = listaA.copy()
# print(listaB)
"""

"""
# Podemos verificar o tamanho da lista utilizando a função length
# listaA = list('abcdefghijklmnopqrstuvwxyz')
# print(len(listaA))
"""

"""
# Podemos remover um item da lista utilizando pop.
# listaa = [1, 2, 3, 4]
# listaa.pop()  # Remove, por padrão, a ultima posição
# listaa.pop(2)  # Podemos definir qual posição queremos remover o elemento
# listaa.clear()  # Podemos remover todos os itens tambem
# listaa = listaa * 3  # Podemos repetir elementos da lista também
# print(listaa)
"""

"""
# Podemos converter uma string para uma lista (É separado pelos espaços)
# jogo = 'The Legend Of Zelda'
# jogo2 = 'The,Legend,Of,Zelda'
# jogo3 = ['The', 'Legend', 'Of', 'Zelda']
# print(jogo2)
# lista_jogo = jogo2.split(',')
# print(lista_jogo)

# Pegamos cada elemento da lista (jogo3) e pedimos para juntar ela separando apenas por espaços
# jogo4 = ' '.join(jogo3)
# print(jogo4)
"""

"""
# Iterando sobre listas
listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = list('teste lista')
soma = 0
for elmto in listaA:
    print(elmto)
    soma = soma + elmto

print(soma)
"""

"""
carrinho = []
produto = ''

while produto != 'sair':
    print("Digite um produto ou escreva 'sair' para finalizar: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

print(carrinho)
"""

"""
# Podemos acessar de maneira inversa também
posicao = [1, 2, 3, 4]
print(posicao[-1])
print(posicao[-2])
print(posicao[-3])
print(posicao[-4])

print(posicao[0])
print(posicao[1])
print(posicao[2])
print(posicao[3])
"""

"""
#cores = ['azul', 'vermelho', 'cinza', 'preto']
#for indice, cor in enumerate(cores):
    # print(indice, cor)
"""

"""
Podemos fazer uma busca dentro dos itens de um range utilizando index.

numeros = list(range(0, 100))
print(numeros.index(56))

Podemos dizer a partir de qual elemento ele deve fazer a busca
print(numeros.index(30, 26))

Tambem podemos dizer em qual intervalo ele deve pesquisar o elemento
print(numeros.index(10, 9, 11))
"""


"""
Podemos checar certas propriedades e atributos da lista
lista1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sum(lista1))  # Checa a soma de todos os elementos da lista
print(max(lista1))  # Checa o maior elemento da lista
print(min(lista1))  # Checa o menor elemento da lista
print(len(lista1))  # Checa o tamanho da lista
"""


"""
Podemos desempacotar a lista
lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
"""

"""
# Deep Copy
lista1 = [1, 2, 3]
print(lista1)

nova = lista1.copy()
nova.append(4)

print(lista1)
print(nova)

"""


# Shallow copy

lista1 = [1, 2, 3]
print(lista1)

nova = lista1
nova.append(4)

print(lista1)
print(nova)
