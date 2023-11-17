from collections import namedtuple
# named_tuple são tuplas nomeadas

"""
tupla1 = (1, 2, 3)  # tupla comum
tupla1 = (num1=1, num2=2, num3=3)  # tupla nomeadas
"""

# forma 1:
cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2:
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3:
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

gato = namedtuple('gato', ['idade', 'raca', 'nome'])

Morgana = gato(idade=2, raca='sla', nome='morgana')

kiara = cachorro(idade=2, raca='vira_lata', nome='kiara')


print(Morgana)
