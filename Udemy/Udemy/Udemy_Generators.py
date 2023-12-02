# Retorna a quantidade de bytes em memoria ocupada pelo elemento passado
from sys import getsizeof

"""
Tuples comprehension --> Generators Expression


nomes = ['Carlos', 'Cristina', 'Carla', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)

# Generator (Uses less resources and memory)
res2 = (nome[0] == 'C' for nome in nomes)
print(type(res2))

print(getsizeof('Geek'))
print(getsizeof('Jonathan'))
print(getsizeof(92))
print(getsizeof(9213127312))
print(getsizeof(True))
"""

# Uso de memoria para a mesma funcao

list_comp = getsizeof([x * 10 for x in range(1000)])
print(list_comp)

generator = getsizeof((x * 10 for x in range(1000)))
print(generator)

dictionary = getsizeof({x: x * 10 for x in range(1000)})
print(dictionary)

"""
gen = ((x * 2 for x in range(1,10)))
print(type(gen))

for num in gen:
    print(num)
"""