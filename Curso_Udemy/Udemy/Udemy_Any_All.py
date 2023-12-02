"""
Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio
"""

# Exemplo all()

# print(all([0,1,2,3,4,5]))  # Vai retornar False por conta do 0
# print(all([1,2,3,4,5]))  # Vai retornar True
# print(all([]))  # Todos os numeros são verdadeiros ? -> True
# print(all([(1,2,3,4)]))  # Podemos usar tuplas
# print(all([{1,2,3,4}]))  # Podemos usar sets
# print(all('Jonathan'))  # Podemos usar strings
nomes = ['Carla', 'Cristina', 'Carmen', 'Cristian', 'Vivian']
print(all(nome[0] == 'C' for nome in nomes))  # Verifique se o nome, na posicao 0, em nomes, comeca com C
nomes2 = ['']
# print(all(nomes2))  # False

# print(all([letra for letra in 'mnp' if letra in 'aeiou']))  # Vai gerar True, pois o iteravel será vazio

"""
Any() -> Retorna um booleano (True) se qualquer um dos elementos do iteravel for verdadeiro. Se o iteravel estiver vazio,
retorna False.
"""
# Exemplos Any()
# print(any([1,2,3,4,5,0]))  # Retorna True, mesmo com o 0
# print(any([0, False, [], {}, ()]))  # Retorna False
# print(any([letra for letra in 'mvp' if letra in 'aeiou']))