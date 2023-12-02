"""
    The first section of the following archive is used for introduction to lists

# Exemplos
carro = ['Toyota', "Supra", 400000.00, 4000, True]
lista_vazia = []
lista = list()
range_10 = list(range(10))

print(range_10)
print("==========================================")

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Acesso direto
print(matriz[0])  # Primeira lista de matriz
print(matriz[1][2])  # Ultimo elemento da segunda lista dentro de matriz
print("==========================================")

# Slice
nome = list('Jonathan')
print(nome[:4])
print(nome[4:8])
print(nome[-1:])
print(nome[:-4])
print("==========================================")

# iterar sobre listas
for letra in nome:
    print(letra)
print("==========================================")

# Enumerate
for indice, letra in enumerate(nome):
    print(f"{indice} : {letra}")
print("==========================================")

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

print(numeros)
print(pares)

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
        numeros.remove(numero)

print(numeros)
print(pares)
print("==========================================")

# Compreensao de lista 
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

    This is the ending of the first section.

"""

"""
    The second section is used for the methods of the list
"""

# Append method

lista01 = []
lista01.append(1)
lista01.append("Python")
lista01.append([1,2,3,4])
print(lista01)
print("==========================================")

# Clear method
print(lista01)
lista01.clear()
print(lista01)
print("==========================================")

# Copy method - Deep Copy (Duas listas diferentes)
lista01 = [1, 'Python', [1, 2, 3, 4]]
lista02 = lista01.copy()
print(lista01)
print(lista02)
print(id(lista01), id(lista02))

print("==========================================")

# Count Method
lista01 = [1,1,1,3,3,1,2,3]
print(lista01.count(1))
print(lista01.count(2))
print(lista01.count(3))
print("==========================================")

# Extend method
lista01 = [1,2,3]
print(lista01)
lista02 = [6,7,8]
lista01.extend([4,5])
lista01.extend(lista02)
print(lista01)
print(lista02)
print("==========================================")

# index method
lista01 = ['a','b','c','d','e','f','g','h','i','j']
print(lista01.index('c'))
print("==========================================")

# pop method
lista01 = ['a','b','c','d','e','f','g','h','i','j']
lista01.pop()
print(lista01)
lista01.pop(2)
print(lista01)
print("==========================================")

# remove method
lista01 = ['a','b','c','d','e','f','g','h','i','j']
lista01.remove('j')
print(lista01)
print("==========================================")

# reverse method
lista01 = ['a','b','c','d','e','f','g','h','i','j']
lista01.reverse()
print(lista01)
print("==========================================")

# sort method
lista01 = ['python', 'java', 'c', 'c#', 'js']
lista01.sort()
print(lista01)
lista01.sort(reverse=True)
print(lista01)
lista01.sort(key=lambda x: len(x))
print(lista01)
lista01.sort(key=lambda x: len(x), reverse=True)
print(lista01)
print("==========================================")

# sorted method
sorted(lista01, key=lambda x: len(x))
sorted(lista01, key=lambda x: len(x), reverse=True)

n = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(n)