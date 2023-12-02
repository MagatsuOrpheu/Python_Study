"""
Tuplas são parecidas com listas.

diferenças basicas:
1 - são representadas com parentes;
2 - As tuplas são imutaveis, ao se criar uma tupla, a mesma não muda. toda operação em uma tupla gera outra nova tupla
"""

"""
a = (1, 2, 3, 4, 5, 6)  # ISSO É UMA TUPLA
print(type(a))
b = 2, 4, 6, 8, 10  # ISSO É UMA TUPLA
print(type(b))
d = 4,  # ISSO É UMA TUPLA
print(type(d))
c = 4  # ISSO NÃO É UMA TUPLA
print(type(c))
"""

"""
tupla = tuple(range(0, 10))
print(tupla)
print(type(tupla))
"""

"""
tupla = 'Nome do Escola', 'Nome do aluno'
escola, aluno = tupla

print(escola)
print(aluno)
"""

"""
tupla1 = 1, 2, 3, 4
tupla2 = 5, 6, 7, 8
print(tupla1 + tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2
print(tupla1)
"""

"""
tupla = (1, 2, 3)
print(3 in tupla)
print(33 in tupla)
"""
"""
tupla = 1, 2, 3, 4, 5, 6
# for n in tupla:
#     print(n)

for indice, numero in enumerate(tupla):
    print(indice, numero)
"""

nome = tuple('Magatsu Orpheus')
print(nome)
print(nome.count('a'))
