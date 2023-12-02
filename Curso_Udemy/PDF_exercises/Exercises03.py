# Faça um programa que lê 6 valores inteiros e depois mostre na tela os valores lidos
def exc_01():
    numbers = []
    i = 0
    while i != 6:
        x = int(input('Digite um numero inteiro: '))
        numbers.append(x)
        i += 1
    print(numbers)


# Faça um programa que lê 6 valores inteiros e depois mostre na ordem inversa
def exc_02():
    lista = []
    i = 0

    while i != 6:
        x = int(input('Digite um numero inteiro: '))
        lista.append(x)
        i += 1

    print(lista[::-1])


# Faça um programa que lê 6 valores, mas somente pares
def exc_03():
    lista = []
    i = 0

    while i != 6:
        x = int(input('Digite um numero inteiro: '))
        if x % 2 == 0:
            lista.append(x)
            i += 1
        else:
            print(
                'O valor precisa obrigatóriamente ser um numero par, tente novamente !!')
    print(lista)


# Faça um programa que leia 5 valores e mostre todos os valores lidos, a media, o menor e o maior
def exc_04():
    lista = []
    i = 0
    soma = 0

    while i != 5:
        x = int(input('Digite um valor: '))
        lista.append(x)
        i += 1
        soma = x + soma

    media = soma / i

    print(f"valores = {lista}")
    print(f"Maior valor da lista = {max(lista)}")
    print(f"Menor valor da lista = {min(lista)}")
    print(f"Média da lista = {media}")


# Faça um programa que leia 5 valores e nos dê o maior e menor valor, e indique as suas posições
def exc_05():
    lista = {}
    i = 0

    while i != 5:
        x = int(input('Digite um valor: '))
        lista[i] = x
        i += 1

    print(f"Maior valor da lista = {max(lista)}")
    print(f"Menor valor da lista = {min(lista)}")


exc_05()
