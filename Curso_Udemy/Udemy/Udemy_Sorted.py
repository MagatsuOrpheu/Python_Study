"""
Podemos usar o sorted() para qualquer iteravel.
Diferente do sort() que serve somente para listas.
"""

# O sorted não modifica a lista, ele apenas retorna uma nova lista. A original se mantem intacta
tupla = (1, 9, 5, 22, 3)
print(f"Sem o Sorted(): {tupla}")
print(f"Com o Sorted(): {sorted(tupla)}")
print(f"Imprimindo novamente: {tupla}")

lista = [9, 5, 23, 6, 1]
print(sorted(lista))

sets = {1, 5, 3, 10, 99}
print(sorted(sets))

# Adicionando parametros ao sorted()
print(sorted(tupla, reverse=True))  # Ordena e inverte a lista

# Podemos usar o sorted para coisas mais complexas
usuarios = [
    {"Usuario": 'Milicent', 'Tweets': ['Quero comer pizza', 'bati o carro']},
    {"Usuario": 'Marcos', 'Tweets': []},
    {"Usuario": 'Priscila', 'Tweets': ['Minha mãe fez pudim']},
    {"Usuario": 'Luffy', 'Tweets': [], 'filme': 'Bladerunner'},
    {"Usuario": 'Leticia', 'Tweets': ['Eu amo meu gat o']},
    {"Usuario": 'Gyarados', 'Tweets': ['Digam não às pokebolas'], 'cor': 'azul', 'Musica': 'Rock'}
]


# print(sorted(usuarios, key=len))

# print(sorted(usuarios, key=lambda usuario: usuario['Usuario']))

# print(sorted(usuarios, key=lambda usuario: len(usuario['Tweets'])))

print(sorted(usuarios, key=lambda usuario: [x[0] for x in usuario['Tweets']]))

musicas = [
    {'Nome':'Stairway To Heaven', 'Tocada': 100},
    {'Nome':'Back in Black','Tocada':74},
    {'Nome':'Free Bird','Tocada':44},
    {'Nome':'Fly Me To The Moon','Tocada':29}
]

print(sorted(musicas, key=lambda musica: musica['Tocada'], reverse=True))
