"""
*Modulo Colletions*

Conhecido como High Performance Container Datetypes
"""
from collections import Counter

"""
lista = [1,1,1,1,1,2,3,4,1,2,4,2,4,6,4,3,4,5,6,7,4,2,3,5,6,7,8,5,3,2,2,4,5,6,7,6,7,8,9,6,9,5,9,6,9,0,0,9,7,0,0]
res = Counter(lista)
print(res)
"""

# print(Counter('Jonathan Gabriel de Freitas Melo'))

texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"""

palavras = texto.split()

print(Counter(palavras))


