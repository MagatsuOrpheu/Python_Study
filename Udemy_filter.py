"""
Filter serve para filtrar dados de determinada coleção.


# Para dados estatisticos
import statistics

# dados coletados de algum sensor
dados = [1.4, 3.2, -0.2, 3.8, 6.3, 9.5]

# Calculando a media utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como map, a função filter recebe dois parâmetros: uma função e um iteravel
res = filter(lambda x: x > media, dados)
print(list(res))

# Assim como na função Map, após ser utilizado uma vez, os dados de filter são apagados.
print(list(res))


paises = ['', 'Argentina', 'Colombia', '', 'Chile', 'China', '', '']
print(paises)

# res = filter(None,paises)
# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)
print(list(res))
"""

# Diferença de map e filter

# Map() -> recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento

# Filter() -> recebe dois parametros, uma função e um iteravel e retorna um objeto filtrando os elementos


usuarios = [
    {"Usuario": 'Jonathan', 'Tweets': ['Quero comer pizza', 'bati o carro']},
    {"Usuario": 'Marcos', 'Tweets': []},
    {"Usuario": 'Priscila', 'Tweets': ['Minha mãe fez pudim']},
    {"Usuario": 'Luffy', 'Tweets': []},
    {"Usuario": 'Leticia', 'Tweets': ['Eu amo meu gato']},
    {"Usuario": 'Gyarados', 'Tweets': ['Digam não às pokebolas']}
]

filtro = list(filter(lambda u: len(u['Tweets']) == 0, usuarios))
filtro2 = list(filter(lambda usuario: not usuario['Tweets'], usuarios))

print(filtro)
print(filtro2)

# Combinar Filtro e Map
# selecionar os nomes que contenham menos de 5 letras

nomes = [
    'Vanessa',
    'Ana',
    'Julia',
    'João',
    'Angélica'
]

filtered_list = list(map(lambda x: f"O nome {x} tem menos de 5 letras", filter(lambda y: len(y) < 5, nomes)))

print(list(filtered_list))
