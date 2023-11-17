# OrderedDict são dicts ordenados, como diz o prefixo do nome

from collections import OrderedDict
dicionario = {'a': 1, 'b': 2, 'c': 3}

# for chave, valor in dicionario.items():
#     print(f'chave={chave} e valor={valor}')

dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 2, 'a': 1}

print(dic1 == dic2)

##############################

odic1 = OrderedDict({'a': 1, 'b': 2})
odic2 = OrderedDict({'b': 2, 'a': 1})

print(odic1 == odic2)
