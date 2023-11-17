# Faça um programa que determine os 5 primeiros multiplos de 3. Considerando os maiores que 0.
def exc01():
    for numero2 in range(1, 16):
        if numero2 % 3 == 0:
            print(numero2)
    """
    for numero in range(3, 16, 3):
    print(numero)
    """


# Faça um programa que escreva na tela, de 1 ate 100, de 1 em 1. utilizando While, For e Do While
def exc02_1():
    for numero in range(1, 101):
        print(numero, end=' ')


def exc02_2():
    numero = 1
    while numero <= 100:
        print(numero, end=' ')
        numero += 1


def exc02_3():
    numero = 1
    while True:
        if numero < 100:
            print(numero, end=' ')
            numero += 1
        else:
            print(numero)
            break


# Faça um algoritmo que utilize While e faça uma contagem regressiva, com a mensagem "FIM"
def exc04():
    numero = 10
    while numero > 0:
        print(numero)
        numero -= 1
    print('FIM!')


# Faça um algoritmo que declare um valor como 0 e vá incrementando o mesmo de 10 em 10
def exc05():
    numero = 0
    while numero < 100:
        print(numero)
        numero += 10
    print(numero)


def exc06():
    numero = int(input('Digite o numero: '))
    for x in range(1, 100):
        if x % 2 != 0:
            print(x, end=' ')
            numero -= 1
            if numero == 0:
                break


def exc07():
    soma = 0
    total = 0
    for x in range(1, 200):  # 200 é um numero aleatório, para
        if x % 2 == 0:
            soma = soma + x
            total += 1
            if total == 50:
                break
    print(f'Resultado = {soma}')


