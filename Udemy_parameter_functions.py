"""
Funções que recebem dados para serem processados internamente.
"""

# def nome_da_funcao(parametro):
#    bloco da funcao

"""
def sqrt(numero):
    return numero * numero


print(sqrt(7))
print(sqrt(2))
print(sqrt(4))
ret = sqrt(9)
print(ret)
"""

"""
Pode conter varios parametros

def documento(nome, rg, idade):
    print(f'Nome: {nome}')
    print(f'RG: {rg}')
    print(f'Idade: {idade}')


documento('Jonathan', 123456789, 21)


def soma(a,b):
    return a + b


print(soma(8, 9))
"""

"""
def nome_completo(nome, sobrenome):
    return f"Seu nome completo é: {nome} {sobrenome}"


nome_1 = "Elizabeth"
sobrenome_1 = "Lail"
print(nome_completo('Angelina', 'Jolie'))
print(nome_completo(nome_1, sobrenome_1))
print(nome_completo(nome='Maria', sobrenome='Luisa'))
"""


def calcular_impares(numeros):
    total = 0
    for n in numeros:
        if n % 2 != 0:
            total = total + n
        return total # Vai retornar apenas 1 pois não faz a iteração sobre o resto da lista
    return total


lista = [1,2,3,4,5,6,7]
print(calcular_impares(lista))
