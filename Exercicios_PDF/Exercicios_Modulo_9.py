# 1) Write a Python program to triple all numbers in a given list of integers. Use Python map.

lista = [1, 2, 3, 4, 5, 6, 7]
print(f"First list: {lista}")
triples = list(map(lambda x: x * 3, lista))
print(f"Triple of said list numbers: {triples}")

# 2) Write a Python program to add three given lists using Python map and lambda.

lista_01 = [1, 2, 3]
lista_02 = [4, 5, 6]
lista_03 = [7, 8, 9]


final_list = list(map(lambda x, y, z: x + y + z ,lista_01, lista_02, lista_03))

print(final_list)