"""
    Commons about sets.
    Sets don't have duplicated itens.
lista_dupla = [1,2,3,4,1,2,3,3,2,1]
lista_set = set(lista_dupla)
print(lista_set)

fruta = set('abacaxi')
print(fruta)

# Acessando sets
# É necessario converte-los para uma lista
lista = list(lista_set)
print(lista[0])

# podemor iterar utilizando o for
for letra in fruta:
    print(letra)

for indice, numero in enumerate(lista_set):
    print(f"{indice} : {numero}")

"""


    # Sets methods:

# union

conj_a = {1,2,3}
conj_b = {4,5,6}

print(conj_a.union(conj_b)) # {1,2,3,4,5,6}

# intersection
conj_a = {1,2,3}
conj_b = {2,3,4}

print(conj_a.intersection(conj_b)) # {2,3}

# difference
conj_a = {1,2,3}
conj_b = {2,3,4}

print(conj_a.difference(conj_b)) # {1}
print(conj_b.difference(conj_a)) # {4}

# symmetric_difference
conj_a = {1,2,3}
conj_b = {2,3,4}

print(conj_a.symmetric_difference(conj_b)) # {1,4}

# issubset
conj_a = {1,2}
conj_b = {1,2,3,4,5}

print(conj_a.issubset(conj_b)) # True
print(conj_b.issubset(conj_a)) # False

# issuperset
conj_a = {1,2}
conj_b = {1,2,3,4,5}

print(conj_a.issuperset(conj_b)) # False
print(conj_b.issuperset(conj_a)) # True


# isdisjoint
conj_a = {1,2,3,4}
conj_b = {5,6,7,8}
conj_c = {1,5}

print(conj_a.isdisjoint(conj_b))  # True
print(conj_a.isdisjoint(conj_c))  # False
print(conj_b.isdisjoint(conj_c))  # False

# add
conj_a = {1,2,3,4}
conj_a.add(5)
conj_a.add(1)
print(conj_a)

# clear
conj_a.clear()
print(conj_a)

# copy
conj_a = {1,2}
x = conj_a.copy()
print(x)

# discard
conj_a.discard(1)
conj_a.discard(10000000)  # Don't return error
print(conj_a)

# pop
print(conj_b)
conj_b.pop()
print(conj_b)

# remove
print(conj_b)
conj_b.remove(5)
conj_b.remove(100000)  # return keyError

