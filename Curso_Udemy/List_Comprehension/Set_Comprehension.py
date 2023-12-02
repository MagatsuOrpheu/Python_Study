"""
Set Comprehension

lista = [1,2,3,4]
set = {1,2,3,4}
"""

# Ex 1
numeros = {num for num in range(0,7)}

print(numeros)
print(type(numeros))

# Ex 2
num = {x ** 2 for x in range(10)}

print(num)

# transformando em dict

num2 = {x:x ** 2 for x in range(10)}

print(num2)
print(type(num2))

# Ex 3
letras = {letra for letra in 'Jonathan'}

print(letras)
print(type(letras))
