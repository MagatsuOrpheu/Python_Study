"""
Podemos utilizar o *args como um parâmetro qualquer, podendo ser chamado de qualquer nome.
"""


def soma(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]
numeros2 = (1, 2, 3, 4, 5, 6, 7)

print(soma(1, 2, 3, 4, 5, 6, 7))  # Funciona

# para conseguir fazer os dois prints abaixo deve ser utilizado o desempacotador do Python, usando o asterisco
# print(soma(numeros2)) # erro
# print(soma(numeros)) # erro

print(soma(*numeros))  # Funciona
print(soma(*numeros2))  # Funciona

"""
def dicionario(*args):
    if 'Jonathan' and 'Gabriel' in args:
        return "Bem vindo Jonathan Gabriel"
    else:
        return "Usuario desconhecido"


print(dicionario('Jonathan', 'Melo'))
print(dicionario('Jonathan', 'Gabriel'))
print(dicionario('Pedro', 'Freitas'))
"""
