"""
Import from collections

Dict normais
Dicionario = {'Curso': 'Programação em Python', 'Curso2' : 'Programação em Java'}
print(Dicionario)
print(Dicionario['Curso'])
print(Dicionario['Outro'])  # <- Gera KeyError
"""

# Default Dict <- Você cria um dicionario com um valor default, podendo usar lambda para isso

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['Nome'] = 'Jonathan'

print(dicionario)

print(dicionario['Idade'])  # <- Não é gerado KeyError

print(dicionario)
