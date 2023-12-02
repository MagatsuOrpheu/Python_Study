"""
Em algumas linguagens temos estruturas de dados:
- Unidimensionais: arrays/vetores e matrizes
- Multidimensionais: Matrizes

Em Python nós temos listas
"""

# Ex

listas = [[1,2,3],[4,5,6],[7,8,9]]

# for lista in listas:
#     for numero in lista:
#         print(numero)


# [[print(valor) for valor in lista] for lista in listas]


tabuleiro = [[numero for numero in range(1,4)] for coluna in range(1,4)]

print(tabuleiro)

x = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for coluna in range(1,4)]

print(x)

o = [['O' for numero in range(1,4)] for coluna in range(1,4)]

print(o)

