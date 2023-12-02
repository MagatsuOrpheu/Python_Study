"""
Sets ou conjuntos são os conjuntos que vemos em Matematica
São representados com {}, mas possuem diferenças dos mapas / dicionarios
    * Dicionarios possuem chave e valor
    * Sets possuem apenas valor

Sets tem algumas caracteristicas importantes:
    - Não possuem valores duplicados
    - Não possuem valores ordenados
    - Não são indexados

São recomendados para trabalhar com conjuntos que não possuem uma ordem, e quando não precisamos nos preocupar com
chaves, valores ou itens duplicados.

"""
"""
Os numeros repetidos são ignorados
conjunto_1 = {1,2,3,4,5,6,7,8,10,1,2,4,6,3,2,4,6,6,2,3,4,5,1,2}
print(conjunto_1)
print(type(conjunto_1))
"""

"""
lista = [10, 21, 3, 4, 66, 12, 4, 6, 8, 92, 10, 2]
print(f"lista = {lista}")

tupla = (10, 21, 3, 4, 66, 12, 4, 6, 8, 92, 10, 2)
print(f"Tupla = {tupla}")

dicionario = {}.fromkeys([10, 21, 3, 4, 66, 12, 4, 6, 8, 92, 10, 2], 'None')
print(f"Dicionario = {dicionario}")

conjunto = {10, 21, 3, 4, 66, 12, 4, 6, 8, 92, 10, 2}
print(f"Conjunto = {conjunto}")
"""

"""
Adicionar ou remover nos conjuntos
conjunto = set({3,6,8,192,3,2,1,218,312,2,3,5,111})
print(conjunto)
conjunto.add(100)
print(conjunto)
conjunto.remove(3) # Se o valor não for encontrado gera erro
print(conjunto)
conjunto.discard(111) # Se o valor não for encontrado não gera erro
print(conjunto)
"""

"""
Deep copy
s = {1,2,3}
t = s.copy()
t.add(4)
print(s)
print(t)
"""

"""
Shallow copy
s = {1,2,3}
t = s
t.add(4)
print(s)
print(t)
"""

"""
Unificar sets
Python = {'Julia', 'Leticia', 'Maria', 'Marcos', 'Lucas', 'João'}
Java = {'Lucas', 'Victoria', 'Fernanda', 'Mariane', 'Julia'}
Escola = Python.union(Java)
Escola2 = Python | Java
print(Escola)
print(Escola2)
"""

"""
Intersecção, ou seja, em ambos os cursos
Python = {'Julia', 'Leticia', 'Maria', 'Marcos', 'Lucas', 'João'}
Java = {'Lucas', 'Victoria', 'Fernanda', 'Mariane', 'Julia'}
Ambos = Python.intersection(Java)
Ambos2 = Python & Java
print(Ambos)
print(Ambos2)
"""

"""
Apenas os que estudam um
Python = {'Julia', 'Leticia', 'Maria', 'Marcos', 'Lucas', 'João'}
Java = {'Lucas', 'Victoria', 'Fernanda', 'Mariane', 'Julia'}
so_python = Python.difference(Java)
print(so_python)

so_java = Java.difference(Python)
print(so_java)
"""


