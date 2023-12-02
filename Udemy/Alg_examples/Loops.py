# Loop For #

# For item in iteravel:
#   Execução do loop

"""
# Iterando sobre uma String:
nome = 'Jonathan'
for letra in nome:
    print(letra)
"""


"""
# Iterando sobre uma lista:
lista = (1, 2, 4, 5, 6, 7, 8, 10)
for numero in lista:
    print(numero)
"""


"""
# Iterando sobre um range:
numeros = range(1, 10)
# O ultimo numero da Range não é incluso
for numero in numeros:
    print(numero)
"""

"""
nome = 'abcdefghij'

(MÉTODO REDUNDANTE)
for indice, letra in enumerate(nome):
    print(nome[indice])

(MÉTODO MAIS PRÁTICO)
for indice, letra in enumerate(nome):
    print(letra)

(PODEMOS DESCARTAR UM VALOR DESNECESSARIO UTILIZANDO UNDERLINE)
for _, letra in enumerate(nome):
    print(letra)

nome = 'abcdef'
for x in enumerate(nome):
    print(x[1])
"""

"""
qtd = int(input('Quantas vezes tal loop deve ocorrer ?'))
soma = 0

for n in range(1, qtd+1):
    soma = soma + \
        int(input('informe o valor que deve ser adicionado ao total: '))
print(soma)

nome = 'Teste quebra de linha'
for letra in nome:
    print(letra, end="")
"""

"""
num = 5
while num < 10:
    print(num)
    num += 1

# EM UM LOOP WHILE, É IMPORTANTE TER UM CRITÉRIO DE PARADA
"""

resposta = ''

while resposta != 'nao':
    print('Quer repetir? ')
    resposta = input('')
