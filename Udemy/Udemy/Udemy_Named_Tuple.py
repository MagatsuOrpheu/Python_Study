"""
Import from collections
"""

# Named Tuple são tuplas que especificamos um nome para a mesma e também parametros

from collections import namedtuple
# modo 1
cachorro = namedtuple('Cachorro', 'idade raca nome')

# modo 2
cachorro = namedtuple('Cachorro', 'idade, raca, nome')

# modo 3
cachorro = namedtuple('Cachorro', ['idade', 'raca', 'nome'])

Orpheu = cachorro(idade='5', raca='Bulldog', nome='Orpheu')

# Acessando os dados - forma 1
print(Orpheu)
print(Orpheu[0])  # Idade
print(Orpheu[1])  # Raça
print(Orpheu[2])  # Nome

# Acessando os dados - forma 2
print(Orpheu.idade)
print(Orpheu.raca)
print(Orpheu.nome)

# Os outros metodos normais funcionam tambem
print(Orpheu.index('5'))
print(Orpheu.count('Orpheu'))