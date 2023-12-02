"""
Utilizando List Comprehension...

- Podemos gerar novas listas com dados processados a partir de outro iteravel

# Sintaxe da List Comprehension
[dado for dado in iteravel]

- for numero in numeros - part 1
- numero * 10 - part 2
"""
# Exemplos
numeros = [1, 2, 3, 4]
res = [numero * 10 for numero in numeros]
print(res)

res = [numero / 2 for numero in numeros]
print(res)


def function(valor):
    return valor * valor


res = [function(numero) for numero in numeros]
print(res)

# Sem list comprehension #
double = []
for numero in numeros:
    double.append(numero * 2)

print(double)

# Com List Comprehension
double_2 = [numero * 2 for numero in numeros]
print(double_2)

# Mais exemplos

# 01
nome = 'João da Silva'
print([letra.upper() for letra in nome])


# 02
# def caixa_alta(nome):
#     nome = nome.replace(nome[0], nome[0].upper())
#     return nome

pessoas = ['jonathan', 'marcelo']
#
print([pessoa.title() for pessoa in pessoas])

# 03

print([numero * 3 for numero in range(1,11)])

# 04
print([bool(valor) for valor in [0,'',(),1,True, '1.34']])

# 05
print([str(numero) for numero in [1, 2, 3, 4, 5]])
