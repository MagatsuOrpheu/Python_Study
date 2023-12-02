"""
Com map fazemos mapeamento de valores para função.
Fórmula de MAP = map(FUNÇÃO, ITERAVEL)
Ele mapeia os dados e aplica a função

# Exemplo sem map

def area(r):
    ""
    Calcula a area de um circulo de raio 'r'
    ""
    return math.pi * (r ** 2)


raios = [1, 3, 6, 8, 44, 12, 423, 8, 9]
areas = []

for r in raios:
    areas.append((area(r)))

print(areas)

"""

import math
import random




# Utilizando a função map
def funcao(r):
    return math.pi * (r ** 2)


conjunto_de_numeros = [1, 3, 5, 7, 9, 11]
areas = map(funcao, conjunto_de_numeros)

print(areas)  # Retorna um map object
print(list(areas))  # Converte em lista para visualização

# Usando lambda
print(list(map(lambda r: math.pi * (r ** 2), conjunto_de_numeros)))




"""
# após ser usada uma vez, o objeto é zerado
def quadrado(numero):
    return numero ** 2


lista = [1, 2, 3, 4, 5]
numeros = map(quadrado, lista)

print(list(numeros))  # Primeiro uso
print(list(numeros))  # Tentativa de utilizar novamente = zerado
"""

"""
paises = [('Brasil', 29), ('França', 30), ('EUA', 23), ('Alemanha', 29), ('Japão', 19)]

# f = 9/5 * C + 32

c_para_F = lambda F: (F[0], (9/5) * F[1] + 32)

print(list(map(c_para_F, paises)))
"""