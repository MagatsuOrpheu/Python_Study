"""
List Comprehension pt.2

Podemos adicionar estruturas lógicas condicionais
"""

# SEM ESTRUTURA CONDICIONAL
numeros = [1, 2, 3, 4, 5]

#pares = [numero for numero in numeros if numero % 2 == 0]
#impares = [numero for numero in numeros if numero % 2 != 0]
#print(pares)
#print(impares)

# COM ESTRUTURA
# Qualquer numero par modulo de 2 é 0, e 0 em Python é False
pares = [numero for numero in numeros if not numero % 2]
# Qualquer numero impar modulo de 2 é 0, e 0 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)


# 02

res = [numero * 2 if numero % 2 == 0 else numero /2 for numero in numeros]
print(res)
