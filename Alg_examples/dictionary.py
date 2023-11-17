"""
Dicionarios são representados por chaves:

EX: Paises
"""

paises = {'Br': 'Brasil', 'EUA': 'Estados Unidos', 'Arg': 'Argentina'}
pagamento = {'Janeiro': 500, 'Fevereiro': 300, 'Março': 400}

# print(paises['Ru']) < -  Dá erro
# print(paises.get('Ru')) < - Não dá erro, apenas retorna None

"""
teste = paises.get('Ru')
if teste:
    print(f'Encontrei o {teste}')
else:
    print('Não encontrei o pais requisitado')
"""

"""
Podemos atribuir um elemento para caso não encontremos o país

teste = paises.get('Ru', 'Vou aparecer caso o país dito não seja encontrado')
teste01 = paises.get('Br', 'Vou aparecer caso o país dito não seja encontrado')
print(teste01)
"""

"""
A busca só é feita por meio de chaves

print('Br' in paises)
print('Ru' in paises)
print('Argentina' in paises)
"""

"""
escritorios = {
    (31.02931321, -88.85923232): 'São Paulo',
    (61.13945381, -23.02934324): 'Campinas',
    (-76.02934324, 30.329344232): 'Osasco'
}

print(escritorios)
print(type(escritorios))
"""

"""
Podemos adicionar novos dados para o dicionario de certas formas

pagamento = {'Janeiro': 200, 'Fevereiro': 300, 'Março': 400}

print(pagamento)
print(type(pagamento))


pagamento['Abril'] = 500

print(pagamento)
print(type(pagamento))

novo_mes = {'Maio': 600}

pagamento.update(novo_mes)

print(pagamento)
print(type(pagamento))
"""

"""
Podemos atualizar valores dentro dos dicionarios de duas formas

pagamento['Março'] = 450
print(pagamento)

pagamento.update({'Março': 500})
print(pagamento)
"""

"""
Remover dados de um dict pode ser feito usando pop ou del
print(pagamento)
dele = pagamento.pop('Janeiro')
print(dele)
print(pagamento)
del pagamento['Fevereiro']
print(pagamento)
"""

"""
Podemos simular um carrinho de compras online dessa maneira

carrinho = []

produto_1 = {'nome': 'Zelda Tears of The Kingdom', 'preço': 300}
produto_2 = {'nome': 'Persona 6', 'preço': 290}

carrinho.append(produto_1)
carrinho.append(produto_2)

print(carrinho)
"""

"""
Forma não usual de criação de dicionarios
usuario = {}.fromkeys(['nome', 'idade', 'genero', 'email'], 'desconhecido')
print(usuario)
"""

"""
novo = {}.fromkeys(range(1, 10), 'novo')
print(novo)
"""

"""
podemos iterar sobre dicionarios dessa formas

print(pagamento)
for chave in pagamento.keys():
    print(chave)

for valor in pagamento.values():
    print(valor)
"""
