"""
Dicionarios em python são conhecidos por mapas em outras linguagens, pois são coleções do tipo chave e valor
São representados por {}.
Segue esse formato para declarção -> Chave : valor
Podem ser de qualquer tipo de dados
Podemos misturar tipos de dados
"""
"""
Forma 1
paises = {'BR': 'Brasil', 'EUA': 'United States'}
print(paises)
print(type(paises))
"""
"""
Forma 2
paises2 = dict(BR='Brasil', Eua='United States')
print(paises2)
print(type(paises2))
"""

paises = {'BR': 'Brasil', 'EUA': 'United States'}

#Acessando elementos em dicionarios"
"""
Forma 1: Acessando via chave
print(paises['BR'])
print(paises['EUA'])
print(paises['RU']) # Gera KeyError, pois a chave não existe
"""

"""
Forma2: Acessando via GET
print(paises.get('BR'))
print(paises.get('EUA'))
print(paises.get('RU')) # Não vai gerar um erro, retorna apenas o valor None

russia = paises.get('RU', 'Vou aparecer somente se o pais não for encontrado')
brasil = paises.get('BR', 'Vou aparecer somente se o pais não for encontrado')

print(russia)
print(brasil)
"""

"""
Buscando chaves nos dicionarios
print('BR' in paises)  # True
print('RU' in paises)  # False
print('United States' in paises)  # False (Busca somente as chaves, não os valores)
"""

"""
Dicionarios aceitam qualquer tipo de dado
escritorios = {
    ("10.22", "20.23"): "Campinas",
    ("20.21", "29.47"): "Jundiai"
}
print(escritorios)
"""

"""
Adicionando elementos em dicionarios
paises['AR'] = 'Argentina'
russia = {'RU': 'Russia'}
paises.update(russia)
paises.update({'JP': 'Japão'})
print(paises)
"""

"""
Atualizando valores em dicionarios
print(paises)
paises['BR'] = 'NOVO PAIS'
print(paises)
paises.update({'EUA':'Estados Unidos'})
print(paises)
"""

"""
Remover dados de um dicionario
retorno = paises.pop('BR') # Apaga e retorna o elemento do dicionario
del paises['EUA'] # Apaga o elemento do dicionario
print(f"Aqui vai o retorno: {retorno}")
print(paises)
"""

"""
Outra forma de criação de dicionarios
Usuario2 = {}.fromkeys('Nome', 'Jonathan')
print(Usuario2)
"""

"""
Iterar sobre dicionarios
Usuario = {}.fromkeys(['Nome', 'Idade', 'Gênero'], 'Desconhecido')
# Método 1
for chave in Usuario.keys():
    print(f"{chave} : {Usuario[chave]}")

# Método 2
for chave in Usuario:
    print(f"{chave} = {Usuario[chave]}")
    
Usuario = {}.fromkeys(['Nome', 'Idade', 'Gênero'], 'Desconhecido')

for chave, valor in Usuario.items():
    print(f"Chave = {chave}, Valor = {valor}")
"""



