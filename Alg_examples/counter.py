from collections import Counter

# EX1

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = Counter(lista1)
# print(type(res))
# print(res)

# EX2

nome = 'Aprendizagem Python'
# print(Counter(nome))

# EX3

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

palavras = texto.split()

result = Counter(palavras)

print(result.most_common(8))
