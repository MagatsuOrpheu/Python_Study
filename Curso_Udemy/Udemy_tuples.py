# Tuplas são representadas por ().
# Tuplas são imutaveis
# também podem ser declaradas sem (), veja:
"""
tupla1 = 1, 2, 3, 4, 5, 6
print(tupla1)
print(type(tupla1))

tupla2 = (1, 2, 3, 4)
print(tupla2)
print(type(tupla2))

# ISSO NÃO É UMA TUPLA
tupla3 = (4)
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

# Tuplas são definidas pelo uso da virgula, não do parenteses

tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tuplas
tupla = ('João', '18')
nome, idade = tupla
#nome, idade, estado = tupla # Gera um erro pois há uma chave a mais
print(nome)
print(idade)

#tupla2 = ('A', 'B', 'C')
#a, b = tupla2 # Gera um erro pois está faltando uma chave
"""
