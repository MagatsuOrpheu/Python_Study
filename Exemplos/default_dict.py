# Default dict -> ao criar um dict usando o default dict, nós informamos um valor padrão (default) utilizando um lambda. Esse valor sempre será utilizado quando for feito uma chamada de uma chave sem um valor definido. E caso tal chave não exista, ela será criada.

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['Teste'] = 'Fui criado!'

print(dicionario)

print(dicionario['Teste2323'])

print(dicionario)
