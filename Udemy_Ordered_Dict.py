"""
Import from collections
"""
from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dicionario2 = {'c': 3, 'd': 4, 'a': 1, 'b': 2}
print(dicionario)
print(dicionario2)
print(dicionario == dicionario2)  # Vai gerar True pois a ordem não importa para o dicionario
dicionario3 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
dicionario4 = OrderedDict({'c': 3, 'd': 4, 'a': 1, 'b': 2})
print(dicionario3)
print(dicionario4)
print(dicionario3 == dicionario4)  # Vai gerar false, pois a ordem dos dois não é a mesma