"""

    # Basic struture of dicts



pessoa = {'nome':"Jonathan", 'idade': 21}
pessoa = dict(nome='Jonathan', idade=21)
pessoa['telefone'] = '1234-4321'
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

# dicionarios aninhados

pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'},
    'Leticia':{'email':'leticia.email@gmail.com', 'telefone':'7767-9989'},
    'Larissa':{'email':'larissa.email@gmail.com', 'telefone':'8822-3344', 'info':{'comida':'Frango'}}    
}

# print(pessoas['Larissa']['email'])
# comida = pessoas['Larissa']['info']['comida']
# print(comida)

for chave in pessoas:
    print(chave)


for chave, valor in pessoas.items():
    print(f"chave : {chave} - valor: {valor}")
"""


"""
    Methods for dicts

    
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'}
}

jonathan = pessoas.copy()
jonathan['Jonathan'] = {'nome':'Jhow'}

print(jonathan)
print(pessoas)    


# fromkeys
new = {}
new = dict.fromkeys(['Nome', 'Telefone']) # atribui o valor None pra chaves
new = dict.fromkeys(['Nome', 'Telefone'], 'Vazio')  # Atribui "vazio" para as chaves

print(new)

# get
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'},
    'Leticia':{'email':'leticia.email@gmail.com', 'telefone':'7767-9989'},
}

print(pessoas.get('Larissa'))  # Não gera erro caso a chave nao exista
print(pessoas.get('Fernanda'), {})  # pode ser passado um valor default para que ele retorne
print(pessoas.get('Jonathan'))

# items
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'},
    'Leticia':{'email':'leticia.email@gmail.com', 'telefone':'7767-9989'},
}
print(pessoas.items())


# keys
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'},
    'Leticia':{'email':'leticia.email@gmail.com', 'telefone':'7767-9989'},
}
print(pessoas.keys())


# pop
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'},
    'Leticia':{'email':'leticia.email@gmail.com', 'telefone':'7767-9989'},
}
retorno = pessoas.pop('Jonathan')
retorno2 = pessoas.pop('Fernanda', 'Chave nao encontrada')
print(retorno)
print(retorno2)


# popitem  <- Remove os items sem possibilidade de instrucao
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'},
    'Leticia':{'email':'leticia.email@gmail.com', 'telefone':'7767-9989'},
}

print(pessoas.popitem())
print(pessoas.popitem())
print(pessoas)


# setdefault
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'}
}

pessoas.setdefault('email', 'jonathan2@gmail.com')  # Nao há mudancas pois já existe um valor utilizando essa chave, logo ele nao substitui
print(pessoas)

pessoas.setdefault('idade', 21)
print(pessoas)



"""

# update
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'}
}

pessoas.update({'Jonathan':{'email':'jon@gmail.com'}}) # caso ja exista uma chave com tal valor, ele substitui
print(pessoas)

pessoas.update({'Fernanda':{'email':'fernada@gmail.com'}})  # caso nao exista nenhuma chave, ele cria uma nova
print(pessoas)


# values
pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'}
}

print(pessoas.values())  # Retorna apenas os valores do dicionario

# in

pessoas = {
    'Jonathan':{'email':'jonathan.email@gmail.com', 'telefone':'1234-4321'},
    'Fernanda' : {'email':'fernanda.email@gmail.com','telefone':'8887-9998'},
    'Larissa': {'email':'larissa.email@gmail.com','telefone':'8888-9998'}
}

print('Fernanda' in pessoas)
print('telefone' in pessoas['Fernanda'])