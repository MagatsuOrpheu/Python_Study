"""
Dictionary comprehension

sintaxe : {chave:valor for valor in iteravel} <- Dictionary comprehension

lista = [1, 2, 3, 4]
tupla = 1, 2, 3, 4
conjunto = {1, 2, 3, 4}
dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print(lista)
print(tupla)
print(conjunto)
print(dictionary)

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # dict
numeros_2 = [1, 2, 3, 4]
numeros_3 = 1, 2, 3, 4

num_quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
num_soma = {valor: valor + 1 for valor in numeros_2}
num_sub = {valor:valor - 1 for valor in numeros_3}

print(num_quadrado)
print(num_soma)
print(num_sub)
"""

chaves = 'abcd'
valores = 1, 2, 3, 4

mistura = {chaves[i]:valores[i] for i in range(0,len(valores))}

print(mistura)

numeros = 1,2,3,4,5

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
