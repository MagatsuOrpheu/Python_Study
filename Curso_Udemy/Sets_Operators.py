a = {1,5,6,3,9,10,24}
b = {2,5,8,0,1,23,11}
c = {1,2,3,4}
d = {1,2,3,4,5,6,7,8,9,10}

""""
# Retorna a juncao de A e B. Mantem os originais.
print(a.union(b))
print(b.union(a))
print(a)
print(b)
"""  # Union

"""
# Realiza a junção de A com B, e altera A. Nao tem retorno(None).
a.update(b)
print(a)
print(b)
"""  # Update

"""
# Retorna a intersecao de A e B, sem alterar os originais
print(a.intersection(b))
print(a)
print(b)
"""  # Intersection

"""
# Realiza a interscao de A e B, e altera A. Nao tem retorno(None).
a.intersection_update(b)
print(a)
print(b)
"""  # Intersection_update

"""
# Retorna a diferença de A e B. Mantem os originais.
print(a.difference(b))
print(a)
print(b)
"""  # Difference

"""
# Na pratica, realiza a remocao em A os elementos que estiverem em B
a.difference_update(b)
print(a)
print(b)
"""  # Difference_update

"""
# Retorna a diferenca simetrica de A e B (Elementos em A e B que nao estao em ambos).
print(a.symmetric_difference(b))
"""  # Symmetric_difference

"""
# Armazena a diferenca simetrica de A e B em A.
a.symmetric_difference_update(b)
print(a)
"""  # Symmetric_difference_update

"""
# Retorna (em bool) se C é subconjunto de D. Mantem os originais.
print(c.issubset(d))
"""  # Issubset

"""
# Retorna (em bool) se D é superconjunto de C. Mantem os originais 
print(d.issuperset(c))
"""  # Issuperset



