"""

lista = [1, 2, 3, 4, 5, 6, 7]
print(f"First list: {lista}")
triples = list(map(lambda x: x * 3, lista))
print(f"Triple of said list numbers: {triples}")
"""  # 1) Write a program to triple all numbers in a given list of integers. Use Python map.
""" 

lista_01 = [1, 2, 3]
lista_02 = [4, 5, 6]
lista_03 = [7, 8, 9]


final_list = list(map(lambda x, y, z: x + y + z ,lista_01, lista_02, lista_03))

print(final_list)
"""  # 2) Write a program to add three given lists using Python map and lambda.
"""
dados = ['Red', 'Green', 'Blue']
print(f"Lista original: {dados}")
dados = list(map(list,dados))
print(f"Lista final: {dados}")
"""  # 3) Write a program to listify the list of given strings individually using Python map
"""
lista = [4,5,2,9]
square = list(map(lambda x: x ** 2, lista))
print(square)
"""  # 4) Write a program to square the elements of a list using the map() function
"""
caracteres = ['a', 'b', 'C', 'D', 'E', 'f', 'g', 'h', 'i', 'J']


def case_change(x):
    return str(x).upper(), str(x).lower()


lista_final = list(map(case_change, caracteres))

print(f"Lista inicial: {caracteres}")
print(f"Lista Final: {lista_final}")
"""  # 5) Write a program to convert characters into uppercase and lowercase and eliminate duplicate letter
"""lista01 = [6, 5, 3, 9]
lista02 = [0, 1, 7, 7]


def operations(x, y):
    return x + y, x - y


print(f"Lista_1 = {lista01}\nLista_2 = {lista02}")
lista_final = list(map(operations, lista01, lista02))

print(f"Resultado: {lista_final}")
"""  # 6) Write a program to add two given lists and find the difference between them.

lista01 = [6, 5, 3, 9]
lista02 = [0, 1, 7, 7]


def operations(x, y):
    return x + y, x - y


print(f"Lista_1 = {lista01}\nLista_2 = {lista02}")
lista_final = list(map(operations, lista01, lista02))

print(f"Resultado: {lista_final}")
